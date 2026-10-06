# Helikon Mini 4.1.0 — installation QA

Record the client, plan, model, date and package version. Keep account settings and transcripts private. Artifact validation does not prove a live installation.

## 1. Saved settings and source

Read back both saved Personalization fields and check that the exact Mini snippets are present and unrelated content remains intact. Read the complete runtime from its saved Library item and check all four identity pairs against the install package. Distinguish direct observations from user reports.

## 2. Fresh ordinary-chat access

Open a fresh ordinary non-project, non-Temporary chat. Do not attach the runtime to this primary test. Ask:

> Locate my designated Helikon Mini runtime in Library. Use supported source tools to read its complete exact content in bounded ranges. Report the four identity pairs you actually observed and any missing portions. Do not infer a complete read from the filename, hash, remembered text or an activation claim.

Keep the real tool results and complete coverage evidence. A response claiming activation is insufficient by itself. If access fails, record the failure; manual Add from Library, Work mode and Project tests are separate results.

## 3. Behavior cases

Run these after the exact source is available. Keep the actual responses, including failures.

| ID | Prompt / setup | Required observation |
|---|---|---|
| exact_json | Return exactly this JSON object and nothing else: {"ready":true} | Exactly {"ready":true}, with no footer, heading or explanation |
| duration_capacity | I have 150 minutes. Keep A at 45 minutes, B at 30 minutes and C at 60 minutes. Schedule all three, report the total and spare capacity, and do not add work. | Durations unchanged; total 135 minutes; 15 minutes unused |
| missing_source | In a controlled test where the designated runtime is actually unavailable, ask the chat to read it and then calculate 17 + 25. Do not delete the user's Library file to create this condition. | Explicitly reports missing source without claiming activation; still answers independent arithmetic as 42 |
| wrong_source | In a separate test chat, provide a copy whose runtime version is intentionally different and ask whether that file establishes the designated runtime. Keep the real saved runtime unchanged. | Rejects the mismatch as evidence for the designated runtime; no silent substitution |

If a controlled source-failure condition cannot be established, record that case as **not run**. Do not fake unavailable access with a transcript or merely ask the model to pretend. Wrong-source rejection may coexist with a successful read of the real designated source; record both accurately.

## Report separately

- Package consistency: pass / fail.
- Personalization save/readback: observed / user-reported / unknown / failed.
- Complete runtime access in fresh ordinary chat without attachment: observed / unknown / failed.
- Four behavior cases: pass / fail / not run, with actual evidence.

No aggregate FULL label is defined. Work or Project success cannot complete ordinary-chat acceptance. A maintained record can be checked with the repository's `tools/installer.py`, but the checker cannot independently authenticate the UI, tool history or account.
