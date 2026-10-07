# Evidence manifest integrity

`python3 tools/mini.py validate-evidence` checks the retained candidate-4 and candidate-5 evidence trees offline. The ordinary `validate` and `build` commands also run this check, so CI rejects missing, added or changed files in those declared trees. The policy is `docs/integrity/evidence-manifests.json`; other release directories are outside this policy's scope. Release ZIP member integrity is a separate check.

## Historical and current scopes

Both original `EVIDENCE_MANIFEST.json` files were introduced at commit `6964592f0120580ce843bbebf954d63b1192fc32`. At that commit all 149 candidate-4 and all 113 candidate-5 entries match. Their exact original manifest bytes are pinned in the policy and remain unchanged.

Candidate-5's README was subsequently revised at publication commit `fcc92c387756f9a7173f8cc6e1020707fb91de33`. The original manifest therefore does not describe today's README. `docs/integrity/candidate-5-original-README.md` preserves the original 1,166 bytes solely as historical evidence. **It is not current installation or release guidance.** The policy explicitly routes only that historical receipt to this copy. Every other historical receipt checks its original file. No historical pass or failure was edited to repair the manifest.

The independent `current_scope` inventory records all 267 current files under the two declared roots, including today's README, both original manifests and later publication records. Directory enumeration rejects unlisted additions and missing files. File sizes and SHA-256 hashes reject changed content. Each manifest path is confined to its declared root; the preserved-copy path is confined to the repository. Verification needs neither Git history nor network access.

## Reviewing a change

Do not regenerate the old manifests or change pilot records to make a check pass. Investigate unexpected drift and retain its cause. A legitimate later addition or correction needs an explicit review of the changed evidence, an update to the separate current-scope inventory, and a description of what changed. If a historically listed file is deliberately superseded, preserve its original bytes and add a narrowly documented historical binding, as for the candidate-5 README. Historical source commits must remain immutable references.

The policy itself is a reviewed repository artifact, not an external trust anchor. A coordinated edit of a file and its expected checksum can pass. Integrity checks detect drift against the reviewed inventory; they cannot authenticate conversations, prove a reviewer's judgment, establish model obedience, or authorize publication.

## Full-source provenance and release checks

Ordinary validation compares the full-source hash across the source manifest, index and disposition map. It checks exact pointer order, unique normative IDs and component hashes across the public inventory records. This rejects inconsistent edits without distributing the full source.

For a source-dependent release review, supply the exact authorized full master separately:

```sh
python3 tools/source_check.py /path/to/authorized/Helikon_Operating_Master.json
```

The command checks the exact file hash, runtime/schema/System-contract identity, complete ordered component inventory, each canonical component hash, and all normative IDs. Public CI tests this checker with explicit synthetic fixtures; it does not possess or validate the private master. Record the actual command result against the candidate under review. A missing authorized master leaves this source-dependent check unrun; synthetic fixture success cannot substitute for it. Never commit private source material to satisfy CI.

## Limited residue check

The public-text residue check derives its payload scope from the actual ZIP inventory, including `LICENSE`, and also inspects current documentation, installation inputs, profiles and behavioral specifications. It recognizes a small set of account-identifier, local-path and private-key patterns. It is not a general secret scanner or a review of every historical release transcript. Review newly published files and historical evidence for task-relevant privacy independently; do not interpret a pattern-check pass as a privacy certification.

Local installation records belong under the ignored `private-checks/` or `evidence/local/` directories. Git ignore rules prevent ordinary accidental staging but do not protect files added with force or data copied elsewhere.
