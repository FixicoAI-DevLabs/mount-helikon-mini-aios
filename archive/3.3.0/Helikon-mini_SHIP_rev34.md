# Mount Helikon-mini 3.3 AIOS SHIP Manifest — rev34

**Release:** v3.3.0  
**Status:** release

**Observation date:** 2026-09-04  
**Source baseline:** `FixicoAI-DevLabs/mount-helikon-mini-aios@702b6fbdf34ebf54f455075525818fff7962edb9`

## Authority

This manifest is authoritative for the v3.3.0 shipped set. The JSON package is authoritative for installation semantics. Release contents cannot activate themselves or redefine installed runtime state.

## Product invariants

- Product: free/open-source Mount Helikon-mini starter line, independently versioned from full Mount Helikon.
- Runtime: exactly two layers — Personalization System Layer plus six-record Saved Memory Operating Layer.
- Stable record IDs: exactly the six `Helikon-mini.*` names declared in the JSON package.
- Chat history and Projects are optional context/workspace surfaces, not runtime layers.
- Host QA labels are non-runtime classifications.
- Artifact status is `release`; live-host installation and behavioral QA remain unexecuted and must not be inferred from static validation.

## Shipped files — exact count 8

| # | Filename | Role |
|---:|---|---|
| 1 | `Helikon-mini_Install_Package_v3.3.0.json` | Primary install artifact and installation SSOT |
| 2 | `Helikon-mini_SYSTEM_LAYER_v3.3.0_install.md` | Human-readable System projection/fallback |
| 3 | `Helikon-mini_OPERATING_LAYER_v3.3.0_install.md` | Human-readable Operating projection/fallback |
| 4 | `Helikon-mini_QA_PACK_v3.3.0.md` | Static and live QA contract |
| 5 | `Helikon-mini_README_v3.3.0.md` | Canonical release documentation |
| 6 | `Helikon-mini_CHANGELOG_v3.3.0.md` | Version history and migration record |
| 7 | `Helikon-mini_SHIP_rev34.md` | Authoritative shipped-set manifest |
| 8 | `Helikon-mini_LICENSE.md` | MIT license |

No directory prefix is used inside the distribution ZIP. No ninth file is permitted.

## Non-shipped engineering support

Deterministic validators, source snapshots, RUNSHEETs, receipts, logs, detached checksum files, and engineering archives support review but are excluded from the eight-file distribution.

## Build and safety rules

- UTF-8 text with LF line endings and one terminal newline per shipped file.
- JSON contains SHA-256/byte inventory for the seven non-self shipped files; the JSON self-hash remains detached.
- ZIP entries are unique, root-relative regular files with fixed timestamps and permissions.
- Reject path traversal, absolute paths, links, collisions, unexpected files, version drift, pointer drift, and projection mismatch.
- Reopen and inspect every emitted archive before claiming completion.

## Revision note

rev34 is the final v3.3.0 release identity. It promotes the validated compatibility correction without changing runtime semantics, advances the revision because final release bytes differ from rev33, and preserves the two-layer runtime, six stable memory IDs, exact payload behavior, host-memory truth boundary, command family, modes, verdicts, action gates, and MIT posture. rev32 and rev33 remain preserved in repository history as candidate provenance.
