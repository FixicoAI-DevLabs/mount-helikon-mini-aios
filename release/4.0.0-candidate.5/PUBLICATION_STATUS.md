# Mini 4 publication status — October 6, 2026

**Published:** [Helikon Mini 4 — Project beta (candidate 5)](https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/releases/tag/v4.0.0-candidate.5), October 6, 2026 at 13:48:40 UTC. The repository update, prerelease publication and public-download verification are complete. Existing account migration is outside this task. The additional fresh ChatGPT installation smoke check remains unrun because browser access was unavailable.

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

## Earlier browser blocker and retained attempts

The connected GitHub interface could merge the PR and inspect releases, but exposes no create-release, create-tag or release-asset-upload action. Browser initialization failed three times: documentation restoration, surface inventory after reset, and a direct attempt to open the repository's release editor. Each returned `js execution timed out; kernel reset, rerun your request`. The direct attempt produced no usable page or confirmed UI action. No draft release, tag creation, upload or publish action was submitted through the browser.

A GitHub release-list read during that earlier blocked session still returned only `v3.3.0`. There was no fresh-project installation attempt. The earlier candidate-5 installation and behavioral results remain their original evidence.

## Publication completed through GitHub Actions

A repository-native publishing workflow on `release/mini-project-beta` used repository-scoped `contents: write` permission for its publishing job. It fixed the target commit, title, prerelease classification and exact two asset names/hashes; it does not overwrite conflicting tags, releases or assets. The original validation workflow and repository permission settings were not changed.

[Workflow run 37473490390](https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/actions/runs/37473490390), attempt 1, created draft release ID `404775395` but stopped because its immediate list read did not return the draft. A separate API read subsequently confirmed the draft, exact target and empty asset inventory. Attempt 2 resumed that draft, uploaded and byte-checked both assets, then published it. The failure and consumed attempt remain in the run history.

The successful job reran all 38 deterministic tests, rebuilt the exact 98,043-byte ZIP, checked the target Git tree, verified each uploaded draft asset before publishing, resolved the public tag to the approved merge commit, and downloaded both public asset URLs without authentication. Their bytes matched the local approved files; ZIP inventory/member checks also passed. Separate connector reads confirmed the public release, tag target and asset digests.

See [publication-receipt.json](publication-receipt.json) for the exact URLs, hashes, target, workflow and observation scope. The main README and start guide now link directly to the published package.

Runtime support remains experimental and project-scoped. No fresh post-publication ChatGPT installation result is claimed. This limitation does not change the exact prior installation/behavior evidence or the verified identity of the released package.
