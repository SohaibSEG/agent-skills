# Loop Templates

Use only the sections needed for the task.

## Master Plan

```markdown
# Goal
<One observable outcome>

## Done When
- [ ] <Behavior or artifact>
- [ ] <Integration or migration condition>
- [ ] <Validation condition>

## Sources of Truth
1. <Newest user decision>
2. <Issue or specification>
3. <Existing architecture and tests>

## Constraints
- <Branch, merge, tooling, service, or design rule>

## Deferred
- <Decision>: <reason and owner>

## Slices
| Slice | Outcome | Dependencies | Acceptance | Validation | Delivery |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | commit/PR |

## Integration Gate
- <Cross-slice review>
- <Full relevant suite>
- <Deployment or migration check>
```

## Checkpoint

```markdown
# Recovery
Goal: <short goal>
Workspace: </tmp/path>
Updated: <ISO timestamp>

## Git
Base: <remote/base @ sha>
Branch: <branch>
HEAD: <sha>
PR stack: <issue/PR states, including PRed>
Worktree: <relevant modified and untracked files>

## Active Slice
Outcome: <one sentence>
Status: <not started | implementing | validating | reviewing | published>
Exact next action: <one command or edit>

## Completed
- <Behavior, commit, PR, test evidence>

## Decisions
- <Decision and reason>

## Findings
- <Only findings that affect the goal>

## Validation
- PASS: <command or behavior>
- FAIL: <command and current cause>
- PENDING: <integration gate>

## Deferred
- <Item, reason, destination issue or owner>

## Blockers
- <External dependency or "None">
```

## Slice Review

```markdown
## Slice <n>: <name>
- Planned outcome:
- Implemented behavior:
- Positive case:
- Negative or boundary case:
- Specification alignment:
- Architecture alignment:
- Upstream compatibility:
- Cleanup performed:
- Deferred findings:
- Tests:
- Commit or PR:
- Verdict: complete | incomplete
```

## Status Reply

```markdown
Implemented: <concrete behaviors>.
Active: <current slice and exact state>.
Remaining: <ordered deliverables>.
Deferred: <items with reasons>.
Blocked: <external dependency or none>.
```

## Rabbit-Hole Check

Before continuing an investigation, answer:

1. Does it block an acceptance criterion?
2. Does it expose a correctness, data-loss, security, or deployment risk?
3. Will the answer change the active slice?

If all answers are no, record it under `Deferred` and continue the planned slice.
