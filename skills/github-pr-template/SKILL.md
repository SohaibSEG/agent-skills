---
name: github-pr-template
description: Use when Codex creates, opens, updates, or drafts a GitHub pull request or PR description, especially for Siraj-Solutions/ecommerce-front or when the user says "pr", "pull request", "use the template", or asks for setup/change/test details in a PR body. This skill defines the preferred PR body format and should override generic PR body guidance from GitHub publishing skills; use other GitHub skills only for mechanics such as pushing branches and creating the PR.
---

# GitHub PR Template

## Purpose

Use this skill to write PR titles and bodies. If another GitHub skill is also active, use that skill for Git/GitHub operations and use this skill for the PR description.

The PR body must be concrete, scoped to the actual branch diff, and structured for reviewers who need to understand behavior, setup impact, and validation quickly.

## Workflow

1. Inspect the branch scope before writing:
   - `git status -sb`
   - `git diff --stat <base>..HEAD`
   - `git diff --name-only <base>..HEAD`
   - `git log --oneline <base>..HEAD`
2. Use the repository default branch as base unless the user specifies another base.
3. Summarize the full branch diff, not only the latest commit.
4. Keep the PR title short and action-oriented.
5. Use the template below with the same section order.
6. Mark checks as complete only when they were actually run in this session or already verified in the current conversation.

## Branch naming

- Never create or use branches prefixed with `codex/` or `prfix/`, and never use `prfix` as a branch-name segment.
- Use `<type>/<short-kebab-case>` with the established prefix that matches the dominant change: `fix/`, `feat/`, `refactor/`, `doc/`, `test/`, `ci/`, or `chore/`.
- Prefer an established repository-specific conventional prefix when the repository already uses one.
- Keep stacked branches on distinct names and set each PR base to the renamed branch immediately below it.
- Before creating or renaming a branch, verify that the target name does not already exist locally or remotely.

## Title

Use one conventional, reviewer-readable title:

```text
fix: scope promo pricing by customer role
feat: streamline tenant runtime deployment
refactor: move catalog pricing to price lists
```

For broad branches, name the dominant product outcome:

```text
fix: optimize tenant runtime and refactor pricing
```

## Body Template

```markdown
## Summary

One or two paragraphs explaining the product/backend outcome, the root cause when this is a fix, and the user/developer impact. Mention the major areas touched when the branch is broad.

---

## What changed

### Area 1
- Concrete change
- Concrete change

### Area 2
- Concrete change
- Concrete change

### Tests and validation
- Concrete test or validation change

---

## Technical notes

- Important implementation details reviewers need before reading the diff.
- Runtime/config/migration behavior.
- Compatibility or rollout notes.
- Known constraints or non-goals.

---

## Test plan

- [x] `command that was run`
- [x] Manual or automated verification that was completed
- [ ] Reviewer/operator step still required
- [ ] Follow-up environment validation still required

---

## Files overview

| Area | Key files |
|------|-----------|
| Area name | `path`, `path` |
```

## Writing Rules

- Use real details from the diff. Do not fill sections with generic claims.
- Group changes by reviewer concern, not by commit order.
- Prefer business and operational language over internal implementation narration.
- Include setup and env var changes when Docker, compose, runtime config, or deployment files changed.
- Include migrations by path when Prisma migrations changed.
- Include i18n/locales when message files changed.
- Include tests by command and by test file when relevant.
- Document only files, behavior, and configuration changes that are part of committed branch diff. Do not mention untracked files, local-only files, ignored files, secrets, credentials, local validation artifacts, or anything intentionally excluded from the PR.
- Include UI screenshots or design changes when relevant and possible.
- Keep checkboxes honest: use `[x]` only for completed checks and `[ ]` for required manual validation.
- Do not paste huge file lists into prose. Put representative paths in the Files overview table.
- Do not claim production validation unless it happened.

## Broad Branch Guidance

When a branch covers multiple feature areas, keep `Summary` short and make `What changed` carry the structure. Good area headings include:

- Docker, tenant runtime, and setup
- Runtime configuration and media
- Sync and webhooks
- Ops scripts
- Admin pricing model and UX
- Storefront behavior
- Tests and validation

## GitHub Mechanics

This skill does not replace GitHub tooling. To create the PR, use the available GitHub workflow or `gh pr create` with a body file:

```bash
gh pr create --draft --base <base> --head <branch> --title "<title>" --body-file <body-file>
```

Default to draft PRs unless the user explicitly asks for a ready PR.
