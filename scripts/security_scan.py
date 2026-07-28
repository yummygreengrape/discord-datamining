#!/usr/bin/env python3
"""Fail closed when public artifacts contain secrets or personal identifiers."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import ipaddress
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Iterable, Iterator, Sequence


MAX_FILE_BYTES = 16 * 1024 * 1024
DEFAULT_EXCLUDED_PARTS = {".git", "__pycache__", ".venv", "node_modules"}
SELF_PATH = "scripts/security_scan.py"
ALLOWLIST_PATH = "security/public-data-allowlist.json"

PRIVATE_STATE_PATHS = {
    "data/api_endpoints.json",
    "data/english_strings.json",
    "data/english_strings_extracted.json",
    "data/en_strings_net.json",
    "data/en_strings_test.json",
    "data/experiments.json",
    "data/history.json",
    "data/korean_strings.json",
    "data/message.txt",
    "data/previous_state.json",
}
RAW_REPORT_NAME_PATTERNS = (
    "*filtered_user_messages*",
    "*moderation-report*",
    "*moderation_report*",
    "*raw-message*",
    "*raw_message*",
)


@dataclass(frozen=True)
class PatternRule:
    rule_id: str
    category: str
    pattern: re.Pattern[str]


@dataclass(frozen=True)
class Finding:
    rule: str
    category: str
    path: str
    line: int
    fingerprint: str
    allowed: bool = False


@dataclass(frozen=True)
class AllowlistEntry:
    rule: str
    path: str
    fingerprint: str
    reason: str
    expires_on: date


PATTERN_RULES: tuple[PatternRule, ...] = (
    PatternRule(
        "private_key",
        "secret",
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    ),
    PatternRule(
        "github_token",
        "secret",
        re.compile(r"\b(?:github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,})\b"),
    ),
    PatternRule(
        "aws_access_key",
        "secret",
        re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    ),
    PatternRule(
        "discord_webhook",
        "secret",
        re.compile(
            r"https?://(?:canary\.|ptb\.)?discord(?:app)?\.com"
            r"/api(?:/v\d+)?/webhooks/\d{17,20}/[A-Za-z0-9._-]{20,}",
            re.IGNORECASE,
        ),
    ),
    PatternRule(
        "discord_token",
        "secret",
        re.compile(
            r"(?<![A-Za-z0-9_-])[A-Za-z0-9_-]{20,30}\."
            r"[A-Za-z0-9_-]{6}\.[A-Za-z0-9_-]{20,}(?![A-Za-z0-9_-])"
        ),
    ),
    PatternRule(
        "discord_mfa_token",
        "secret",
        re.compile(r"(?<![A-Za-z0-9_-])mfa\.[A-Za-z0-9_-]{20,}(?![A-Za-z0-9_-])"),
    ),
    PatternRule(
        "bearer_token",
        "secret",
        re.compile(r"\bBearer\s+[A-Za-z0-9._~+/=-]{20,}", re.IGNORECASE),
    ),
    PatternRule(
        "discord_mention",
        "pii",
        re.compile(r"<(?:@!?|@&|#)\d{17,20}>"),
    ),
    PatternRule(
        "discord_snowflake",
        "pii",
        re.compile(r"(?<!\d)\d{17,20}(?!\d)"),
    ),
    PatternRule(
        "email_address",
        "pii",
        re.compile(r"(?<![\w.+-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![\w.-])", re.IGNORECASE),
    ),
    PatternRule(
        "ipv4_address",
        "pii",
        re.compile(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])"),
    ),
    PatternRule(
        "ipv6_address",
        "pii",
        re.compile(
            r"(?<![0-9A-Fa-f:])(?=[0-9A-Fa-f:]{2,39}(?![0-9A-Fa-f:]))"
            r"(?=[0-9A-Fa-f:]*:)[0-9A-Fa-f:]{2,39}(?![0-9A-Fa-f:])"
        ),
    ),
    PatternRule(
        "phone_number",
        "pii",
        re.compile(
            r"(?<![\w])(?:"
            r"\+\d{1,3}(?:[ .()-]?\d){7,12}"
            r"|(?:\(\d{2,4}\)\s*|\d{2,4}[- ])\d{3,4}[- ]\d{4}"
            r")(?![\w])"
        ),
    ),
)

SENSITIVE_JSON_KEYS = {
    "access_token",
    "api_key",
    "authorization",
    "client_secret",
    "cookie",
    "password",
    "private_key",
    "refresh_token",
    "secret",
    "token",
    "webhook_url",
}
IDENTIFIER_JSON_KEYS = {
    "author_id",
    "channel_id",
    "discord_id",
    "guild_id",
    "ip_address",
    "message_id",
    "moderator_id",
    "user_id",
}
ALLOWLISTABLE_RULES = {
    "discord_mention",
    "discord_snowflake",
    "email_address",
    "ipv4_address",
    "ipv6_address",
    "phone_number",
}


def fingerprint(value: str) -> str:
    return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def _configuration_finding(rule: str, path: str, value: str) -> Finding:
    return Finding(
        rule=rule,
        category="configuration",
        path=path,
        line=1,
        fingerprint=fingerprint(value),
    )


def load_allowlist(path: Path) -> tuple[list[AllowlistEntry], list[Finding]]:
    if not path.exists():
        return [], [_configuration_finding("allowlist_missing", path.as_posix(), "missing")]

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [], [_configuration_finding("allowlist_invalid", path.as_posix(), type(exc).__name__)]

    if not isinstance(payload, dict) or payload.get("version") != 1 or not isinstance(payload.get("entries"), list):
        return [], [_configuration_finding("allowlist_invalid", path.as_posix(), "schema")]

    entries: list[AllowlistEntry] = []
    errors: list[Finding] = []
    today = date.today()
    for index, raw_entry in enumerate(payload["entries"]):
        entry_path = f"{path.as_posix()}#entries[{index}]"
        if not isinstance(raw_entry, dict):
            errors.append(_configuration_finding("allowlist_invalid", entry_path, "not-object"))
            continue
        try:
            expires_on = date.fromisoformat(str(raw_entry["expires_on"]))
            entry = AllowlistEntry(
                rule=str(raw_entry["rule"]),
                path=str(raw_entry["path"]),
                fingerprint=str(raw_entry["fingerprint"]),
                reason=str(raw_entry["reason"]).strip(),
                expires_on=expires_on,
            )
        except (KeyError, TypeError, ValueError) as exc:
            errors.append(_configuration_finding("allowlist_invalid", entry_path, type(exc).__name__))
            continue

        valid_fingerprint = re.fullmatch(r"sha256:[0-9a-f]{64}", entry.fingerprint) is not None
        valid_path = (
            entry.path.startswith("data/")
            and ".." not in Path(entry.path).parts
            and entry.path not in {"data/*", "data/**", "data/**/*"}
        )
        if (
            entry.rule not in ALLOWLISTABLE_RULES
            or not valid_path
            or len(entry.reason) < 20
            or not valid_fingerprint
        ):
            errors.append(_configuration_finding("allowlist_invalid", entry_path, "required-field"))
            continue
        if entry.expires_on < today:
            errors.append(_configuration_finding("allowlist_expired", entry_path, entry.fingerprint))
            continue
        if (entry.expires_on - today).days > 366:
            errors.append(_configuration_finding("allowlist_invalid", entry_path, "expiry-too-long"))
            continue
        entries.append(entry)
    return entries, errors


def is_allowed(finding: Finding, entries: Sequence[AllowlistEntry]) -> bool:
    if finding.rule not in ALLOWLISTABLE_RULES:
        return False
    return any(
        finding.rule == entry.rule
        and finding.fingerprint == entry.fingerprint
        and fnmatch.fnmatchcase(finding.path, entry.path)
        for entry in entries
    )


def _iter_files(root: Path, requested_paths: Sequence[str]) -> Iterator[Path]:
    resolved_root = root.resolve()
    seen: set[Path] = set()
    for requested in requested_paths:
        target = root / requested
        resolved_target = target.resolve()
        try:
            resolved_target.relative_to(resolved_root)
        except ValueError:
            raise ValueError(f"scan path escapes root: {requested}") from None
        candidates: Iterable[Path] = (
            target.rglob("*")
            if target.is_dir() and not target.is_symlink()
            else (target,)
        )
        for path in candidates:
            absolute_path = path.absolute()
            relative = absolute_path.relative_to(resolved_root)
            if path.is_symlink():
                pass
            elif not path.is_file():
                continue
            if any(part in DEFAULT_EXCLUDED_PARTS for part in relative.parts):
                continue
            relative_text = relative.as_posix()
            if relative_text in {SELF_PATH, ALLOWLIST_PATH} or relative_text.startswith("tests/"):
                continue
            if absolute_path in seen:
                continue
            seen.add(absolute_path)
            yield path


def _line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _pattern_findings(relative_path: str, text: str, secrets_only: bool) -> list[Finding]:
    findings: list[Finding] = []
    occupied_snowflakes: set[tuple[int, int]] = set()
    for rule in PATTERN_RULES:
        if secrets_only and rule.category != "secret":
            continue
        for match in rule.pattern.finditer(text):
            value = match.group(0)
            if rule.rule_id in {"ipv4_address", "ipv6_address"}:
                try:
                    parsed_ip = ipaddress.ip_address(value)
                except ValueError:
                    continue
                expected_version = 4 if rule.rule_id == "ipv4_address" else 6
                if parsed_ip.version != expected_version:
                    continue
            if rule.rule_id == "phone_number":
                digit_count = sum(char.isdigit() for char in value)
                if not 8 <= digit_count <= 15:
                    continue
            if rule.rule_id == "discord_snowflake":
                occupied_snowflakes.add(match.span())
            if rule.rule_id == "phone_number" and any(
                match.start() >= start and match.end() <= end for start, end in occupied_snowflakes
            ):
                continue
            findings.append(
                Finding(
                    rule=rule.rule_id,
                    category=rule.category,
                    path=relative_path,
                    line=_line_for_offset(text, match.start()),
                    fingerprint=fingerprint(value),
                )
            )
    return findings


def canonical_json_key(value: object) -> str:
    text = str(value)
    text = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", text)
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    return re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_").lower()


def _walk_json(
    value: object,
    path: str = "$",
    field_name: str | None = None,
) -> Iterator[tuple[str, str | None, object]]:
    yield path, field_name, value
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            yield from _walk_json(child, child_path, str(key))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            child_path = f"{path}[{index}]"
            yield from _walk_json(child, child_path)


def _json_findings(relative_path: str, text: str, secrets_only: bool) -> list[Finding]:
    if not relative_path.endswith(".json"):
        return []
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        return [
            Finding(
                rule="invalid_json",
                category="integrity",
                path=relative_path,
                line=exc.lineno,
                fingerprint=fingerprint(type(exc).__name__),
            )
        ]

    findings: list[Finding] = []
    for json_path, field_name, value in _walk_json(payload):
        key = canonical_json_key(field_name) if field_name is not None else ""
        if key in SENSITIVE_JSON_KEYS and value not in (None, "", [], {}):
            findings.append(
                Finding(
                    rule="sensitive_json_field",
                    category="secret",
                    path=relative_path,
                    line=1,
                    fingerprint=fingerprint(f"{json_path}:{type(value).__name__}"),
                )
            )
        if secrets_only:
            continue
        if key in IDENTIFIER_JSON_KEYS and value not in (None, "", [], {}):
            findings.append(
                Finding(
                    rule="private_identifier_field",
                    category="pii",
                    path=relative_path,
                    line=1,
                    fingerprint=fingerprint(f"{json_path}:{type(value).__name__}"),
                )
            )

    if not secrets_only:
        for json_path, _field_name, value in _walk_json(payload):
            if not isinstance(value, dict):
                continue
            canonical_keys = {canonical_json_key(key) for key in value}
            if "content" in canonical_keys and canonical_keys.intersection(
                {"author", "author_id", "username", "user_id"}
            ):
                findings.append(
                    Finding(
                        rule="raw_message_record",
                        category="pii",
                        path=relative_path,
                        line=1,
                        fingerprint=fingerprint(json_path),
                    )
                )
    return findings


def scan_paths(
    root: Path,
    requested_paths: Sequence[str],
    allowlist: Sequence[AllowlistEntry],
    *,
    secrets_only: bool = False,
) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    for requested in requested_paths:
        requested_path = (root / requested).resolve()
        try:
            relative = requested_path.relative_to(root).as_posix()
        except ValueError:
            raise ValueError(f"scan path escapes root: {requested}") from None
        if not requested_path.exists():
            findings.append(
                Finding(
                    rule="missing_scan_path",
                    category="integrity",
                    path=relative,
                    line=1,
                    fingerprint=fingerprint(relative),
                )
            )
    for path in _iter_files(root, requested_paths):
        relative = path.absolute().relative_to(root).as_posix()
        if path.is_symlink():
            findings.append(
                Finding(
                    rule="symbolic_link",
                    category="integrity",
                    path=relative,
                    line=1,
                    fingerprint=fingerprint(relative),
                )
            )
            continue
        if not secrets_only:
            if relative in PRIVATE_STATE_PATHS:
                findings.append(
                    Finding(
                        rule="private_state_file",
                        category="private_state",
                        path=relative,
                        line=1,
                        fingerprint=fingerprint(relative),
                    )
                )
            if any(fnmatch.fnmatchcase(path.name.lower(), pattern) for pattern in RAW_REPORT_NAME_PATTERNS):
                findings.append(
                    Finding(
                        rule="raw_report_file",
                        category="private_state",
                        path=relative,
                        line=1,
                        fingerprint=fingerprint(relative),
                    )
                )

        try:
            if path.stat().st_size > MAX_FILE_BYTES:
                findings.append(
                    Finding(
                        rule="file_too_large",
                        category="integrity",
                        path=relative,
                        line=1,
                        fingerprint=fingerprint(str(path.stat().st_size)),
                    )
                )
                continue
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            findings.append(
                Finding(
                    rule="unreadable_file",
                    category="integrity",
                    path=relative,
                    line=1,
                    fingerprint=fingerprint(type(exc).__name__),
                )
            )
            continue

        findings.extend(_pattern_findings(relative, text, secrets_only))
        findings.extend(_json_findings(relative, text, secrets_only))

    unique: dict[tuple[str, str, int, str], Finding] = {}
    for finding in findings:
        key = (finding.rule, finding.path, finding.line, finding.fingerprint)
        unique[key] = Finding(
            rule=finding.rule,
            category=finding.category,
            path=finding.path,
            line=finding.line,
            fingerprint=finding.fingerprint,
            allowed=is_allowed(finding, allowlist),
        )
    return sorted(unique.values(), key=lambda item: (item.path, item.line, item.rule, item.fingerprint))


def write_report(path: Path, findings: Sequence[Finding], configuration_findings: Sequence[Finding]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    blocked = [finding for finding in findings if not finding.allowed]
    payload = {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "blocked" if blocked or configuration_findings else "passed",
        "summary": {
            "blocked": len(blocked),
            "allowed": sum(finding.allowed for finding in findings),
            "configuration_errors": len(configuration_findings),
        },
        "findings": [asdict(finding) for finding in findings],
        "configuration_findings": [asdict(finding) for finding in configuration_findings],
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=["data"], help="paths relative to --root")
    parser.add_argument("--root", default=".", help="repository root")
    parser.add_argument("--allowlist", default=ALLOWLIST_PATH, help="allowlist path relative to --root")
    parser.add_argument("--report", help="write a redacted JSON report")
    parser.add_argument("--secrets-only", action="store_true", help="disable PII and private-state checks")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(args.root).resolve()
    allowlist_path = (root / args.allowlist).resolve()
    allowlist, configuration_findings = load_allowlist(allowlist_path)
    try:
        findings = scan_paths(root, args.paths, allowlist, secrets_only=args.secrets_only)
    except ValueError as exc:
        configuration_findings.append(
            _configuration_finding("scan_path_invalid", root.as_posix(), type(exc).__name__)
        )
        findings = []

    if args.report:
        write_report(Path(args.report), findings, configuration_findings)

    blocked = [finding for finding in findings if not finding.allowed]
    if blocked or configuration_findings:
        print(
            "Public-data security scan blocked: "
            f"{len(blocked)} finding(s), {len(configuration_findings)} configuration error(s)."
        )
        for finding in [*configuration_findings, *blocked]:
            print(
                f"- {finding.rule} {finding.path}:{finding.line} "
                f"fingerprint={finding.fingerprint[:19]}..."
            )
        return 1

    print(f"Public-data security scan passed ({len(findings)} reviewed allowlisted finding(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
