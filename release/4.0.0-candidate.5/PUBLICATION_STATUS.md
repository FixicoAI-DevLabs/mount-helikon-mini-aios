# Mini 4 publication status — October 6, 2026

The user approved the reviewed project-beta publication proposal. The repository update is complete; GitHub prerelease publication and its fresh-download installation smoke check are pending.

## Observed completed work

- [PR #9](https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/pull/9) was marked ready and merged with an expected-head check against `c4d847762dd3d4375b573eafeccccc335c8e6a65`.
- Merge commit: `733a9d5ff2a7eda17e4adc8cddd7cacada6a0f12`. GitHub subsequently reported PR #9 merged and `main` at that commit.
- Its Git tree is `61bac510d20626c05305c70cc6acec1cba4ca216`, identical to the reviewed PR tree.
- [Hosted CI run 37470386186](https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/actions/runs/37470386186) completed successfully for the merge commit. This is separate from the previously passing PR-head run.
- Local working files were clean before publication. The ZIP, runtime and System SHA-256 values were rechecked and still match the frozen candidate-5 package.

| Artifact | SHA-256 |
|---|---|
| `Helikon-Mini-4.0.0-candidate.5.zip` | `d4fcf46e86ba349906ce5ade1572502adbdfeec1849ff19f62b2372b0176653a` |
| `Helikon_Mini_Operating_Master.json` | `21f2635f72b3e519d4d25041ef968d2b121df4e8bfb5552a0cc595374c02e378` |
| `Helikon_Mini_System.md` | `f8432f2f677cca9c95d4a813e4609586eed067e545ff397fcc5b99de56d5ea3f` |

The documentation update containing this record does not change those payload files or historical test evidence. The six protected Mini 3.3 files are unchanged in the merged reviewed tree.

## Publication blocker and retained attempts

The connected GitHub interface could merge the PR and inspect releases, but exposes no create-release, create-tag or release-asset-upload action. Browser initialization failed three times: documentation restoration, surface inventory after reset, and a direct attempt to open the repository's release editor. Each returned `js execution timed out; kernel reset, rerun your request`. The direct attempt produced no usable page or confirmed UI action. No draft release, tag creation, upload or publish action was submitted through the browser.

A subsequent GitHub release-list read still returned only `v3.3.0`. No Mini 4 release is claimed. There was no fresh-project installation attempt in this publication session. The earlier candidate-5 installation and behavioral results remain their original evidence, not a replacement for the pending download test.

## Resume from here

1. Restore a working supported GitHub release interface. Inspect releases and tags first to resolve any intervening changes; do not blindly duplicate publication.
2. Create the prerelease `v4.0.0-candidate.5` at the verified merge commit above, using [RELEASE_NOTES.md](RELEASE_NOTES.md). Upload the [ZIP](Helikon-Mini-4.0.0-candidate.5.zip) and [checksum](Helikon-Mini-4.0.0-candidate.5.zip.sha256), inspect the draft, then publish.
3. Download the actual published asset, verify the frozen checksum and tag target, then perform the approved fresh-project installation smoke check.
4. Replace pending-publication wording with the verified release URL and append the actual download/installation evidence. Preserve this interruption history and all earlier failures.

The existing approval covers this sequence within the [release plan](../../docs/release-plan.md). Runtime support remains experimental and project-scoped. Do not promote stable/global/free-account support or alter the frozen bytes as a workaround for interface failure.
