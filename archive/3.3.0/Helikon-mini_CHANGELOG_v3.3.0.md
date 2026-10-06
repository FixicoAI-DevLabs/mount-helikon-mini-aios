# Mount Helikon-mini 3.3 AIOS Changelog

This changelog tracks the independently versioned free/open-source mini line. Full Mount Helikon versions are compatibility references only and do not determine mini's version.

## v3.3.0 — rev34 release (2026-09-04)

- Promotes the validated v3.3.0 candidate into the final public release without changing the two-layer runtime or six-memory Operating Layer.
- Advances SHIP identity from rev33 to rev34 so final release bytes do not reuse candidate identity.
- Replaces current candidate lifecycle labels and pointers with final release metadata.
- Moves the six v3.2.0 artifacts from the repository root to `release/v3.2.0/` without changing their bytes.
- Adds final deterministic archive and checksum procedures, release-oriented CI, and a tagged GitHub Release path.
- Preserves the RC1 and RC2 entries below as historical provenance.
- Live-host installation and behavioral QA remain unexecuted and must not be inferred from static release validation.

## v3.3.0 — rev33 draft candidate / RC2 (2026-09-04)

- Restores `install_package_protocols.shared_prereqs.reference_saved_memories` to Boolean `true` for backward-compatible consumers.
- Adds `reference_saved_memories_policy: required_if_available` as the separate host-aware policy field.
- Restores all v3.2 `system_layer.ui_route_guidance` and `system_layer.setup_output_contract` field names with their legacy JSON types while retaining RC1's additive label-based and missing-field rules.
- Restores the full ten-step `system_layer.operator_flow` sequence.
- Adds a non-runtime `backward_compatibility_contract` documenting the compatibility surface.
- Restores `HM_KERNEL_SENTINEL` to the independently versioned `HMK-3.0.0-REV1`; no kernel-contract change was established by the package version bump.
- Advances SHIP identity to rev33 and reruns exact projections, file hashes, source preservation, archive safety, and reproducible packaging checks.
- Preserves RC1's memory IDs, memory payload semantics/sentinels, Operating installer, host-memory truth rules, commands, modes, verdicts, and draft-candidate posture.


## v3.3.0 — rev32 draft candidate / RC1 (2026-09-04)

- Built from and preserves the exact v3.2.0 GitHub baseline at commit `702b6fbdf34ebf54f455075525818fff7962edb9`.
- Completes the canonical eight-file release family in a dedicated version directory; README and license are now exact versioned ship artifacts rather than missing root-only substitutes.
- Keeps exactly two runtime layers and the same six `Helikon-mini.*` memory IDs.
- Makes `FULL` contingent on direct inspection of all six exact records and sentinels; synthesized/merged/opaque host memory is `PARTIAL`, normally with `missing: unknown`.
- Adds QA-only host classifications without promoting them into runtime layers, modes, directives, verdicts, or authority.
- Restores the closing boundary after memory #6 and adds exact JSON ↔ Markdown projection checks.
- Reduces the visible normal-answer footer to a single confidence line and removes the always-on policy-attestation string.
- Clarifies that current-message `APPROVE` is bounded to named build/mutation work and does not authorize external actions.
- Updates UI navigation to label-based guidance, links current official host documentation, and keeps Projects/chat history optional.
- Excludes the optional installer GPT from authoritative release scope unless separately synchronized and verified.
- Adds deterministic validators, reproducible ZIP assembly, reopened-archive inspection, and detached checksums as non-shipped engineering support.
- Live ChatGPT installation, persistence, upgrade, and rollback tests remain deferred; status stays `draft_candidate`.

## v3.2.0 — rev31 draft candidate (2026-05-06)
- Advances the active public/system identity to **Mount Helikon-mini 3.2 AIOS** for the v3.2.0 behavior-hardening release.
- Selectively backports Mount Helikon 5.0 hardening patterns after re-expressing them in mini's own six-memory Operating Layer and QA surfaces.
- Adds mini-native host/model/tool capability boundary, structured-input handling, retrieval-necessity gating, claim atomization, uncertainty abstention, confidence-boundary wording, compact retention/watch-item posture, active-link shielding, and hygiene-honesty rules.
- Updates the System Layer active product-name text and short footer marker to the 3.2 line while preserving the same System Layer behavior and compact Personalization footprint intent.
- Preserves the Free Starter descriptor, 2-layer runtime, 6-memory Operating Layer, JSON-first installation SSOT, live command family, `Helikon-mini_*` filename namespace, and `Helikon-mini.*` Saved Memory namespace.
- Preserves historical 3.1 references only inside prior-release changelog/SHIP history.
- Recomputed stored System snippet hashes, Operating script hash, memory payload hashes, character counts, and source-file inventory hashes/bytes.

## v3.1.3 — rev30 draft candidate (2026-05-06)
- Name-parity and integrity repair patch on top of the 3.1.2 metadata-truth closure candidate.
- Bumped `Helikon-mini_Install_Package_v3.1.3.json` to remove remaining stale or malformed active product-name references so active install/runtime/procedure surfaces consistently use **Mount Helikon-mini 3.1 AIOS**, including the System Layer More-about-you setup heading and the embedded Operating Layer installation script.
- Bumped `Helikon-mini_SYSTEM_LAYER_v3.1.3_install.md` and `Helikon-mini_OPERATING_LAYER_v3.1.3_install.md` to keep synchronized markdown projections aligned with the JSON-first installation SSOT, including exact System snippet parity, exact Operating script parity, and normalized memory-payload boundary parity.
- Bumped `Helikon-mini_README_v3.1.3.md`, `Helikon-mini_QA_PACK_v3.1.3.md`, and `Helikon-mini_SHIP_rev30.md` to the synchronized name-parity and integrity repair candidate set.
- Bumped `Helikon-mini_CHANGELOG_v3.1.3.md` to record the repair and preserve historical 3.0 references only inside clearly historical entries.
- Recomputed stored System snippet hashes, Operating script hash, memory payload hashes, character counts, and source-file inventory hashes/bytes.
- Left the 2-layer runtime shape, the 6-memory Operating Layer, the live command family, payload IDs, memory content semantics, and `Helikon-mini.*` Saved Memory namespace unchanged.

## v3.1.2 — rev29 draft candidate (2026-04-22)
- Narrow metadata-truth closure patch on top of the 3.1.1 cleanup-closure candidate.
- Bumped `Helikon-mini_Install_Package_v3.1.2.json` to repair the remaining stale `3.1.0 draft candidate set` note inside the JSON metadata and refresh the synchronized source-file inventory for the repaired shipped set while preserving JSON-first install authority, the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity.
- Bumped `Helikon-mini_SYSTEM_LAYER_v3.1.2_install.md` and `Helikon-mini_OPERATING_LAYER_v3.1.2_install.md` only to keep the synchronized projection pointers aligned with the new JSON package line while leaving System snippet text, the 6-memory install loop, payload IDs, and memory payload text unchanged.
- Bumped `Helikon-mini_README_v3.1.2.md`, `Helikon-mini_QA_PACK_v3.1.2.md`, and `Helikon-mini_SHIP_rev29.md` to the synchronized metadata-truth closure candidate set.
- Bumped `Helikon-mini_CHANGELOG_v3.1.2.md` to record the closure patch and preserve a fully truthful shipped history surface.
- Left the 2-layer runtime shape, the 6-memory Operating Layer, the live command family, payload IDs, memory payload text, and `Helikon-mini.*` Saved Memory namespace unchanged.

## v3.1.1 — rev28 draft candidate (2026-04-21)
- Narrow cleanup-closure patch on top of the 3.1.0 Free-fit onboarding redesign candidate.
- Bumped `Helikon-mini_Install_Package_v3.1.1.json` to refresh the synchronized package pointers and source-file inventory for the repaired shipped set while preserving JSON-first install authority, the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity.
- Bumped `Helikon-mini_SYSTEM_LAYER_v3.1.1_install.md` and `Helikon-mini_OPERATING_LAYER_v3.1.1_install.md` only to keep the synchronized projection pointers aligned with the new JSON package line while leaving System snippet text, the 6-memory install loop, payload IDs, and memory payload text unchanged.
- Bumped `Helikon-mini_README_v3.1.1.md`, `Helikon-mini_QA_PACK_v3.1.1.md`, and `Helikon-mini_SHIP_rev28.md` to the synchronized cleanup-closure candidate set.
- Bumped `Helikon-mini_CHANGELOG_v3.1.1.md` to repair the malformed historical `v3.0.6 — rev20` heading and preserve a clean shipped history surface.
- Left the 2-layer runtime shape, the 6-memory Operating Layer, the live command family, payload IDs, memory payload text, and `Helikon-mini.*` Saved Memory namespace unchanged.

## v3.1.0 — rev27 draft candidate (2026-04-21)
- Free-fit onboarding and posture redesign patch on top of the 3.0.12 branding-hygiene closure candidate.
- Bumped `Helikon-mini_Install_Package_v3.1.0.json` to recast the public package posture as benefit-first while preserving JSON-first install authority, the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity.
- Bumped `Helikon-mini_SYSTEM_LAYER_v3.1.0_install.md` to keep the beginner-explicit `SETUP` truth contract while rewriting the wrapper prose around the same compact account-level posture and updating the More about you snippet to emphasize memory-backed continuity and Projects as a recommended workspace wrapper rather than merely a caveat.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.1.0_install.md` to keep the same 6-memory install loop and payload text while reframing the Operating Layer explicitly as mini's continuity layer and clarifying that the install loop is a one-time activation/repair path rather than mini's everyday identity.
- Bumped `Helikon-mini_README_v3.1.0.md` to move the public entrypoint from installer-first to benefit-first, add an explicit “Why memory matters” section, and reposition Projects as a recommended workspace wrapper while keeping plain chat as the canonical install and QA baseline.
- Bumped `Helikon-mini_QA_PACK_v3.1.0.md` to add public-posture, memory-centrality, and Projects-boundary locks while preserving bundle-integrity, separation, JSON-authority, parity, and command-family regression checks.
- Bumped `Helikon-mini_SHIP_rev27.md` to the synchronized 3.1.0 candidate set and recorded the redesign as a public-posture change rather than a runtime architecture remap.
- Left the 2-layer runtime shape, the 6-memory Operating Layer, the live command family, payload IDs, memory payload text, and `Helikon-mini.*` Saved Memory namespace unchanged.

## v3.0.12 — rev26 draft candidate (2026-04-07)
- Branding-hygiene closure patch on top of the 3.0.11 cleanup/truth-closure candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.12.json` to correct the remaining stale package-set note inside the JSON metadata so the package now consistently refers to the **3.0.12 draft candidate set** while preserving the outward product name/descriptor, the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.12_install.md` to keep the embedded installation-script package pointer synchronized with the new JSON package line while leaving payload IDs and payload text unchanged.
- Bumped `Helikon-mini_QA_PACK_v3.0.12.md`, `Helikon-mini_README_v3.0.12.md`, and `Helikon-mini_SHIP_rev26.md` to the synchronized branding-hygiene candidate set, and standardized the shipped `Helikon-mini_LICENSE.md` title to **Mount Helikon Mini 3.0 AIOS License (MIT)** while leaving the filename unchanged for namespace continuity.
- Left live commands, System Layer snippet payload text, payload IDs, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.11 — rev25 draft candidate (2026-04-07)
- Cleanup/truth-closure patch on top of the 3.0.10 branding-standardization candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.11.json` to correct the remaining stale JSON runtime-status wording so `none_state_rule` now refers to **Mount Helikon Mini 3.0 AIOS** rather than the older outward `Helikon-mini` label, while preserving the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.11_install.md` to keep the embedded installation-script package pointer synchronized with the new JSON package line while leaving payload IDs and payload text unchanged.
- Bumped `Helikon-mini_QA_PACK_v3.0.11.md` to close the stale regression-lock wording that still referenced the active surfaces as `3.0.9`, and bumped `Helikon-mini_README_v3.0.11.md` plus `Helikon-mini_SHIP_rev25.md` to the synchronized cleanup candidate set.
- Left live commands, System Layer snippet payload text, payload IDs, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.10 — rev24 draft candidate (2026-04-07)
- Branding/descriptor standardization + synchronized-surface closure on top of the 3.0.9 SETUP-to-INSTALL handoff candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.10.json` so the package now identifies the product as **Mount Helikon Mini 3.0 AIOS** and standardizes the outward descriptor as **the Free Starter operating system line for ChatGPT** while preserving the 2-layer runtime, the 6-memory Operating Layer, the live command family, and the existing `Helikon-mini_*` file namespace plus `Helikon-mini.*` Saved Memory namespace for runtime continuity.
- Bumped `Helikon-mini_SYSTEM_LAYER_v3.0.5_install.md` to mirror the same standardized product identity across the SETUP surface and pasted System Layer snippets while keeping the Custom instructions payload within limit and leaving runtime semantics unchanged.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.10_install.md` to keep the package-pointer text and outward Operating Layer labeling synchronized with the new package line while leaving payload IDs and payload text unchanged.
- Bumped `Helikon-mini_QA_PACK_v3.0.10.md`, `Helikon-mini_README_v3.0.10.md`, and `Helikon-mini_SHIP_rev24.md` to the synchronized branding-standardization candidate set.
- Left live commands, payload IDs, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.9 — rev23 draft candidate (2026-04-06)
- SETUP-to-INSTALL handoff hard-binding + synchronized-surface closure on top of the 3.0.8 memory-settings hard-binding candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.9.json` so the System Layer install authority now hard-binds the actual `SETUP` response to tell the operator, after both Personalization saves are confirmed, to return to the chat and send `INSTALL` to begin the 6-memory Operating Layer install loop while preserving the beginner-facing Personalization walkthrough, Memory-settings step, two-box mapping, and ordered save/reopen flow.
- Bumped `Helikon-mini_SYSTEM_LAYER_v3.0.4_install.md` to mirror the same hard-bound `SETUP` command surface in the synchronized human-readable projection/fallback.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.9_install.md` to keep the package-pointer text synchronized with the new JSON package line while leaving payload text and runtime semantics unchanged.
- Bumped `Helikon-mini_QA_PACK_v3.0.9.md` to fail if the actual emitted `SETUP` response omits the required post-save handoff back to chat with `INSTALL`.
- Bumped `Helikon-mini_README_v3.0.9.md` and `Helikon-mini_SHIP_rev23.md` to the synchronized closure candidate set.
- Left live commands, System Layer snippet payload text, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.8 — rev22 draft candidate (2026-04-02)
- Memory-settings hard-binding + synchronized-surface closure on top of the 3.0.7 SETUP-output hard-binding candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.8.json` so the System Layer install authority now hard-binds the actual `SETUP` response to tell the operator, before pasting the snippets, to turn **Reference saved memories** ON, treat **Reference chat history** as optional best-effort only if present, and use a normal non-Temporary chat for installation while preserving the beginner-facing Personalization walkthrough, two-box mapping, and ordered save/reopen steps.
- Bumped `Helikon-mini_SYSTEM_LAYER_v3.0.3_install.md` to mirror the same hard-bound `SETUP` command surface in the synchronized human-readable projection/fallback.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.8_install.md` to keep the package-pointer text synchronized with the new JSON package line and restore exact markdown↔JSON payload-boundary parity for the six Operating payload mirrors while leaving runtime semantics unchanged.
- Bumped `Helikon-mini_QA_PACK_v3.0.8.md` to fail if the actual emitted `SETUP` response omits the required Memory-settings step before the snippet text.
- Bumped `Helikon-mini_README_v3.0.8.md` and `Helikon-mini_SHIP_rev22.md` to the synchronized closure candidate set.
- Left live commands, System Layer snippet payload text, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.7 — rev21 draft candidate (2026-04-02)
- SETUP output hard-binding + synchronized-surface closure on top of the 3.0.6 SETUP-clarity candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.7.json` so the System Layer install authority now hard-binds the actual `SETUP` response to begin with a beginner-facing Personalization walkthrough before the snippets: plain-language explanation of Personalization as ChatGPT’s settings/customization area, profile/avatar/name-menu routing, explicit two-box mapping, explicit “do not paste both snippets into the same field” warning, and ordered save/reopen steps.
- Bumped `Helikon-mini_SYSTEM_LAYER_v3.0.2_install.md` to mirror the same hard-bound `SETUP` command surface in the synchronized human-readable projection/fallback.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.7_install.md` to keep the package-pointer text synchronized with the new JSON package line while leaving payload text and runtime semantics unchanged.
- Bumped `Helikon-mini_QA_PACK_v3.0.7.md` to fail if the actual emitted `SETUP` response omits the beginner-facing walkthrough before the snippet text.
- Bumped `Helikon-mini_README_v3.0.7.md` and `Helikon-mini_SHIP_rev21.md` to the synchronized closure candidate set.
- Left live commands, System Layer snippet payload text, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.6 — rev20 draft candidate (2026-04-02)
- SETUP clarity + synchronized-surface closure on top of the 3.0.5 command-order-truth candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.6.json` so the System Layer install authority explicitly routes first-time users to **Personalization** and the two correct paste targets (**Custom instructions** and **About you → More about you**) while leaving the runtime snippet payloads unchanged.
- Bumped `Helikon-mini_SYSTEM_LAYER_v3.0.1_install.md` to teach the same two-box SETUP path in the human-readable projection/fallback.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.6_install.md` to keep the package-pointer text synchronized with the new JSON package line while leaving payload text and runtime semantics unchanged.
- Bumped `Helikon-mini_QA_PACK_v3.0.6.md` to add an explicit SETUP-clarity lock for first-time users.
- Bumped `Helikon-mini_README_v3.0.6.md` and `Helikon-mini_SHIP_rev20.md` to the synchronized closure candidate set.
- Left live commands, System Layer snippet payload text, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.5 — rev19 draft candidate (2026-04-02)
- Command-order truth + regression-lock hardening closure on top of the 3.0.4 exact-parity candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.5.json` to align the Operating Layer live-command metadata array with the taught operator flow and refresh the synchronized source-file inventory for the v3.0.5 set.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.5_install.md` to keep the embedded installation script and package-pointer text synchronized with the new JSON package line while leaving payload text and runtime semantics unchanged.
- Bumped `Helikon-mini_QA_PACK_v3.0.5.md` to expand the command-family regression lock so it also scans for `HKS` and `HKO` in the active runtime/install/procedure surfaces.
- Bumped `Helikon-mini_README_v3.0.5.md` and `Helikon-mini_SHIP_rev19.md` to the synchronized closure candidate set.
- Left live commands, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.4 — rev18 draft candidate (2026-04-01)
- Exact payload-parity + SHIP truth closure on top of the 3.0.3 integrity-closure candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.4.json` to refresh synchronized package metadata and source-file inventory for the v3.0.4 set while leaving runtime semantics unchanged.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.4_install.md`, `Helikon-mini_QA_PACK_v3.0.4.md`, `Helikon-mini_README_v3.0.4.md`, and `Helikon-mini_SHIP_rev18.md` to the synchronized exact-parity closure candidate set.
- Restored exact markdown↔JSON parity for all six Operating payload mirrors by matching the markdown payload-block boundary text exactly.
- Fixed the stale 3.0.2 supersession wording in SHIP.
- Left live commands, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.3 — rev17 draft candidate (2026-04-01)
- Final integrity/truth closure on top of the 3.0.2 truth-polish candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.3.json` to correct stale System-layer payload-integrity metadata and refresh the synchronized source-file inventory for the v3.0.3 set.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.3_install.md`, `Helikon-mini_QA_PACK_v3.0.3.md`, `Helikon-mini_README_v3.0.3.md`, and `Helikon-mini_SHIP_rev17.md` to the synchronized integrity-closure candidate set.
- Fixed the stale shipped-files version label and duplicated/mislabeled revision-note entry in SHIP, and fixed the remaining stale 3.0.1 label in the QA command-family regression lock.
- Left runtime semantics, live commands, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.2 — rev16 draft candidate (2026-04-01)
- Final doc truth polish on top of the 3.0.1 closure candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.2.json` to correct stale package-set wording inside the JSON metadata and refresh the synchronized source-file inventory for the v3.0.2 set.
- Bumped `Helikon-mini_OPERATING_LAYER_v3.0.2_install.md`, `Helikon-mini_QA_PACK_v3.0.2.md`, `Helikon-mini_README_v3.0.2.md`, and `Helikon-mini_SHIP_rev16.md` to the synchronized truth-polish candidate set.
- Corrected the stale 3.0.0 supersession wording in SHIP and fixed the v3.0.0 changelog entry so it names `Helikon-mini_Install_Package_v3.0.0.json` rather than the later 3.0.1 file.
- Left runtime semantics, live commands, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.1 — rev15 draft candidate (2026-04-01)
- Narrow closure patch on top of the 3.0.0 draft candidate.
- Bumped `Helikon-mini_Install_Package_v3.0.1.json` and `Helikon-mini_OPERATING_LAYER_v3.0.1_install.md` to restore exact embedded Operating installation-script parity between the JSON package and markdown projection.
- Bumped `Helikon-mini_QA_PACK_v3.0.1.md` so the old-token regression scan targets only active runtime/install/procedure surfaces and no longer false-fails on explicitly historical mentions inside SHIP/changelog.
- Bumped `Helikon-mini_README_v3.0.1.md` and `Helikon-mini_SHIP_rev15.md` to the synchronized closure candidate set.
- Left runtime semantics, live commands, 2-layer runtime shape, and 6-memory Operating Layer unchanged.

## v3.0.0 — rev14 draft candidate (2026-04-01)
- Major starter-line rebase from the 2.3.7 baseline.
- Added `Helikon-mini_Install_Package_v3.0.0.json` as the **primary install artifact** and **installation SSOT**.
- Re-labeled the System and Operating `_install` files as synchronized human-readable projections / fallbacks.
- Normalized the installer command family to:
  - `SETUP`
  - `INSTALL`
  - `EXTRACT`
  - `REMEMBER`
  - `NEXT`
  - `FINAL_VERIFY`
- Retired:
  - `HMS`
  - `HMO`
- Changed the build gate token from `HK_UNLOCK` to `APPROVE`.
- Preserved the 2-layer runtime:
  - System Layer = Personalization
  - Operating Layer = 6 Helikon-mini Saved Memories
- Preserved the compact 6-memory topology rather than expanding to a 12-pillar operating layer.
- Added explicit optional Projects booster posture while keeping projects outside the normative runtime contract.
- Bumped README, QA, SHIP, and installer surfaces to the 3.0.0 candidate set.

## v2.3.7 — rev13 (2026-02-17)
- Build gate token is now `HK_UNLOCK`.
- System Layer install surface bumped to v2.3.3 (kernel sentinel update).
- Operating Layer install surface bumped to v2.3.4 (Meleteon.Builder memory update).
- QA Pack + README bumped to v2.3.7 to match shipped pointers.

## v2.3.6 — rev12 (2026-02-17)
- Operating Layer install surface bumped to v2.3.3; Aoideon.Canon memory content bumped to v2.3.2.
- Aoideon.Canon now anchors `EXPECTED_OPERATING_MEMORIES (6)` and a deterministic FULL/PARTIAL/NONE + missing-names rule to prevent hallucinated missing-name lists under PARTIAL installs.
- QA + README prompts updated to reference the anchored expected set and allow `missing: unknown` when the expected set is unavailable.

## v2.3.5 — rev11 (2026-02-17)
- Mechanical lineage renumber from the prior `0.3.x` kit series to `2.3.x` to avoid collision with archived Helikon-mini 1.x artifacts.
- Renamed shipped artifacts to `v2.3.x` and updated pointers/sentinels accordingly. No behavioral/protocol changes intended.
- Helikon-mini major versions are independent of Helikon (core) major versions.
