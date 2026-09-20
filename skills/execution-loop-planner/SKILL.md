---
name: execution-loop-planner
description: Run implementation work that spans multiple slices or context windows while preserving the original goal. Use when the user explicitly asks for an execution loop, phased delivery, durable recovery state, or bounded multi-PR execution. Do not use for ordinary single-slice tasks.
---

# Execution Loop Planner

Optimize for delivery of the user's goal, not maintenance of the plan. The loop state is a recovery aid, never a deliverable.

## Operating modes

- **Plan:** inspect and propose slices without changing code or external state.
- **Run:** implement the next slice and validate it. Local edits are allowed only when the user's request authorizes implementation.
- **Resume:** recover the original goal and exact next action from the compact state packet, then return to implementation.
- **Close:** verify the original completion criteria and report remaining work.

Committing, pushing, updating issues or PRs, merging, deploying, and tracker writes require authorization from the user or the active task. They are not automatic parts of the loop.

## Goal lock

Before implementation, establish:

- one observable goal;
- a short list of completion criteria;
- explicit non-goals and constraints;
- a few vertical slices, each producing reviewable behavior;
- the source-of-truth order when instructions conflict.

The newest user direction wins. Do not reinterpret the goal merely to match completed work. If the requested outcome changes materially, close or abandon the old loop and initialize a new goal; use replan only to change the route to the same goal.

## Use the state tool

For work likely to cross a context window, use `scripts/loop_state.py`. Read [references/tooling.md](references/tooling.md) only when initializing, recovering, or changing loop state.

The tool stores compact state outside the repository and emits a small recovery packet. Do not create or maintain `GOAL.md`, `CHECKPOINT.md`, progress diaries, or parallel plan files unless the user explicitly asks for them.

State-write budget:

1. Initialize once.
2. Finish once per completed slice.
3. Write an exceptional transition only for a real blocker, resume, or approach-changing replan.
4. Close once.

Do not update state after every edit, command, test, finding, or message. If two consecutive actions only reorganize the loop instead of inspecting, implementing, or validating the product, stop administrating the loop and execute the recorded next action.

## Execute the active slice

For each slice:

1. Read the compact packet only when orientation is needed.
2. Inspect the smallest relevant source and tests.
3. Implement the smallest coherent behavior that advances the active slice.
4. Run focused validation, including a failure or boundary case when relevant.
5. Compare the result with the original goal and current acceptance criteria.
6. Mark the slice finished with concise behavior and validation evidence; the tool activates the next slice.

Use the repository diff, tests, commits, and service state as evidence. Do not duplicate their contents into checkpoint prose. Run the full relevant suite only at an integration boundary or when shared behavior changes.

## Stay bounded

- Keep one code-writing agent at a time unless the user asks for parallel implementation.
- Use subagents only for clearly independent review or testing when authorized.
- Timebox investigations. If the answer will not change correctness, design, or validation of the active slice, defer it and continue.
- Do not widen a slice because adjacent code is imperfect.
- Stop and ask when required local services are unavailable and repository instructions prohibit fallbacks.
- After two failed implementation attempts with the same symptom, diagnose before editing again.
- After three unsuccessful iterations, replan or ask for user input; do not keep cycling.

Specialist skills are optional routes, not mandatory ceremony. Use `$diagnosing-bugs` for a stubborn failure, `$pr-review-qa` for an explicitly requested final review, `$github-pr-template` when publishing an authorized PR, and `$handoff-session-context` only when the user wants a session handoff.

## Completion

Close only when every original completion criterion has current evidence, required validation has run, and blockers are absent. Report implemented behavior, validation, remaining work, and deferred items. Activity counts and polished checkpoint files do not establish completion.
