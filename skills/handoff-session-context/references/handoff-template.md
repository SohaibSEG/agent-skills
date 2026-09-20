# Handoff Template

Remove empty sections.

```markdown
# Session Handoff: <topic>

Generated: <ISO timestamp>
Repository: <absolute path or "none">

## Current Goal
<One observable outcome>

## Latest Request
<The newest user instruction this handoff must serve>

## Done When
- [ ] <Completion condition>

## Sources of Truth
1. <Newest user decision>
2. <Specification, issue, or plan>
3. <Existing architecture or tests>

## Binding Constraints
- <Tooling, scope, branch, merge, service, or validation rule>

## Current Decisions
- Decision: <rule>
  Reason: <why>
  Supersedes: <obsolete approach, if needed>

## Repository State
- Base: `<remote/base @ sha>`
- Branch: `<branch>`
- HEAD: `<sha>`
- Upstream: `<tracking branch>`
- Migration heads: `<heads or not applicable>`
- Required services: `<state>`

### Relevant Worktree Changes
- `<path>`: <ownership and purpose>

### Unrelated Worktree Changes
- `<path>`: leave untouched

## Delivery State
| Issue/PR | State | Branch/Base | Purpose | Merge order |
|---|---|---|---|---|
| ... | planned/in progress/PRed/merged/blocked | ... | ... | ... |

## Implemented
- <Behavior> Evidence: `<commit, path, test, or PR>`

## Active Work
- Status:
- Last completed action:
- Current failure or open question:

## Validation
- PASS: `<command>`: <result>
- FAIL: `<command>`: <cause>
- PENDING: <required gate>

## Findings That Matter
- <Finding and its effect on the goal>

## Deferred
- <Item>: <reason and owner or destination issue>

## External Work
- <Operator, deployment, permission, or third-party dependency>

## First Actions
1. `<exact command or file inspection>`
2. <next implementation or validation step>
3. <checkpoint update>

## Do Not Repeat
- <Completed investigation, rejected design, or redundant validation>

## Restart Protocol
Read this handoff and any linked checkpoint. Verify live Git, PR, CI, service,
and migration state before editing. Apply newer user instructions first.
Resume from "First Actions" and update the existing checkpoint.
```

## Quality Test

A recipient with no conversation history must be able to answer:

1. What outcome is required?
2. What is already done, with evidence?
3. What is currently incomplete?
4. Which constraints must not be violated?
5. What exact action should happen first?
6. Which facts require revalidation?

If any answer is missing, revise the handoff before transfer.
