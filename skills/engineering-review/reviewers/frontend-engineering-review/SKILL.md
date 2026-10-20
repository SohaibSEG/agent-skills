---
name: frontend-engineering-review
description: Review frontend state, API contracts, async behavior, component responsibilities and browser trust boundaries through source inspection.
---

# Frontend Engineering Review

Read the [shared review contract](../../references/review-contract.md). Inherit the
parent's frozen target, assigned gate and evidence scope. Record loaded guides,
inspected paths and open proof requirements in the shared coverage record.

Use the procedure below for implementation review. Trace producers, state transitions, transport and consumers; consult
[Code design](../code-design-review/SKILL.md) for unresolved ownership questions.
Return source-backed behavior, correction boundaries and required interaction proof.
Coordinate task outcomes with User Journey Review and rendered states with UI/UX
Review. Do not certify their coverage from implementation inspection.

Use at the implementation gate. Trace source contracts and supplied evidence;
[UI/UX](../ui-ux-review/SKILL.md) owns rendered conformance/accessibility and [User journeys](../user-journey-review/SKILL.md)
owns task completion. Request execution through [QA evidence](../../references/qa-evidence.md).

## State and transport

Map page composition, components, state/query hooks, typed transport and schemas.
Identify the source of truth and all state writers. Trace view/edit/dirty/submitting/
saved/loading/empty/error/denied states as applicable. Inspect cancellation, retries,
repeated submissions, stale async completion, record/tenant changes, unmounting and
cache invalidation. A response for a previous scope must not overwrite the current
one. Server refresh must respect the intended dirty-form contract.

Distinguish request failure from an empty result, acceptance from completed work,
and optimistic display from durable success. Trace decoding, validation, error
mapping, authentication expiry and API contract changes into callers. Preserve
valid input and expose actionable recovery; coordinate ambiguous retry outcomes
with backend review. Do not treat client checks as server authorization.

## Boundaries, rendering and data volume

Inspect shared-control contracts and feature-specific policy leaks; use
[Code design](../code-design-review/SKILL.md) for a responsibility question. Follow effects,
subscriptions and resource cleanup through lifecycle changes. Inspect keys and
identity across reordered, filtered or paginated collections.

Check bounded fetching, N+1 requests, search/pagination and large in-memory lists
against real usage. Trace state and CSS ownership into the rendered states; send
layout, cascade, focus and accessibility evidence to UI/UX review. Avoid declaring
a visual defect from a component name alone. Use [stale async completion](../../references/worked-examples.md#stale-async-completion)
and [failure disguised as empty](../../references/worked-examples.md#failure-disguised-as-empty)
when their causal questions apply.

## Browser trust boundaries

- Trace URL parameters, stored values, server responses and message payloads into HTML/DOM rendering, script execution and navigation. Inspect the actual sink and context-specific escaping or sanitization; framework defaults do not protect escape hatches. Show a supported untrusted producer and affected sink before alleging an exploit. [OWASP: DOM-based XSS prevention](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
- Inspect cross-window messages for origin, sender and payload validation, and changed browser persistence for sensitive data exposure and stale authority. Client-side state is not authorization. Follow protected operations through the server boundary using the applicable [backend authorization checks](../backend-data-security-review/SKILL.md#2-follow-authorization-through-reads-and-writes). [OWASP: HTML5 security](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html)
- Inspect destinations derived from untrusted input, including redirect targets and link protocols. Establish the permitted destination contract and reachable consequence. Separate an unsafe navigation or data exposure path from an ordinary external link; do not demand blanket restrictions unsupported by the product.
