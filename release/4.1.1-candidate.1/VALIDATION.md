# Candidate validation — 4.1.1-candidate.1

Observed locally on October 7, 2026, against the repaired candidate derived from `1826830243dc6e629ad80c52493306073c180df2`. Status: **offline checks passed; live account acceptance not run**. See [machine-readable results](engineering-validation.json).

## Executed checks

- **102 unit and negative regression tests passed**: 38 existing candidate/evidence tests, 40 installer tests and 24 integrity tests.
- Main artifact validation passed: runtime schema/references, unchanged reviewed runtime-policy anchors, reviewed new snippets/protocol, generated projections, exact embedded runtime, profile hash/identity bindings, and limited public-payload residue checks.
- Exact authorized full-source verification passed: **92 components and 474 normative IDs**. This checks source identity and inventory, not semantic equivalence or model behavior.
- Historical manifest verification passed for **262 entries**. The original manifests and pilot files remain intact; the superseded README is checked using preserved original bytes.
- Separate current inventory verification passed for **267 files** across candidate-4 and candidate-5.
- Two independent builds were byte-identical. The committed candidate archive is a direct copy of that checked build: **8 members, 87,520 bytes**.
- Existing release files remain unchanged. The preserved 3.3 source hashes also pass; only archive navigation documentation was clarified.
- Snippets contain **1,100 and 867 characters**, including terminal newlines. These are measured artifact lengths, not observed host field limits.
- Diff whitespace review passed. Hosted CI must be inspected on the actual published commit; a local pass does not predict its result.

Archive SHA-256:

```text
a45c75ef307cde09774bea5f69b7a1eec7e18ac3b20e709a5b7b5793e89cb5eb
```

Runtime SHA-256:

```text
531ea75853845f0e31a2a8ce03fc469fb8a5af2d4dabb73672ed2a1e9075eccd
```

## Reproduced failure cases now covered

Tests reject stale embedded runtime after a line-ending change, stale profile hash or identity, drifted fresh-chat prompt copies, missing record evidence, incorrect surfaces, failed/unknown checkpoints, incomplete host metadata, missing backups, manifest drift, inventory changes, source-map inconsistencies, malformed negative-source hashes and payload residue in formerly omitted files. Exclusive template creation preserves an existing record. An explicitly regenerated CRLF runtime can pass only with exact matching embedded bytes and a corrected profile binding.

Synthetic fixtures intentionally exercise the checker; they are never live account evidence. A complete consistent installation record always returns `release_ready: false` and requires semantic review.

## Unexecuted acceptance

No Personalization settings were changed. Fresh ordinary-chat automatic Library access, actual Free-account installation, guided host installation, restoration and model-behavior acceptance were not run for this candidate. Use the [manual acceptance package](../../docs/account-acceptance.md) and [private recording guide](../../docs/acceptance-recording.md). Every live case begins not run; historical full Helikon or project observations cannot fill it.

This record does not authorize merging, tagging, release promotion or account changes. It establishes only the executed checks listed above.
