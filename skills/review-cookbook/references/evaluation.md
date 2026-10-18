# Evaluate the review system

For skill maintainers; this is not a request to benchmark every user PR. Evaluate the complete discovery → verification → omission-audit workflow, retaining intermediate artifacts. Longer reports, more agents and more findings are not success measures.

## Freeze the comparison

Use immutable base/candidate source, original raw discussions and applicable engineering rules. Choose cases and repetitions before observing outcomes. Reuse established samples when requested; label repeated cases as regression tests rather than unseen generalization. Include repaired versions to test false accusations as well as faulty versions. Keep repaired variants anonymous to reviewers.

Freeze skill files and role prompts before launch. Record identities, content hashes, model/host configuration where observable, allowed tools, role allocation and execution permissions. Keep control conditions identical except the intended intervention. When comparing old single-review runs with a new multi-stage pipeline, disclose both the historical-control limitation and the extra work; do not attribute results to prompt quality alone.

Use fresh independent contexts. Reviewers receive the skill, raw case and task, never expected findings, historical answers, other cases or evaluation catalogs. Verifiers can receive candidates; omission auditors must record an independent inventory before seeing them. Shared-filesystem blinding is an instruction boundary unless actual access isolation exists; do not describe it as sandbox enforcement.

## Judge actual defects

Have independent adjudication inspect source before receiving the historical catalogue. Treat the catalogue as nonexhaustive hypotheses, not unquestionable ground truth. Establish the required rule and supported failure for new and old claims. Record full causal detection, partial recognition, missing cause/consequence, unsupported claim, or legitimately deferred layer. Do not count a runtime proof gap as a technical defect or penalize a later gate correctly deferred by a design blocker.

Compare distinct confirmed causes and material consequences. Check recommendation completeness and whether it removes the faulty rule. Include false alarms on repaired behavior and wrong business assumptions. Preserve incidental later-gate detections without claiming systematic coverage of those gates.

## Diagnose losses by stage

For each established defect distinguish:

- Path absent from the inventory or not inspected.
- Path inspected but rule/causal consequence misunderstood.
- Candidate found but incorrectly excluded, filtered or merged away.
- Accepted finding lost or weakened in the final report.
- Required evidence genuinely unavailable or business rule unresolved.

Track findings added by omission inspection and findings removed by verification, with their eventual correctness. Record coverage overclaims separately. Inspect runtime oracles for circularity; generated tests may encode the same wrong assumption as the reviewed code.

## Interpret honestly

Report per-case findings and limitations before aggregate counts. Report resource use when available without imposing arbitrary review-work quotas. Small, repeated or single-run samples cannot establish reliability, generalization or stable detection probability. Vendor metrics do not substitute for this evidence. Do not tune the skill mid-round or keep adding runs until it wins; changes start a new frozen round.

Keep experimental results and raw artifacts outside the product and skill package. Publish only requested changes and accurately scoped claims. Passing packaging checks establishes portability/format, not review quality.
