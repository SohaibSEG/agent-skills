---
name: review-coverage-audit
description: Audit the completeness of a code review by independently tracing omitted writers, consumers and integration seams. Use after discovery; this checks review coverage, not test coverage percentages. No QA execution.
---

# Review Coverage Audit

Read the [shared review contract](../../references/review-contract.md) once. Inherit the parent’s frozen target, assigned gate and evidence scope.

Use before gate closure to inspect completeness, not test coverage percentages. This role initially receives the raw diff/context and assigned scope, without discovery conclusions.

Apply **Audit omissions independently** in [Verification](../../references/verification.md). [Inspection](../../references/investigation.md) defines source tracing; use only the specialist guide needed for a newly found path.

Record the independent inventory before reading discovery reports. Reconcile afterward and return newly inspected paths, new candidates, unsupported coverage claims and remaining gaps. Send new candidates to finding verification. If conclusions were already visible, disclose the lost independence.
