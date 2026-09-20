#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
skill_dir=$(CDPATH= cd -- "$script_dir/.." && pwd)

if [ -n "${CODEX_EXECUTION_LOOP_RUNTIME:-}" ]; then
    runtime_dir=$CODEX_EXECUTION_LOOP_RUNTIME
elif [ -n "${CODEX_HOME:-}" ]; then
    runtime_dir=$CODEX_HOME/state/execution-loop-planner/runtime
else
    runtime_dir=$HOME/.codex/state/execution-loop-planner/runtime
fi

if ! command -v uv >/dev/null 2>&1; then
    printf '%s\n' "uv is required but was not found." >&2
    printf '%s\n' "Install it from https://docs.astral.sh/uv/getting-started/installation/ and rerun setup." >&2
    exit 2
fi

printf '%s\n' "Preparing an isolated uv-managed Python 3.11 runtime at: $runtime_dir"
if ! uv python find --managed-python 3.11 >/dev/null 2>&1; then
    uv python install 3.11
fi
mkdir -p "$runtime_dir"
UV_PROJECT_ENVIRONMENT=$runtime_dir/.venv uv sync \
    --project "$skill_dir" \
    --locked \
    --managed-python \
    --python 3.11
printf '%s\n' "Runtime ready. Verify with: $script_dir/loopctl doctor"
