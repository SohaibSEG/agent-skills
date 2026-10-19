# Coordinate independent reviewers

The coordinator owns the integrated result. Use independent contexts for substantial or cross-boundary work when available and authorized; roles are responsibilities, not a fixed agent count. The [shared contract](review-contract.md) supplies authority and evidence policy.

## Delegate different questions

Use delegation when independent reasoning or distinct source paths can close a real coverage gap. Do not ask several agents to “review everything” and treat agreement as confidence. Choose responsibilities from the change, not a fixed swarm size:

| Responsibility | Concrete assignment | Evidence to return |
|---|---|---|
| Problem framing | Establish the required outcome independently of the proposed mechanism; inspect who should own the rule and whether the representation expresses it. | Source-backed contract, competing interpretation, causal design candidates and unresolved product decisions. |
| Focused inspection | Own a consequential flow or boundary. Follow its inputs through decisions, persistence and effects, including callers outside the diff. | Actual trace, preserved invariants, failure candidates, defenses and uninspected seams. |
| Independent coverage | Start from consequential consumers/effects and trace backward to their producers. Choose paths from source without the discovery map or conclusions. | Independent inventory, alternative writers/lifetimes and omitted paths; then compare coverage. |
| Finding verification | Challenge the union of candidates, including unresolved or discarded candidates and their dismissal reasons. | Accept/narrow/reject/unresolved decisions supported by the rule, trigger and source; not a vote. |

Give each assignment a question that can be answered from named source entry points and an explicit owner for shared seams. “Review the backend” is insufficient; “trace application submission through stored state and downstream effects, including competing callers” defines a responsibility without prescribing a defect. Load only the relevant role guides. Allow discovery beyond the initial entry points; report consequential paths outside the assignment for integration.

A small change can use one discovery reviewer plus an independent checker who saves a blind coverage inventory before seeing candidates. Separate framing or additional flow reviewers when their questions warrant it. Parallelize independent discovery within the current gate; do not pre-certify later gates. The coordinator owns integration and gate decisions, even when specialists agree. If capacity is limited, sequence independent contexts rather than duplicate work or abandon a boundary.

## Prepare and assign

Freeze the target and raw context once. Build a provisional source inventory, identify shared seams and give each an integration owner. Split by consequential flows or responsibility within the current gate, not arbitrary file chunks.

Pass each reviewer:

```text
Target/base/candidate and current gate: [...]
Read the shared review contract and assigned role at: [...]
Question, source entry points, responsibility and owned/shared seams: [...]
Raw requirements/discussion, source and existing evidence: [...]
Provisional inventory, if any (discovery only; omit for blind audit): [...]
External artifact destination: [...]
Return source-backed paths, candidates (including discarded/unresolved with reasons), counterevidence and gaps.
```

The [parent routing table](../SKILL.md) supplies role paths. Reviewers read the contract and their role, then only the guide sections needed for the assignment; they need not reload the full parent workflow or all references. Prior findings and expected answers are excluded from initial discovery. Share new source facts for integration afterward, retaining conflicting interpretations.

## Keep the inputs independent

| Responsibility | Initial inputs | Later inputs |
|---|---|---|
| Discovery, including problem framing | Frozen source, raw context, assigned scope | New source facts for integration; no expected answers |
| Finding verification | Source/context and union of candidates, including unresolved/discarded ones and reasons | Clarifications and new evidence |
| Coverage audit | Source/context and scope, without discovery conclusions | Discovery report only after saving the independent source inventory |

[Verification](verification.md) owns the verification and omission procedures. One agent may verify findings after recording a blind audit inventory; it must not seed that inventory with the candidate list. For large scopes partition by flows while retaining a seam owner. If independent contexts are unavailable, disclose the sequential check; a different role label or model does not establish independence.

## Reconcile

Resolve disagreements at their source. Record accepted, narrowed, rejected and unresolved decisions, and route newly found candidates through verification. Reopen affected traces when another writer, consumer or lifetime is found; do not repeat settled work merely to satisfy a pass count.

Combine specialist coverage with explicit gaps and supplied QA provenance. A coordinator cannot upgrade missing evidence to a cleared gate. Use the parent’s gate/report decisions; delegation never expands authority or starts QA.
