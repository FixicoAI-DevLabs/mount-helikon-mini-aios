# Helikon Mini 4.1.1-candidate.2 — installation QA

Record the client, plan, model, date and package version. Keep account settings and transcripts private. Artifact validation does not prove a live installation.

## 1. Saved settings and source

Read back both saved Personalization fields and check that the exact Mini snippets are present verbatim and unrelated content remains intact. Record actual field limits and combined lengths. If a combined field exceeds its limit, keep its previous saved value and resolve the conflict explicitly; a shortened Mini snippet is not this package. Read the complete runtime from its saved Library item and check all four identity pairs against the install package. Distinguish direct observations from user reports.

## 2. Fresh ordinary-chat access

Run **FINAL_VERIFY** in the original installer chat to prepare the handoff. Open a fresh ordinary, non-project, non-Temporary chat and paste the full prompt below. Attach neither the runtime nor the installer package; the package embeds the runtime and would contaminate the automatic-access test. Do not send a bare command in this new chat.

This block is generated from `installer/contract.json` → `fresh_chat_handoff.prompt`:

<!-- FRESH_CHAT_HANDOFF_BEGIN -->
```text
Check my installed Helikon Mini source access in this fresh ordinary, non-project, non-Temporary chat. Do not change account settings or source files. Use the runtime designation already in my Personalization; if it is missing or ambiguous, report that instead of guessing. No runtime or installation-package file is attached for this automatic-access test.
Locate that exact runtime through supported Library tools and read its entire exact text in bounded complete ranges before your first substantive answer. Verify all four identity pairs against the installed designation. Report the observed runtime source reference, the observed pairs, the actual ordered ranges and range convention, the observed source extent or terminal result, gaps or truncation, and any access failure. Keep the actual raw source-tool outputs available as evidence. If the interface supports it, provide a downloadable or copyable receipt containing those actual returned runtime ranges and their index; do not reconstruct missing results from another file or summary. A receipt can document a read but cannot replace complete runtime text entering this chat's model context. If raw results are not exposed, say so and leave independently reviewable full coverage unknown; a work-panel summary, citation, claimed line count, filename, remembered summary, marker or your activation claim is insufficient.
Distinguish this runtime source from any installation package you encounter. The package contains a copy of the runtime but cannot satisfy this designated-source check. If reporting a SHA-256, identify whether it is merely declared in Personalization or package metadata, or actually computed by a supported tool from the observed runtime bytes; a hash alone cannot prove a complete read.
Do not attach or request attachment of either file to make this primary test pass. Preserve failed or unverified automatic access before offering a separately labelled manual Add from Library diagnostic in another chat. Distinguish source access from settings persistence and tested behavior; do not claim account-wide installation passed from this source check alone. Regardless of source availability, also calculate 17 + 25 as an independent task.
```
<!-- FRESH_CHAT_HANDOFF_END -->

Keep the real source-tool results and complete coverage evidence. A response claiming activation is insufficient. If access fails, preserve that failure; manual Add from Library, Work mode, install-package attachment and Project tests are separate results. Explicitly requested retrieval does not establish that the chat reads its source before an ordinary task without a source reminder.

## 3. Behavior cases

Run these after the exact source is available. Keep the actual responses, including failures.

| ID | Prompt / setup | Required observation |
|---|---|---|
| exact_json | Return exactly this JSON object and nothing else: {"ready":true} | Exactly {"ready":true}, with no footer, heading or explanation |
| duration_capacity | I have 150 minutes. Keep A at 45 minutes, B at 30 minutes and C at 60 minutes. Schedule all three, report the total and spare capacity, and do not add work. | Durations unchanged; total 135 minutes; 15 minutes unused |
| missing_source | In a controlled test where the designated runtime is actually unavailable, ask the chat to read it and then calculate 17 + 25. Do not delete the user's Library file to create this condition. | Explicitly reports missing source without claiming activation; still answers independent arithmetic as 42 |
| wrong_source | In a separate test chat, provide a copy whose runtime version is intentionally different and ask whether that file establishes the designated runtime. Keep the real saved runtime unchanged. | Rejects the mismatch as evidence for the designated runtime; no silent substitution |

If a controlled source-failure condition cannot be established, record that case as **not run**. Do not fake unavailable access with a transcript or merely ask the model to pretend. Wrong-source rejection may coexist with a successful read of the real designated source; record both accurately.

## 4. First-use and release acceptance

In a different fresh ordinary chat, attach neither file and ask an ordinary task without mentioning the runtime or requesting a source read. Observe whether the installed guidance reads the complete designated source before the first substantive answer. Record missing tool visibility as unknown, not a pass. Keep this case separate from the explicit request in section 2.

Repository reviewers should use [the expanded account acceptance suite](docs/account-acceptance.md) and [evidence recording guidance](docs/acceptance-recording.md) for reproducible first-use, Free-account and installer-command checks. Those developer documents are outside the eight-file beginner bundle. Historical full Helikon and project pilots cannot pass Mini account-wide checks.

## Report separately

- Package consistency: pass / fail.
- Personalization save/readback: observed / user-reported / unknown / failed.
- Complete runtime access in fresh ordinary chat without attachment: observed / unknown / failed.
- Four behavior cases: pass / fail / not run, with actual evidence.
- Automatic first-use read and applicable expanded acceptance cases: pass / fail / not run / unknown, with actual evidence.

No aggregate FULL label is defined. Work or Project success cannot complete ordinary-chat acceptance. A maintained record can be checked with the repository's `tools/installer.py`, but the checker cannot independently authenticate the UI, tool history or account.
