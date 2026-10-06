# Helikon Mini 4.1.0 — start here

Mini adds compact Helikon 6-derived guidance to ordinary ChatGPT chats. Your Personalization settings provide the System Layer; one JSON file in Library provides the Operating Layer. Projects are optional. This installer replaces the old six-memory approach.

**Testing build:** live ordinary-chat automatic source access is not yet verified. This is a prompt configuration, not executable software or a guarantee of model behavior.

## Guided setup

1. Unzip the bundle. Keep its eight files together.
2. Open a normal ChatGPT chat, outside any Project and outside Temporary Chat.
3. Upload **Helikon_Mini_Install_Package.json**.
4. Send: **SETUP**.
5. Follow the guide one step at a time. It will first preserve your existing settings, then help you save the exact runtime JSON in Library and copy two separate snippets into Personalization.
6. Send **NEXT** to continue an unfinished step, **STATUS** to see what is actually verified, or **FINAL_VERIFY** to begin the fresh-chat checks.

You do not need Python, a terminal, a custom GPT or a Project. If the chat cannot extract the embedded runtime exactly, use **Helikon_Mini_Operating_Master.json** from this bundle. Do not paste the entire install package into Personalization.

## Keep existing settings

Back up the exact current contents of **Custom instructions** and **More about you** privately. Keep your personal details and unrelated preferences. The guide must review combined field lengths and conflicts before saving; it must never silently truncate them.

If you already use full Helikon, review Mini without replacing your working setup. A Mini test does not authorize overwriting full Helikon.

## Save the Operating Layer

Save or upload **Helikon_Mini_Operating_Master.json** into your account Library. Check the saved file's contents and identity. A download link alone does not prove it is stored there.

Where available, Library search is controlled under **Settings → Personalization → Advanced**. Availability and actual source access must be checked in your account. If a fresh chat cannot retrieve the exact file, use **Add from Library** as a manual fallback and record that automatic access failed.

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
