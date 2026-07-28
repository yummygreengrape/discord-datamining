# Agent security and privacy rules

This is the public, generated-data repository. The private runner lives in a
separate checkout and is the only component that may regenerate the JSON under
`data/`.

Before changing code, workflows, documentation, or generated-data contracts:

1. Inspect the input, authentication, storage, logging, outbound-network,
   dependency, and container boundaries affected by the change.
2. Never add raw Discord messages, user/guild/channel/message identifiers,
   moderation exports, runner state, credentials, cookies, IP addresses, email
   addresses, phone numbers, or webhook URLs.
3. Do not manually edit files under `data/`. Fix generation in the private
   runner. Public schema changes must be additive and optional until all
   consumers have migrated.
4. Run `python3 scripts/security_scan.py --root . .` and
   `python3 -m unittest discover -s tests -p 'test_*.py'`.
5. An allowlist entry is permitted only for verified non-user product metadata.
   It must use an exact SHA-256 fingerprint, a narrow path, a specific reason,
   and a review expiry date. Never allowlist a token, credential, webhook, raw
   message, or project user identifier.
6. Update `docs/DATA_INVENTORY.md` and `docs/SECURITY_PRIVACY.md` in the same
   change when collection, publication, retention, deletion, or recipients
   change.
7. Final reports must include a `Security/privacy impact` section and the exact
   checks run.

If the purpose, minimum fields, storage/recipient, retention, deletion path,
backup behavior, or access controls for personal data are unclear, stop and ask
before publishing.
