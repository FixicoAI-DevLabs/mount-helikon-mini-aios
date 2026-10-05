# Validation and maintenance

Run from the repository root with Python 3.10+ and its standard library:

```sh
python3 tools/mini.py validate
python3 -m unittest discover -s tests -v
python3 tools/mini.py build --out build/first
python3 tools/mini.py build --out build/second
cmp build/first/Helikon-Mini-4.0.0-candidate.1.zip build/second/Helikon-Mini-4.0.0-candidate.1.zip
python3 tools/mini.py verify-archive build/first/Helikon-Mini-4.0.0-candidate.1.zip
```

`python3 tools/mini.py render` regenerates the reading copy. ZIP members have sorted names, fixed timestamps/permissions and stored compression for reproducibility without compressor-version dependence. The manifest hashes each payload; the outer checksum covers the whole ZIP. Integrity alone does not authenticate a publisher: compare against a separately trusted reviewed checksum.

The published schema uses a small standard JSON Schema Draft 2020-12 subset. The offline validator rejects unknown keywords rather than silently ignoring them. It checks exact types, closed objects, constants, nonempty content, references, invocation cycles, owner coverage, design budgets, legacy bytes, profiles, source coverage and private-default patterns.

Independent reviewed anchors lock behavioral prose, bootstrap, procedures, owners, extensions and System bytes. They detect semantic-text changes even if packaging hashes are regenerated. They do not prove meaning or compliance. A maintainer can change code and anchors; explicit semantic review and targeted regression checks are required before rebaselining. No automatic rebaseline command is shipped.

The source map inventories components and nested normative IDs. It does not claim every original schema or rule is preserved verbatim. `python3 tools/source_check.py PATH_TO_AUTHORIZED_FULL_MASTER` verifies the pinned source hash, component hashes and complete inventory without copying the master into this repository.

Negative tests cover reversed completeness, disabled safeguards, altered/blank policies, wrong identities, missing references, cycles, stale projections, contradictory evidence, unsupported pass labels, private defaults and archive tampering. Synthetic fixtures exercise validators; they are never live transcripts.

## Live evidence

The behavior pilot has 16 cases with three fresh runs each; format variants and installation transitions are additional. Utility has eight tasks, three conditions and three runs (72). Retain every failure and rerun, record uncontrolled host differences and blind comparison labels where feasible.

```sh
python3 tools/evidence.py template --out evidence/local/pilot.json
python3 tools/evidence.py validate evidence/local/pilot.json
```

The template is explicitly unrun. Actual evidence needs local transcript files/hashes, host context, candidate hashes and criterion findings tied to excerpts. Validation establishes record completeness and consistency, not independent authentication of host observations or review. Its strongest result is `record_consistent_manual_review_required`; it never grants release approval. An unrun, empty or contradictory record cannot pass through a status label.

Before production publication resolve the ordinary-chat delivery scope, identify an isolated authorized host, run installation/migration/recovery/fresh-chat cases, complete behavior and utility pilots, and review failures and costs. Prepare exact candidate bytes, diff, destinations and support claims for the reserved publication review. Static checks cannot supply missing live evidence or permission.

GitHub Actions is configured to repeat local checks and compare two builds. Local success does not mean hosted CI ran. The workflow pins checkout, uses read-only permission, and contains no publishing or account mutation.
