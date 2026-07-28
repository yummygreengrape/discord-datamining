import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("security_scan", ROOT / "scripts" / "security_scan.py")
security_scan = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = security_scan
SPEC.loader.exec_module(security_scan)


class SecurityScanTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "data").mkdir()

    def tearDown(self):
        self.temp_dir.cleanup()

    def scan(self, allowlist=()):
        return security_scan.scan_paths(self.root, ["data"], allowlist)

    def test_malicious_secret_and_private_identifiers_are_blocked(self):
        token = "gh" + "p_" + ("A" * 36)
        snowflake = "123456789012345678"
        payload = {
            "token": token,
            "author_id": snowflake,
            "content": "private message",
            "author": "person",
        }
        (self.root / "data" / "candidate.json").write_text(json.dumps(payload), encoding="utf-8")

        findings = self.scan()
        blocked_rules = {finding.rule for finding in findings if not finding.allowed}

        self.assertIn("github_token", blocked_rules)
        self.assertIn("sensitive_json_field", blocked_rules)
        self.assertIn("discord_snowflake", blocked_rules)
        self.assertIn("private_identifier_field", blocked_rules)
        self.assertIn("raw_message_record", blocked_rules)

    def test_each_public_identifier_detector_blocks_a_realistic_shape(self):
        samples = {
            "discord_webhook": (
                "https://discord.com/api/webhooks/"
                + "123456789012345678"
                + "/"
                + ("A" * 40)
            ),
            "discord_token": ("A" * 24) + "." + ("B" * 6) + "." + ("C" * 30),
            "discord_mfa_token": "mfa." + ("D" * 32),
            "bearer_token": "Bearer " + ("E" * 32),
            "discord_mention": "<@" + "123456789012345678" + ">",
            "email_address": "person" + "@" + "example.invalid",
            "ipv4_address": "198.51.100.42",
            "ipv6_address": "2001:db8:85a3:0:0:8a2e:370:7334",
            "phone_number": "+82 10-1234-5678",
        }
        for expected_rule, sample in samples.items():
            with self.subTest(rule=expected_rule):
                candidate = self.root / "data" / f"{expected_rule}.txt"
                candidate.write_text(sample, encoding="utf-8")
                rules = {finding.rule for finding in self.scan()}
                self.assertIn(expected_rule, rules)
                candidate.unlink()

    def test_legitimate_public_api_template_passes(self):
        payload = {
            "name": "WEBHOOK_ROUTE",
            "url": "/api/webhooks/:param/:param",
            "timestamp": "2026-07-28T01:02:03+00:00",
        }
        (self.root / "data" / "candidate.json").write_text(json.dumps(payload), encoding="utf-8")

        self.assertEqual(self.scan(), [])

    def test_json_key_normalization_blocks_secret_and_raw_message_variants(self):
        payload = {
            "accessToken": "short synthetic access value",
            "refresh-token": "short synthetic refresh value",
            "client_secret": "short synthetic client value",
            "apiKey": "short synthetic api value",
            "privateKey": "short synthetic private value",
            "authorId": "synthetic-author",
            "content": "private message",
        }
        (self.root / "data" / "candidate.json").write_text(
            json.dumps(payload),
            encoding="utf-8",
        )

        findings = self.scan()
        blocked_rules = [finding.rule for finding in findings if not finding.allowed]

        self.assertGreaterEqual(blocked_rules.count("sensitive_json_field"), 5)
        self.assertIn("private_identifier_field", blocked_rules)
        self.assertIn("raw_message_record", blocked_rules)

    def test_allowlist_requires_exact_fingerprint_and_nonexpired_reason(self):
        email = "security" + "@" + "example.invalid"
        (self.root / "data" / "candidate.json").write_text(json.dumps({"label": email}), encoding="utf-8")
        entry = security_scan.AllowlistEntry(
            rule="email_address",
            path="data/*.json",
            fingerprint=security_scan.fingerprint(email),
            reason="Synthetic documentation fixture",
            expires_on=date.today() + timedelta(days=30),
        )

        findings = self.scan([entry])

        self.assertEqual(len(findings), 1)
        self.assertTrue(findings[0].allowed)

    def test_secret_cannot_be_allowlisted(self):
        token = "gh" + "p_" + ("A" * 36)
        (self.root / "data" / "candidate.txt").write_text(token, encoding="utf-8")
        entry = security_scan.AllowlistEntry(
            rule="github_token",
            path="data/*.txt",
            fingerprint=security_scan.fingerprint(token),
            reason="Secrets must remain blocked",
            expires_on=date.today() + timedelta(days=30),
        )

        findings = self.scan([entry])

        self.assertEqual(len(findings), 1)
        self.assertFalse(findings[0].allowed)

    def test_expired_allowlist_entry_is_rejected(self):
        allowlist_path = self.root / "allowlist.json"
        allowlist_path.write_text(
            json.dumps(
                {
                    "version": 1,
                    "entries": [
                        {
                            "rule": "email_address",
                            "path": "data/*.json",
                            "fingerprint": "sha256:" + ("0" * 64),
                            "reason": "Expired allowlist fixture",
                            "expires_on": (date.today() - timedelta(days=1)).isoformat(),
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )

        entries, errors = security_scan.load_allowlist(allowlist_path)

        self.assertEqual(entries, [])
        self.assertEqual([error.rule for error in errors], ["allowlist_expired"])

    def test_raw_private_state_filename_is_blocked(self):
        (self.root / "data" / "history.json").write_text("{}\n", encoding="utf-8")

        findings = self.scan()

        self.assertIn("private_state_file", {finding.rule for finding in findings})

    def test_missing_requested_path_fails_closed(self):
        findings = security_scan.scan_paths(self.root, ["data/missing.json"], [])

        self.assertEqual([finding.rule for finding in findings], ["missing_scan_path"])

    def test_symbolic_link_is_not_skipped(self):
        target = self.root / "data" / "target.txt"
        target.write_text("public fixture\n", encoding="utf-8")
        link = self.root / "data" / "linked.txt"
        try:
            link.symlink_to(target.name)
        except OSError as exc:
            self.skipTest(f"symbolic links unavailable: {type(exc).__name__}")

        findings = self.scan()

        self.assertIn("symbolic_link", {finding.rule for finding in findings})


if __name__ == "__main__":
    unittest.main()
