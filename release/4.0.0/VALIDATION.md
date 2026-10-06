# Mini 4.0.0 validation

Checks run October 6, 2026 against the final 4.0.0 installation pair and package:

- Static artifact validation passed; all 38 automated tests passed.
- Two independent builds produced byte-identical ZIPs, with 15 members.
- The pinned Helikon 6 source inventory passed: 92 components, 474 nested normative IDs.
- Compared the root runtime, System and schema against the frozen candidate-5 ZIP. The only runtime differences are the runtime version (4.0.0) and schema version (1.0.5). The System differs only at those version labels. Schema structure is unchanged, with its exact identity values advanced.
- Behavioral anchors are unchanged. Archived 3.3 files retain their original SHA-256 values. Historical candidate release files and transcripts are unchanged.

The runtime is 22,239 bytes and System is 1,466 characters. These are engineering measurements, not provider limits or token counts. Exact hashes and check results are in `validation.json`.

## Live evidence carried forward

Candidate 5 recorded 48 core case-runs, five supplementary probes, 24 utility runs and three additional planning probes. Its full runtime was reconstructed exactly in bounded copies, and the saved System and completed upload were checked. Those observations remain labelled candidate 5; they are not newly executed 4.0.0 tests.

The browser service was unavailable for a fresh 4.0.0 installation smoke check. The unchanged operational content supports carrying forward the existing bounded evidence, but identity-only equivalence cannot prove the host will behave identically. Hidden complete-runtime input each turn, other models/tiers, global-chat delivery and general benefit are unverified. The strict evidence gate remains unmet and unchanged. Candidate 5's single-response full-copy failure remains in its record.

Hosted CI and public asset download results are recorded in the publication receipt after they are observed. Local validation alone does not claim publication succeeded.
