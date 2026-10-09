# Implementation status — 4.1.1-candidate.2

This revised testing candidate addresses installation guidance, exact snippet boundaries and source-evidence gaps identified while testing 4.1.1-candidate.1. It retains two Personalization snippets, compact Helikon 6-derived runtime JSON and an eight-file end-user bundle. Projects remain optional. Runtime policy is unchanged apart from identity; System delivery and evidence tooling have changed.

## Implemented scope

- Exact-byte runtime handling and generated projection checks.
- Non-overwriting installation-record creation and explicitly versioned evidence records.
- Host metadata, observation methods, backup state and all eight installer checkpoints.
- Shorter snippets with explicit combined-field length checks and preservation of existing settings.
- Canonical snippet strings without terminal newlines, checked as exact newline-bounded blocks without trimming saved fields.
- Operator-assisted manual UI installation when direct host writes are unavailable, with action attribution and persisted readback requirements.
- Self-contained fresh ordinary-chat verification, separate from the installer conversation.
- Separate source-access assertions, actual returned source text, coverage evidence and manual diagnostics.
- Per-attempt task-output, source-delivery and observability dimensions alongside the unchanged v2 record schema.
- Explicit immutable historical evidence bindings plus a current candidate-4/5 inventory.
- Source-inventory consistency checks, targeted negative tests and limited residue scanning of the complete distributed payload.
- Manual acceptance instructions in [account acceptance](account-acceptance.md).

Use the [validation guide](validation.md) for candidate-specific checks. The archived [candidate.1 validation record](../release/4.1.1-candidate.1/VALIDATION.md) describes that earlier artifact only and remains unchanged. A template, proposed test, or earlier candidate's check is not a candidate.2 observation.

## Not established

Candidate.2's focused retest on October 9, 2026 observed exact persisted Personalization values after saving and reopening both fields. With the complete package pasted after an upload failure, the installer gave manual UI guidance and supplied both exact snippets on NEXT. These observations support the settings and guidance repairs on that tested surface.

Both the package attachment and a separate standalone-runtime Library upload failed with “Unable to upload.” Candidate.2 source storage and complete runtime reading remain unestablished. A fresh diagnostic honestly reported no supported source read and answered the independent arithmetic correctly. The six-trial acceptance series was not run because its saved-source prerequisite was not established. Full installation, automatic runtime delivery and Free-account compatibility remain unverified. See the [focused retest summary](../release/4.1.1-candidate.2/LIVE_RETEST.md); it does not promote this candidate.

Private candidate.1 testing observed persisted settings and restoration that preserved unrelated preferences, but did not establish automatic runtime delivery. Its saved fields omitted the canonical terminal newlines, so strict snippet exactness failed under that candidate's contract. Three explicit fresh-chat trials included two reported access failures and one unsupported success assertion. Three ordinary-task responses were correct without sufficient evidence of runtime loading. Upload failures blocked the wrong-version test. These earlier results remain candidate.1 findings, not passing evidence for candidate.2 or a full Free-account compatibility claim; private account details and transcripts are not distributed in this repository.

The historical 4.1.0 browser connection failed before page state was returned. Earlier Mini project pilots and full Helikon 6 installation evidence concern different revisions or surfaces. They cannot satisfy this candidate's account acceptance gate.

GitHub's regular v4.0.0 release remains the project edition. This candidate does not promote account support or replace that release.
