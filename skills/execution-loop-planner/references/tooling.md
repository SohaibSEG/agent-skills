# Compact loop-state tool

Use this reference only when creating, resuming, or transitioning a durable execution loop.

`loopctl` runs `loop_state.py` in an isolated uv environment. By default, runtime and loop state live under `$XDG_STATE_HOME/agent-skills/execution-loop-planner`, or `~/.local/state/agent-skills/execution-loop-planner` when `XDG_STATE_HOME` is unset. Both locations are outside the target repository and host-specific configuration directories.

Set `EXECUTION_LOOP_STATE`, pass `--root`, or set `EXECUTION_LOOP_RUNTIME` to override those locations. The legacy `CODEX_EXECUTION_LOOP_STATE` and `CODEX_EXECUTION_LOOP_RUNTIME` names remain accepted.

Run commands from the target repository. Replace `<skill-dir>` with the directory containing this `SKILL.md`. In Claude Code use `${CLAUDE_SKILL_DIR}`; in Codex use the installed path from the skill catalog.

## Runtime prerequisite

Check without changing the machine:

```bash
<skill-dir>/scripts/loopctl doctor
```

If the check fails, stop and tell the user what is missing. Do not install dependencies automatically.

- If `uv` is missing, ask the user to install it from the official uv installation instructions.
- If the isolated runtime is missing, explain that setup will verify or install uv-managed Python 3.11 and create a dedicated environment outside project repositories. Ask before running:

```bash
<skill-dir>/scripts/setup_runtime.sh
```

The setup does not use, modify, or install packages into system Python. Normal `loopctl` commands are locked, offline, and cannot synchronize or install dependencies.

## Initialize once

```bash
<skill-dir>/scripts/loopctl init \
  --id checkout-tax \
  --goal "Tax is calculated consistently through checkout" \
  --criterion "API returns the agreed tax breakdown" \
  --criterion "UI presents the returned totals" \
  --constraint "No production deployment" \
  --slice "Backend contract::Return and validate the tax breakdown" \
  --slice "Checkout integration::Render and submit the agreed totals" \
  --next "Locate the current tax calculation boundary and its tests"
```

Keep identifiers stable and shell-safe. Each slice uses `title::outcome`. Initialization activates the first slice.

## Recover without loading a plan

```bash
<skill-dir>/scripts/loopctl packet --id checkout-tax
```

The packet is intentionally small. Treat `NEXT` as the immediate action. Inspect the repository diff when the packet reports a dirty worktree; do not expand the packet into new planning files.

Use `status --id <id> --json` only for exceptional recovery or debugging the state tool.

## Finish a slice

After implementation and focused validation:

```bash
<skill-dir>/scripts/loopctl finish \
  --id checkout-tax \
  --evidence "Tax response now includes jurisdiction totals" \
  --validation "Focused API tests pass" \
  --next "Wire the checkout summary to the returned totals"
```

This completes the active slice and activates the next one. `--next` is required while another slice remains.

## Exceptional transitions

Use these only when implementation cannot continue:

```bash
<skill-dir>/scripts/loopctl block \
  --id checkout-tax \
  --reason "Required Postgres service is unavailable" \
  --next "Ask the user to start Postgres"

<skill-dir>/scripts/loopctl resume \
  --id checkout-tax \
  --next "Run the integration test against Postgres"

<skill-dir>/scripts/loopctl replan \
  --id checkout-tax \
  --reason "The provider adapter is the actual ownership boundary" \
  --next "Reinspect the provider boundary before editing"
```

`resume` clears a resolved blocker. `replan` increments the plan revision but cannot rewrite the original goal or slices. If the requested outcome materially changes, initialize a new loop after confirming the new contract.

## Close

After all slices are finished:

```bash
<skill-dir>/scripts/loopctl close \
  --id checkout-tax \
  --criterion-evidence "API contract test verifies the tax breakdown" \
  --criterion-evidence "Browser test verifies the displayed totals"
```

Provide one evidence item for each original criterion, in the same order. The tool refuses to close otherwise.

`list` shows known loops for the current repository. The append-only `events.jsonl` is for exceptional audit or recovery; do not load it during normal execution.
