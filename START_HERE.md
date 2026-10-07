# Helikon Mini 4.1.1-candidate.1 — start here

Mini adds compact Helikon 6-derived guidance to ordinary ChatGPT chats. Your Personalization settings provide the System Layer; one JSON file in Library provides the Operating Layer. Projects are optional. This installer replaces the old six-memory approach.

**Repair candidate, not a regular release:** live ordinary-chat automatic source access is not yet verified. The latest regular release is the earlier 4.0 project edition. This is a prompt configuration, not executable software or a guarantee of model behavior.

## Guided setup

1. Unzip the bundle. Keep its eight files together.
2. Open a normal ChatGPT chat, outside any Project and outside Temporary Chat.
3. Upload **Helikon_Mini_Install_Package.json**.
4. Send: **SETUP**.
5. Follow the guide one step at a time. It will first preserve your existing settings, then help you save the exact runtime JSON in Library and copy two separate snippets into Personalization.
6. In this installer chat, send **NEXT** to continue an unfinished step, **STATUS** to see what is verified, or **FINAL_VERIFY** to obtain the complete fresh-chat test prompt below.
7. Open a new ordinary, non-project, non-Temporary chat and paste that whole prompt. Attach neither the runtime nor the install package. A bare **FINAL_VERIFY** has no defined protocol in that new chat.

You do not need Python, a terminal, a custom GPT or a Project. If the chat cannot extract the embedded runtime exactly, use **Helikon_Mini_Operating_Master.json** from this bundle. Do not paste the entire install package into Personalization.

## Keep existing settings

Back up the exact current contents of **Custom instructions** and **More about you** privately. Keep your personal details and unrelated preferences. The guide must preserve the Mini snippets verbatim and review conflicts and each complete combined field against the actual account limit. Snippet budgets are 1,100 and 900 characters. If existing text plus the snippet does not fit, the existing saved field stays unchanged until you choose an explicit resolution; the guide must never silently truncate or rewrite either snippet.

If you already use full Helikon, review Mini without replacing your working setup. A Mini test does not authorize overwriting full Helikon.

## Save the Operating Layer

Save or upload **Helikon_Mini_Operating_Master.json** into your account Library. Check the saved file's contents and identity. A download link alone does not prove it is stored there.

Where available, Library search is controlled under **Settings → Personalization → Advanced**. Availability and actual source access must be checked in your account. If a fresh chat cannot retrieve the exact file, use **Add from Library** as a manual fallback and record that automatic access failed.

## Fresh-chat source prompt

This prompt is copied from `installer/contract.json` → `fresh_chat_handoff.prompt`. Use it only after the installer has checked the saved settings and runtime. Keep the actual fresh-chat tool results; the answer alone is not proof of a complete read.

<!-- FRESH_CHAT_HANDOFF_BEGIN -->
```text
Check my installed Helikon Mini source access in this fresh ordinary, non-project, non-Temporary chat. Do not change settings or files. Use the runtime designation already in my Personalization; if it is missing or ambiguous, report that instead of guessing. No runtime or installation-package file is attached for this automatic-access test.
Locate that exact runtime through supported Library tools and read its entire exact text in bounded complete ranges before your first substantive answer. Verify all four identity pairs against the installed designation. Report the observed source reference, observed pairs, complete coverage or missing ranges, and any access failure. Keep the actual source-tool results available as evidence. A filename, hash, remembered summary, marker or your own activation claim cannot prove a complete read.
Do not attach or request attachment of either file to make this primary test pass. Record failed automatic access before any separately labelled manual fallback. Distinguish source access from settings persistence and tested behavior; do not claim account-wide installation passed from this source check alone. Regardless of source availability, also calculate 17 + 25 as an independent task.
```
<!-- FRESH_CHAT_HANDOFF_END -->

Run the separate behavior cases in [Helikon_Mini_QA.md](Helikon_Mini_QA.md) afterward. An explicit source prompt checks requested retrieval; a separate first-use test is needed to establish reading triggered by an ordinary task.

## What is in the download?

| File | Use |
|---|---|
| START_HERE.md | This guide |
| Helikon_Mini_Install_Package.json | Upload this and send SETUP; authoritative install content |
| Helikon_Mini_System.md | The two separate copyable Personalization snippets |
| Helikon_Mini_Operating_Master.json | Exact runtime-only JSON to save in Library |
| Helikon_Mini_QA.md | Fresh ordinary-chat checks |
| MANIFEST.json | File sizes, identities and checksums |
| CHANGELOG.md | Version history |
| LICENSE | MIT license |

The package and companion files must agree. If they disagree, stop the dependent installation step and obtain a matching bundle. **REMEMBER** explains the retired memory route; it does not write or delete memories. **RESTORE** uses your private backup to undo only authorized Mini settings edits; it does not delete your files.
