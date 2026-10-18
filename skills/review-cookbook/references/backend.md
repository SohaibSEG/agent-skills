# Backend review cookbook

Use the applicable sections to trace changed behavior from entry point to durable effects. These are review steps and recommendation patterns, not authorization to edit code. Inspect existing evidence; run validation only when authorized and consistent with project rules; recognize authorization already established in the session. Record missing essential runtime proof as a readiness blocker. A causal design flaw remains blocking until addressed; unrelated architectural renovation needs separate authorization. PostgreSQL examples below are engine-specific; verify equivalent behavior for the actual database and version.

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

## 3. Compare data contracts and upgrade behavior

1. Compare the schema, application models, serializers, and migration sequence for types, nullability, defaults, precision, relationships, and deletion behavior. Diagnose disagreement from committed contracts; one developer database is insufficient evidence of the intended schema.
2. Check whether application-only uniqueness or relationship validation admits races or alternate writers. Recommend an appropriate database constraint alongside useful application errors. **PostgreSQL:** inspect nullable uniqueness semantics, and do not rely on a `CHECK` that reads other rows. [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
3. Inspect upgrade ordering, existing data, backfill restartability, and compatibility while old and new application versions overlap. Recommend staged expansion, data transition, and later removal where a single destructive step breaks supported deployments. [Evolutionary database design](https://martinfowler.com/articles/evodb.html)
4. Request fresh-install and supported-upgrade evidence on the real database engine when applicability changes. Include representative existing values and interrupted backfills. Identify which contract fails; do not recommend suppressing fields or rewriting migration history merely to match a local instance.

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
3. **PostgreSQL:** inspect representative `EXPLAIN (ANALYZE, BUFFERS)` evidence for estimates versus actual rows, loops, filtering, and I/O. Compare query shape and index choices against realistic cardinality; a sequential scan is not automatically a flaw. `ANALYZE` executes the statement, so obtain authorization and use a safe disposable environment for effectful queries. [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
4. Define before/after latency, query-count, memory, and result-correctness evidence appropriate to the claim. Do not accept an index's presence or a tiny fixture's timing as proof of scale.

## 8. Trace unsafe inputs and dependency exposure

1. Follow untrusted data into query languages, command execution, and other interpreters. Recommend parameterized APIs and constrained mappings for dynamic identifiers where string construction changes executable meaning. Check stored procedures and abstraction escape hatches too. [OWASP injection prevention](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html)
2. Inspect changed dependencies and their transitive resolution against current first-party advisories. Establish affected versions, reachable functionality, exploitation prerequisites, and runtime compatibility before assigning impact.
3. Recommend a supported upgrade, removal, or narrowly justified mitigation. Treat a wrapper as temporary only if its checks demonstrably block the specific exploit across every affected path; record residual risk and the required follow-up. [OWASP dependency management](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html)
4. Define regression proof at the actual unsafe boundary and the integration that consumes the dependency. Confirm hostile input fails without partial effects or sensitive error output. Separate verified defects from unanswered applicability questions; neither a clean scanner report nor a version bump proves safety.
