---
name: backend-data-security-review
description: Review server contracts, authorization, transactions, audit, migrations, dependencies and operational failure boundaries through source-to-sink inspection.
---

# Backend, Data and Security Review

Read the [shared review contract](../../references/review-contract.md) once. Inherit the parent’s frozen target, assigned gate and evidence scope.

Use at the implementation gate for server, data, security and operational boundaries. Read these paths earlier when they establish a design consequence.

Use [Inspection](../../references/investigation.md) when building or extending the source map, including backward traces to alternate writers. Use the procedure below for alternate writers, authorization/tenancy, transactions, audit, retries, external effects and dependency exposure. Inspect changed configuration, secret boundaries, release ordering and resource budgets without executing plans. Route schema, query/index, growth and migration work to [Database Review](../database-review/SKILL.md); coordinate shared transaction/tenancy claims without duplicating or silently dropping them.

For relevant boundary contrasts, use [identity without authority](../../references/worked-examples.md#identity-without-authority) or [check then act](../../references/worked-examples.md#check-then-act).

Return entry-to-effect traces, concrete invariant violations, defended boundaries and required real-service proof. For a model/authority defect, send the evidence back to system design rather than treating it as a local guard omission.

Use relevant sections to trace server operations from entry to durable effects. PostgreSQL-specific checks require the actual engine/version; do not generalize them to another database without evidence.

## 1. Locate the operation and its invariant

1. Trace every entry point for the changed operation: request, worker, import, scheduled job, and administrative command. Identify trusted inputs, protected assets, downstream effects, and error exits. Compare the complete call path with the diff. [OWASP secure code review](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html)
2. Write the invariant in observable terms: who may approve, which transitions are legal, what must remain unique, or which balance cannot become negative. Inspect server-side enforcement against skipped, repeated, reordered, and expired steps; client validation cannot establish these guarantees. [OWASP business logic](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html)
3. Identify duplicated orchestration that lets entry points disagree. Recommend one operation boundary owning shared policy and transaction outcome when that duplication causes the defect. Do not prescribe classes, directories, or extra layers without a demonstrated responsibility. [Service Layer](https://martinfowler.com/eaaCatalog/serviceLayer.html)
4. Define proof through each affected entry point: the invalid operation must leave state and external effects unchanged. A patched return value or successful HTTP status does not establish the invariant.

## 2. Follow authorization through reads and writes

1. Enumerate actor, action, resource, and scope combinations, including unauthenticated access where relevant. Check default denial, object ownership, privileged operations, and field-level changes; authentication alone establishes none of these permissions.
2. Follow caller-supplied identifiers through lookups, joins, bulk operations, exports, caches, and downloads. Determine whether one authorized parent can accidentally expose unrelated children. Verify permissions before protected information or effects escape.
3. Inspect asynchronous execution for explicit identity and scope. Check whether work is authorized using the intended execution-time or submission-time policy, rather than inheriting ambient request state or trusting a payload's actor identifier.
4. For a missing scope predicate or inconsistent policy, recommend shared enforcement at the applicable boundary. Define paired allowed/denied tests using existing foreign resources, alternate entry points, and mixed-scope batches; assert both returned data and persisted effects. [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

## 3. Coordinate stored integrity and upgrade behavior

Use [Database Review](../database-review/SKILL.md) for normalization,
constraints/model alignment, physical query/index design, data growth and migration
chains. Backend owns the application-side use case and error contract: trace how
constraint failures, changed fields and old/new schema compatibility affect callers,
workers and audit. Assign the shared transaction boundary once and exchange source
traces; neither role's presence proves the other's work was inspected.

## 4. Challenge transaction and concurrency assumptions

1. Draw the interleaving for each read-decide-write sequence. Identify what another session can change between the decision and mutation, including rows that do not yet exist. Being inside a transaction alone does not prevent every anomaly.
2. Inspect the actual isolation level and locking semantics. Recommend conditional writes, version checks, appropriate locks, constraints, or serializable execution according to the invariant. Rechecking affected-row counts must distinguish a lost race from success.
3. **PostgreSQL:** account for statement snapshots under Read Committed, updated rows returned after lock waits, and whole-transaction retries after serialization failures. Inspect whether business decisions are recomputed after waiting or retrying. [PostgreSQL isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
4. Define a competing-session test with controlled ordering, committed final-state assertions, and rollback coverage. Include both winning orders where they matter. Missing real-engine evidence prevents treating concurrency correctness as verified and blocks readiness; source-review progression follows the parent skill. Sequential tests and mocked locks cannot establish concurrency correctness.

## 5. Examine retries and external effects

1. Enumerate failure windows around remote requests: before delivery, after remote acceptance, before local commit, and after commit but before acknowledgment. Check whether a timeout becomes an honest unknown/pending outcome or a misleading success/failure.
2. Inspect deduplication scope and persistence. Recommend stable operation identity and recorded outcomes when retries can repeat a charge, notification, or resource creation. Define proof for duplicate and concurrent submissions, including reuse of an identity with different input. [Idempotent Receiver](https://martinfowler.com/articles/patterns-of-distributed-systems/idempotent-receiver.html)
3. Identify database/message dual writes. Recommend an outbox or another justified coordination protocol when a crash can lose or invent an event. Inspect relay redelivery and consumer idempotency; an outbox does not eliminate duplicates. [Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html)
4. Review deadlines, retry budgets, cancellation, and resource release. Define failure-injection evidence for malformed responses, connection loss, and exhausted retries, with final business state and downstream effect counts rather than response status alone.

## 6. Verify audit meaning and durability

1. Inspect whether records identify the actor, action, target, scope, time, outcome, and correlation needed to reconstruct the operation. Distinguish attempted actions from committed changes; infrastructure logs may lack business meaning.
2. Check that background actions preserve the initiating context where required. Trace before/after values to actual state rather than untrusted request fields. Recommend recording at the operation boundary when scattered logging loses this meaning.
3. Examine the required durability contract. Where committed mutations require audit evidence, identify crash windows between the two writes and recommend atomic persistence or durable delivery. Keep failed-attempt telemetry distinguishable from committed business events. [Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html)
4. Define evidence for attribution, rollback, denied attempts, duplicate delivery, and logging failure. Inspect access restrictions, retention, injection-resistant formatting, and secret redaction. Record-count assertions alone cannot establish correctness. [OWASP logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

## 7. Bound work and inspect query behavior

1. Trace list, search, export, and batch work as data volume grows. Identify unbounded reads, repeated per-row queries, unstable pagination, large in-memory materialization, and input-controlled fan-out. Recommend bounded work or batching where the mechanism is demonstrated.
2. Inspect request sizes, concurrent work, queue capacity, and slow dependencies. Recommend explicit budgets and isolation where one expensive operation can exhaust shared resources. Define overload evidence that includes other callers' progress. [OWASP denial of service](https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html)
3. Coordinate storage access and performance evidence with [Database Review](../database-review/SKILL.md). Backend owns request/worker fan-out and budgets; database review owns generated query plans, index fit and storage cost. Define end-to-end result correctness and resource proof across that seam.

## 8. Trace unsafe inputs and dependency exposure

1. Follow untrusted data into query languages, command execution, and other interpreters. Recommend parameterized APIs and constrained mappings for dynamic identifiers where string construction changes executable meaning. Check stored procedures and abstraction escape hatches too. [OWASP injection prevention](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html)
2. Inspect changed dependencies and their transitive resolution against current first-party advisories. Establish affected versions, reachable functionality, exploitation prerequisites, and runtime compatibility before assigning impact.
3. Recommend a supported upgrade, removal, or narrowly justified mitigation. Treat a wrapper as temporary only if its checks demonstrably block the specific exploit across every affected path; record residual risk and the required follow-up. [OWASP dependency management](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html)
4. Define regression proof at the actual unsafe boundary and the integration that consumes the dependency. Confirm hostile input fails without partial effects or sensitive error output. Separate verified defects from unanswered applicability questions; neither a clean scanner report nor a version bump proves safety.
