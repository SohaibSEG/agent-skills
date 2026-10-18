# Coordinate independent review

Use this procedure for substantial or cross-boundary changes when delegation is available and authorized. The coordinator owns the integrated result. The roles below are responsibilities, not a fixed agent count. Do not manufacture independence by asking the same context-filled agent to pretend it has not seen a finding.

## Prepare once

Freeze base, candidate, stack scope and permitted evidence. Provide raw requirements, issues and discussion with provenance. Establish applicable engineering rules and execution boundaries. Keep descriptions useful but challengeable. Identify the current gate and the obligations it must settle.

Create a tentative source-backed path inventory. Reviewers must inspect and extend it; it is not an exhaustive specification. Define shared seams and assign their integration owner. Do not give reviewers historical answers, expected defects, other reviewers' conclusions or evaluation catalogues.

## Discover independently

Split by consequential flows or responsibilities within the current gate, for example rule ownership, identity/history, or state transitions/effects. For implementation, assign relevant code-design/backend/frontend-state/security responsibilities; for experience, task paths, visual conformance and accessibility. The split follows the change rather than mandatory role names.

Give each reviewer:

```text
Review [base → candidate] using [skill] at the [gate] gate.
Your responsibility: [behavior or contract], including [shared seams].
Raw context and permitted source: [locations].
Known inventory: [entry points/owners/sinks, explicitly provisional].
Inspect code and establish the rule independently. Follow effects across files.
Return source-backed paths, candidate findings, counterevidence and gaps.
Do not read peers' conclusions or evaluation answers. Do not implement.
Execution permissions and artifact destination: [explicit boundary].
```

Keep initial discovery independent. Share newly established source facts for integration afterward, preserving contradictory interpretations for investigation. Do not require a different model, paid service or tool; model diversity is an experiment, not proof of independence.

## Challenge framing at the design gate

Assign a framing challenger where the problem statement, model or relied-on contract needs independent scrutiny. This is a responsibility, not a compulsory extra agent on every change. Use the bundled [Adversarial design reviewer](../reviewers/adversarial-design-review/SKILL.md) for that role. Pass its exact local path to the reviewer and have it read the instructions directly; it is part of this package, not a separately installed dependency. Its responsibilities are:

- Recover the required outcome and constraints from raw context and source, separating them from proposed mechanisms and motivating examples.
- Identify the owner of each consequential rule and the input that actually selects behavior. Inspect its creators, editors and consumers.
- Derive a supported counterexample that distinguishes the intended rule from an incidental dependency. Trace it to the consequential sink, then inspect the strongest defense.
- Classify a justified challenge as problem/specification, design/contract or implementation. A valid inherited flaw cannot be excluded merely because its line is unchanged; establish whether the current outcome depends on it.
- Recommend the smallest complete correction and explain any warranted reframe under the same requirements. Accept a sound design; do not demand novelty, abstraction or disagreement.

Give this role raw source and discussion before peer findings. Send its evidence through the same finding verification as other candidates. Do not let a design challenge replace source coverage, code-quality, security, test or UX responsibilities. All reviewer instructions and shared references are contained in the parent `review-cookbook` directory.

## Verify on separate inputs

Use [Verification](verification.md) for two distinct tasks:

- **Finding verification:** give the verifier raw evidence and the union of candidates, including unresolved ones. Require a decision and evidence for each. Agreement frequency is not the decision rule.
- **Omission audit:** give a fresh reviewer source, raw context, the current gate and responsibility scope. Have them independently enumerate relevant paths before revealing discovery findings or coverage conclusions. Then compare inventories, inspect missing paths and report integration gaps. Preserve their initial inventory so the independence claim is auditable.

These tasks may share an agent after the blind inventory is recorded, but the verifier must not seed that inventory with the finding list. For a large change, partition omission inspection by flows and retain an integration owner. If tooling cannot supply independent contexts, perform explicit sequential checks and report that limitation.

## Reconcile and close the gate

Inspect disagreements at their source and resolve them by rule, supported trigger and causal consequence. Newly found candidates receive the same verification as initial candidates. Reopen affected traces when the auditor discovers another writer, lifetime or consumer. Keep rejected candidates with reasons to distinguish justified filtering from lost defects.

Conclude each responsibility as inspected under stated conditions, contradicted, unresolved, excluded with evidence, or deferred by a blocked gate. A coordinator's summary cannot upgrade missing specialist evidence. Record material scope gaps and runtime proof separately. Advance only after the current gate satisfies the parent skill's criteria.

Repeat investigation for specific new evidence or unfinished obligations. Avoid endless agent chains, redundant retracing and wholesale re-review of settled code. Relevant coverage determines completion; there is no fixed number of passes or findings.

## Preserve authorization and portability

Subagents inherit the review-only and environment boundaries. Do not send reviews to authors, start implementation, install tools or provision test services through delegation. Keep artifacts external to the product checkout. A standalone host can follow the same procedures sequentially; it must not claim independent review it did not perform.
