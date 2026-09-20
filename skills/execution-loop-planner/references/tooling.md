# Compact loop-state tool

Use this reference only when creating, resuming, or transitioning a durable execution loop.

`loop_state.py` stores state under `~/.codex/state/execution-loops` by default. Set `CODEX_EXECUTION_LOOP_STATE` or pass `--root` to use another external directory. It never writes into the target repository.

Run commands from the target repository. Replace `<skill>` with the installed skill directory.

## Initialize once

```bash
python3 <skill>/scripts/loop_state.py init \
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
python3 <skill>/scripts/loop_state.py packet --id checkout-tax
```

The packet is intentionally small. Treat `NEXT` as the immediate action. Inspect the repository diff when the packet reports a dirty worktree; do not expand the packet into new planning files.

Use `status --id <id> --json` only for exceptional recovery or debugging the state tool.

## Finish a slice

After implementation and focused validation:

```bash
python3 <skill>/scripts/loop_state.py finish \
  --id checkout-tax \
  --evidence "Tax response now includes jurisdiction totals" \
  --validation "Focused API tests pass" \
  --next "Wire the checkout summary to the returned totals"
```

This completes the active slice and activates the next one. `--next` is required while another slice remains.

## Exceptional transitions

Use these only when implementation cannot continue:

```bash
python3 <skill>/scripts/loop_state.py block \
  --id checkout-tax \
  --reason "Required Postgres service is unavailable" \
  --next "Ask the user to start Postgres"

python3 <skill>/scripts/loop_state.py resume \
  --id checkout-tax \
  --next "Run the integration test against Postgres"

python3 <skill>/scripts/loop_state.py replan \
  --id checkout-tax \
  --reason "The provider adapter is the actual ownership boundary" \
  --next "Reinspect the provider boundary before editing"
```

`resume` clears a resolved blocker. `replan` increments the plan revision but cannot rewrite the original goal or slices. If the requested outcome materially changes, initialize a new loop after confirming the new contract.

## Close

After all slices are finished:

```bash
python3 <skill>/scripts/loop_state.py close \
  --id checkout-tax \
  --criterion-evidence "API contract test verifies the tax breakdown" \
  --criterion-evidence "Browser test verifies the displayed totals"
```

Provide one evidence item for each original criterion, in the same order. The tool refuses to close otherwise.

`list` shows known loops for the current repository. The append-only `events.jsonl` is for exceptional audit or recovery; do not load it during normal execution.
