# Try Mini 4 in a dedicated ChatGPT project

Mini 4 rebuilds the compact runtime from released Helikon 6.0.0. The current package is `4.0.0-candidate.5`, proposed for a public project beta. Its live evidence covers browser ChatGPT on Pro with GPT-5.6 Sol / Medium. Other account tiers, models and ordinary global chats are outside that tested scope.

## Download

- [Mini 4 candidate ZIP](release/4.0.0-candidate.5/Helikon-Mini-4.0.0-candidate.5.zip) — open the file page and choose **Download raw file**.
- [SHA-256 checksum](release/4.0.0-candidate.5/Helikon-Mini-4.0.0-candidate.5.zip.sha256).
- [Observed results and known limits](release/4.0.0-candidate.5/browser-pilot-05/README.md).

The ZIP is 98,043 bytes. Its SHA-256 is `d4fcf46e86ba349906ce5ade1572502adbdfeec1849ff19f62b2372b0176653a`. No Python, command-line tool or local build is required to install these files.

## Install

1. Download and extract the ZIP. Use `Helikon_Mini_System.md` and `Helikon_Mini_Operating_Master.json` from that same package.
2. Create a separate ChatGPT project with project-only memory. Keep the project you currently use for full Helikon intact.
3. Open the System file as plain text. Copy its complete contents into the new project's Instructions. Save, reopen the setting and compare the complete text with the file.
4. Upload the Operating Master JSON under project Sources. Wait for upload completion and confirm its content is readable.
5. Open a fresh chat in that project. Try a normal task with a checkable answer. Ask what runtime source is available and have it report missing or mismatched content honestly. A filename or the model's assurance alone does not prove a complete read.

The ZIP's `START_HERE.md` contains the detailed tested installation procedure. See [installation details](docs/install.md), [support boundaries](docs/support-matrix.md) and [recovery](docs/recovery.md). Account controls may differ from the recorded test environment.

## Already using Mini 3.3?

This is a manual move to a project-based edition. A repository update or downloaded ZIP cannot update instructions or Saved Memories already in your ChatGPT account.

1. Preserve a copy of the old Mini configuration and any relevant personal settings you can actually inspect.
2. Try Mini 4 in a separate project before retiring the old setup. Do not paste the Mini 3.3 install-package JSON or its six memory bodies into the new project.
3. Check representative real tasks and look for conflicting legacy guidance. Do not assume old global guidance has disappeared merely because a new project exists.
4. If you choose to retire Mini 3.3, identify each Mini-owned setting or memory and its dependencies before removing it. Preserve unrelated preferences and full Helikon settings. Actual migration of the six Saved Memories has not been live-tested; there is no bulk-delete or automatic migration tool.
5. If the new setup is unsuitable, stop using the Mini project and restore any settings you deliberately changed from their observed backups. Verify the restored state; do not delete unrelated project work.

[Mini 3.3's release](https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/releases/tag/v3.3.0) stays available for historical reference. See the complete [migration procedure](docs/migration.md).

## What the beta means

The candidate passed its recorded core behavior criteria and targeted planning regressions. Hidden complete-runtime delivery on every turn is unverified, the strict source-evidence gate remains unmet, and general benefit over a concise baseline is unproven. Both machine-readable profiles remain `experimental_unverified`. The publication proposal is for voluntary project evaluation, with no stable or global/free-account support claim.
