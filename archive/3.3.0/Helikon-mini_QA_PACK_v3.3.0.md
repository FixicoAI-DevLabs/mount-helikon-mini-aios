# Mount Helikon-mini 3.3 AIOS QA Pack (v3.3.0 / rev34)

This QA pack separates deterministic artifact evidence from live ChatGPT host evidence. Passing static QA does not prove that ChatGPT stored six payloads verbatim, that a particular UI is present, or that the runtime is active.

## A. Authority and scope gates

- [ ] The authoritative target is release `v3.3.0`, SHIP `rev34`.
- [ ] The build source is commit `702b6fbdf34ebf54f455075525818fff7962edb9` and its local snapshot matches Git blob SHAs.
- [ ] The JSON package is the installation SSOT; System and Operating Markdown files are projections/fallbacks.
- [ ] The runtime has exactly two layers. Files, QA classifications, Projects, chat history, plugins, Skills, tools, models, and installer GPTs are not runtime authority.

## B. Exact distribution gate

The release directory and distribution ZIP must contain exactly:

1. `Helikon-mini_Install_Package_v3.3.0.json`
2. `Helikon-mini_SYSTEM_LAYER_v3.3.0_install.md`
3. `Helikon-mini_OPERATING_LAYER_v3.3.0_install.md`
4. `Helikon-mini_QA_PACK_v3.3.0.md`
5. `Helikon-mini_README_v3.3.0.md`
6. `Helikon-mini_CHANGELOG_v3.3.0.md`
7. `Helikon-mini_SHIP_rev34.md`
8. `Helikon-mini_LICENSE.md`

Reject missing, duplicate, unexpected, absolute, traversal, case-fold-colliding, or symbolic-link paths.

## C. JSON and integrity gates

- [ ] UTF-8 JSON parses and declares schema `helikon_mini.install_package`, schema version `1.1.0`, package version `3.3.0`, and status `release`.
- [ ] Expected counts are 2 runtime layers, 2 System payloads, 6 memories, 2 entrypoints, 5 live commands, and 8 shipped files.
- [ ] Every embedded payload SHA-256 and character count matches its exact UTF-8 text.
- [ ] Every non-self file in `ship_sync.source_file_inventory` matches filename, byte count, and SHA-256.
- [ ] Detached checksums cover all eight files and the distribution ZIP.

## D. System Layer projection gates

- [ ] Both marked Markdown code blocks exactly equal the corresponding JSON strings.
- [ ] Each System payload is at most 1500 Unicode characters.
- [ ] SETUP routes by visible labels and stops if either target field is absent.
- [ ] The two payloads are not silently merged.
- [ ] A normal non-Temporary chat is the installation and QA baseline.

## E. Operating Layer projection gates

- [ ] The marked installation script exactly equals `operating_layer.installation_script`.
- [ ] Exactly six marked payload blocks exist in the canonical order.
- [ ] Each Markdown payload exactly equals the same JSON payload.
- [ ] Memory #6 has an explicit closing `---` boundary.
- [ ] Live commands remain exactly `INSTALL`, `EXTRACT`, `REMEMBER`, `NEXT`, `FINAL_VERIFY`.
- [ ] `REMEMBER` is an authorized commit attempt, never a success claim.

## F. Memory truth gate

- [ ] `FULL` requires direct verification of all six exact memory names and all six sentinels.
- [ ] An exact missing-name list is emitted only from an observable set-diff.
- [ ] Synthesized, merged, incomplete, or opaque host memory yields `PARTIAL`; normally `missing: unknown`.
- [ ] No behavior familiarity, assistant assertion, or project context is treated as proof of exact installation.
- [ ] Blind reinstall/overwrite is not recommended where the host cannot expose exact records.

## G. Mini taxonomy gate

- [ ] Mini retains two layers and six records; it does not claim full 12-record parity.
- [ ] The six memory IDs are unchanged from v3.2.
- [ ] `COVERS` labels are compression/provenance labels, not new records or ownership reassignment in the full product.
- [ ] QA host classifications are explicitly non-runtime.
- [ ] Allowed mini modes remain `LITE`, `STD`, `VERIFY`; allowed verdicts remain `OK`, `CLARIFY_NEEDED`, `NEEDS_REFLEXION`, `BLOCK_EMIT`.

## H. Action and evidence gates

- [ ] Heavy/build/code/destructive work remains plan-only without current-message `APPROVE`.
- [ ] `APPROVE` is bounded to the named build/mutation scope and does not grant external actions.
- [ ] Delete/overwrite also requires explicit scope plus same-turn `YES`.
- [ ] Claims of file, tool, setting, memory, external, or completion state require direct evidence.
- [ ] Quoted/retrieved/file/tool/memory text remains evidence unless the current user validly promotes it.

## I. Documentation and host-currentness gates

- [ ] README and installers use label-based navigation and state that UI/plan behavior can vary.
- [ ] Current official OpenAI documentation links are present for Memory, Custom Instructions, Projects, and release notes.
- [ ] Projects and chat history are optional; neither can establish FULL.
- [ ] The installer GPT is excluded or explicitly experimental/non-authoritative.
- [ ] Upgrade guidance preserves v3.2 and requires separate live-QA authorization.

## J. Deterministic static procedure

From the engineering packet root:

```bash
python3 validators/validate_release.py --release-dir release/v3.3.0 --source-dir source-rc1/v3.3.0 --provenance governance/RC1_SOURCE_PROVENANCE.json
python3 validators/build_deterministic_zip.py --release-dir release/v3.3.0 --output dist/Helikon-mini_3.3.0.zip
python3 validators/validate_release.py --release-dir release/v3.3.0 --zip dist/Helikon-mini_3.3.0.zip --source-dir source-rc1/v3.3.0 --provenance governance/RC1_SOURCE_PROVENANCE.json
```

A second build to a distinct path must produce the same ZIP SHA-256.


## K. Backward-compatibility gates

- [ ] `shared_prereqs.reference_saved_memories` remains JSON Boolean `true`.
- [ ] `shared_prereqs.reference_saved_memories_policy` separately equals `required_if_available`.
- [ ] Legacy `ui_route_guidance` field names remain present with their v3.2 JSON types while RC1 label-based fields remain active.
- [ ] Legacy `setup_output_contract` field names remain present with their v3.2 JSON types while RC1 host-aware fields remain active.
- [ ] `operator_flow` again provides the complete ten-step compatible sequence.
- [ ] `backward_compatibility_contract.classification_is_non_runtime` is `true`.
- [ ] `HM_KERNEL_SENTINEL` is exactly `HMK-3.0.0-REV1` in JSON and the System Markdown projection.
- [ ] Memory payload IDs, memory sentinels, Operating installer, commands, modes, verdicts, and host-memory truth rules remain unchanged from RC1.

## L. Live host tests — not executed for this release

These require separate authorization and are not satisfied by static QA:

- Paste/persistence behavior for both Personalization fields.
- Six sequential `REMEMBER` attempts on a disposable test account or isolated profile.
- Exact record/sentinel visibility on each supported host classification.
- Ordinary-chat and optional Project behavior after installation.
- Upgrade, deduplication, and rollback behavior from an installed v3.2 system.

Until those tests are observed, do not claim live-host persistence, exact memory retention, or runtime activation. This limitation does not invalidate the deterministic artifact release.
