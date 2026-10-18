# Verify claims and inspect omissions

Finding correctness and review completeness are different questions. Complete both for the reached gate. Preserve the evidence and rejection reasons using [Review records](review-records.md).

## Verify a candidate finding

1. **Establish the obligation independently.** Locate the requirement, authoritative contract, supported invariant or applicable visual pattern. Separate business outcomes from proposed implementation mechanisms. If the outcome depends on an unresolved product choice, retain that question; proving behavior alone does not prove a defect.
2. **Reconstruct the supported trigger and causal chain.** Inspect the cited revision and surrounding code, producers, guards and sinks. Confirm that the proposed input/state can arise through a supported path. Trace the actual failure, including omitted effects. Check the changed baseline to distinguish introduced regressions from relevant inherited weaknesses.
3. **Try the strongest competing explanation.** Inspect existing enforcement, dependency behavior, legitimate contrasts and explicit scope decisions. Treat author replies, tests and prior approvals as evidence to investigate. An unchanged file, rarity claim, best-effort label or proposed future work does not itself refute a current contractual violation.
4. **Match impact and correction to evidence.** State concrete consequences and qualifying conditions without assuming prevalence. Check that the recommended boundary removes the cause while preserving supported alternatives and historical meaning. Separate behavior changes from behavior-preserving refactoring. Broad redesign remains a scope recommendation, not implementation authority.
5. **Record the decision.** Accept a verified defect, reject with decisive counterevidence, or retain an unresolved contract/proof gap. Never silently discard a candidate because another reviewer missed it. Group duplicate manifestations only when the cause and correction are shared; preserve distinct effects and affected consumers.

For runtime assertions inspect supplied QA evidence and record what actually ran, its producer, identity and environment. Do not execute QA to manufacture that evidence during review. Source-proven conditional failure is valuable but is not an executed reproduction. Missing required proof is a readiness gap, not automatically a technical defect. A test's passing result cannot refute a path its fixtures or assertions do not exercise.

## Audit omissions independently

Begin from the raw diff, source and context before reading the discovery report. Build a provisional inventory of required outcomes, preserved contracts, writers, decision owners, transitions and sinks for the current gate. Inspect the relevant source, rather than generating an inventory from generic risk headings. Record this first inventory before consulting prior findings.

Then compare it with the discovery coverage:

- **Unaccounted entry or writer:** follow its actual input, enforcement and effect. Determine whether shared enforcement truly makes it equivalent to an inspected route.
- **Unaccounted transition or lifetime:** follow updates, repeats, competing operations, reversal, regeneration or later consumption where supported by this change. Check whether the same identity and meaning survive.
- **Unaccounted effect or consumer:** inspect both extra effects and required effects that can be skipped. Follow exports, materialized data, background work and user-visible outcomes beyond the initial success response.
- **Unaccounted seam:** inspect the combined assumptions of separately reviewed parts. Check units, versions, scope, defaulting, authority and failure outcomes where relevant.
- **Unsupported coverage claim:** reopen broad conclusions based on a narrow route, a component test, a search hit or mere file access. Mark truly unavailable evidence rather than certifying it.

This is an investigation task. A checklist of possible gaps without inspected consequences is not a completed audit. Send substantive candidates through finding verification. Retain precise unassessed paths where investigation cannot finish. A blocked design gate leaves implementation and UX deferred, but does not excuse omitted design obligations whose evidence lives in those layers.

## Establish the final disposition

Reconcile the inspected inventory with the complete change and affected contracts. Record source gate status, runtime proof and remaining gaps separately. Recheck citations against the frozen candidate. If relevant source changed, invalidate dependent evidence and re-scope before claiming completion.

No findings is compatible with incomplete inspection. Ready requires the parent skill's applicable gates and essential proof, not a majority vote, empty candidate list, clean scanner output or passing ledger check.
