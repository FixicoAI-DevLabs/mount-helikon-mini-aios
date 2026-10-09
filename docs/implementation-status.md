# Implementation status — 4.1.1-candidate.3

This revised testing candidate addresses the delayed SETUP copy blocks and altered handoff formatting observed in candidate.2, while retaining the earlier exact-snippet and source-evidence repairs. It retains two Personalization snippets, compact Helikon 6-derived runtime JSON and an eight-file end-user bundle. Projects remain optional. Runtime policy and System contract 2.2.0 are unchanged; candidate identity and installer protocol are revised.

## Implemented scope

- Exact-byte runtime handling and generated projection checks.
- Non-overwriting installation-record creation and explicitly versioned evidence records.
- Host metadata, observation methods, backup state and all eight installer checkpoints.
- Shorter snippets with explicit combined-field length checks and preservation of existing settings.
- Canonical snippet strings without terminal newlines, checked as exact newline-bounded blocks without trimming saved fields.
- Operator-assisted manual UI installation when direct host writes are unavailable, with action attribution and persisted readback requirements.
- Both exact snippet previews required in the first SETUP response, without treating preview text as a save or backup.
- Self-contained fresh ordinary-chat verification, separate from the installer conversation.
- A single-line exact handoff under installer protocol 2.3.0, with malformed-whitespace rejection and a canonical guide fallback that preserves the failed attempt.
- Separate source-access assertions, actual returned source text, coverage evidence and manual diagnostics.
- Per-attempt task-output, source-delivery and observability dimensions alongside the unchanged v2 record schema.
- Explicit immutable historical evidence bindings plus a current candidate-4/5 inventory.
- Source-inventory consistency checks, targeted negative tests and limited residue scanning of the complete distributed payload.
- Manual acceptance instructions in [account acceptance](account-acceptance.md).

Use the [validation guide](validation.md) for candidate-specific checks. The archived [candidate.1 validation record](../release/4.1.1-candidate.1/VALIDATION.md) and [candidate.2 validation record](../release/4.1.1-candidate.2/VALIDATION.md) describe their earlier artifacts and remain unchanged. A template, proposed test or earlier candidate's check is not a candidate.3 observation.

## Not established

The [candidate.3 focused retest](../release/4.1.1-candidate.3/LIVE_RETEST.md) observed both exact snippets in the first SETUP response. FINAL_VERIFY initially omitted its handoff; one corrective follow-up reproduced the 2,223-character prompt exactly. A tiny TXT control upload failed despite available displayed storage, so further uploads stopped. Candidate.2 settings were retained; candidate.3 installation and six primary fresh-chat trials were not performed. First-response handoff reliability, full Free-account compatibility and automatic runtime reading remain unestablished.

Candidate.2's focused retest on October 9, 2026 observed exact persisted Personalization values after saving and reopening both fields. With the complete package pasted after an upload failure, the installer gave manual UI guidance and supplied both exact snippets on NEXT. These observations support the settings and guidance repairs on that tested surface.

Both the package attachment and a separate standalone-runtime Library upload failed with “Unable to upload.” Candidate.2 source storage and complete runtime reading remained unestablished. A fresh diagnostic honestly reported no supported source read and answered the independent arithmetic correctly. The six-trial acceptance series was not run because its saved-source prerequisite was not established. Its installer handoff failed exactness by adding three newline characters. See the [candidate.2 focused retest summary](../release/4.1.1-candidate.2/LIVE_RETEST.md); these observations do not pass candidate.3 gates.

Private candidate.1 testing observed persisted settings and restoration that preserved unrelated preferences, but did not establish automatic runtime delivery. Its saved fields omitted the canonical terminal newlines, so strict snippet exactness failed under that candidate's contract. Three explicit fresh-chat trials included two reported access failures and one unsupported success assertion. Three ordinary-task responses were correct without sufficient evidence of runtime loading. Upload failures blocked the wrong-version test. These earlier results remain candidate.1 findings, not passing evidence for candidate.3 or a full Free-account compatibility claim; private account details and transcripts are not distributed in this repository.

The historical 4.1.0 browser connection failed before page state was returned. Earlier Mini project pilots and full Helikon 6 installation evidence concern different revisions or surfaces. They cannot satisfy this candidate's account acceptance gate.

GitHub's regular v4.0.0 release remains the project edition. This candidate does not promote account support or replace that release.
