# Challenge the design using the source

Use these operations where the inspected code creates the question. The goal is a discriminating case with a causal trace, not a catalogue of imagined failures. Start with the ordinary successful path so the criticism targets what the system actually promises.

The role entry point defines the decision trace. Use [Inspection](../../../references/investigation.md) for forward/backward source traversal; select the following probes only where that trace leaves a material assumption to challenge.

## Choose a source-backed challenge

| Signal in the source | Review operation | Evidence that can defeat the challenge |
|---|---|---|
| One representation selects policy, capability or identity | Find who creates/edits it. Identify a supported change that preserves meaning but changes representation, or preserves representation but changes meaning. Trace whether behavior incorrectly follows it. | Representation is the documented canonical identity, changes intentionally change the rule, or an enforced mapping preserves the contract. |
| A named example drives logic in a shared component | Identify the underlying operation the caller needs. Compare actual consumers: which share that operation and which legitimately differ? Locate the owner that knows the distinction. | The component's explicit contract is genuinely domain-specific and every relevant caller meets it; no hidden inference is needed. |
| Repeated guards or slightly different copies enforce a rule | Trace writers and final effect. Determine whether copies can disagree or bypass enforcement. Consider one authoritative policy with explicit contextual inputs before inventing a framework. | Separate owners implement intentionally distinct rules, or copies cannot drift because the real invariant is enforced centrally. |
| A pre-check or remembered state is treated as a guarantee | Trace its validity interval through waits, retries, multiple actors and commits. Construct a legal interleaving and inspect the lock, constraint, claim or revalidation that should exclude it. | The invariant is enforced atomically, serialized by a demonstrated boundary, or the outcome explicitly tolerates the duplicate/stale state. |
| A result depends on mutable settings, child state or current definitions | Identify what is historical fact versus current policy. Read saved records through today's projections, exports and user decisions. Trace whether editing definitions changes the meaning of completed work. | Required history is captured immutably and consumers use it, or recalculation is an explicit product rule. |
| Different transports, actors or entry points perform the same operation | Trace policy and effects across each relevant entry point. Trace whether an implementation detail changes an invariant that should be transport-independent. | Authority/context intentionally differs and that distinction is explicit and enforced. |
| A visible error is suppressed, defaulted or repaired downstream | Follow the earliest producer and the first boundary where invalid state could be rejected or represented honestly. Check whether all writers share the cause. | The condition is valid uncertainty with an explicit lifecycle, and recovery preserves required information and outcomes. |
| A user-facing fix adds explanation or steps | Follow what the user knows, what action is available, what it changes and how completion is visible. Check whether the model requires users to resolve distinctions the system already knows. | The choice is genuinely theirs, necessary information is available, and the interaction makes its consequences clear. |
| Claimed scalability or extensibility depends on today's input shape | Trace cardinality, query count, storage growth and actual extension points. Use supported input limits or concrete callers; distinguish growth from arbitrary extrapolation. | Enforced bounds or existing contracts make the proposed load/change irrelevant; complexity buys an actual needed capability. |

These are operations, not mandatory findings or a comprehensive code-review checklist. Follow a consequential new lead even if it does not fit this table.

## Prove the counterexample and try to refute it

A useful challenge has an input or sequence the system permits, an independently justified expected outcome, the exact branch/decision reached, and a violated downstream effect. Mark each inferential step. Give the source trace and the separate QA proof still needed; claim reproduction only when supplied execution evidence establishes it.

For concurrency, distinguish mutual exclusion from revalidation: a wait may serialize writes without making an earlier observation true again. Read the actual database constraint and transaction boundary. For history, distinguish preserving a stored number from preserving how a user interprets it later. For interaction, distinguish saving successfully from reaching the promised outcome.

Ask what would make your accusation false, and inspect that mechanism. A comment about guarantees is a lead; its implementation is evidence. Check the base before saying the PR introduced a flaw. Explain why any inherited flaw still undermines the current changed or relied-on contract.

## Compare correction boundaries fairly

Compare behavior, ownership, compatibility, failure modes and maintenance burden under the same constraints. Consider an explicit existing parameter, type, state or authoritative operation before adding new layers. Do not substitute a different incidental discriminator for the old one. Equally, do not claim every condition needs a new type or every repeated operation needs a shared abstraction.

Trace the proposed boundary through its relevant writers, serialized contracts, saved data and consumers. A more elegant interface that drops a required behavior is not a complete correction. Distinguish a local contract repair from a system redesign, and retain product questions as questions.

Keep the distinguishing case and counterevidence in the parent’s [working record](../../../references/review-records.md); do not duplicate a second report template here.
