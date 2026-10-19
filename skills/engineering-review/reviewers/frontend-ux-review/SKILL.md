---
name: frontend-ux-review
description: Review frontend state and user journeys, visual consistency, accessibility and reusable controls using code and available rendered evidence.
---

# Frontend and UX Review

Read the [shared review contract](../../references/review-contract.md) once. Inherit the parent’s frozen target, assigned gate and evidence scope.

Use the assigned gate, not the entire UI checklist at once:

- **Implementation:** frontend state, shared-control contracts, CSS ownership and browser trust boundaries in [Frontend](../../references/frontend.md). Use [Code design](../../references/code-design.md) only for an unresolved responsibility/reuse question.
- **Experience:** [User journeys](../../references/user-journey.md) owns task goals, decisions, disclosure, recovery and completion. [Frontend](../../references/frontend.md) owns component conformance, rendered states, CSS and accessibility evidence.

For source-supported UI-state contrasts, use [stale async completion](../../references/worked-examples.md#stale-async-completion) or [failure disguised as empty](../../references/worked-examples.md#failure-disguised-as-empty).

Return the user/state transition affected, source or rendered evidence, applicable established pattern and correction boundary. Distinguish observed visual defects from predicted friction. Request missing interaction evidence from separate QA; do not execute the flow.
