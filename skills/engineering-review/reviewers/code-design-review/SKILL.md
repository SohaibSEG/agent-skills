---
name: code-design-review
description: Review module boundaries, contracts, control flow and reusable abstractions; recommend evidence-backed refactoring without implementing it.
---

# Code Design Review

Read the [shared review contract](../../references/review-contract.md) once. Inherit the parent’s frozen target, assigned gate and evidence scope.

Use at the implementation gate for responsibility, interface, coupling, control-flow and resource-lifetime questions.

Apply [Code design](../../references/code-design.md). Consult the specific [Refactoring pattern](../../references/refactoring-patterns.md) only after identifying a supported correction; preserve its behavior constraints. Backend policy and frontend behavior remain with their specialist roles.

For concrete responsibility contrasts, use [wrong abstraction](../../references/worked-examples.md#wrong-abstraction) or [query with hidden effects](../../references/worked-examples.md#query-with-hidden-effects).

Return the failing caller/contract, causal code path and smallest responsibility change. Distinguish a behavior-preserving refactor from a bug fix. Reopen design when the problem is the model, not its implementation.
