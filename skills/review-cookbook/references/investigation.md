# Investigation procedure

Use this procedure within the parent skill's sequential gates. It structures evidence collection; it does not authorize execution or implementation. Use one evolving working record, in existing review notes or an authorized external artifact. A compact entry is enough when the responsibility is small. Keep the final report focused on consequential findings and missing proof.

## 1. Establish the coverage boundary

Read the complete change and available requirements and discussion. Separate established outcomes and constraints from proposed mechanisms and unverified claims. State what the change must achieve and what existing behavior it must preserve. Unresolved business meaning is a product question; the implementation cannot settle it merely by behaving one way.

Map the supported flows affected by changed assumptions, including an existing contract the new behavior relies on. Link each obligation to its selecting authority and affected outcome. Do this before concentrating on suspected defects, and update it as source reveals omitted dependencies. Group equivalent paths only when their shared enforcement is demonstrated; retain different owners, state transitions or consequences separately.

Stop expanding at a demonstrated unchanged contract. A call into existing code is neither automatic clearance nor a reason to audit its unrelated responsibilities. The map is proportionate to the affected behavior, not every input in the repository.

## 2. Trace inputs and control to outcomes

For each affected flow, establish the actual reachable chain:

```text
producer / entry → representation and transformations → decision / authority
→ guard and state boundary → dependent write, output or external effect
```

An input can be a request value, stored record, template, configuration, permission, clock, event or provider response. Follow whichever inputs select the relevant behavior. Record who creates or changes a decision input, what it represents, how it is normalized or derived, and why the consumer may trust it. Do not assume a mutable description or incidental state is authoritative just because it reaches a capable helper.

Trace control as well as data: branching, early exits, absence, defaults, ordering, handoffs and delayed work can decide whether a required effect happens at all. Identify where values are read and where their validity must still hold. At persistence or external boundaries, establish the actual transaction, ownership and failure semantics relevant to the obligation. A final consumer may sit outside the changed component.

At consequential sinks, work backward to discover alternative supported writers and decision paths. Check whether they converge on the same enforcement or bypass it. Reuse already established paths; expand only where dependencies differ. For UX, include the user's action, displayed state, persisted outcome and feedback path; source tracing does not establish visual quality or human usability.

Keep references to decisive producers, transformations, guards and consumers. A list of filenames or an architectural arrow diagram without evidence is an index, not a verified trace.

## 3. Derive hypotheses from the map

Use a mismatch, ambiguous authority, lifecycle transition or untested assumption to propose a concrete case. Derive the expected outcome from the obligation rather than copying the current implementation or its tests. Vary an input or ordering only where the actual supported flow permits it; select combinations when a relationship makes them relevant, not by enumerating an arbitrary Cartesian matrix.

A useful hypothesis says:

```text
Under [reachable condition], [obligation] requires [observable outcome].
The implementation may instead [different outcome] because [suspected responsibility failure].
It would be refuted if [specific reachable guard, transformation or contract] prevents that consequence.
```

Record what is known and what remains to be established. Alternative explanations can include incorrect fixtures, a deliberately narrower contract, an upstream normalization or an effective downstream guard. Do not assume the author's diagnosis or your first interpretation is correct. Do not require a defect hypothesis for every sound path; positive evidence and explicit unknowns also contribute to coverage.

## 4. Test the hypothesis against the actual path

Follow the distinguishing case through real callers, transforms, state changes and final consumer. Check both the predicted failure and the strongest evidence against it. Read surrounding code, relevant producers, canonical schema and existing tests as needed; a diff line alone rarely establishes a cross-layer consequence.

For each relied-on guard, establish its scope, inputs and lifetime. Determine whether it protects the dependent effect, including relevant supported changes between selection and use. Presence of validation, a lock, constraint or snapshot is not proof of its protection; absence of one particular technique is not proof of a defect either. Explain what the actual mechanism guarantees.

When execution is authorized and needed, choose a check whose observations distinguish the competing explanations. Inspect its independent oracle, setup and assertions using [Test quality](test-quality.md). Do not patch the disputed behavior, substitute a forbidden service, or treat a sequential scenario as evidence for an overlapping one. State the exact remaining proof if execution is unavailable or outside scope. Source reasoning and executed observations may support different portions of the same case.

If the trace reveals a different relevant failure, link it to its obligation and investigate it separately. Do not force evidence into the original theory or count manifestations with the same cause as independent discoveries. Reopen earlier conclusions when their assumptions change.

## 5. Resolve cases separately from coverage

A hypothesis has one disposition:

- **Supported:** the stated reachable case violates an established obligation through the demonstrated path. Describe the consequence and the smallest complete correction boundary, preserving legitimate contrasting behavior. This is not permission to implement.
- **Disproved:** specific counterevidence prevents the predicted failure under the stated conditions. Record that boundary so the case is not repeatedly rediscovered.
- **Unresolved:** name the missing contract, path evidence or execution observation and what would distinguish the alternatives. Do not convert uncertainty into a confirmed bug or a clean bill of health.

Record the evidence basis separately: source-established, execution-observed, or a combination, with conditions and limits. A source-supported finding can coexist with outstanding runtime proof; a hypothesis can be disproved only for the scenario actually assessed.

Then reconcile the obligations themselves. Mark each as supported under explicit conditions, contradicted by a linked finding, unresolved in a named respect, or outside scope with a justified boundary. Narrow proof does not close a broader obligation. Compare the map with the complete change and actual affected flows: are meaningful inputs, alternative producers, skipped effects or downstream consumers still unaccounted for? This is a scope check, not a guarantee of exhaustive correctness.

Closing every hypothesis you generated is not the same as investigating every affected obligation. A blocked gate still requires investigation of its other relevant responsibilities. Do not claim later-gate coverage because its files were used to assess the current gate. Follow the parent skill's progression and readiness rules.

## Working record

Keep linked evidence rather than repeated narratives. This is a suggested compact shape, not a required storage format or public report template:

```text
Obligation O1: outcome / preservation rule; basis; affected flows; gate
Path P1: producer → decision owner → guard/state boundary → effect; source references
Hypothesis H1 (O1/P1): condition; expected/predicted outcomes; possible falsifier
Evidence: actual trace; strongest counterevidence; source/execution basis and limits
Case disposition: supported / disproved / unresolved; consequence or missing proof
Obligation disposition: supported under conditions / contradicted / unresolved / outside scope
Correction boundary, if established: failed responsibility; legitimate contrasts to preserve
```

One hypothesis may involve multiple obligations, and an obligation may have several distinct cases. Share paths and evidence by reference without silently merging different responsibilities. Retain detailed working notes; report the decisive causal evidence, useful corrections and material gaps. There are no hypothesis quotas, fixed checklist counts or report-length targets.
