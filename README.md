# Sohaib's Agent Skills

A public collection of skills for Codex and Claude Code. It combines personal workflows with attributed third-party skills adapted for explicit invocation, bounded authority, and non-invasive use in shared repositories.

## Design principles

- **No repository bootstrap:** installing these skills does not add configuration, scratch files, or planning artifacts to a project.
- **Local by default:** drafts, diagnostics, and temporary state remain local until publication or another shared mutation is explicitly approved.
- **Goal before ceremony:** planning and checkpoint state support implementation; they are not the deliverable.
- **Portable instructions:** each skill keeps its core behavior in `SKILL.md`; Codex-specific metadata is additive under `agents/`.
- **Respect existing teams:** skills do not introduce repository-wide conventions, commit, push, publish, or change shared infrastructure merely because they were invoked.

## Install

Use the skills CLI and choose Codex, Claude Code, or both when prompted:

```bash
npx skills@latest add SohaibSEG/agent-skills
```

To install a single skill with Codex's bundled GitHub installer, replace `<skill-name>` with a directory from the catalog:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo SohaibSEG/agent-skills \
  --path skills/<skill-name>
```

Restart the agent host after installation if its skill catalog does not refresh automatically.

## Invocation and compatibility

Invoke an explicit skill as `$skill-name` in Codex or `/skill-name` in Claude Code.

Codex reads the included `agents/openai.yaml` files. Skills marked **Explicit** below set `allow_implicit_invocation: false`, so Codex does not activate them unless requested.

Claude Code reads the shared `SKILL.md` files but does not use Codex's invocation policy. For equivalent behavior, mark the explicit skills as user-only from `/skills` or configure their `skillOverrides` to `user-invocable-only`. Claude-specific frontmatter is intentionally not embedded in the shared files because it would make the same skill fail Codex validation.

Some skills depend on host capabilities such as browser automation, subprocesses, GitHub access, or subagents. A compatible instruction format does not manufacture a tool that the active host does not provide; the skill should stop and report the missing capability.

### Make ADHD mode the session default

Implicit invocation makes `i-have-adhd` available to the model, but a short global instruction is what activates it reliably for every new session.

For Codex, add this to `~/.codex/AGENTS.md`:

```markdown
At the start of every session, load and apply the `$i-have-adhd` skill. Keep it active until I say `stop adhd mode` or `normal mode`.
```

For Claude Code, add this to `~/.claude/CLAUDE.md`:

```markdown
At the start of every session, load and apply the `/i-have-adhd` skill. Keep it active until I say `stop adhd mode` or `normal mode`.
```

These are personal, host-level preferences; they do not modify any project repository. Start a new session after changing them.

## Catalog

| Skill | Purpose | Invocation | Origin |
|---|---|---|---|
| `codebase-design` | Design deep modules and clean seams | Automatic | Matt Pocock |
| `diagnosing-bugs` | Diagnose difficult bugs and regressions without silently implementing a fix | Explicit | Matt Pocock, customized |
| `domain-modeling` | Sharpen domain language, contexts, and architecture decisions | Explicit | Matt Pocock, customized |
| `execution-loop-planner` | Execute long, multi-slice goals with compact recovery state | Explicit | Personal |
| `github-pr-template` | Write consistent, evidence-based pull request descriptions | Automatic | Personal |
| `grill-me` | Explicit entry point for a structured grilling session | Explicit | Matt Pocock, customized |
| `grilling` | Stress-test a plan or decision through dependency-aware questions | Automatic | Matt Pocock |
| `handoff-session-context` | Package actionable context for continuation in a fresh session | Automatic | Personal |
| `i-have-adhd` | Keep responses action-first, compact, and easy to resume | Automatic | Ayoub Ghriss, metadata adapted |
| `playwright` | Automate browser workflows through the Playwright CLI | Automatic | Microsoft/OpenAI adaptation |
| `playwright-interactive` | Run persistent browser and Electron QA sessions | Automatic | OpenAI adaptation; Microsoft assets |
| `pr-review-qa` | Review and test a PR in an isolated worktree across backend, UI, infrastructure, design, quality, and performance | Explicit | Personal |
| `prototype` | Build a throwaway prototype that answers a design question | Explicit | Matt Pocock, customized |
| `research` | Investigate a question using high-trust primary sources | Explicit | Matt Pocock, customized |
| `tdd` | Implement a requested change with a red-green-refactor loop | Explicit | Matt Pocock, customized |
| `to-tickets` | Turn a plan into dependency-aware tracer-bullet tickets | Explicit | Matt Pocock, customized |
| `wayfinder` | Resolve the decision map for work too large for one session | Explicit | Matt Pocock, customized |

`setup-matt-pocock-skills` is intentionally not included. The adapted skills discover context at invocation time and do not require repository-local setup.

## Execution loop runtime

`execution-loop-planner` includes a small state tool so the model does not repeatedly rewrite plan and checkpoint files or reload long histories.

- The runtime requires [`uv`](https://docs.astral.sh/uv/) but does not assume or modify system Python.
- First-time setup is never automatic. The skill checks prerequisites and asks before running `scripts/setup_runtime.sh`.
- Setup provisions a locked, uv-managed Python 3.11 environment with no third-party Python dependencies.
- Runtime and loop state live under `$XDG_STATE_HOME/agent-skills/execution-loop-planner` or `~/.local/state/agent-skills/execution-loop-planner`, outside project repositories.
- Normal state transitions run locked and offline; they cannot install or synchronize packages.

## Safety model

The customized workflows prefer chat drafts, isolated worktrees, disposable local services, and temporary state outside the target repository. They require explicit approval before tracker publication, commits, pushes, pull requests, deployments, or other shared-state mutations unless the active task already grants that authority.

This is a personal modification layer, not an upstream guarantee. Updating a customized skill directly from its upstream source can overwrite these boundaries; review the diff before syncing.

## Attribution and licensing

Personal material is covered by the root [LICENSE](LICENSE). Third-party material remains under its original license and is credited in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), under [`licenses/`](licenses/), and in notices retained inside individual skill directories.
