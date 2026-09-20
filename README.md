# Sohaib's Codex Skills

A private, versioned collection of personal Codex skills plus attributed third-party skills customized for a non-invasive workflow.

## Install

Install interactively with the skills CLI:

```bash
npx skills@latest add SohaibSEG/codex-skills
```

For a single skill, use Codex's GitHub installer with the path under `skills/`, for example:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo SohaibSEG/codex-skills \
  --path skills/pr-review-qa
```

Because this repository is private, installation requires GitHub credentials that can read it.

## Catalog

| Skill | Invocation | Origin |
|---|---|---|
| `codebase-design` | Automatic | Matt Pocock |
| `diagnosing-bugs` | Explicit | Matt Pocock, customized |
| `domain-modeling` | Explicit | Matt Pocock, customized |
| `execution-loop-planner` | Automatic | Personal |
| `github-pr-template` | Automatic | Personal |
| `grill-me` | Explicit | Matt Pocock, customized |
| `grilling` | Automatic | Matt Pocock |
| `handoff-session-context` | Automatic | Personal |
| `i-have-adhd` | Explicit | Ayoub Ghriss, Codex metadata added |
| `playwright` | Automatic | Microsoft/OpenAI Codex adaptation |
| `playwright-interactive` | Automatic | OpenAI Codex adaptation; Microsoft assets |
| `pr-review-qa` | Explicit | Personal |
| `prototype` | Explicit | Matt Pocock, customized |
| `research` | Explicit | Matt Pocock, customized |
| `tdd` | Explicit | Matt Pocock, customized |
| `to-tickets` | Explicit | Matt Pocock, customized |
| `wayfinder` | Explicit | Matt Pocock, customized |

`setup-matt-pocock-skills` is intentionally excluded. The customized planning skills work without repository-local setup and default to drafts or read-only behavior.

## Safety posture

The customized skills prefer chat drafts, isolated worktrees, temporary files outside project repositories, and explicit approval before external or shared-state mutations. This is a personal modification layer, not an upstream guarantee.

Updating directly from an upstream repository can overwrite these safety changes. Review diffs before syncing.

## Attribution and licensing

Original personal material is covered by the root [LICENSE](LICENSE). Third-party material remains under its original license; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), the files under `licenses/`, and any notices retained inside individual skill directories.

