---
name: system-design-review
description: Review the model, authority, identity, lifecycle and consistency contracts of a change before implementation review.
---

# System Design Review

Read the [shared review contract](../../references/review-contract.md) once. Inherit the parent’s frozen target, assigned gate and evidence scope.

Use at the design gate to inspect the model after recovering the intended rule. The [problem framing role](../problem-framing-review/SKILL.md) owns challenges to that framing; this role owns structural consequences.

Apply [System design](../../references/system-design.md) to relevant authority, identity, cardinality, history, consistency, failure and growth contracts. Use [Inspection](../../references/investigation.md) when building or extending the source-to-sink map.

For relevant contract contrasts, use [units erased](../../references/worked-examples.md#units-erased) or [check then act](../../references/worked-examples.md#check-then-act).

Return the invariant/owner map, causal defects, defended boundaries, unresolved product choices and correction scope. Read downstream implementation as evidence when necessary; do not claim implementation or UX coverage.
