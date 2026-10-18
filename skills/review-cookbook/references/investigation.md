# Inspect code and establish coverage

Use the complete candidate diff and raw context. Keep one evolving source-backed map using [Review records](review-records.md). The map is an index to inspected evidence, not evidence by itself. Do not start with a list of imagined bugs and declare coverage when that list is exhausted.

## Establish the affected behavior

1. Classify changed behavior, removed behavior, shared contracts, schema/configuration changes and mechanical moves. Inspect both sides of the diff. For fixes, distinguish the reported symptom from the rule that would prevent that class of failure.
2. Locate entry points and authoritative owners through symbol/reference searches, route registrations, model relationships, event handlers and callers. Use language-server or AST tools where available and text searches otherwise; inspect dynamic registration and reflection where static tools cannot resolve them. Record search boundaries and unresolved edges.
3. Follow the shared symbols to distinct callers and consumers. Group callers only when inspected evidence establishes equivalent policy and execution. A grep hit is a lead; absence from a text search is not proof of absence.
4. Record each relevant path's expected outcome and the independent basis for it. Identify retained behavior and legitimate contrasting cases. Do not assume the issue's proposed mechanism or the new test's expected value defines the business rule.

## Trace forward from inputs

For each meaningful path, inspect the actual control and data flow:

`producer → transport/parsing → validation/authorization → rule selection → transformation → mutation/effect → consumer-visible outcome`

Record decisive source locations and the values crossing boundaries, including identity, units, time basis, version, scope and null/default semantics when relevant. Expand interfaces to the actual implementation used in this configuration. Inspect conditions that skip effects as well as executed effects.

Establish who assigns a decision input, who can change it, what fact it represents, and why the decision may rely on it. A consumer can implement its selected policy perfectly while the producer selects the wrong policy. Inspect copied or derived facts for their update and historical contracts.

Trace errors, cancellation and deferred work where they affect the outcome. Inspect handoff payloads and execution context rather than assuming request state survives a queue, task or later session. Define success at the final relevant sink, not merely at an accepted HTTP response.

## Trace backward from consequential sinks

Start with persisted records, exports, generated artifacts, messages, payments, authorization decisions or rendered state affected by the change. Find all applicable producers and the guards required before the effect. Compare paths that bypass the modified entry point or recreate its state later.

Inspect repeated, competing and reversed operations where the operation's lifecycle supports them. Draw the read/decision/write and external-effect ordering; locate the mechanism that preserves identity and invariants across that ordering. A disabled button, transaction keyword or comment describing best effort is not proof of the desired contract. Conversely, do not invent exactly-once requirements: establish the obligation and supported trigger.

Follow retained records through later edits, deletion, regeneration and consumption when those transitions are relevant. Distinguish immutable historical meaning, live references, projections and caches. A query returning the correct shape does not establish that its facts belong to the correct time or owner.

## Inspect the code within the current gate

Read changed logic with its surrounding branches, callees, schema and relevant assertions. Reconstruct the design that actually executes. Use the gate's specialist guide to assess its responsibilities, including shared seams. Do not relegate concurrency, downstream interpretation or historical meaning to a later gate when they determine whether the current model is valid.

When a concern remains uncertain, state the supported condition, expected outcome and competing explanation. Search for the guard or contract that would disprove it. Straightforward inspected defects and sound paths need no formal hypothesis ceremony.

Trace a proposed correction across affected callers and consumers before recommending it. Identify the smallest complete boundary and preservation constraints. Do not implement, insist on a framework for imagined uses, or narrow the correction to the first symptom when the same faulty rule remains active elsewhere.

## Account for scope and proof

For every affected path record inspected evidence, a relevant blocker, or the precise unresolved/unreviewed portion. A single successful route does not close a family of distinct routes. Mark demonstrated stable boundaries and explain excluded paths. Attribute source evidence to the candidate; record environment and revision for executed proof.

Hand the source-backed inventory to the omission audit. Keep the audit's new paths and the finding verifier's rejected candidates visible. If evidence changes an owner or contract, invalidate affected conclusions and inspect their dependencies again. Close work based on supported coverage, not file-read counts, agreement, time spent or a generated list's completion.
