# Validation

## Local artifact checks

```sh
python3 tools/mini.py render
python3 tools/mini.py validate
python3 -m unittest discover -s tests -v
python3 tools/mini.py build --out build/first
python3 tools/mini.py build --out build/second
cmp build/first/Helikon-Mini-4.1.0.zip build/second/Helikon-Mini-4.1.0.zip
```

These validate the canonical runtime, generated projections, two bounded Personalization snippets, guided protocol, eight-file package, private-data exclusions, unchanged legacy source bytes and adversarial evidence-record cases. They do not prove successful settings writes, source retrieval or behavior on a ChatGPT account.

## Live installation records

```sh
python3 tools/installer.py record-template --out private-checks/installation.json
python3 tools/installer.py verify-record private-checks/installation.json
```

Keep records and source bindings private; do not commit account backups or transcripts containing personal data. The template starts incomplete. Populate only actual observed results and hash-linked evidence. Required checks appear in the root QA sheet. A complete consistent record still needs human review; the checker always returns `release_ready: false` because it cannot authenticate the host or grant release authority.

Historical project evidence uses the earlier `tools/evidence.py` protocol and remains version-specific. It does not satisfy the new account-level gate.
