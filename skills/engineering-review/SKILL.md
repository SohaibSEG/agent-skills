---
name: engineering-review
description: Review a pull request, branch, commit or PR stack for root design flaws, code quality, data/security defects, UX issues and weak tests. Coordinate source-to-sink inspection and independent finding verification. Produce actionable findings without implementing changes or running QA.
---

# Engineering Review

Review whether a change expresses the right rule, implements it correctly and supports the user's intended outcome. Read the [shared contract](references/review-contract.md) first. This is the single entry point for all bundled reviewers; QA remains separate.

## Establish the target

Freeze destination/base, candidate revision and complete stack scope, regardless of author. Use tip versus stack base when tractable, otherwise dependency order followed by the integrated result. Detect target changes before closing the review.

Read repository instructions, the complete diff, issues, PR body and public discussion. Distinguish required outcomes, observations, proposed mechanisms and correctness claims. State the outcome to achieve and behavior to preserve; mark missing context. Do not let the proposed implementation define the rule.

Use [Inspection](references/investigation.md) to map real producers, decision owners, transformations and consumers. Follow inputs forward and consequential sinks backward. For shared contracts or unclear relationships, use [Code discovery](references/code-discovery.md) to select symbol navigation, structural search and boundary tracing rather than relying on repeated keyword searches. Keep one evolving external record using [Review records](references/review-records.md); the map indexes inspected evidence rather than certifying coverage.

## Route the review

Load the roles relevant to the change and current gate. Roles are responsibilities, not a required number of agents. Each specialist SKILL.md contains its authoritative review procedure and references; read its applicable sections. Do not load all references or rediscover settled evidence at each gate. Use the relevant [worked example](references/worked-examples.md) to calibrate a review move; transfer its causal question and legitimate contrast, not its domain or presumed verdict.

| Gate / task | Reviewer | Distinct question |
|---|---|---|
| Design | [Problem framing](reviewers/problem-framing-review/SKILL.md) | Are we solving the underlying problem with the right rule and mechanism? |
| Design | [System design](reviewers/system-design-review/SKILL.md) | Do model, identity, lifecycle and consistency contracts support that rule? |
| Implementation | [Code design](reviewers/code-design-review/SKILL.md) | Are responsibilities, interfaces, reuse and control flow sound? |
| Implementation | [Backend/data/security](reviewers/backend-data-security-review/SKILL.md) | Do use-case authorization, orchestration, transactions, audit and external effects preserve the contract? |
| Design → implementation | [Database](reviewers/database-review/SKILL.md) | Do schema dependencies, constraints, access paths, growth and migration history preserve the data contract? |
| Implementation | [Frontend engineering](reviewers/frontend-engineering-review/SKILL.md) | Are state, transport, async behavior, components and browser trust boundaries correct? |
| Experience | [User journey](reviewers/user-journey-review/SKILL.md) | Can the intended person discover, complete and recover the task with a verifiable outcome? |
| Experience | [UI/UX and accessibility](reviewers/ui-ux-review/SKILL.md) | Do rendered states follow applicable patterns and support visual, responsive and accessible interaction? |
| Every gate | [Test quality](reviewers/test-quality-review/SKILL.md) | Can the tests and supplied evidence detect violations of the claimed rule? |
| Gate closure | [Finding verification](reviewers/review-finding-verification/SKILL.md) | Does each candidate survive source checking and its strongest defense? |
| Gate closure | [Review coverage](reviewers/review-coverage-audit/SKILL.md) | Which consequential paths or seams did discovery overlook? |

For substantial or cross-boundary work, use independent discovery and verification when delegation is available and authorized; this skill requests it under those conditions. Read [Coordination](references/coordination.md) before dispatch. Delegate distinct questions: problem framing, focused source inspection, consumer-first omission checks and candidate verification as warranted. Avoid duplicate whole-change reviews; a small change may need only discovery and an independent checker. Give fresh reviewers the contract, relevant role, frozen source/raw context, concrete question/source entry points and external output location. If independent contexts are unavailable, disclose sequential review.

Apply gate decisions from the shared contract. Read downstream code/screens where needed to establish an upstream consequence; that does not clear the later gate. Retain incidental later-layer findings without claiming that layer is reviewed.

## Make specialist coverage explicit

At each reached gate, route from the changed behavior and its affected consumers,
not only file extensions. Schema, query/access-pattern, retention or transaction
changes require Database Review; frontend behavior requires Frontend Engineering;
changed task paths require User Journey; changed rendered controls/states require
UI/UX. Problem framing and system design resolve material rule/model decisions;
test quality follows the claims in every reached gate. Mark other roles not
applicable with a scope reason. Roles are responsibilities, not an agent quota.

For each applicable role, the assigned reviewer must read its SKILL.md procedure
and any linked methods needed before claiming coverage. Record the loaded paths,
source/claim inspected, evidence and unresolved obligations using
[Review records](references/review-records.md). Loading only this parent or a role
label is insufficient; reading files alone also does not establish coverage.
An applicable role with unread skill procedures or uninspected paths stays pending.
A blocked prerequisite defers dependent work without marking it inapplicable.

For missing rendered, interaction, database or performance proof, use the structured
[QA evidence handoff](references/qa-evidence.md). Separate authorized validation
collects it; the specialist then assesses it before closing the affected obligation.

## Verify and close

Use finding verification to accept, narrow, reject or retain each candidate as unresolved. Independently audit omissions before closing the gate; the auditor records its source inventory before receiving discovery conclusions. Newly found candidates receive the same verification. Reconcile by evidence, retain rejection reasons and inspect uncovered paths rather than appending an unchecked checklist.

Repeat only for new evidence or unfinished obligations. Advance when the current gate's applicable paths and contracts are resolved. An empty finding list, agreement or passing supplied test run does not establish completeness.

## Report and hand off

Lead with distinct findings ordered by impact. Include the violated rule, supported trigger, verified location, consequence, counterevidence disposition and smallest complete correction. Separate technical/visual defects, essential proof gaps and advisory improvements.

State target, reached gates, material omissions and supplied validation provenance once. Report **Blocked** while relevant defects, essential unresolved contracts or required proof gaps remain; otherwise **Ready within reviewed scope** only after all applicable gates and essential supplied proof are complete. Neither status authorizes approval or delivery.

For separate QA, list unverified scenarios, required real boundaries, expected outcomes and acceptance evidence. Stop after the report. Keep detailed working records linked rather than repeating them in the user response.

## Maintainer material

[Review-system research](references/review-system-research.md) records provenance; [Evaluation](references/evaluation.md) explains how to test the skill. These are not routine review inputs. Specialist skills retain their primary-source references and this package's own adaptations.
