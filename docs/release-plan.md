# Release gate — Mini 4.1.1-candidate.3

The target is an account-wide ordinary-chat starter with two Personalization snippets and a guided installer. Project-only success cannot satisfy that claim. This candidate remains a testing build.

## Artifact gate

Validate the runtime schema and references, reviewed policy anchors, exact-byte installer projections, snippet budgets, preserved source artifacts, current and historical evidence manifests, limited public-payload residue checks and eight-file archive inventory. Run the negative regression suite and build twice with byte-identical results. CI must pass on the exact commit prepared for release.

Run the separate source checker against the exact authorized Helikon 6 source. Ordinary CI checks the public source inventory's internal consistency; it cannot authenticate a private source that is not present. Follow [source derivation](source-to-mini-map.md) and the validator command in [validation](validation.md). Do not publish private configuration to satisfy this gate.

## Live account gate

Follow [account acceptance](account-acceptance.md) on an appropriately scoped test account/configuration. Preserve active full Helikon. Record the exact candidate, plan, client, model and date, observation method, settings backups and every checkpoint.

Observe both settings saves and persisted readback, then the saved Library runtime and its complete content. Test fresh ordinary non-project, non-Temporary chats without runtime or installation-package attachments. Keep automatic lookup, manual Add from Library, Work and Project results separate. A prompt explaining a missing installer command must not also supply the runtime under test.

Run the ordinary-task first-use check, explicit source verification, four QA cases, guided installer cases and the Free-plan cases. Retain every attempt, failure and unknown. The existing sixteen-case behavior suite remains separate regression coverage. Settings persistence, source access and task behavior require separate evidence; a matching hash or a passing record checker cannot establish all three.

## Distribution and acceptance

Candidate packaging and a reviewed repository change can proceed with live cases marked not run. A regular account-wide release requires the manual gates to pass on the actual claimed surface and plan, with semantic evidence review. An incomplete or contradictory record blocks that claim.

Preserve old tags, release assets, source files and pilot records. Never rewrite v4.0.0 or the 4.1.0 testing bundle to imply they contained these repairs or passed the new tests. Use a distinct artifact version for changed bytes. Merge, tagging and release promotion are separate from preparing and reviewing the candidate branch.
