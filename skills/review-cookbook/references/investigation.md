# Code inspection and source-to-sink review framework

Code inspection supplies the evidence; source-to-sink tracing connects it into behaviour; the parent skill's gates determine which questions to settle first. Hypotheses are a supporting technique for uncertain findings. A review must cover affected responsibilities even when no suspected bug initially comes to mind.

Use one evolving working record in existing notes or an authorised external artifact. Keep the scope proportionate: a small change may need one trace; a large change needs decomposition and an integration pass. This framework grants no execution, delegation or implementation authority beyond the parent skill and user instructions.

## 1. Map the change into reviewable flows

Read the complete diff and available requirements/discussion. Separate intended outcomes and preservation rules from proposed mechanisms and correctness claims. Index meaningful changes by behaviour, state ownership and shared contracts, including migrations, configuration, tests and UI where affected. Mark generated or mechanical material with its verification basis rather than treating it as uninspected semantic code or a new business flow.

For a large PR or stack, identify the dependency order and shared seams before splitting the work. A flow can cross an API, service, model, worker and screen. Reviewing those files independently does not establish that their contracts agree. Keep dependent PRs in scope regardless of author; inspect tip against stack base where tractable, otherwise review in dependency order and finish with the integrated state.

For each affected flow, identify its entry points, expected outcome, authoritative state and consumers. Track a shared component once, then check the assumptions its distinct callers impose. Do not silently treat inherited code as unrelated when the change relies on it. Stop expanding at demonstrated unchanged contracts, not merely at the diff boundary.

## 2. Inspect the code and follow sources to sinks

Read meaningful changed logic with surrounding control flow, actual callees, relevant models/schema and test assertions. Follow evidence instead of inferring behaviour from names, interfaces, comments or the PR description. Classify what remains unreviewed at the current gate; a file inventory is an index, not proof of inspection.

Build the relevant end-to-end chain from code:

```text
entry / producer → validation and representation → transformation / decision
→ state or handoff boundary → persisted result, external effect or user-visible output
```

Inputs include user values, stored records, configuration, permissions, time and events where they select the affected behaviour. Establish who produces and can change them, what information is copied, derived, defaulted or discarded, and which values the final consumer actually reads. At consequential sinks, trace backward to check alternate supported writers and entry points. Check that shared enforcement genuinely covers them.

Follow control as well as data: branches, early exits, missing values, errors, ordering and delayed work can skip a required effect or change its meaning. Locate the actual transaction, ownership and consistency boundaries. Inspect a guard's scope, inputs and lifetime, including whether its protection still applies when the dependent effect occurs. A lock or validation call is not enough without that relationship; absence of a preferred technique is not by itself a defect.

Extend traces across supported lifecycle transitions that affect the obligation, such as edits, generation, retries, cancellation and recovery. Select combinations because the code or contract couples them, not by enumerating every possible combination. A documented recovery action must be reachable and able to complete the task under the conditions where it is offered; an explicit bound or rejection alone does not establish recovery.

Use [Test quality](test-quality.md) throughout: inspect the oracle, setup, assertions and path actually exercised. When authorised execution is necessary, run an existing meaningful check with proof appropriate to the boundary. Never turn read code into a claimed runtime result, replace a forbidden service, or edit the behaviour under review to manufacture evidence.

## 3. Assess design through the inspected behaviour

The design gate is grounded in code, not limited to diagrams or schema files. Reconstruct the model implemented by producers, representations, relationships, policy selection and consumers. Compare that model with the required outcome before evaluating general implementation quality.

Use [System design](system-design.md) to establish whether:

- identity, scope and cardinality can represent the required distinctions;
- facts and policies have appropriate owners, with authoritative inputs reaching enforcement;
- supported lifecycle changes preserve current and historical meaning;
- invariants and failure boundaries hold across the affected writers and consumers;
- growth, limits and recovery support the required operation without silently losing work or meaning.

These are questions about inspected responsibilities, not a demand for a preferred architecture. A local implementation may execute its algorithm perfectly while selecting the wrong rule, collapsing distinct facts, or relying on an owner that cannot uphold the contract. Those are design defects even when no new model or schema appears in the diff. Conversely, a different structure is only a preference unless a concrete failed responsibility is established.

Complete relevant design investigation across the affected flows before leaving that gate, including when one blocker already exists. A design blocker stops progression to general implementation and UX review; it does not prohibit reading their code to establish the design's actual consequences. Preserve incidental findings without claiming those later layers have been reviewed. Continue through the parent skill's implementation and UX gates only when their prerequisites are met.

## 4. Verify findings; use hypotheses for uncertainty

An actionable technical finding needs two independent supports: an established obligation and a reachable implementation path that violates it. Proving that behaviour occurs does not establish that it is wrong. Derive expected behaviour from requirements and legitimate existing contracts; do not infer it from a preferred redesign, current tests or an assumed external workflow.

For a clear inspected defect, document the trigger, causal path, consequence and strongest counterevidence directly. When uncertainty remains, state a falsifiable case: under which supported condition should which outcome occur, what might differ, and what guard or contract could refute that concern? Inspect the actual path and competing explanation. Retain supported, disproved or unresolved conclusions with their evidence and conditions; do not invent a hypothesis for every inspected line or sound path.

An uncertainty about business meaning needs a product decision. An uncertainty about actual mechanics calls for further authorised source inspection or execution. Keep those separate. Unknown occurrence frequency limits impact estimates; it does not refute a demonstrated violation on supported input. Equally, a merely imaginable input is not a supported producer path or an approved performance requirement.

Record source-established reasoning separately from execution observations. Unperformed essential runtime proof remains a readiness gap, even when source establishes a defect. Unsupported assumptions remain visible instead of being promoted to confirmed technical defects; an unresolved contract indispensable to the current gate still blocks progression under the parent skill. Recommend the smallest complete correction and preserve legitimate contrasting behaviour; review does not authorise implementation.

## 5. Reconcile coverage and the integrated result

Before leaving a gate, compare inspected flows with the complete change and actual affected dependencies. Account for alternate producers, required effects, shared invariants and downstream consumers. Mark obligations supported under stated conditions, contradicted, unresolved, or outside scope with a justified boundary. Mark dependent gates not reviewed where appropriate. Narrow evidence cannot close a broader contract, and resolving every generated hypothesis cannot close uninspected behaviour.

For large changes, revisit the connections between separately reviewed parts: do they use the same identity and meaning, preserve each other's invariants, and agree about state transitions and failure outcomes? Combine changes as they will actually run. Locally correct parts can still form an incorrect system. This integration pass assesses the reached gate; it does not bypass a blocked prerequisite.

If independent reviewers are authorised, give each the same candidate and raw context, a bounded flow or responsibility, its shared dependencies and the current gate. Require a handoff of established contracts, decisive source evidence, findings and gaps. One reviewer reconciles shared seams and the complete changed scope. Specialist backend/frontend/test inspection remains useful, but no layer's isolated approval proves an end-to-end flow.

Keep a compact working map, using the repository's existing record format where available:

```text
Flow / responsibility; required outcome and basis; current gate
Changed code and relied-on owners / callers / consumers
Source-to-sink trace and decisive locations
Design/implementation/UX assessment within the reached gate
Findings, counterevidence and unresolved questions
Coverage boundary; runtime evidence required / observed
```

Hypotheses can be linked to this record where useful; they are not its organising unit. Share settled evidence and reopen it only when relevant assumptions change. Report consequential findings and material gaps rather than reproducing the working map. No fixed hypothesis, file, finding or work-count quotas apply.
