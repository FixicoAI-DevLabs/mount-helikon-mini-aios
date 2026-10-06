# Install Helikon Mini 4.0.0

Use the two matching files in the Mini 4.0.0 release: `Helikon_Mini_System.md` and `Helikon_Mini_Operating_Master.json`. The same canonical files are available at the repository root. No Python, local build or Saved Memory setup is required.

1. Download and extract `Helikon-Mini-4.0.0.zip` from https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/releases/tag/v4.0.0. Optionally compare its SHA-256 with the accompanying checksum file.
2. Create a dedicated ChatGPT project, using project-only memory where available. Keep your existing full Helikon project running separately.
3. Open Project settings. Copy the entire System file into Instructions. Save, reopen and compare the complete value with the file. If the project already has instructions, preserve a copy before replacing them.
4. Under Sources, upload the Operating Master JSON. Wait until upload completes and confirm its content is readable. A listed filename alone is insufficient.
5. Start a fresh project chat. Try an ordinary task with a checkable answer and ask which runtime source is available. The matching identities are Mini runtime `4.0.0`, schema `1.0.5`, System contract `1.0.0` and extension contract `1.0.0`. Supplying those answers to the model does not prove it read the source.

For a quick functional check, request exactly one JSON object with a simple calculated result. Then ask for a two-day schedule containing tasks of 30, 45 and 60 minutes, a 90-minute daily capacity, preserved task durations, and unused capacity left empty. Check formatting, task durations and the 135-minute total yourself.

## Evidence and scope

The project route was exercised using candidate 5 on Pro, browser ChatGPT, GPT-5.6 Sol / Medium, including exact System readback and completed source upload. Version 4.0.0 preserves those operational rules with updated identity labels. Its release validation distinguishes mechanical checks from historical live observations. Account controls may differ.

Short instructions plus a separate source are intentional. A historical attempt to embed the entire runtime exceeded the observed project Instructions capacity. Stored-file presence and a model's self-report do not expose hidden per-turn input. Complete automatic source delivery, global-chat support, free accounts and other models are unverified.

## Updating this project

Keep a copy of the project's current instructions and source. Replace both with a matching release pair, inspect saved state and use a fresh chat. If a save or upload is interrupted, inspect the result before retrying. Recovery uses your saved configuration. Other projects and account settings need no changes for this installation.

A session-only alternative can supply System guidance and the complete JSON in one conversation. It has no separate complete live pilot and makes no persistence claim.
