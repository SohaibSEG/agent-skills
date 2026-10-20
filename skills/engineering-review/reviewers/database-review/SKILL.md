---
name: database-review
description: Review relational models, normalization, constraints, queries, indexes, data growth, transactions and migration chains against real workload and deployment contracts. Inspect source and supplied database evidence; do not execute database operations.
---

# Database Review

Read the [shared review contract](../../references/review-contract.md). Inherit the
frozen candidate/base, assigned gate and repository database/deployment rules.
Use the procedure below, selecting the sections implicated by the change and
recording them in the shared coverage record.

Use for schema/model/migration changes and changes to queries, access patterns,
volume, retention or transaction behavior, even when no migration file changes.
At design, inspect dependencies, identity, normalization and lifecycle. At
implementation, inspect constraints, query plans, indexes, locking and upgrade
behavior. Do not clear a later gate while a prerequisite remains blocked.

Trace actual writers, readers and deployment paths. Backend review owns use-case
authorization, business orchestration and external effects; this role owns stored
integrity, physical access and migration applicability. Coordinate the shared
transaction/tenancy boundary and assign each finding one owner. Return a model
ownership defect to system design when a local database fix cannot resolve it.

Return the data invariant and workload, source-backed failure or defended design,
strongest counterevidence, smallest complete correction, and exact real-engine
proof needed. Distinguish graph closure, schema applicability, data preservation
and performance. Normal-form labels, index presence and tiny-fixture timings are
not verdicts. Inspect supplied plans only: migrations, EXPLAIN ANALYZE, load tests
and data mutation belong to separately authorized validation.

Use the affected engine and version, workload and repository migration policy.
Inspect source and supplied evidence; hand execution to separate authorized QA.
A new query or access pattern can require this review without a schema change.

## 1. Model facts and normalization

Identify each relation's grain, candidate keys, functional dependencies, ownership,
cardinality and lifecycle from domain rules and real writers. Trace insert, update
and deletion anomalies; do not infer dependencies from names or a tiny dataset.

- Check repeating groups and overloaded values against the required operations
  (1NF). For 2NF, inspect non-prime attributes depending on only part of a candidate
  key. For 3NF, each nontrivial functional dependency must have a superkey determinant
  or a prime dependent attribute (one belonging to a candidate key); inspect the
  resulting update anomalies rather than a slogan about one chosen primary key.
  A surrogate key does not remove other dependencies. BCNF requires every nontrivial
  determinant to be a superkey. Verify lossless reconstruction and how dependencies
  remain enforced before recommending a decomposition.
- Distinguish a historical snapshot from a second mutable source of truth. For
  intentional denormalization or aggregates, locate the canonical source, update
  owner, consistency/freshness contract, invalidation and rebuild/reconciliation
  paths. Show a reachable disagreement before alleging corruption.
- Justify new tables/columns against existing capabilities, without minimizing
  table count as an objective. JSON, arrays, event payloads and snapshots can fit
  their domain; inspect schema validation, querying and integrity trade-offs.
  Higher normal forms matter only when actual independent relationships expose
  an anomaly. Do not demand decomposition solely for a formal label.

References: [normalization basics](https://learn.microsoft.com/en-us/previous-versions/troubleshoot/microsoft-365/microsoft-365-apps/access/database-normalization-description),
[functional dependencies, BCNF and decomposition trade-offs](https://cs186berkeley.net/notes/note13/).

## 2. Stored integrity and model alignment

Compare canonical models, migrations and every write path for types, units,
precision, time semantics, nullability, defaults, keys and deletion behavior.
Trace identity through joins, including tenant/scope keys where IDs are not global.
Check whether concurrent or alternate writers can bypass application validation.
Inspect database constraints for the actual invariant and useful application errors.

For PostgreSQL, inspect nullable uniqueness semantics, FK actions and checks in
context. A CHECK cannot safely express arbitrary cross-row integrity. A primary
or unique constraint supplies an index, while a referencing FK does not itself
create one; assess the referencing-side access and deletion workload before
recommending it. Avoid duplicate indexes that add write cost without useful access.

Reference: [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html).

## 3. Query efficiency and index fit

Trace filters, joins, sorting, projection and pagination into the actual generated
query, including ORM lazy loads and background/bulk consumers. Check N+1 queries,
join fan-out and duplicate aggregates, unbounded materialization, stable pagination,
large offsets and repeated scans. Bound work without changing result correctness.

Match each proposed index to concrete predicates and ordering, selectivity, tenant
skew and read/write volume. Inspect composite key order, partial predicates,
expressions, included columns and index method against the engine/version and
actual query. Consider parameterization and casts that prevent intended use.
Do not prescribe an index per column or assume every composite index can replace
its prefixes. Account for uniqueness and other consumers before removing an index.

Assess representative plans: estimated versus actual rows, loops, filtered rows,
sorts/spills, buffers and I/O. A sequential scan can be appropriate. Request
representative cardinality and skew, query-count and before/after latency/resource
results when material performance claims need them. An index's existence or a
fast empty database does not prove the claim. EXPLAIN ANALYZE executes the query;
reviewers inspect supplied output and request safe isolated execution from QA.

References: [multicolumn indexes](https://www.postgresql.org/docs/current/indexes-multicolumn.html),
[plan evidence](https://www.postgresql.org/docs/current/using-explain.html).

## 4. Data growth and operational cost

Estimate growth from supported rates, retention and relationships; label unknowns
instead of inventing production measurements. Include row width, large values,
indexes, history/audit/event amplification, WAL and replication, backfills, and
backup/restore needs. Follow repeated updates/deletes into vacuum and bloat pressure.
Check whether batch size, connection/lock duration and maintenance can bound work.

Inspect archive, expiry and deletion ownership against actual retention obligations.
Partitioning needs a workload or lifecycle reason: inspect pruning, key/constraint
limits, future/default partitions, late arrivals and partition creation/retirement.
Do not prescribe partitioning, caching, sharding or denormalization just because a
table may grow. Request a bounded representative scale scenario where essential.

References: [vacuum and statistics](https://www.postgresql.org/docs/current/routine-vacuuming.html),
[partitioning trade-offs](https://www.postgresql.org/docs/current/ddl-partitioning.html).

## 5. Transactions and competing writers

Draw the relevant interleavings, including absent rows and state changed while
waiting for a lock. Inspect isolation, lock order/duration, conditional writes,
affected-row checks, uniqueness conflicts, retries and deadlocks. Confirm a retry
re-evaluates decisions and does not duplicate external effects. Coordinate with
backend review for the business transaction, audit boundary and outbox consumers.

Request real-engine competing-session evidence with controlled ordering, rollback
and durable assertions for material concurrency guarantees. Sequential tests,
mocked locks and transaction syntax alone do not establish those guarantees.

Reference: [PostgreSQL isolation](https://www.postgresql.org/docs/current/transaction-iso.html).

## 6. Migration graph and deployment safety

Inspect every affected stream at current destination and complete candidate:
unique revision IDs, existing parents/dependencies, cycles, resolved heads and
intended branch labels. Verify the repository's permitted head/merge policy.
An Alembic merge revision joins dependencies; it cannot resolve conflicting DDL
or supply missing prerequisite source. Git history and the migration graph are
separate structures. Check competing PR prerequisites and each deliverable state.

Establish protected deployed history using repository policy and deployment/migration
evidence. Preserve applied revisions, including partially applied failed releases;
unknown status is not permission to rewrite them. Local database state is diagnostic.
Where policy permits unmerged feature cleanup, reconcile all references and repair
only its owned local database; prove the resulting source independently.

Inspect populated data, backfill resumability and partial failure, old/new application
overlap, defaults, validation, table rewrites, locks and available disk during DDL.
For concurrent index creation, verify transaction-block restrictions, invalid-index
failure recovery and runner support; do not recommend CONCURRENTLY blindly.
Plan expand/backfill/contract and rollback or roll-forward according to supported
operations, not an assumed reversible downgrade.

Request fresh-install and current-destination upgrade evidence on the actual engine,
plus supported older paths, representative populated data and interruption/concurrency
scenarios where implicated. Distinguish successful schema installation from preserved
business meaning, model alignment and runtime audit/tenancy behavior.

References: [Alembic branches and merges](https://alembic.sqlalchemy.org/en/latest/branches.html),
[PostgreSQL index creation](https://www.postgresql.org/docs/current/sql-createindex.html).

## Evidence and reporting

Tie each finding to its rule, reachable writer/query/deployment, affected data or
workload and strongest defense. Record required proof in the
[QA evidence handoff](../../references/qa-evidence.md). Recommend the smallest complete correction;
label missing production scale or deployment evidence as uncertainty, not a measured
failure. Engine documentation informs checks; repository policy supplies deployment
and acceptance obligations. Fetch version-specific details when they affect a verdict.
