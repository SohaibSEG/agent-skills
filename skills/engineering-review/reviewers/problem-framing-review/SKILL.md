---
name: problem-framing-review
description: Review whether a proposed change solves the underlying problem and uses the right rule, owner and mechanism. Use for root-cause and problem-framing challenges; recommend reframing only with causal source evidence. No implementation or QA execution.
---

# Problem Framing Review

Determine whether the proposed solution solves the right problem through a defensible contract. Test the strongest version of the design, including its specification; disagreement is not the objective. Code inspection and source-to-sink analysis are the evidence. A hypothesis, smell name or alternative design is not a finding.

Read the [shared review contract](../../references/review-contract.md) once. Inherit the parent’s frozen target and assigned scope.

## 1. Recover the problem before accepting its mechanism

Read the raw context and diff, then inspect the affected entry points, decision owners and visible effects. Record the actual failure or new capability, who needs it, the required outcome, behavior to preserve, and constraints with their sources. Distinguish observations from assertions not yet corroborated.

Express the required operation or invariant without depending on the proposed mechanism or the example's name. Preserve genuine domain distinctions and mandated constraints. This is a test of the problem framing, not permission to expand the product or build a general framework. A category of examples is not automatically the rule that separates valid from invalid behavior.

Separate the **domain purpose**, the **operational rule**, and the **enforcement mechanism**. Describe the rule as an allowed value, relationship, state transition or effect condition; repeating the motivating category’s name is not yet an explanation of that rule. Identify which domain facts the operation really needs and which are merely how the example was recognized. Preserve specialization that the rule genuinely requires.

For each consequential design decision, locate **what selects the behavior**, **who owns the rule**, and **where it takes effect**. Trace the selection input back to its creators and editors, then forward to enforcement, persistence and consumers. Reading the function that implements a decision is insufficient if its inputs have the wrong meaning or authority.

## 2. Establish why the design should work

State the implemented implication: “this observable value/state means this rule applies.” Inspect what makes that implication valid. Is it an explicit contract, a stable identity, a contextual decision, an incidental correlation, or merely today's fixture? Check who can change the input, how it travels, and whether distinct concepts have been collapsed into one representation.

When a consequential assumption needs a distinguishing case, consult the relevant row in [Challenge operations](references/challenge-operations.md). Select from actual source; do not fill the table mechanically.

Assess a weakness by its causal relevance to the promised outcome, not whether its line was added in this diff. An inherited assumption can invalidate a new feature. Conversely, unrelated debt is outside scope. If excluding a weakness, identify the stable boundary or explicit limitation that makes the required outcome independent of it. “Unchanged,” “best effort” and “the tests pass” alone do not establish that boundary.

## 3. Try to distinguish the rule from the shortcut

Derive a reachable scenario that would separate the intended rule from the implemented decision. Explain why the outcome should stay the same or change, citing a requirement, supported editing/creation path, caller contract or actual consumer. Do not invent hypothetical product capabilities to make the design fail.

Trace the scenario from input to its last consequential effect. Check alternate writers and read projections, not just the row or return value named in the PR. For temporal claims, enumerate the legal sequence or competing operations and identify the enforcement boundary. Separate source-established consequences, executed reproductions and still-unverified assumptions.

Actively seek the strongest defense: a relevant constraint, identity guarantee, lock, validator, immutable snapshot, caller restriction, or intentionally different business rule. Follow it to the code that enforces it. Withdraw or narrow the challenge if the defense holds. A raw string may be a valid protocol identity; a specialized component may be the right boundary. Neither is defective by appearance.

## 4. Reframe only where it changes the correction

Classify the cause rather than treating every defect as architecture:

- **Problem/specification:** the requested mechanism conflicts with the required outcome, or a material business rule is unresolved.
- **Design/contract:** the outcome is sound, but authority, identity, representation or responsibility makes the required behavior unreliable.
- **Implementation:** the contract is sound, but a path violates it.
- **No supported defect:** the suspected weakness is defended by source and applicable constraints.

When a reframe is justified, state the original framing, the underlying operation/invariant, and the counterexample that requires the change. Compare the submitted approach with the smallest materially different correction under the **same** requirements. Explain what stays specialized, what becomes explicit or shared, and the affected writers, consumers and history. Reuse existing capabilities when they fit. Do not recommend a framework merely because more cases can be imagined.

Recommend the smallest complete correction boundary. If it is broad, explain why a narrower correction cannot satisfy the evidenced contract, describe trade-offs and separate any unresolved product choice. A recommendation does not authorize implementation or a broad refactor. A sound design may require only a local fix or no change.

## 5. Return the framing decision

Return the required operational rule, the mechanism that currently selects it, the supported distinguishing case and strongest defense. Classify the cause as above and state any justified reframe and correction boundary. “No supported reframe” is valid when the design holds.

Send candidates to the parent's [finding verifier](../review-finding-verification/SKILL.md). This role does not certify structural completeness, code quality, test quality or UX; those have separate owners.

## Maintainer references

[Research and evaluation](references/research-and-evaluation.md) explains the primary-source influences, limits of the method and how to measure finding quality. It is not required reading for every review. This reviewer is bundled beneath the parent `engineering-review` skill. The parent loads these instructions directly; no separate installation, vendor API or particular model is required.
