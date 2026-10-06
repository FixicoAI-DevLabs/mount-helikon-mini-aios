# Candidate 5 regression and source record

Candidate 5 corrects a planning defect exposed by candidate 4: adding work to fill available capacity while still claiming the original task total. The System and runtime review rule now explicitly preserve supplied durations and reconcile task, day and project totals. The identity-pinned schema advances to 1.0.4; its structure is unchanged. Exact tested sources are retained beside this report.

All 16 behavior cases were rerun in three fresh chats each. All 48 case-run observations met their specified acceptance criteria. B03 uses a wrong-version and a truncated-file conversation for each run, making 51 primary conversations. Five separate supplementary probes cover wrong/partial source, raw Python, CSV and an exact template. The negative fixtures are preserved. B09, B10, B12 and B16 include successive turns; B12 deliberately seeds a wrong unverified draft.

Three fresh repetitions of the original eight-hour planning prompt now preserve task durations, daily limits, dependencies and the eight-hour total. Three new planning probes also preserve fractional allocations and spare capacity, and identify an infeasible five-hour workload within four hours of capacity. Minor wording remains imperfect: the infeasible-plan reply describes a daily-limit problem while its table actually illustrates an incomplete four-hour allocation; its conclusion correctly says that one hour remains unscheduled.

## Exact source and installation

A clean project was created with project-only memory and Space disabled. The exact 1,490-character System was saved, reopened and compared, and the runtime upload reached the completed Preview state. The negative-test project's existing fictional note was preserved and exact readback confirmed. Candidate 4's more extensive installation/recovery transitions remain historical evidence, not secretly relabelled candidate-5 tests.

Eight bounded returned sections reconstruct the 22,251-byte runtime exactly, including all 18 rules and 12 owners. SHA-256: `21f2635f72b3e519d4d25041ef968d2b121df4e8bfb5552a0cc595374c02e378`. Structural JSON whitespace was regenerated; all values and key order match. The one-response reproduction request still failed and asserted an unobserved output-size limit; `R01.json` retains the response. The bounded result demonstrates accessible content in that conversation, not hidden full-body delivery in every ordinary turn.

## Limits and review scope

Host: browser ChatGPT, Pro, GPT-5.6 Sol / Medium. Exact backend build and hidden per-turn model input were not exposed. Fresh project chats are not proven independent. No production full Helikon settings, memories, Skills or unrelated projects were changed.

Optional configuration citations and extra checking/follow-up prose still appear in ordinary responses. B09's announcement has two sentences, with surrounding prose; its scoped-authorization criteria passed, but this is not a universal two-sentence compliance claim. The raw JSON/Python/CSV/template cases are checked separately. B13's absent optional Skills and B15's unknown write are explicitly posed scenarios, not proof of actual capability removal or a real write.

These are externally observed responses and manual criterion reviews. The strict gate's complete-body fields have not been asserted from filenames, model self-report or one other conversation's source copy. Ordinary global-chat delivery, free accounts and actual six-memory migration remain untested. This candidate is suitable for further isolated project evaluation; it is not certified as a general replacement for full Helikon or a production global-chat release.

## Utility rerun

All 24 candidate-5 utility responses met the supplied task criteria (eight tasks, three runs each). The three original U04 planning retests are counted once. Ninety-word counts and JSON outputs were mechanically checked; inspected Python functions were executed and passed empty, singleton and mixed-value tests. The three additional planning probes also passed their substantive duration/capacity/dependency checks. Raw responses, reviews and character counts are retained in `utility-review.json`. The plain and concise controls belong to the earlier candidate-4 comparison and were not rerun; this is a targeted regression, not a new 72-response comparison or a claim of general superiority.

All 83 primary/supplementary/utility/additional conversation records were restored from a complete in-memory checkpoint after shared-file synchronization dropped some individual exports. These retain the actual copied response text, not reconstructed summaries or reruns. The source-copy records were separately checkpointed and checked against the canonical source.
