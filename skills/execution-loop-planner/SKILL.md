---
name: execution-loop-planner
description: Design and run recoverable implementation loops for multi-slice engineering goals. Use when work spans several commits, issues, pull requests, migrations, services, or context windows; when Codex must prevent scope drift and rabbit holes; or when the user asks for an execution loop, phased delivery, checkpoint management, stacked PR strategy, progress recovery, review delegation, or a plan that survives context compaction.
---

# Execution Loop Planner

Build a loop that can stop, compact, rebase, or fail without losing the goal. Keep the plan tied to observable deliverables rather than a list of intentions.

Read [references/templates.md](references/templates.md) when creating the master plan or checkpoint files.

## 1. Establish the Contract

Inspect the repository, active branch, specifications, issue or PR state, and relevant local instructions before planning.

Write down:

- One concrete goal.
- Observable completion criteria.
- Explicit non-goals and deferred decisions.
- User constraints, including branch, merge, test, tooling, and deployment rules.
- Source-of-truth artifacts in priority order.
- Assumptions that would change the design if false.

Resolve contradictions before implementation. Treat the newest user direction as authoritative, then update the checkpoint so stale instructions do not return after compaction.

## 2. Map the Current State

Record facts, not expectations:

- Current base, branch, commit, worktree state, and migration heads.
- Existing implementation and known gaps.
- Upstream changes that affect the goal.
- Available local services and required external dependencies.
- Existing issues and PRs, including merged, open, draft, blocked, and PRed states.
- Tests that exercise the touched behavior.

Do not encode coverage inventories, execution commands, issue state, or checkpoints in production code. Keep operational state outside the repository unless the user requests a tracked artifact.

## 3. Cut Vertical Slices

Each slice must produce a reviewable behavior or operational capability. Define:

1. Outcome.
2. Files or ownership boundaries likely to change.
3. Acceptance examples, including a negative case.
4. Dependencies and migration impact.
5. Targeted validation.
6. Review point against the master goal and source specifications.
7. Commit or PR boundary.

Prefer a small number of meaningful slices over many thin PRs. Stack only when dependency order makes independent review useful. Consolidate related stacked PRs before final integration.

Allow cleanup in touched paths when it removes duplication, clarifies ownership, or makes the requested behavior easier to verify. Timebox it and attach it to a slice outcome. Reject speculative frameworks, unrelated rewrites, and abstractions with no current caller.

## 4. Install Guardrails

Use these defaults unless the user overrides them:

- Keep one code-writing agent at a time. Use subagents for independent review or testing, not simultaneous edits.
- Do not auto-merge into the protected base.
- Do not rewrite merged history. Start a new branch from the current base.
- Keep internal progress out of code comments, documentation, and user-facing output.
- Test behavior and contracts, not a hardcoded coverage inventory.
- Prefer repository patterns and supported APIs. Record justified exceptions.
- Stop and ask when a required local service is unavailable if repository instructions prohibit fallbacks.
- Do not widen a slice merely because adjacent code is imperfect.
- When upstream changes land, rebase once, inventory the affected behavior, and add missing integration work to the active slice.

Set a rabbit-hole budget. If an investigation does not change the active slice's design, correctness, or verification, record it as deferred and return to the slice.

## 5. Persist Recovery State

For long loops, create a private workspace such as:

```text
/tmp/<repo>-<goal>/
  GOAL.md
  CHECKPOINT.md
  FINDINGS.md
  VALIDATION.md
```

Use a stable, easily rediscovered directory name. Tell the user the path once. Do not place these files in the repository or leak their contents into source comments.

Update the checkpoint:

- Before the first edit.
- After each slice, commit, PR, rebase, or merge.
- When a decision changes scope or architecture.
- After a failed validation that changes the next step.
- Immediately before expected context compaction.

Keep `CHECKPOINT.md` short enough to reread in one command. Put raw logs and detailed investigation notes in the other files.

## 6. Execute the Slice Loop

For every slice:

1. **Restore:** Read `GOAL.md` and `CHECKPOINT.md`. Verify branch, base, status, and newest user instruction.
2. **Orient:** Read only the source and tests needed for the slice. Confirm the failure or missing behavior when practical.
3. **Implement:** Make the smallest coherent change that owns the behavior. Decompose route or UI handlers when service ownership becomes clearer.
4. **Validate:** Run focused static checks and behavior tests. Include one success case and one failure or boundary case.
5. **Review:** Compare the result with the original goal, specifications, architecture constraints, and upstream behavior. Passing tests alone is insufficient.
6. **Record:** Update completed work, findings, validation, deferrals, and the exact next action.
7. **Publish:** Commit and push the coherent slice. Update its issue or PR with concrete behavior and honest test status.

Do not repeat full validation after every edit. Run targeted checks during development and the full relevant suite at integration boundaries, before consolidating a stack, or when shared behavior changes.

## 7. Use Review Agents Deliberately

Use independent reviewers only when allowed and useful.

- Give reviewers the specification, plan, and raw diff or branch.
- Ask for behavior gaps, regressions, architecture divergence, and missing tests.
- Do not give them the expected finding.
- Keep reviewers read-only unless the user explicitly authorizes parallel edits.
- After all slices, request one cross-slice review of the whole implementation rather than isolated migration-only reviews.

Reconcile findings by severity and goal relevance. Fix critical and high findings first. Defer lower-value work explicitly.

## 8. Manage Failures

When CI or a migration stalls:

1. Identify the exact step, revision, test, or request.
2. Separate infrastructure failure from code failure.
3. Explain the cause before editing when the user asks for diagnosis only.
4. Fix the root behavior and add a regression test.
5. Avoid fallback services or weaker validation without approval.
6. Update the checkpoint with the failure and the evidence that closes it.

Do not call a branch ready while required checks, migration compatibility, upstream feature coverage, or source-spec review remain open.

## 9. Close the Loop

Completion requires:

- All acceptance criteria mapped to implemented behavior.
- Deferred items listed with reasons and owners where known.
- Migrations and deployment requirements stated.
- Frontend and external call sites checked when contracts changed.
- Targeted tests green and the agreed integration suite run.
- PR stack consolidated into meaningful review units.
- PR bodies updated with architecture, workflows, rollout impact, and QA instructions where relevant.
- Checkpoint marked complete with final branch, commit, PR, and validation state.

Report what is implemented, what remains, what is deferred, and what is waiting on another operator. Never substitute activity count for goal completion.
