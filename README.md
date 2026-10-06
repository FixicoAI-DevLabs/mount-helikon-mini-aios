# Mount Helikon Mini

<p align="left">
  <a href="CHANGELOG.md"><img alt="Mount Helikon Mini 4.1.0" src="https://raw.githubusercontent.com/FixicoAI-DevLabs/mount-helikon-mini-aios/main/assets/badges/version.png" width="157" height="20"></a>
  <img alt="Line: Free Starter" src="https://raw.githubusercontent.com/FixicoAI-DevLabs/mount-helikon-mini-aios/main/assets/badges/line.png" width="109" height="20">
  <a href="release/4.1.0/"><img alt="Release: 4.1.0 testing build" src="https://raw.githubusercontent.com/FixicoAI-DevLabs/mount-helikon-mini-aios/main/assets/badges/release.png" width="166" height="20"></a>
  <a href="#two-layers"><img alt="Runtime: 2 layers, JSON Operating" src="https://raw.githubusercontent.com/FixicoAI-DevLabs/mount-helikon-mini-aios/main/assets/badges/runtime.png" width="150" height="20"></a>
  <a href="START_HERE.md"><img alt="Install: Guided JSON" src="https://raw.githubusercontent.com/FixicoAI-DevLabs/mount-helikon-mini-aios/main/assets/badges/install.png" width="127" height="20"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://raw.githubusercontent.com/FixicoAI-DevLabs/mount-helikon-mini-aios/main/assets/badges/license.png" width="83" height="20"></a>
</p>

**Start here:** [🚀 Quickstart](#start-here) · [🧠 How Mini works](#two-layers) · [🧩 Runtime contract](docs/architecture.md) · [🛠️ Troubleshooting](docs/recovery.md) · [✅ QA](Helikon_Mini_QA.md)

**Helikon 6-derived JSON guidance, with account-wide Personalization and a guided installer for ordinary ChatGPT chats.** Mini is a free, open-source starter. Projects are optional.

The 4.1.0 implementation restores the setup model used by Mini 3.3: two Personalization snippets, one guided install package and an eight-file download. The Operating Layer is now a compact JSON runtime instead of six Saved Memories. The project-only 4.0 release did not preserve that setup model.

**Status:** the corrected installer is available here for review and testing. Live account installation and fresh ordinary-chat automatic Library access remain unverified. The published 4.0 release is the earlier project edition; it is not the account-wide installer described here. Do not treat a project test as proof of ordinary-chat support.

## Start here

1. Download [the 4.1.0 testing bundle](release/4.1.0/Helikon-Mini-4.1.0.zip) and unzip it.
2. Open a normal, non-Temporary ChatGPT chat. Upload **Helikon_Mini_Install_Package.json** and send **SETUP**.
3. Follow the guided steps to back up existing settings, save the runtime JSON in Library, and install the two Personalization snippets.
4. Run **FINAL_VERIFY** in a fresh ordinary chat. Keep automatic Library access, manual file attachment and Project results separate.

See [START_HERE](START_HERE.md), [installation details](docs/install.md) and [QA checks](Helikon_Mini_QA.md). No terminal or Python is required to install. If full Helikon already runs on your account, keep it in place while reviewing Mini; this installer must not replace it merely to perform a test.

## Two layers

| Layer | Where it lives | Purpose |
|---|---|---|
| System | Custom instructions + More about you | Account-wide guidance and an explicit runtime designation |
| Operating | Helikon_Mini_Operating_Master.json saved in Library | Complete compact Helikon 6-derived rules and procedures |

Each shipped Personalization snippet fits within 1,500 characters. Existing profile text must be preserved and the combined field length reviewed. The installer contains the exact snippets and exact runtime bytes; generated companion files are checked against it.

A saved file is not evidence that every chat has read it. The installer attempts supported Library access, checks all identity pairs and complete content, and discloses missing access. Manual **Add from Library** is an explicit fallback, not a passing automatic-access test. No Saved Memory installation, mandatory footer or universal APPROVE ritual is required.

## Repository

- [Architecture and 3.3-to-4.1 mapping](docs/architecture.md)
- [Support boundaries](docs/support-matrix.md) and [implementation status](docs/implementation-status.md)
- [Validation](docs/validation.md), [release gate](docs/release-plan.md) and [recovery](docs/recovery.md)
- [Helikon 6 source mapping](docs/source-to-mini-map.md)
- [Unchanged Mini 3.3 files](archive/3.3.0/) and historical [release evidence](release/)

Development: `python3 tools/mini.py render`, `python3 tools/mini.py validate`, `python3 -m unittest discover -s tests -v`, then `python3 tools/mini.py build --out build`. These check artifacts and evidence consistency; they do not operate or authenticate a ChatGPT account.

Licensed under [MIT](LICENSE).
