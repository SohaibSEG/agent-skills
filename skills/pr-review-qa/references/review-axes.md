# Review Axes

Apply the baseline to every PR. Add conditional axes based on the changed surfaces; do not burden backend-only changes with UI ceremony or skip architecture because a change looks small.

## Baseline: every PR

- **Specification:** Map every acceptance criterion to implementation and QA evidence. Identify missing, partial, contradicted, and out-of-scope behavior.
- **PR claims:** Verify each material claim in the title/body against code and runtime evidence. Treat undocumented behavior and overstated test claims as findings when they affect review confidence.
- **System design:** Check boundaries, coupling, ownership, failure propagation, compatibility, evolution path, and whether complexity is proportional to the problem.
- **Domain modeling:** Check terminology, invariants, state transitions, illegal states, identifiers, lifecycle rules, and consistency with the existing model.
- **Code hygiene:** Check correctness, readability, duplication, dead paths, error handling, resource cleanup, test quality, and consistency with repository conventions. Avoid subjective style findings that tooling or documented standards do not support.

## Backend, API, and data

- Public contract compatibility: requests, responses, events, schemas, defaults, versioning, and consumers.
- Authentication, authorization, tenancy, validation, privacy, and information disclosure.
- Transactions, retries, idempotency, ordering, races, locks, timeouts, cancellation, and partial failure.
- Database integrity: constraints, indexes, query shape, N+1 behavior, pagination, retention, and large-data behavior.
- Migrations: fresh install, upgrade from base, backfill correctness, mixed-version operation, locking/downtime risk, and rollback policy.
- Observability: actionable logs, metrics, traces, correlation, health checks, and failure diagnostics without leaking secrets.

## Infrastructure and delivery

- Configuration ownership, environment parity, secret handling, least privilege, network exposure, and isolation.
- Infrastructure lifecycle, naming collisions, state drift, idempotency, resource leaks, and cleanup.
- Build and deployment ordering, immutable artifacts, migration sequencing, health verification, rollback, and failure recovery.
- Capacity, connection budgets, concurrency limits, queues, retry storms, timeouts, cost, and operational blast radius.
- CI enforcement: required checks correspond to real risks and cannot report green while skipping changed behavior.

## UI and UX

- End-to-end task completion, navigation, permissions, validation, recovery, destructive-action safeguards, and data freshness.
- Loading, empty, error, offline/degraded, partial-data, long-content, and boundary-value states.
- Keyboard operation, focus order, visible focus, accessible names/roles, announcements, contrast, and reduced-motion behavior where relevant.
- Responsive behavior at representative desktop and mobile sizes; overflow, density, touch targets, and layout stability.
- Browser console errors, failed/cancelled requests, duplicate submissions, stale state, and optimistic-update rollback.
- Consistency with the product's existing components and interaction language. Prefer demonstrated usability problems over aesthetic preference.

## Performance

- Algorithmic growth, repeated work, blocking I/O, serialization, memory retention, connection usage, and concurrency bottlenecks.
- Query counts/plans, payload sizes, caching correctness, bundle size, render churn, layout shift, and startup/runtime hot paths as applicable.
- Prefer repeatable base-versus-head measurements on representative inputs. Record the harness and variance. Without a credible harness, report risks as unverified rather than presenting estimates as measurements.

## Cross-repository impact

- Identify affected consumers, providers, submodules, generated clients, shared schemas, deployment order, and compatibility windows.
- Keep this inspection read-only. State what another repository would need verified; do not expand execution scope without explicit approval.

