# System-design review: inspect the model through its effects

Use this reference within the parent skill's design gate when a change affects business meaning, authority, identity, relationships, lifecycle, module contracts, execution topology or growth assumptions. A model includes configuration and decision inputs as well as persisted entities. Review only: inspect source and existing evidence, run only authorized safe checks, and recommend corrections without implementing them.

Start with the code and supported flows. Reuse the shared [inspection record](review-records.md) to connect requirements, owners, decisions, effects and evidence. Hypotheses help resolve uncertainty found along those traces; they are not a substitute for inspecting the changed responsibilities. Establish unchanged contracts proportionately and stop expansion there. Do not turn a local change into an unrelated architecture audit.

Design precedes implementation and UX review. A design blocker stops progression to those gates, but finish the other relevant design responsibilities before reporting. Read downstream services, workers, queries, tests and screens whenever they supply evidence for the design contract. Their location does not make that evidence out of scope, and reading them does not clear a later gate.

## 1. Recover intent and contrast it with the actual decision

1. Read the issue, PR description, linked requirements, discussion, author replies and prior findings alongside the complete candidate diff. Extract the affected actor, attempted operation, observed outcome, desired outcome and binding constraints. Separate observations and requirements from suggested diagnoses, mechanisms and claims of correctness. Retain useful context while checking its claims; neither the latest comment nor the existing implementation is automatically the business specification.
2. Locate the code that selects the behavior and follow its inputs back to their origins. Record the proposed explanation of the failure beside the actual selection rule. Inspect a supported case where competing explanations predict different outcomes. Distinguish a product defect from a fixture, tool or environment failure using the failing boundary and its evidence.
3. Express the obligation as observable behavior: the trigger, actor and scope, applicable states, required outcome and behavior that must remain unchanged. Contrast the new behavior with the destination revision and existing contracts. Include supported combinations and inverse operations affected by the changed assumption, not only the reported example.
4. Resolve disagreements using source traces, authoritative contracts and domain evidence. Existing code and tests show behavior; they do not independently establish its business meaning. Mark inaccessible context and unresolved product decisions explicitly. Investigate technical facts available in the repository before asking the user to supply them.
5. Convert quality claims into operating conditions and measures. Use documented requirements or measured workloads for latency, capacity and recovery expectations. Record unknown targets rather than inventing them or promoting desirable future capability to a current obligation.

Keep the problem statement, required rule, preservation obligations and unresolved meaning in the shared record. Scenario-based evaluation here is a lightweight application of the [SEI Architecture Tradeoff Analysis Method](https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/), not a claim to perform the full method.

## 2. Reconstruct authority, identity and relationships from source

1. Inspect the relevant schema, migrations, models, command inputs, configuration, serializers and consuming expressions. Establish stable identity, scope, relationship direction, cardinality, optionality and deletion behavior from their actual definitions and use. Compare the storage contract with what commands admit and what readers assume; class names and diagrams alone establish neither.
2. For each decision input, trace who establishes it, who can change it, who derives or defaults it and who enforces the resulting policy. Inspect the assignment at the caller as well as the consuming helper. A suitable field type or correctly implemented helper does not establish that its caller supplied an authoritative value. Follow trust transitions, scope and privileges through those assignments.
3. Inspect values used for more than one purpose. Trace each consuming rule to distinguish independent dimensions from coupled states. Compare reachable combinations with required combinations and locate enforcement of forbidden states. Several flags can admit contradictions; one enum can exclude valid independent choices. Recommend a representation change only where the traced behavior demonstrates the mismatch.
4. Work backward from consequential reads to find assumptions hidden in joins, filters, caches, serialization and display. Check first-item selection, scalar representations of collections, inferred uniqueness and display text used as identity. Trace whether supported writers can produce values or memberships those consumers misinterpret.
5. Separate authoritative facts, intentional snapshots and derived projections. Inspect invalidation, versioning and refresh paths before calling a copy competing truth. Where contexts intentionally use different meanings, inspect their translation boundary and ownership rather than imposing a single universal model.

Use a compact map when it clarifies the trace:

| Fact or relationship | Meaning, identity and scope | Authority and supported writers | Decisions and consumers | Valid states and enforcement evidence |
|---|---|---|---|---|
| Changed or relied-on fact | Contract established from evidence | Actual assignments and commands | Actual expressions and sinks | Guard, constraint, protocol or gap |

[Fowler's Bounded Context](https://martinfowler.com/bliki/BoundedContext.html) informs explicit translation between distinct models. It does not justify inconsistent meanings within a shared contract.

## 3. Trace supported writers and consumers through the lifecycle

1. Follow each changed operation from its entry point through validation, transformations, authority selection, state transitions and final effects. Search callers and writes to the same state to find supported alternate paths, including imports, generation, transfers, administrative commands and background work. Classify their relevance from the contract they share, not whether their files appear in the diff.
2. At each transformation, inspect the values copied, derived, defaulted, discarded or reinterpreted. Follow missing, unknown and stale values into the next decision. Establish whether a fallback preserves the rule, rejects an unsupported state or silently invents a plausible outcome.
3. Continue from durable state and dispatched work to the actual consumers: operational decisions, external effects, reporting and user-visible results where applicable. Read the fields and predicates used. Record skipped effects and early exits as well as executed effects; successful return values do not prove the intended outcome occurred.
4. Trace supported edits, regeneration, renewal, cancellation, correction, deletion and retries that touch the same obligation. Inspect the selected set of records and references to determine whether the command affects one instance, membership, future occurrences or historical outcomes. Compare forward and inverse actions for preserved identity, ownership and permitted state transitions.
5. Contrast displayed state with decision-making state when presentation supplies evidence of the model. Trace both to their sources. A display of current configuration may differ legitimately from an operation's historical snapshot; establish the required semantics before treating the difference as a defect.

Retain source locations for `entry point → transformation → authoritative fact → decision → sink`, including alternate paths that alter the conclusion. Verify every supported writer and affected consumer of the changed invariant, grouping paths only after establishing the common enforcement boundary. Do not infer coverage from a touched-file list or from checking one writer with several names.

## 4. Inspect consistency, time and repeated operations

1. Identify the records, memberships and effects that must agree at each operation boundary. Locate the owner able to enforce that agreement and inspect the actual commit, dispatch and acknowledgment boundaries. Separate immediate consistency from permitted delayed propagation; for delayed views, inspect acceptable staleness, ordering, versions, recovery and action-time revalidation against authority.
2. Trace stable identity separately from versions. Inspect the use of occurrence time, effective time and the time information became known where they differ. Determine whether each decision consumes current policy, policy effective at the event, or policy known at the original decision. Include queued work whose inputs or policy can change between submission and execution.
3. Follow configuration or template edits into existing instances and historical records. Inspect which values remain linked and which are snapshots, then trace corrections, overlapping versions, deletion and retention. Recomputing from today's values can change historical meaning even when the new calculation is internally correct.
4. Construct reachable interleavings for commands sharing the invariant. Locate reads, waits, state checks and writes; inspect what another supported command can change between them. Follow repeated, concurrent, reversed, late and out-of-order operations to final state and effects. Identify the exact agreement lost if both commands succeed locally; a request for “more transactions” does not establish a mechanism or correction.
5. Inspect operation identity and effect ownership across retries. Trace a repeated request, duplicate delivery or recovery attempt to deduplication and recorded outcomes; distinguish another attempt at the same operation from a new operation with similar inputs. Check that denial, cancellation or partial failure cannot leave effects attributed to a different identity or scope.

Use the [backend reference](backend.md) for detailed transaction, retry and audit inspection where needed to establish these design boundaries. Keep source conclusions separate from runtime evidence: an interleaving supported by source can establish a defect, while a protocol's runtime correctness may still require controlled competing sessions or failure injection.

[DDD aggregates](https://martinfowler.com/bliki/DDD_Aggregate.html) describe an integrity owner; [Temporal Object](https://martinfowler.com/eaaDev/TemporalObject.html) distinguishes continuing identity from versions. Neither mandates a class hierarchy, ORM or event-sourced architecture. Fowler labels the temporal material as draft guidance.

## 5. Inspect responsibility and caller obligations

1. Inventory the existing owners, shared controls and operation boundaries serving the changed flow. Compare callers that appear similar to establish whether they share policy or only syntax. Inspect their legitimate differences before proposing consolidation.
2. Read call sites and implementations together. Record the arguments, configuration, scope, ordering, error handling, retries and transaction obligations callers must understand. Identify internal decisions repeated across callers or sequences of private operations callers must coordinate to preserve one invariant.
3. Trace each suspected responsibility leak to a concrete bypass, divergent rule or coupling cost relevant to the change. Compare a coherent operation owned at the existing boundary with the proposed interface. Preserve transport parsing and provider I/O at their appropriate boundaries; a new service or helper name alone does not move responsibility.
4. Conceptually remove an abstraction and follow the obligations that would return to callers. Distinguish hidden necessary complexity from forwarding code. Recommend extraction, movement or removal only when it improves the evidenced responsibility boundary; use the [refactoring reference](refactoring-patterns.md) to describe preservation constraints and affected callers.
5. Contrast logical separation with process or service separation. Trace additional failure, authorization, compatibility and operational obligations introduced by a network boundary. Require a supported ownership, isolation or capacity benefit before recommending it.

Record the owner and caller obligations that explain the conclusion. Retain a sound existing boundary. Do not manufacture generic managers, pass-through layers or line-count targets. The [Ousterhout–Martin discussion](https://github.com/johnousterhout/aposd-vs-clean-code) informs complexity and decomposition trade-offs; it is not an authority for choosing one author's style universally.

## 6. Trace failure boundaries and growth costs

1. Identify the inputs that determine work: active entities, supported relationships, retained history, concurrent operations and fan-out. Follow loops, queries, payload construction and materialization to estimate how work and memory grow. Distinguish sparse supported relationships from constructing every possible pair. Compare estimates with documented conditions and available measurements.
2. Locate scarce resources and queues: pools, locks, workers, remote quotas, memory and rendered elements where applicable. Inspect admission bounds, backpressure, cancellation and resource release. Trace whether a heavy request or tenant can prevent other supported work from progressing. Establish the limiting resource before recommending caching, queues or horizontal scaling.
3. Trace failure windows before and after local commit, dispatch, remote acceptance and acknowledgment. Inspect the state exposed after timeout, cancellation, ownership expiry and retry exhaustion. Determine whether the outcome is known, pending or ambiguous, and whether recovery can lose or duplicate effects. A correct calculation does not establish a correct delivery protocol.
4. Follow the operator's available evidence from failure to diagnosis and recovery. Inspect attributable state, correlation, durable outcomes and replay or repair controls. Logs alone may not reveal whether a remote action committed. Establish a safe recovery path where the business contract requires one, including how its own repetition behaves.
5. Trace identity, authorization and configuration through each execution boundary, including jobs and caches. Compare equivalent operations across supported execution modes. Verify that changing transport, scheduling or storage does not silently change authority or business meaning.

For each credible failure or bottleneck, retain its source mechanism, affected condition and distinguishing proof. Mark unmeasured estimates as estimates. [Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/) informs bounded work and overload behavior; a thought experiment does not prove throughput.

## 7. Resolve uncertainty with contrasts and counterevidence

Use a hypothesis when the inspected source leaves a consequential uncertainty. Directly established defects and sound paths need no hypothesis ceremony. Select contrasts from actual supported behavior and decision inputs, not a fixed scenario quota.

| Uncertainty found in the trace | Concrete inspection or distinguishing evidence |
|---|---|
| A decision may depend on a non-authoritative value | Trace its assignment and mutations; compare supported inputs with the same business meaning and different representation. |
| A shared invariant may hold only on one path | Follow another supported writer to the same state and inspect the strongest shared guard or constraint. |
| Coupled fields may suppress valid combinations | Follow an independent input change through each consuming predicate and contrast the required outcomes. |
| Historical meaning may change after an edit | Compare current and historical consumers, their source versions and the update propagation path. |
| Repetition, concurrency or failure may corrupt an outcome | Derive a reachable order of reads, effects and acknowledgments, then inspect protections and committed outcomes. |
| A documented variation or workload may exceed the design | Trace the additional supported case through ownership and bounded work; separate measured evidence from estimates. |

State the prediction that distinguishes the suspected failure from the sound explanation. Inspect the strongest guard, constraint, snapshot, protocol or consumer check that could refute it. Establish reachability and consequence before reporting a defect; naming a mutable input or requesting a test is insufficient. Keep disproved cases and unresolved assumptions distinct from findings, and reopen them only when relevant evidence changes.

A future variation can inform a trade-off. It blocks only when it exposes a current required rule or an explicitly committed requirement. Do not manufacture extension requirements to justify a preferred model.

## 8. Recommend the smallest complete correction and its transition

1. Assess the submitted change against the established rule and supported paths. Identify exactly what it corrects and any remaining violation. Recommend a correction at the responsible owner or representation that closes the demonstrated gap while preserving sound identity and contracts. The submitted patch may already be that correction; do not invent another option merely to produce a comparison.
2. Trace the recommended boundary through storage, public contracts, generated data, background work and consumers. Identify the behavior preserved and the intentional correction separately. Include effects that simplification could remove. Stop at demonstrated unchanged contracts and distinguish necessary scope from optional cleanup or speculative capability.
3. Compare a materially different alternative only when it exposes a real trade-off. Use the same conditions: invariant coverage, caller obligations, supported variation, failure behavior, user flow, data transition and change surface. Recommend one option with its main cost and the evidence that would change the recommendation. A larger model or broader refactor is not inherently more complete.
4. Inspect existing data and supported deployment overlap for the proposed transition. Identify deterministic conversions, ambiguous records requiring a decision, compatibility windows, resumable backfills and the condition for retiring old paths. Do not assume empty data, active tenants or a clean cutover without evidence. Separate application rollback from data reversibility and identify recovery where forward repair is required.
5. Specify proof at the affected contract: preserved and corrected behavior through supported writers and consumers, historical semantics, state and side effects after failure, and transition applicability. Record what source already establishes and what requires authorized execution. Do not implement the correction, provision validation infrastructure or start a fix loop under this review.

Use [evolutionary database design](https://martinfowler.com/articles/evodb.html) for controlled transitions, without treating permanent dual authority as a default. Separate read and write needs where justified; [Fowler's CQRS guidance](https://martinfowler.com/bliki/CQRS.html) addresses the additional complexity of a larger separation. [Sandi Metz on wrong abstractions](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction) supports examining shared reasons to change rather than equating similar syntax with shared policy.

## 9. Reconcile design coverage and report

Return to the shared map of changed assumptions and preservation obligations. Account for their authority, relationships, lifecycle, supported writers and consumers, side effects, failure boundaries and relevant growth conditions. Close each applicable obligation with evidence or an explicit gap. Finding a blocker, reading all changed files or resolving all listed hypotheses does not establish that the remaining design responsibilities were reviewed.

Use the parent skill's findings format, with consequential findings first. Keep detailed maps as supporting evidence and expose only what the decision needs:

```text
Required outcome and preservation obligations:
Actual authority, identity, relationships and historical meaning:
Causal path, supported trigger, consequence and counterevidence:
Smallest complete correction, affected contracts and main trade-off:
Transition risks and required proof, distinguishing source from execution:
Design source status, uncovered obligations and downstream gate status:
```

A confirmed design defect, unresolved business contract or missing evidence indispensable to assessing design blocks progression. Complete the remaining relevant design investigation and leave dependent gates not reviewed. Missing runtime execution alone does not stop otherwise assessable source review, but essential missing execution evidence blocks readiness under the parent skill. Apply that distinction to deterministic local behavior as well as database and provider behavior. If later evidence invalidates a design assumption, reopen it and mark dependent conclusions affected.

Do not clear a design because tests pass or it uses a familiar architecture name. Do not block it for aesthetic preference without a causal defect. If the complete correction needs broader work, report that boundary and any unresolved scope decision without implementing it. The review ends with evidence-backed conclusions and explicit limits, not a claim that every architectural risk has been eliminated.
