---
name: system-design-review
description: Review the model, authority, identity, lifecycle and consistency contracts of a change before implementation review.
---

# System Design Review

Read the [shared review contract](../../references/review-contract.md) once. Inherit the parent’s frozen target, assigned gate and evidence scope.

Use at the design gate to inspect the model after recovering the intended rule. The [problem framing role](../problem-framing-review/SKILL.md) owns challenges to that framing; this role owns structural consequences.

Use the procedure below for relevant authority, identity, cardinality, history, consistency, failure and growth contracts. Use [Inspection](../../references/investigation.md) when building or extending the source-to-sink map.

For relevant contract contrasts, use [units erased](../../references/worked-examples.md#units-erased) or [check then act](../../references/worked-examples.md#check-then-act).

Coordinate relational dependencies and data lifecycle with [Database Review](../database-review/SKILL.md); it owns detailed normalization and storage evidence.

Return the invariant/owner map, causal defects, defended boundaries, unresolved product choices and correction scope. Read downstream implementation as evidence when necessary; do not claim implementation or UX coverage.

Use for authority, identity, relationships, lifecycle, consistency, topology and growth assumptions. Configuration and decision inputs are part of the model, not only database entities. Apply the [shared review contract](../../references/review-contract.md).

## Start from the established rule

Use the parent’s target, outcome and preservation obligations. For disputed problem framing, use [Problem framing](../problem-framing-review/SKILL.md). For source traversal use [Inspection](../../references/investigation.md). This guide owns structural contracts, not another intent-recovery or generic tracing procedure.

## Reconstruct authority, identity and relationships from source

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

## Inspect consistency, time and repeated operations

1. Identify the records, memberships and effects that must agree at each operation boundary. Locate the owner able to enforce that agreement and inspect the actual commit, dispatch and acknowledgment boundaries. Separate immediate consistency from permitted delayed propagation; for delayed views, inspect acceptable staleness, ordering, versions, recovery and action-time revalidation against authority.
2. Trace stable identity separately from versions. Inspect the use of occurrence time, effective time and the time information became known where they differ. Determine whether each decision consumes current policy, policy effective at the event, or policy known at the original decision. Include queued work whose inputs or policy can change between submission and execution.
3. Follow configuration or template edits into existing instances and historical records. Inspect which values remain linked and which are snapshots, then trace corrections, overlapping versions, deletion and retention. Recomputing from today's values can change historical meaning even when the new calculation is internally correct.
4. Construct reachable interleavings for commands sharing the invariant. Locate reads, waits, state checks and writes; inspect what another supported command can change between them. Follow repeated, concurrent, reversed, late and out-of-order operations to final state and effects. Identify the exact agreement lost if both commands succeed locally; a request for “more transactions” does not establish a mechanism or correction.
5. Inspect operation identity and effect ownership across retries. Trace a repeated request, duplicate delivery or recovery attempt to deduplication and recorded outcomes; distinguish another attempt at the same operation from a new operation with similar inputs. Check that denial, cancellation or partial failure cannot leave effects attributed to a different identity or scope.

Use the backend sections [Transactions](../backend-data-security-review/SKILL.md#4-challenge-transaction-and-concurrency-assumptions), [Retries](../backend-data-security-review/SKILL.md#5-examine-retries-and-external-effects) and [Audit](../backend-data-security-review/SKILL.md#6-verify-audit-meaning-and-durability) for detailed inspection where needed to establish these design boundaries. Keep source conclusions separate from runtime evidence: an interleaving supported by source can establish a defect, while a protocol's runtime correctness may still require controlled competing sessions or failure injection.

[DDD aggregates](https://martinfowler.com/bliki/DDD_Aggregate.html) describe an integrity owner; [Temporal Object](https://martinfowler.com/eaaDev/TemporalObject.html) distinguishes continuing identity from versions. Neither mandates a class hierarchy, ORM or event-sourced architecture. Fowler labels the temporal material as draft guidance.

## Responsibility and execution boundaries

Inspect which owner can enforce each invariant and what callers must coordinate. Trace a suspected responsibility leak to a supported bypass or coupling consequence. For module depth, reuse and local interface shape, use [Code design](../code-design-review/SKILL.md) rather than repeating that review here.

Distinguish logical separation from a process/service boundary. A network split introduces failure, authorization, compatibility and operational obligations; require an evidenced ownership, isolation or capacity benefit. The [Ousterhout–Martin discussion](https://github.com/johnousterhout/aposd-vs-clean-code) informs decomposition trade-offs without mandating one style.

## Trace failure boundaries and growth costs

1. Identify the inputs that determine work: active entities, supported relationships, retained history, concurrent operations and fan-out. Follow loops, queries, payload construction and materialization to estimate how work and memory grow. Distinguish sparse supported relationships from constructing every possible pair. Compare estimates with documented conditions and available measurements.
2. Locate scarce resources and queues: pools, locks, workers, remote quotas, memory and rendered elements where applicable. Inspect admission bounds, backpressure, cancellation and resource release. Trace whether a heavy request or tenant can prevent other supported work from progressing. Establish the limiting resource before recommending caching, queues or horizontal scaling.
3. Trace failure windows before and after local commit, dispatch, remote acceptance and acknowledgment. Inspect the state exposed after timeout, cancellation, ownership expiry and retry exhaustion. Determine whether the outcome is known, pending or ambiguous, and whether recovery can lose or duplicate effects. A correct calculation does not establish a correct delivery protocol.
4. Follow the operator's available evidence from failure to diagnosis and recovery. Inspect attributable state, correlation, durable outcomes and replay or repair controls. Logs alone may not reveal whether a remote action committed. Establish a safe recovery path where the business contract requires one, including how its own repetition behaves.
5. Trace identity, authorization and configuration through each execution boundary, including jobs and caches. Compare equivalent operations across supported execution modes. Verify that changing transport, scheduling or storage does not silently change authority or business meaning.

For each credible failure or bottleneck, retain its source mechanism, affected condition and distinguishing proof. Mark unmeasured estimates as estimates. [Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/) informs bounded work and overload behavior; a thought experiment does not prove throughput.

## Review the correction's transition

Trace a proposed correction through storage, public contracts, generated data, background work and consumers. Distinguish preserved behavior from the intentional fix; account for effects simplification might remove. Compare alternatives only when they expose a real trade-off under the same requirements.

Inspect existing data and supported deployment overlap: deterministic conversions, ambiguous records requiring a decision, compatibility windows, resumable backfills and the condition for retiring old paths. Do not assume empty data, active tenants or a clean cutover without evidence. Separate application rollback from data reversibility and forward repair. Define the evidence needed to preserve writers, readers and historical semantics through transition; hand execution to separate QA.

[Evolutionary database design](https://martinfowler.com/articles/evodb.html) informs controlled transitions; permanent dual authority is not a default. [Fowler's CQRS guidance](https://martinfowler.com/bliki/CQRS.html) addresses the cost of separating read and write models. [Sandi Metz on wrong abstractions](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction) supports comparing shared reasons to change rather than matching syntax.

## Return structural evidence

Record authority/identity, relationships, lifecycle/history, consistency, failure and growth conclusions against the source map. Include affected contracts, transition risks and unresolved proof in the [working record](../../references/review-records.md). The parent owns gate disposition and reporting; independent coverage audit checks omitted paths.
