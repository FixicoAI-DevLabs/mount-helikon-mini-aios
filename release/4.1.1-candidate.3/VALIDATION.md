# Candidate validation — 4.1.1-candidate.3

Observed locally on October 9, 2026, against the revised candidate derived from `5ad51ac4febf7c07de4c01ef52d1c2e30527db4d`. Status: **offline checks passed; candidate-specific live acceptance pending**. See [machine-readable results](engineering-validation.json).

## Executed checks

- **110 unit and negative regression tests passed** in 2.391 seconds.
- Main artifact validation passed, including runtime schema/references, unchanged reviewed runtime-policy anchors, snippet/protocol bindings, exact embedded runtime, generated projections, profile identity/hash bindings and configured integrity/residue checks.
- A direct comparison confirmed that every runtime member outside identity is unchanged from candidate.2.
- Two independent builds were byte-identical (`cmp` exit 0). This archive is a direct copy of the checked build: **8 members, 102,786 bytes**.
- The copied release archive passed the explicit archive inventory/integrity verifier.
- Canonical snippets contain **1,099 and 866 characters**, with no terminal newline. The handoff contains **2,223 characters on one logical line**, with no CR/LF or outer whitespace.
- Diff whitespace review passed. Earlier release paths were unchanged before this new directory was created.

These sizes are artifact measurements, not host limits. Exact authorized full-source inventory verification was **not rerun for this candidate**. Earlier source-check counts remain evidence for their recorded revision; this record makes no new full-source or semantic-equivalence claim. Hosted CI must be inspected on the actual published commit.

Archive SHA-256:

```text
261c26dbf8cc1f212acf85319ca2d3a7d7a7d0220fe6916215dcaee2ce47fb31
```

Runtime SHA-256:

```text
1d5d7648a6dd2580fe8d0b451b398bfe675edb6eb0af4177e3bbe5cfb9430cd4
```

## Targeted regressions

The new format regression supplies inserted LF, CRLF, blank paragraphs, leading/trailing spaces and a terminal newline while keeping package and guide projections synchronized. Protocol 2.3.0 rejects these malformed canonical handoffs. A separate historical regression loads the preserved candidate.1 and candidate.2 archives and confirms that their exact multiline prompts remain valid under their original protocols. Existing exact snippet, preservation, package-drift and evidence-consistency tests continue to pass.

Synthetic tests establish implementation behavior only. The separate [live retest](LIVE_RETEST.md) observed immediate exact SETUP previews, a failed initial handoff emission and exact reproduction after one corrective follow-up. A consistent installation record always returns `release_ready: false` and requires semantic review.

## Live acceptance boundary

The [focused installer retest](LIVE_RETEST.md) records candidate-specific response observations. Candidate.3 settings were not saved, and a tiny TXT upload failure stopped further source-upload attempts. Saved-runtime availability, full readback and six primary ordinary-chat trials remain unestablished or not_run. Prior candidate results cannot pass these gates. Follow the [manual acceptance suite](../../docs/account-acceptance.md) and [private recording guide](../../docs/acceptance-recording.md).

This record establishes only the listed checks. It does not authorize merging, tagging or release promotion.
