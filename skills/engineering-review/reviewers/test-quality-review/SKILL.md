---
name: test-quality-review
description: Review tests, fixtures, assertions and submitted execution evidence for fault sensitivity and production-path coverage; do not run or rewrite tests.
---

# Test Quality Review

Read the [shared review contract](../../references/review-contract.md) once. Inherit the parent’s frozen target, assigned gate and evidence scope.

Use within every reached gate. Apply [Test quality](../../references/test-quality.md) to the claim being assessed, rather than reviewing test volume indiscriminately.

Trace the independent oracle, production decision, substitutions, fixture realism and consequential assertions. Assess supplied execution identity/results; do not run tests or create fault experiments.

Return each unsupported guarantee, the test design that fails to establish it, a precise improvement and missing QA proof. A green result cannot defend a path or state the test never exercises.
