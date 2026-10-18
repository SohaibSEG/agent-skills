---
name: backend-data-security-review
description: Review server contracts, authorization, transactions, audit, migrations, dependencies and operational failure boundaries through source-to-sink inspection.
---

# Backend, Data and Security Review

Read the [shared review contract](../../references/review-contract.md) once. Inherit the parent’s frozen target, assigned gate and evidence scope.

Use at the implementation gate for server, data, security and operational boundaries. Read these paths earlier when they establish a design consequence.

Use [Inspection](../../references/investigation.md) when building or extending the source map, including backward traces to alternate writers. Apply [Backend](../../references/backend.md) to relevant alternate writers, authorization/tenancy, schema/migrations, transactions, audit, retries, external effects, query growth and dependency exposure. Inspect changed configuration, secret boundaries, release ordering and resource budgets without executing plans.

Return entry-to-effect traces, concrete invariant violations, defended boundaries and required real-service proof. For a model/authority defect, send the evidence back to system design rather than treating it as a local guard omission.
