# Candidate validation — 4.1.1-candidate.2

Observed locally on October 9, 2026, against the revised candidate derived from `433fd7749d9b91e4957182749005c97365abc767`. Status: **offline checks passed; focused live retest confirmed exact settings persistence, but account acceptance remains incomplete**. See [machine-readable results](engineering-validation.json) and the [focused live retest](LIVE_RETEST.md).

## Executed checks

- **108 unit and negative regression tests passed.**
- Main artifact validation passed, including runtime schema/references, unchanged reviewed runtime-policy anchors, snippet/protocol bindings, generated projections, exact embedded runtime, profile identity/hash bindings and configured integrity/residue checks.
- Two independent builds were byte-identical. This archive is a direct byte-for-byte copy of the checked build: **8 members, 99,047 bytes**.
- Archive inventory/integrity verification passed. Membership and hashes were also independently inspected while preparing this directory.
- Canonical snippets contain **1,099 and 866 characters**, with no terminal newline. These are artifact measurements, not observed host field limits.
- Earlier release directories were unchanged before this new directory was created.

Exact authorized full-source inventory verification was **not rerun for this candidate**. Earlier counts and results remain evidence for their recorded revision; this record makes no new semantic-equivalence or full-source verification claim. Hosted CI must be checked on the actual published commit.

Archive SHA-256:

```text
fc1ec33458ff8faa6bb38eb09cd27e32819f6efb24608a967fdac542f88b3ad2
```

Runtime SHA-256:

```text
2afe9b2b83ae6ac91c09ab4c5232ed1e9f8bc22f69c840b908d5107cb6447daf
```

## Targeted regressions

Tests cover exact snippet matching without whitespace normalization, newline boundaries around preserved unrelated preferences, rejection of partial-line matches and altered internal whitespace, preservation of historical terminal-newline requirements, Markdown-only fence separators and rejection of distributed package/projection drift during record verification.

Synthetic fixtures check the implementation; they do not establish host behavior. A consistent installation record still returns `release_ready: false` and requires semantic review.

## Live acceptance boundary

The [focused live retest](LIVE_RETEST.md) observed improved manual guidance and exact persisted snippet values. Package and standalone runtime uploads failed with no established cause, leaving candidate.2 Library storage unestablished. One fresh diagnostic reported no supported runtime read; its correct arithmetic did not pass source delivery. The installer reported the partial state appropriately, but its handoff failed exactness by three added newline characters.

The six-trial primary series was not run because saved-source prerequisites were unmet. A07, four behavior cases and restoration were not rerun for candidate.2. Automatic full-runtime delivery, full Free-account compatibility and overall account acceptance remain unestablished. Candidate.1 results cannot fill candidate.2 gates. Follow the [manual acceptance suite](../../docs/account-acceptance.md) and [private recording guide](../../docs/acceptance-recording.md).

This record establishes only the checks listed above. It does not authorize merging, tagging or release promotion.
