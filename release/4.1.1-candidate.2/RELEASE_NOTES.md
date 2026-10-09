# Helikon Mini 4.1.1-candidate.2 — installation repairs

Status: **review/testing candidate; candidate-specific live acceptance pending**. This archive preserves the earlier candidate and regular project release. It does not promote account support.

Candidate.1 live testing exposed three gaps: a manual installer that stopped when direct settings-write tools were unavailable, canonical terminal newlines that the settings UI omitted, and source-read success assertions without observable complete source coverage. Candidate.2 revises the installer and evidence requirements in response.

The installer now provides an operator-assisted route with backups, exact copy blocks, save/reopen instructions and action attribution. Canonical snippets have no terminal newline and contain 1,099 and 866 characters. Saved-text validation requires exact snippet content at newline boundaries, permits preserved unrelated preferences, and does not trim saved fields. Historical snippets retain their historical newline requirement.

The source workflow separates task correctness, source delivery and observability. Citations, hashes, summaries and model assertions do not establish a complete runtime read. An optional explicit Library-attachment diagnostic is recorded separately after the primary automatic-access attempt; it cannot retroactively pass that attempt.

Runtime rules, procedures, bootstrap, owners and extension declarations are unchanged. Version axes are runtime 4.1.1-candidate.2, schema 1.0.8, System contract 2.2.0 and installer protocol 2.2.0. Extension contract 1.0.0, install-package schema 2.1.0 and installation-record schema 2.0.0 remain unchanged.

Use the bundle's START_HERE.md for an authorized test installation. See [executed offline checks](VALIDATION.md), [repair disposition](REPAIR_MAP.md) and the [manual acceptance suite](../../docs/account-acceptance.md). Candidate.1 observations motivate these changes but cannot pass candidate.2 acceptance. No general usefulness advantage is claimed.
