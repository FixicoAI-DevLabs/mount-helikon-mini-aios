# Helikon Mini 4.1.1-candidate.3 — exact installer handoff

Status: **review/testing candidate; candidate-specific live acceptance pending**. This archive preserves the earlier candidates and regular project release. It does not promote account support.

Candidate.2 testing found that SETUP deferred the snippet copy blocks until NEXT and FINAL_VERIFY added three newline characters to the canonical handoff. Candidate.3 addresses those observed installer defects without changing runtime policy.

Installer protocol 2.3.0 requires both exact snippet previews in the first SETUP response after checking the complete package and identity. The previews do not satisfy backup, conflict, length or save checks. The fresh-chat source prompt is now one exact logical line. Validation rejects inserted CR/LF and outer whitespace even if the package and guide projections match that malformed value. If an installer response alters the prompt, preserve the failed attempt and copy the canonical guide block directly; do not attach the guide to the primary automatic-access test.

Runtime rules, procedures, bootstrap, owners and extension declarations are unchanged. Runtime is 4.1.1-candidate.3, schema 1.0.9 and installer protocol 2.3.0. System contract 2.2.0, extension contract 1.0.0, install-package schema 2.1.0 and installation-record schema 2.0.0 remain unchanged. Canonical Personalization snippets still contain 1,099 and 866 characters without terminal newlines.

Use the bundle's START_HERE.md for an authorized test installation. See [executed offline checks](VALIDATION.md), [repair disposition](REPAIR_MAP.md), the [focused live retest](LIVE_RETEST.md) and the [manual acceptance suite](../../docs/account-acceptance.md). Historical candidates retain their exact multiline handoffs and observed outcomes. Candidate.3 delivered both exact SETUP previews immediately; its first FINAL_VERIFY omitted the handoff, and one corrective follow-up reproduced it exactly. Upload failure still blocks source prerequisites and full account acceptance.
