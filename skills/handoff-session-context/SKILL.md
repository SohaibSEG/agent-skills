---
name: handoff-session-context
description: Prepare and transfer actionable context from a long Codex session into a fresh session or task. Use when the user asks for a handoff, context transfer, session restart, continuation in a new task, compact briefing, recovery package, or a durable summary that lets another agent resume without rereading the full conversation.
---

# Session Context Handoff

Produce a restart package, not a transcript summary. Preserve current truth, decisions, evidence, and the next executable step while removing stale discussion.

Read [references/handoff-template.md](references/handoff-template.md) before writing the artifact.

## Choose the Mode

Use **prepare-only** by default:

- Create a handoff file in `/tmp`.
- Return its absolute path and a short bootstrap prompt for the new session.
- Do not create or message another task.

Use **transfer** only when the user explicitly asks to create, fork, hand off to, or message a new Codex task:

- Use the available thread-management tool.
- Give the new task the handoff artifact or its complete actionable content.
- Do not assume that a new task inherits this conversation.

## Reconstruct Current Truth

Gather context in this order:

1. Newest user instructions and corrections.
2. Live repository state: branch, base, HEAD, worktree, migrations, services, and running processes.
3. Current issue, PR, CI, and review state when relevant.
4. Existing checkpoint, goal, plan, or ledger files.
5. Specifications and architecture documents that still govern the work.
6. Older conversation history only to recover decisions not represented elsewhere.

Prefer observed state over remembered state. Mark unresolved inferences as assumptions.

Do not make code changes while preparing a handoff unless the user asks to finish work first.

## Distill, Do Not Replay

Include:

- The current goal in one sentence.
- The latest user request.
- Completion criteria.
- Binding constraints and rejected approaches.
- Decisions that still affect implementation.
- Implemented behavior with file, commit, issue, or PR evidence.
- Active work and exact incomplete state.
- Relevant modified and untracked files.
- Validation already run, including failures that remain relevant.
- External dependencies and operator-owned work.
- Deferred items with reasons.
- The exact first actions for the recipient.

Exclude:

- Chronological conversation retelling.
- Superseded plans and corrected misunderstandings.
- Internal reasoning or chain of thought.
- Raw test logs when a result and command are enough.
- Unrelated repository findings.
- Repeated explanations.
- Secrets, tokens, credentials, cookies, private keys, and environment values.
- Personal or tenant data not required for the task.

State that a secret exists and where it must be configured without copying its value.

## Preserve Decision History Carefully

Record a decision only when it changes what the next session should do. Use:

```text
Decision: <current rule>
Reason: <short technical or product reason>
Supersedes: <old approach, only if it could otherwise return>
```

Keep user corrections that prevent known divergence. Examples include forbidden tooling, ownership boundaries, merge rules, validation limits, and explicitly deferred scope.

Do not preserve frustration, conversational tone, or obsolete intermediate designs.

## Capture Repository State

For code tasks, verify and record:

- Absolute repository path.
- Base and active branch.
- HEAD SHA and upstream tracking branch.
- `git status --short`, separated into relevant and unrelated changes.
- Commit or PR stack and merge order.
- Current migration heads when migrations are involved.
- Required local services and whether they are running.
- Active terminal sessions that must be completed or terminated.

Never tell the recipient to discard uncommitted files without identifying their ownership.

## Write a Durable Artifact

Create:

```text
/tmp/<repo>-handoff-<topic>.md
```

Use a stable topic name rather than a random identifier. If an execution-loop checkpoint exists, link it and update it before producing the handoff.

Keep the default artifact under 2,000 words. Use precise paths, commands, commits, and URLs instead of broad prose. For a large multi-PR program, add appendices only when the recipient needs them immediately.

## Validate the Handoff

Before returning it:

1. Recheck the newest user request.
2. Verify branch, HEAD, status, and PR or issue state.
3. Confirm referenced local files exist.
4. Confirm pending commands are not still running.
5. Remove all secret values.
6. Remove contradicted and duplicated instructions.
7. Check that the first next action is executable.
8. Ensure completed work has evidence and pending work is not presented as done.

## Bootstrap the Recipient

End the artifact with a restart protocol:

1. Read the handoff and any linked checkpoint.
2. Verify live Git and external state because it may have changed.
3. Reconcile any newer user instruction.
4. Resume from the listed first action.
5. Update the same checkpoint instead of creating a competing plan.

Provide this short prompt with the artifact:

```text
Read <absolute-handoff-path>, verify its Git and external state, then resume from "First actions." Treat newer user instructions as authoritative.
```

If transferring through a task tool, send the bootstrap prompt and the essential handoff content or file reference. Wait for the target to acknowledge that it can read the artifact before declaring the transfer complete.
