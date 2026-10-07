# Validation

## Local artifact checks

```sh
python3 tools/mini.py render
python3 tools/mini.py validate
python3 -m unittest discover -s tests -v
python3 tools/mini.py build --out build/first
python3 tools/mini.py build --out build/second
cmp build/first/Helikon-Mini-4.1.1-candidate.1.zip build/second/Helikon-Mini-4.1.1-candidate.1.zip
```

These check the canonical runtime, generated projections, two bounded Personalization snippets, guided protocol, eight-file package, limited private-marker exclusions, unchanged legacy source bytes and evidence-record rejection cases. These are commands to run, not a claim that this document has run them. They do not prove successful settings writes, source retrieval or behavior on a ChatGPT account.

## Exact source derivation check

Obtain the exact authorized full Helikon source privately, then replace the example path with its actual local path:

```sh
python3 tools/source_check.py /path/to/authorized/Helikon_Operating_Master.json
```

This separate check compares the supplied master's exact hash, identity, component inventory and normative IDs with the repository provenance records. It does not prove semantic equivalence or activate full Helikon. Ordinary CI checks public inventory consistency without possessing that private master. An absent source leaves this stronger check unrun; do not substitute a similarly named file or commit private configuration to make CI pass.

## Live installation records

```sh
python3 tools/installer.py record-template --out private-checks/run-001/installation.json
python3 tools/installer.py verify-record private-checks/run-001/installation.json
```

Keep records and source bindings private; do not commit account backups or transcripts containing personal data. The template starts incomplete and refuses to overwrite an existing record. Populate only actual observed results and hash-linked evidence. Use [account acceptance](account-acceptance.md) for reproducible prompts, expected results and the manual release matrix, [acceptance recording](acceptance-recording.md) for v2 fields and per-attempt worksheets, and the [root QA sheet](../Helikon_Mini_QA.md) for the compact four-case check and self-contained fresh-chat handoff.

The fresh ordinary-chat automatic-access tests prohibit runtime and install-package attachments. Manual Add from Library, Project delivery and Work mode are separate outcomes. A correct ordinary answer without evidence of the required source read does not pass automatic delivery. Actual Free-account validation needs an observed Free account and exposed capabilities; a snippet-length check alone is insufficient.

Inspect both the checker's result JSON and process exit status: `0` means a consistent current record requiring manual review, `2` means incomplete or legacy evidence, and `1` means invalid input or an evidence-consistency error. The checker always returns `release_ready: false` because it cannot authenticate the host or grant release authority. The expanded manual suite includes repetition, Free compatibility and recovery cases beyond the minimum record schema. Conditional unknown-write and duplicate-source cases remain unrun when those conditions do not occur; they do not alone block the basic account claim.

Historical project evidence uses the earlier `tools/evidence.py` protocol and remains version-specific. It does not satisfy the new account-level gate.
