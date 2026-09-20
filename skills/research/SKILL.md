---
name: research
description: Investigate a question against high-trust primary sources and return cited findings without changing the project unless explicitly requested.
---

Spin up a **background agent** to do the research, so you keep working while it reads.

## Mutation boundary

Return findings in chat by default. Do not write into the repository, create branches, commit, publish, or update trackers. Write a Markdown artifact only when the user explicitly requests a file; use their stated path or the current Codex task's user-facing output directory, not the project repository, unless they explicitly choose a repository path.

Its job:

1. Investigate the question against **primary sources** (official docs, source code, specs, first-party APIs), not a secondary write-up of them. Follow every claim back to the source that owns it.
2. Return a compact cited synthesis in chat.
3. If the user requested a file, write one Markdown artifact at the explicitly approved non-project path and report its location.
