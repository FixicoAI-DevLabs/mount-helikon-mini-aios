# Mount Helikon Mini

<p align="left">
  <a href="CHANGELOG.md"><img alt="Mount Helikon Mini 4.1.1-candidate.2" src="https://img.shields.io/badge/Mount%20Helikon%20Mini-4.1.1-candidate.2-blue"></a>
  <img alt="Line: Free Starter" src="https://img.shields.io/badge/line-Free%20Starter-2ea44f">
  <a href="release/4.1.1-candidate.2/"><img alt="Release: 4.1.1-candidate.2 testing build" src="https://img.shields.io/badge/release-4.1.1-candidate.2%20testing%20build-orange"></a>
  <a href="#two-layers"><img alt="Runtime: 2 layers, JSON Operating" src="https://img.shields.io/badge/runtime-2%20layers%20%7C%20JSON%20Operating-purple"></a>
  <a href="START_HERE.md"><img alt="Install: Guided JSON" src="https://img.shields.io/badge/install-Guided%20JSON-informational"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-green"></a>
</p>

**Start here:** [🚀 Quickstart](#start-here) · [🧠 How Mini works](#two-layers) · [🧩 Runtime contract](docs/architecture.md) · [🛠️ Troubleshooting](docs/recovery.md) · [✅ QA](Helikon_Mini_QA.md)

**Helikon 6-derived JSON guidance, with account-wide Personalization and a guided installer for ordinary ChatGPT chats.** Mini is a free, open-source starter. Projects are optional.

The 4.1 line restores the setup model used by Mini 3.3: two Personalization snippets, one guided install package and an eight-file download. The Operating Layer is now a compact JSON runtime instead of six Saved Memories. The project-only 4.0 release did not preserve that setup model.

**Status:** this is the 4.1.1-candidate.2 repair candidate for review and testing, not a new regular release. Live account installation and fresh ordinary-chat automatic Library access remain unverified. The published 4.0 release is the earlier project edition; it is not the account-wide installer described here. Do not treat a project test as proof of ordinary-chat support.

## Start here

1. Download [the 4.1.1-candidate.2 testing bundle](release/4.1.1-candidate.2/Helikon-Mini-4.1.1-candidate.2.zip) and unzip it.
2. Open a normal, non-Temporary ChatGPT chat. Upload **Helikon_Mini_Install_Package.json** and send **SETUP**.
3. Follow the guided steps to back up existing settings, save the runtime JSON in Library, and install the two Personalization snippets.
4. Send **FINAL_VERIFY** in the installer chat. It supplies a complete prompt to paste into a fresh ordinary, non-project, non-Temporary chat. Attach neither the runtime nor the install package to that primary automatic-access test; do not send a bare command in the fresh chat. Keep automatic access, manual attachment and Project results separate.

See [START_HERE](START_HERE.md), [installation details](docs/install.md) and [QA checks](Helikon_Mini_QA.md). No terminal or Python is required to install. If full Helikon already runs on your account, keep it in place while reviewing Mini; this installer must not replace it merely to perform a test.

## Two layers

| Layer | Where it lives | Purpose |
|---|---|---|
| System | Custom instructions + More about you | Account-wide guidance and an explicit runtime designation |
| Operating | Helikon_Mini_Operating_Master.json saved in Library | Complete compact Helikon 6-derived rules and procedures |

The two snippets have design budgets of 1,100 and 900 characters. These are engineering budgets, not observed host limits. Check the actual account limit and complete combined field length. Preserve each Mini snippet verbatim and retain unrelated text; if it does not fit, leave the saved field unchanged until the user chooses an explicit resolution. The canonical snippets omit a terminal newline; their internal line breaks are significant. The installer contains the exact snippets and exact runtime bytes; generated companion files are checked against it.

The installer supports an operator-assisted path: when the chat cannot edit settings itself, it provides concrete UI steps and separate copyable snippets. Reported saves remain distinct from direct readback. Unverified source access stays visible even when independent settings steps can proceed.

A saved file is not evidence that every chat has read it. Before the first substantive answer in each chat, the installed guidance requires an attempt at a complete supported read of the designated runtime and verification of all four identity pairs; lost text or source changes require a refresh. Missing access is disclosed while independent help can continue. Manual **Add from Library** is an explicit fallback, not a passing automatic-access test. No Saved Memory installation, mandatory footer or universal APPROVE ritual is required.

## Repository

- [Architecture and 3.3-to-4.1 mapping](docs/architecture.md)
- [Support boundaries](docs/support-matrix.md) and [implementation status](docs/implementation-status.md)
- [Validation](docs/validation.md), [account acceptance tests](docs/account-acceptance.md), [release gate](docs/release-plan.md) and [recovery](docs/recovery.md)
- [Helikon 6 source mapping](docs/source-to-mini-map.md)
- [Unchanged Mini 3.3 files](archive/3.3.0/) and historical [release evidence](release/)

Development: `python3 tools/mini.py render`, `python3 tools/mini.py validate`, `python3 -m unittest discover -s tests -v`, then `python3 tools/mini.py build --out build`. These check artifacts and evidence consistency; they do not operate or authenticate a ChatGPT account.

Licensed under [MIT](LICENSE).
