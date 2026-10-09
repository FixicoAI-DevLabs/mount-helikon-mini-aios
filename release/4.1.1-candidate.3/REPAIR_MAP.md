# Candidate.3 repair disposition

Baseline: repository commit `5ad51ac4febf7c07de4c01ef52d1c2e30527db4d` and preserved candidate.2 live observations. Reviewed October 9, 2026. Executed engineering checks are in [VALIDATION.md](VALIDATION.md). This map records implemented repairs, not live host success.

| Observed gap | Candidate.3 repair | Remaining boundary |
|---|---|---|
| SETUP gave manual steps but withheld exact copy blocks until NEXT | Installer protocol 2.3.0 explicitly requires both exact previews in its first SETUP response after complete package/identity checks | A live first-response comparison is still required; previews cannot count as backups or saves |
| FINAL_VERIFY added three newline characters to the canonical prompt | One logical-line handoff with no CR/LF or outer whitespace, synchronized across package and guides; validator rejects malformed canonical values despite matching projections | The model's actual copyable response must still match exactly; soft visual wrapping is not a text change |
| Normalizing a changed response could conceal a failed exact handoff | Preserve the failed attempt and use the canonical guide block as a separately identified fallback | Fallback success cannot retroactively pass the failed handoff; guides cannot be attached to the primary source test |
| A stricter new format could reject preserved earlier artifacts | Apply the one-line rule only to protocol 2.3.0 and regression-check archived candidate.1/candidate.2 multiline prompts | Historical results remain bound to their original versions |
| Revised identity could drift across package, schema, profile and projections | Advance runtime to candidate.3/schema 1.0.9, update exact hash/profile bindings and regenerate outputs | Identity consistency and archive integrity do not prove account installation or runtime delivery |

Runtime non-identity content and System contract 2.2.0 are unchanged. Earlier release artifacts and live evidence remain intact. This candidate does not repair or establish host Library availability through artifact changes alone.
