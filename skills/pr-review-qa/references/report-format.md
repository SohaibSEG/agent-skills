# Review Report Format

Lead with findings. Do not begin with a process recap. Omit empty subsections except the explicit no-findings statement.

## Findings

Order findings by severity, then by confidence and blast radius:

- **P0 — Critical:** Immediate severe loss, security compromise, unrecoverable corruption, or broad production outage.
- **P1 — High:** Likely correctness, security, migration, availability, or major user-flow failure that should block merge.
- **P2 — Medium:** Material defect, maintainability risk, degraded UX, or performance regression with bounded impact.
- **P3 — Low:** Real but limited issue worth correcting; never use P3 for subjective preference.

For each finding include:

1. A concise imperative title with severity.
2. Exact evidence: file and line, command result, screenshot, request/response, query plan, or reproducible behavior.
3. The consequence and affected scenario.
4. Why existing tests or safeguards do not catch it.
5. The smallest useful remediation direction without implementing it.

If no actionable findings survive verification, say: **No actionable findings found.** Then still report test coverage and limitations.

## PR Claim Verification

Use one row per material claim:

| PR claim | Code evidence | Runtime/test evidence | Verdict |
|---|---|---|---|
| Claim text | Location or absence | Command/artifact or unavailable | Verified / Partial / Contradicted / Unverified |

## QA Evidence

Group commands and scenarios by status:

- **Passed:** command/scenario and the behavior it proves.
- **Failed:** command/scenario, observed failure, and related finding.
- **Blocked:** missing service, credential, data, or access required.
- **Skipped:** applicable work not run, with the concrete reason.
- **Not applicable:** potentially expected track excluded by the actual diff.

For UI work, link retained screenshots and note viewport, route, state, console errors, and failed network requests.

## Review Coverage

Give each applicable axis one verdict: **Verified**, **Concern**, **Blocked**, or **Not applicable**. Cover specification, PR claims, system design, domain model, code hygiene, infrastructure/security, performance, backend/data, and UI/UX as applicable.

## Environment and Cleanup

Report:

- Base and head SHAs.
- Worktree location while active and confirmation that it was removed.
- Disposable services/data created and their cleanup result.
- Retained redacted artifact paths outside the repository.
- Any exact resource left behind and its safe recovery command.

End with the most important unresolved blocker or merge-blocking finding. Do not approve, merge, comment on, or modify the PR.

