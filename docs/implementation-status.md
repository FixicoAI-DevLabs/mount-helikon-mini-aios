# Implementation status — 4.1.1-candidate.1

This testing candidate repairs the reviewed 4.1.0 account installer. It retains two Personalization snippets, compact Helikon 6-derived runtime JSON and an eight-file end-user bundle. Projects remain optional. Runtime policy is unchanged apart from identity; System delivery and evidence tooling have changed.

## Implemented scope

- Exact-byte runtime handling and generated projection checks.
- Non-overwriting installation-record creation and explicitly versioned evidence records.
- Host metadata, observation methods, backup state and all eight installer checkpoints.
- Shorter snippets with explicit combined-field length checks and preservation of existing settings.
- Self-contained fresh ordinary-chat verification, separate from the installer conversation.
- Explicit immutable historical evidence bindings plus a current candidate-4/5 inventory.
- Source-inventory consistency checks, targeted negative tests and limited residue scanning of the complete distributed payload.
- Manual acceptance instructions in [account acceptance](account-acceptance.md).

Exact executed checks and remaining limitations are recorded in the [candidate validation record](../release/4.1.1-candidate.1/VALIDATION.md). A template or a proposed test is not an observation.

## Not established

Live installation, automatic full-runtime Library reading in fresh ordinary chats, Free-account compatibility and installer-driven host behavior remain unverified for this candidate. No account settings were changed during these repository repairs.

The historical 4.1.0 browser connection failed before page state was returned. Earlier Mini project pilots and full Helikon 6 installation evidence concern different revisions or surfaces. They cannot satisfy this candidate's account acceptance gate.

GitHub's regular v4.0.0 release remains the project edition. This candidate does not promote account support or replace that release.
