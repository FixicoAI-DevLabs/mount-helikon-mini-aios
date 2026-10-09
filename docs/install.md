# Install Helikon Mini 4.1.1-candidate.3

Use [START_HERE](../START_HERE.md) for the beginner flow. The primary input is [Helikon_Mini_Install_Package.json](../Helikon_Mini_Install_Package.json): upload it in an ordinary non-Temporary chat and send **SETUP**. The install package embeds both exact Personalization snippets, the complete runtime text and the guided protocol.

## Guided commands

| Command | Action |
|---|---|
| SETUP | Check the complete package, show both exact snippet previews immediately, inspect capabilities and prepare the private settings backup |
| EXTRACT | Produce the exact runtime JSON, or use its byte-identical bundle copy |
| INSTALL | Save the runtime to Library and guide the two Personalization edits |
| NEXT | Resume the next unfinished observed checkpoint |
| FINAL_VERIFY | In the installer chat, check settings and supply the complete prompt for a separate fresh-chat source test |
| STATUS | Separate observed, reported, unknown and failed steps |
| RESTORE | Restore only authorized Mini changes from the exact prior backup |
| REMEMBER | Explain that JSON replaces the old six-memory runtime; perform no memory writes |

## Personalization

[Helikon_Mini_System.md](../Helikon_Mini_System.md) provides two separate copyable blocks. The source templates are maintained in `installer/`; generated copies must match exactly. The Custom instructions snippet has a 1,100-character design budget and the profile snippet a 900-character budget. These are engineering budgets, not observed account limits. Observe the actual limit and count the complete proposed field, including existing text and separators.

Retain each snippet verbatim, preserve existing details and resolve conflicts explicitly. If the combined field does not fit, leave the saved value unchanged and show the unresolved count and proposed changes for the user to decide. Do not silently shorten the Mini snippet or discard unrelated content. A modified snippet needs a separately versioned and validated package; the checker requires the canonical snippet exactly at line boundaries. This candidate omits the terminal newline from each snippet; internal line breaks remain significant, and verification never trims text.

Full Helikon and Mini are different configurations. If full Helikon already runs on the account, preserve it during a Mini preview or test unless the user specifically scoped its replacement.

## Runtime source

Save the standalone JSON in Library and verify the actual saved item. Do not designate the installer JSON, a Markdown projection, a memory summary or a different runtime version as Operating. An observed stable source reference can be added privately when available; no account-specific ID is shipped.

Before the first substantive answer in each fresh ordinary chat, the installed guidance requires an attempt at complete supported reading of the designated source and all four identity checks. Lost required text or an observed source change requires a refresh. Missing access must be disclosed; independent tasks can continue. Inspect the actual **Settings → Personalization** controls and the visible Library search label, if available; do not assume an Advanced section exists. If automatic access fails, the assistant must say so; **Add from Library** is a manual fallback and must be recorded separately. A file being stored does not prove its complete content was read.

The host documentation describes [account-wide Custom Instructions](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions) and [Library storage, search controls and manual attachment](https://help.openai.com/en/articles/20001052-file-storage-and-library-in-chatgpt). These features do not establish successful Mini delivery on an untested account.

## Verification and optional Projects

Run **FINAL_VERIFY in the original installer chat**. It displays the complete `fresh_chat_handoff.prompt` from the contract; [the QA sheet](../Helikon_Mini_QA.md) and [START_HERE](../START_HERE.md) contain the same prompt. The protocol 2.3.0 prompt is one logical line with no outer whitespace, CR or LF. If the installer changes it, preserve that failed handoff and copy the canonical block from either guide directly. Paste only the prompt in a fresh ordinary, non-project, non-Temporary chat; do not attach the runtime, install package or either guide. A bare command cannot carry the installer protocol into a fresh chat, and the package's embedded runtime would contaminate an automatic Library test.

Run the separate QA behavior cases and the repository [account acceptance suite](account-acceptance.md) as applicable. First-use reading triggered by an ordinary task is a separate case from explicitly requested source retrieval. Keep settings persistence, source access and behavior distinct. Projects may organize work or provide an explicitly selected delivery surface, but are never an installation prerequisite. Project or Work-mode evidence cannot substitute for the ordinary-chat acceptance test.
