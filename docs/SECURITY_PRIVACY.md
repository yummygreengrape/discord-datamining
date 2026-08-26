# Security and privacy controls

## Publication gate

This repository contains published data and reader-facing documentation only.
It does not execute or distribute the runner, scanner, allowlist, tests, agent
instructions, or CI workflow. Those controls live in the private runner
repository, whose CI checks out this repository and validates it before
publication.

The private publisher installs and stages exactly these seven generated files
after candidate scanning and digest attestation:

- `data/latest_changes.json`
- `data/web/meta.json`
- `data/web/experiments.json`
- `data/web/experiment-details.json`
- `data/web/apis.json`
- `data/web/strings.en.json`
- `data/web/strings.ko.json`

The scanner fails publication for:

- GitHub and Discord tokens, private keys, AWS access keys, and live Discord
  webhook URLs;
- Discord mentions and 17–20 digit snowflakes, email addresses, phone numbers,
  and IPv4/IPv6 addresses;
- JSON fields associated with credentials or private Discord identifiers;
- camelCase, snake_case, and kebab-case variants of credential and identifier
  keys, including access/refresh tokens, client secrets, API/private keys, and
  `authorId` raw-message records;
- records shaped like raw messages;
- known private runner-state paths and raw moderation/message-report names;
- symbolic links and invalid, unreadable, or unexpectedly large JSON artifacts.

Reports contain paths, line numbers, rule names, and SHA-256 fingerprints only.
They never contain the detected value.

## Allowlist policy

The private allowlist is for verified non-user product metadata that a detector
cannot distinguish automatically. It is not published in this repository.
Every entry requires:

- one exact detector rule and SHA-256 fingerprint;
- the narrowest matching public path;
- an evidence-based reason;
- an ISO date after which CI fails until the exception is reviewed.

Never allowlist secrets, authentication material, live webhooks, raw messages,
or identifiers tied to a project user. A new finding should be quarantined and
investigated before any exception is considered.

## Incident handling

If a secret or personal record reaches GitHub, stop the runner, revoke or rotate
the credential when applicable, remove the current artifact, assess Git-history
remediation, and document affected data and recipients. Do not print the value
in logs, issues, or pull requests.
