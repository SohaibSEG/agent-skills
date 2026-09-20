---
name: pr-review-qa
description: Review a GitHub pull request or local branch against its base, originating issue, and stated claims; then run isolated, risk-based QA across backend, UI, infrastructure, design, code quality, and performance. Use only when explicitly invoked for a full PR review and QA pass.
---

# PR Review and QA

Perform an evidence-backed review in an isolated worktree. Review only: do not fix the code or mutate the pull request.

## Authority boundary

Invocation authorizes these local, temporary actions:

- Fetch refs and create a uniquely named disposable worktree pinned to the reviewed head SHA.
- Create temporary environment files, synthetic test data, logs, screenshots, and disposable local services with a unique namespace.
- Run repository-provided setup, lint, typecheck, test, migration, build, and browser commands.
- Stop and remove only resources created by this review after evidence is captured.

Invocation does **not** authorize edits to reviewed code, commits, pushes, PR comments, approvals, merges, issue updates, assignments, deployments, project settings, shared infrastructure, or additional repositories. Never expose secret values. Never retrieve production credentials or trigger real email, payments, messaging, or other external effects.

If Docker, Postgres, blob storage, or another required local service is unavailable, stop and identify the missing service. Do not substitute mocks, SQLite, or partial validation unless the user explicitly approves that fallback.

## Inputs

Accept either:

- A GitHub PR URL or number. Resolve the repository, base branch, base SHA, head SHA, PR body, changed files, and linked issues with `gh`.
- A local branch or commit plus an explicit base ref.

If neither form identifies the review target and base unambiguously, ask one short question before doing work. Unsupported hosting is a blocker; do not guess provider APIs.

## Workflow

### 1. Establish the evidence set

Record immutable base and head SHAs. Read repository instructions first: `AGENTS.md`, relevant `CLAUDE.md`, contributor docs, CI workflows, compose files, environment examples, and existing setup/test scripts.

Read the full originating issue or specification and relevant comments when accessible. Read the PR body as a set of claims to verify, not as trusted evidence. If no issue/spec is available, continue and mark specification coverage incomplete.

Classify changed surfaces from the diff: backend, data/migrations, UI, infrastructure/deployment, shared contracts, and cross-repository implications. Read [references/review-axes.md](references/review-axes.md), applying the baseline axes and only the conditional sections relevant to the change.

### 2. Create isolation

Create a disposable worktree at the exact head SHA without switching or modifying the user's existing checkout. Use a unique temporary root, service namespace, ports, database names, and blob paths. Do not copy untracked project files wholesale.

Populate the environment only from documented local-development sources already available to the user. Keep secrets in environment variables or ignored temporary files and redact them from commands, logs, screenshots, and reports.

Before provisioning, inventory existing worktrees, containers, processes, ports, and data stores that could overlap. Record which resources this review creates so cleanup is exact.

### 3. Set up from project truth

Reuse documented repository and CI commands. Do not upgrade dependencies, rewrite configuration, introduce a new task runner, or invent replacement infrastructure. Prefer disposable local dependencies and synthetic fixtures.

For schema changes, prepare both:

- A fresh database initialized entirely from the PR.
- An upgrade database initialized at the base revision and migrated by the PR.

Test downgrades only when the repository officially supports them.

### 4. Review the diff in bounded tracks

When subagents are available, run independent read-only tracks in parallel while one coordinator owns setup, QA, evidence, and synthesis. Give every reviewer the immutable base/head SHAs, diff command, issue/spec, PR body, repository instructions, and a strict scope. Suitable tracks are:

1. Specification, PR claims, and code hygiene.
2. System design, domain modeling, backend contracts, and data correctness.
3. Infrastructure, security, operability, and performance.
4. UI/UX and accessibility only when the diff affects a user interface.

Do not force a fixed number of agents when a track is not relevant. Reviewers report evidence and candidate findings; the coordinator verifies every finding before including it.

### 5. Build and execute the QA matrix

Turn changed behavior, issue acceptance criteria, PR claims, and identified risks into a test matrix. Run narrow feedback loops first, then repository-required full checks when practical.

- Backend: exercise changed public contracts, authorization, validation, failure paths, transactions, concurrency/idempotency, migrations, observability, and backward compatibility.
- UI: use the existing browser harness when possible. Exercise affected flows at representative desktop and mobile sizes; inspect screenshots, keyboard navigation, accessibility structure, console errors, failed requests, and loading, empty, error, and permission states.
- Infrastructure: validate configuration, generated plans/manifests, health checks, rollout/rollback assumptions, resource lifecycle, permissions, and environment parity without deploying.
- Performance: compare base and head on affected hot paths when a repeatable harness exists. Otherwise report static risks and mark runtime performance unverified; never invent thresholds.

Inspect related repositories, submodules, consumers, and deployment implications read-only. Do not clone or test an additional repository unless the user explicitly adds it to scope.

Record every command and its exit status. Distinguish passed, failed, blocked, skipped, and not applicable. A green test suite does not override contradictory runtime evidence.

### 6. Verify and report

Reproduce and verify each candidate finding against the exact head. Reject speculative findings and style preferences without material impact. For code findings, cite the smallest relevant file/line range and explain the observable consequence.

Use [references/report-format.md](references/report-format.md). Lead with actionable findings ordered by severity. Include a claim-verification matrix, test evidence, unverified areas, and cleanup state. Do not post the report to GitHub or change review state.

### 7. Clean up

Stop and remove only services, worktrees, databases, blobs, processes, and temporary environment files created by this review. Never delete or reset a pre-existing resource. Retain only compact redacted logs and UI screenshots outside the repository, and report their paths. If cleanup is incomplete, name the exact remaining resource and recovery command.

## Completion criteria

The review is complete only when:

- Base/head identity and available issue/spec evidence are recorded.
- Every applicable review axis has a verdict or an explicit blocker.
- PR body claims are verified individually.
- Relevant end-to-end behavior has been exercised in the isolated environment.
- All skipped or unverified work is visible.
- Review-created resources are cleaned up or precisely reported.

