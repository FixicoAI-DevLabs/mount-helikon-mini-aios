# Recording account acceptance evidence

Use this guide with [account-acceptance.md](account-acceptance.md). It records proposed 4.1.1-candidate.1 tests; it is not evidence that installation occurred. Keep account text, backups, source bindings and unredacted transcripts private. Do not put them in runtime JSON, the public package, or committed fixtures.

## Create a private run

From the candidate checkout, create a distinct record path for each target/run:

```sh
python3 tools/installer.py record-template --out private-checks/run-001/installation.json
python3 tools/installer.py verify-record private-checks/run-001/installation.json
```

The first command creates the canonical version-2 record from the actual checked-out package and refuses to overwrite an existing path. Choose a new run name rather than deleting previous evidence. The fresh record is incomplete; the second command should report that state. The `private-checks/` path is excluded from normal Git staging, but the operator still reviews staged files before any publication. An ignore rule is not encryption or an access control.

Store exact backup text, source-read captures, transcripts and screenshots under the same private run directory. The verifier accepts only evidence paths within that directory. Preserve original evidence; store redacted sharing copies separately and never use their hashes as hashes of the original files.

## Canonical v2 record

Generate the template instead of hand-copying a second schema from this document. Its important fields are:

| Field | What to record |
|---|---|
| `record_version` | Generated evidence schema version; do not relabel a legacy record. |
| `package_version`, `installer_protocol_version` | Exact candidate and protocol actually tested. |
| `host` | Observed client, plan, model, timestamp with timezone, observation method and evidence. An unexposed value remains unknown. |
| `checkpoints` | Every canonical installer checkpoint, with result, observation method, evidence references and notes. |
| `backup` | Actual exact-backup availability, private location description, observation method and evidence. A path assertion alone is not a backup. |
| `surface` | Actual account test surface; Project, Work and attached-file trials cannot stand in for ordinary automatic delivery. |
| `settings_readback` | Exact persisted field values, preservation result, observation method and supporting capture. |
| `runtime_readback` | Actual saved Library item, complete captured runtime, read evidence, method and source reference. |
| `ordinary_chat_readback` | Complete read observed in a fresh ordinary non-project chat without attachments, plus its true method/surface. |
| `behavior_results` | The four required IDs, their actual states, methods and evidence. |
| `limitations` | Missing visibility, failed attempts, unavailable capabilities and scope limits. Never clear this merely to obtain a complete-looking record. |

Result states are `not_run`, `unknown`, `failed`, and `passed`. Observation methods are `not_recorded`, `direct_observation`, and `user_reported`. Do not put an assistant's unsupported self-report in the direct-observation category.

An evidence reference identifies an actual UTF-8 file relative to the record directory, its SHA-256, and an exact nonempty excerpt found in that file. Compute the digest from the saved bytes; do not ask the model to invent it. If source evidence is an image, retain the image and create an accurate textual observation sidecar identifying the image and method; the text-reference checker does not authenticate image contents. A copied runtime file proves what bytes were captured, while the associated tool/UI trace is needed to establish where, when and how those bytes were read.

Populate only what was actually observed. Keep unknown write outcomes unknown until state inspection resolves them. Never edit a transcript to improve an answer, remove failed attempts, or replace an older attempted result with a successful retry without retaining both.

## Per-attempt worksheet

Copy this into a separate private Markdown file for each A/I case and each repeated source-access run. The structured v2 installation record covers the minimum installer checkpoint gate; this worksheet preserves the expanded acceptance suite, Free compatibility, repetitions and recovery evidence without pretending the checker verifies them all.

```text
Case ID and attempt number:
Result: not_run
Observation method: not_recorded
Started at / ended at (ISO 8601 with timezone):
Candidate commit and package SHA-256:
Runtime identity pairs and SHA-256:
Installer protocol version:
Client / observed plan / displayed model:
Actual surface (ordinary, Project, Work, other):
New chat identifier or private reference:
Initial attachment state:
Library/search/tool capabilities actually observed:
Authorized target and effects / reserved checkpoints:
Prerequisites and exact backup evidence:
Prompt sent verbatim:
Actual steps and tool/UI results:
Source reference, mechanism, ranges/chunks and truncation status:
Read completed before first substantive answer? Evidence:
Expected result:
Actual entire response:
Checks performed and calculations:
Evidence paths, SHA-256 values and exact excerpts:
Cross-cutting defects and limitations:
Earlier failures or retries linked:
Reviewer and review date:
Restoration state and outstanding effects:
```

For A06/A07, keep one worksheet per fresh chat. A single successful read cannot stand in for all repetitions. The runtime may be stored in Library before these trials, but neither it nor the installer package may be attached or pasted into the primary automatic-access chat. Retain the exact tested prompt, including whether it explicitly mentioned Mini.

For complete source reads, retain the actual returned text in order and a coverage ledger. Account for every part of the document, missing range, truncation and reread. If the host provides only selected search snippets, that is discovery or partial reading. A full canonical file copied from the repository is not evidence that the fresh chat read that file from Library.

For a hash comparison, distinguish original bytes from normalized or reconstructed content. If the host returns text rather than downloadable bytes, disclose any newline/serialization transformation. A value-equivalent reconstruction is weaker evidence than observed original-byte delivery and must be labelled accordingly.

## Review and completion

Run the checker after evidence is saved:

```sh
python3 tools/installer.py verify-record private-checks/run-001/installation.json
```

Inspect the returned JSON and exit status: `2` means incomplete or legacy evidence requiring further work/review; `1` means invalid input or an evidence-consistency error; `0` means the current record is consistent and still requires manual review. Even the latter returns `release_ready: false`. It cannot authenticate UI captures, establish that every transcript is complete, determine the truth of all narrative claims, or authorize release.

Review every required row of the acceptance matrix against the actual files, including cases not encoded in the minimum record. Recompute behavioral arithmetic; inspect entire exact-format responses; check that preservation and restoration compare actual before/after content; confirm that automatic reads occurred in the required clean fresh chats. Keep reported observations labelled as reported. Record disagreements or evidence gaps instead of treating a validator's success as a deciding vote.

Do not convert historical project trials or full Helikon 6 records into new Mini account results. Link them as historical context with their original version, surface, dates and limitations. Legacy evidence records remain historical; create a new v2 record and collect missing observations rather than automatically filling new fields from assumptions.

