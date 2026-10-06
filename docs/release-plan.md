# Mini 4 project-beta publication plan

Status: prepared for review; PR #9 is not merged and no Mini 4 GitHub release has been published. The proposed release makes the rebuilt Mini visible from the default repository entry point while preserving Mini 3.3 as historical material.

## Exact publication scope

| Item | Proposed value |
|---|---|
| Repository | `FixicoAI-DevLabs/mount-helikon-mini-aios` |
| Pull request | [#9](https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/pull/9), `rebuild/mini-from-helikon-6` into `main` |
| Release title | Helikon Mini 4 — Project beta (candidate 5) |
| Tag | `v4.0.0-candidate.5`, created at the verified merged commit |
| GitHub classification | Prerelease, not latest stable |
| Runtime identity | `helikon-mini.operating-master@4.0.0-candidate.5` |
| Schema identity | `helikon-mini.operating-master.schema@1.0.4` |
| ZIP asset | `Helikon-Mini-4.0.0-candidate.5.zip` — 98,043 bytes |
| Checksum asset | `Helikon-Mini-4.0.0-candidate.5.zip.sha256` |
| ZIP SHA-256 | `d4fcf46e86ba349906ce5ade1572502adbdfeec1849ff19f62b2372b0176653a` |
| Release body | [Prepared release notes](../release/4.0.0-candidate.5/RELEASE_NOTES.md) |

The candidate version is intentionally retained. The release distributes exactly the tested payload; it does not rename the runtime to beta.1 and relabel old test evidence. Publication preparation changes entry-point documentation only. The existing archive and its installation documents stay byte-identical.

## Acceptance for this limited release

The public beta offers the isolated project route for evaluation. Its evidence covers Pro, browser ChatGPT, GPT-5.6 Sol / Medium: 48 core case-runs, five supplementary probes, 24 final-candidate utility runs and three additional planning probes. The runtime was fully reconstructed from bounded source copies; exact saved System readback and completed upload were observed. Thirty-eight deterministic tests and reproducible packaging checks pass for the candidate; final publication commits require their own CI result.

This scope is narrower than stable support. Both profiles remain `experimental_unverified`. The strict source-evidence gate remains unmet because hidden full-body input was not observed on every positive turn. No validator is weakened and no unknown observation is converted to a pass. Publishing this beta accepts those stated limits for evaluation; it does not certify automatic global delivery, free accounts, other models, actual six-memory migration or general superiority. The single-response full-source-copy failure and optional extra prose/citations remain documented.

## Remaining sequence

1. Review the exact scope and assets above. Confirm the final PR head still contains the frozen payload, preserved legacy files and this publication plan. Check hosted CI for that exact head.
2. At the final publication decision, mark PR #9 ready and merge it with an expected-head check. Record the resulting commit and confirm `main` contains the reviewed runtime and package. The updated README and root `START_HERE.md` then become the repository's entry point.
3. Create a draft GitHub release for `v4.0.0-candidate.5` at that verified commit. Use the prepared title and body, mark it as a prerelease, and upload the ZIP and checksum before publishing. Inspect the draft's tag target, assets and classification.
4. Publish the prerelease. Verify the public release page and download the published ZIP through its actual asset link. Compare its checksum with the reviewed value. Verify the tag's runtime/System files and the main README's entry links.
5. Complete a fresh-project installation smoke check from that downloaded package: saved System readback, readable JSON, one exact-format task and one duration/capacity planning task. Record the publication and smoke evidence, including any failure. If bytes differ, do not claim the historical tests cover the download; resolve the discrepancy first.
6. Add the verified release link and publication receipt to the repository, replacing preparation-status wording. Keep the candidate's historical evidence unchanged.

These are sequential release actions, not evidence that publication has already happened. Merge and publication are the remaining externally visible transition. No announcement to other people is included.

## What happens to the old Mini

- `main` will point new visitors to Mini 4's project route. The six versioned Mini 3.3 root files and the `v3.3.0` tag/assets remain unchanged.
- Existing installed instructions and Saved Memories do not update automatically. The [start guide](../START_HERE.md#already-using-mini-33) explains the manual move and preserves unrelated settings.
- GitHub does not allow a prerelease to be the latest stable release. Therefore the generic `/releases/latest` route can still resolve to 3.3; new entry points must link to the explicit Mini 4 release or its versioned package. See [GitHub's release API documentation](https://docs.github.com/en/rest/releases/releases#create-a-release), `make_latest`.
- A stable Mini 4 replacement needs a separate support decision and evidence for the delivery routes it promises. Global/free-account compatibility and actual legacy migration stay open; this beta does not silently complete them.

## Recovery after publication

Keep the previous tag and assets intact. If the beta has a material defect, label the release clearly and direct new installs to a corrected revision or the historical release. Do not rewrite a published tag or swap different bytes under the same asset name. Existing downloads cannot be recalled. Account rollback follows the user's observed configuration backup and the [recovery procedure](recovery.md).
