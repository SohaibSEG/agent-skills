"""Compact, external recovery state for execution-loop-planner.

Run this module only through scripts/loopctl, which supplies the isolated uv runtime.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


SCHEMA_VERSION = 1
SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,79}$")


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def limited(value: str, label: str, limit: int) -> str:
    value = " ".join(value.split())
    if not value:
        fail(f"{label} cannot be empty")
    if len(value) > limit:
        fail(f"{label} exceeds {limit} characters")
    return value


def run_git(repo: Path, *args: str) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def discover_repo() -> Path:
    root = run_git(Path.cwd(), "rev-parse", "--show-toplevel")
    if not root:
        fail("run from a Git repository")
    return Path(root).resolve()


def git_snapshot(repo: Path) -> dict[str, Any]:
    branch = run_git(repo, "branch", "--show-current") or "detached"
    head = run_git(repo, "rev-parse", "--short=12", "HEAD") or "unborn"
    porcelain = run_git(repo, "status", "--porcelain=v1")
    dirty = len(porcelain.splitlines()) if porcelain else 0
    fingerprint_input = f"{head}\n{porcelain or ''}".encode()
    return {
        "branch": branch,
        "head": head,
        "dirty_files": dirty,
        "fingerprint": hashlib.sha256(fingerprint_input).hexdigest()[:12],
    }


def default_root() -> Path:
    configured = os.environ.get("CODEX_EXECUTION_LOOP_STATE")
    if configured:
        return Path(configured).expanduser().resolve()
    return Path.home() / ".codex" / "state" / "execution-loops"


def repo_key(repo: Path) -> str:
    readable = re.sub(r"[^A-Za-z0-9._-]+", "-", repo.name).strip("-") or "repo"
    digest = hashlib.sha256(str(repo).encode()).hexdigest()[:8]
    return f"{readable}-{digest}"


def loop_dir(root: Path, repo: Path, loop_id: str) -> Path:
    if not SAFE_ID.fullmatch(loop_id):
        fail("id must be 1-80 shell-safe characters: letters, numbers, dot, underscore, hyphen")
    return root / repo_key(repo) / loop_id


def state_path(root: Path, repo: Path, loop_id: str) -> Path:
    return loop_dir(root, repo, loop_id) / "state.json"


def read_state(root: Path, repo: Path, loop_id: str) -> dict[str, Any]:
    path = state_path(root, repo, loop_id)
    if not path.exists():
        fail(f"loop '{loop_id}' does not exist for this repository")
    try:
        state = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read state: {exc}")
    if state.get("schema_version") != SCHEMA_VERSION:
        fail("unsupported state schema")
    if Path(state.get("repo_path", "")).resolve() != repo:
        fail("state repository does not match the current repository")
    return state


def atomic_write(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".state-", suffix=".json", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def write_transition(
    root: Path, repo: Path, state: dict[str, Any], event: str, detail: dict[str, Any]
) -> None:
    stamp = now()
    state["updated_at"] = stamp
    state["git_at_transition"] = git_snapshot(repo)
    path = state_path(root, repo, state["id"])
    atomic_write(path, state)
    record = {"at": stamp, "event": event, **detail}
    events = path.parent / "events.jsonl"
    with events.open("a") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")


def parse_slice(raw: str) -> dict[str, Any]:
    parts = raw.split("::", 1)
    if len(parts) != 2:
        fail("each --slice must use title::outcome")
    return {
        "title": limited(parts[0], "slice title", 80),
        "outcome": limited(parts[1], "slice outcome", 180),
        "status": "pending",
        "evidence": [],
        "validation": [],
    }


def load(args: argparse.Namespace) -> tuple[Path, Path, dict[str, Any]]:
    repo = discover_repo()
    root = Path(args.root).expanduser().resolve()
    return root, repo, read_state(root, repo, args.id)


def active_slice(state: dict[str, Any]) -> dict[str, Any] | None:
    index = state.get("active_index")
    if index is None:
        return None
    return state["slices"][index]


def command_init(args: argparse.Namespace) -> None:
    repo = discover_repo()
    root = Path(args.root).expanduser().resolve()
    destination = state_path(root, repo, args.id)
    if destination.exists():
        fail(f"loop '{args.id}' already exists; resume it or choose a new id")
    if not args.criterion:
        fail("provide at least one --criterion")
    if len(args.criterion) > 6:
        fail("use at most 6 completion criteria")
    if len(args.constraint or []) > 6:
        fail("use at most 6 constraints")
    if not args.slice:
        fail("provide at least one --slice")
    if len(args.slice) > 8:
        fail("use at most 8 slices")
    slices = [parse_slice(item) for item in args.slice]
    slices[0]["status"] = "active"
    state = {
        "schema_version": SCHEMA_VERSION,
        "id": args.id,
        "repo_path": str(repo),
        "goal": limited(args.goal, "goal", 320),
        "plan_revision": 1,
        "criteria": [limited(item, "criterion", 160) for item in args.criterion],
        "constraints": [limited(item, "constraint", 160) for item in (args.constraint or [])],
        "slices": slices,
        "active_index": 0,
        "status": "active",
        "next_action": limited(args.next, "next action", 180),
        "blocker": None,
        "created_at": now(),
        "updated_at": now(),
    }
    write_transition(root, repo, state, "initialized", {"active_slice": slices[0]["title"]})
    print_packet(state, repo)


def print_packet(state: dict[str, Any], repo: Path) -> None:
    current = git_snapshot(repo)
    completed = sum(item["status"] == "done" for item in state["slices"])
    lines = [
        f"GOAL: {state['goal']}",
        f"PLAN: r{state['plan_revision']}",
        "DONE WHEN: " + " | ".join(state["criteria"]),
        f"PROGRESS: {completed}/{len(state['slices'])} slices; loop {state['status']}",
    ]
    active = active_slice(state)
    if active:
        lines.append(f"ACTIVE: {active['title']} — {active['outcome']}")
    lines.append(f"NEXT: {state['next_action']}")
    if state.get("blocker"):
        lines.append(f"BLOCKER: {state['blocker']}")
    lines.append(f"GIT: {current['branch']}@{current['head']}; dirty files {current['dirty_files']}")
    if state.get("constraints"):
        lines.append("CONSTRAINTS: " + " | ".join(state["constraints"]))
    lines.append("GUARD: execute NEXT; do not edit loop state until a slice boundary or real blocker.")
    print("\n".join(lines))


def command_packet(args: argparse.Namespace) -> None:
    _, repo, state = load(args)
    print_packet(state, repo)


def command_status(args: argparse.Namespace) -> None:
    _, _, state = load(args)
    if args.json:
        print(json.dumps(state, indent=2, sort_keys=True))
    else:
        print(f"{state['id']}: {state['status']} — {state['next_action']}")


def command_finish(args: argparse.Namespace) -> None:
    root, repo, state = load(args)
    if state["status"] != "active":
        fail(f"cannot finish a slice while loop is {state['status']}")
    active = active_slice(state)
    if active is None:
        fail("no active slice")
    active["status"] = "done"
    if len(args.evidence) > 3 or len(args.validation) > 3:
        fail("use at most 3 evidence and 3 validation items per slice")
    active["evidence"] = [limited(item, "evidence", 180) for item in args.evidence]
    active["validation"] = [limited(item, "validation", 180) for item in args.validation]
    next_index = next(
        (index for index, item in enumerate(state["slices"]) if item["status"] == "pending"),
        None,
    )
    if next_index is None:
        if args.next:
            fail("--next is not used after the final slice")
        state["active_index"] = None
        state["status"] = "ready_to_close"
        state["next_action"] = "Verify every original completion criterion, then close the loop"
    else:
        if not args.next:
            fail("--next is required while another slice remains")
        state["active_index"] = next_index
        state["slices"][next_index]["status"] = "active"
        state["status"] = "active"
        state["next_action"] = limited(args.next, "next action", 180)
    state["blocker"] = None
    write_transition(root, repo, state, "slice_finished", {"slice": active["title"]})
    print_packet(state, repo)


def command_block(args: argparse.Namespace) -> None:
    root, repo, state = load(args)
    if state["status"] == "done":
        fail("cannot block a completed loop")
    state["status"] = "blocked"
    state["blocker"] = limited(args.reason, "blocker", 180)
    state["next_action"] = limited(args.next, "next action", 180)
    write_transition(root, repo, state, "blocked", {"reason": state["blocker"]})
    print_packet(state, repo)


def command_resume(args: argparse.Namespace) -> None:
    root, repo, state = load(args)
    if state["status"] != "blocked":
        fail("resume is only valid for a blocked loop")
    state["status"] = "active" if active_slice(state) else "ready_to_close"
    state["blocker"] = None
    state["next_action"] = limited(args.next, "next action", 180)
    write_transition(root, repo, state, "resumed", {})
    print_packet(state, repo)


def command_replan(args: argparse.Namespace) -> None:
    root, repo, state = load(args)
    if state["status"] == "done":
        fail("cannot replan a completed loop")
    reason = limited(args.reason, "replan reason", 180)
    state["plan_revision"] += 1
    state["status"] = "active" if active_slice(state) else "ready_to_close"
    state["blocker"] = None
    state["next_action"] = limited(args.next, "next action", 180)
    write_transition(root, repo, state, "replanned", {"reason": reason})
    print_packet(state, repo)


def command_close(args: argparse.Namespace) -> None:
    root, repo, state = load(args)
    if state["status"] != "ready_to_close":
        fail("finish every slice before closing")
    if len(args.criterion_evidence) != len(state["criteria"]):
        fail("provide exactly one --criterion-evidence for each original criterion")
    evidence = [
        {
            "criterion": criterion,
            "evidence": limited(item, "criterion evidence", 240),
        }
        for criterion, item in zip(state["criteria"], args.criterion_evidence)
    ]
    state["status"] = "done"
    state["next_action"] = "Report the completed goal and evidence to the user"
    state["criterion_evidence"] = evidence
    write_transition(root, repo, state, "closed", {"criteria_verified": len(evidence)})
    print_packet(state, repo)


def command_list(args: argparse.Namespace) -> None:
    repo = discover_repo()
    root = Path(args.root).expanduser().resolve()
    parent = root / repo_key(repo)
    if not parent.exists():
        return
    for path in sorted(parent.glob("*/state.json")):
        try:
            state = json.loads(path.read_text())
            print(f"{state['id']}\t{state['status']}\t{state['goal']}")
        except (OSError, KeyError, json.JSONDecodeError):
            print(f"{path.parent.name}\tinvalid", file=sys.stderr)


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--root", default=str(default_root()), help="external state directory")
    sub = result.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="create a loop and activate its first slice")
    init.add_argument("--id", required=True)
    init.add_argument("--goal", required=True)
    init.add_argument("--criterion", action="append", default=[])
    init.add_argument("--constraint", action="append", default=[])
    init.add_argument("--slice", action="append", default=[])
    init.add_argument("--next", required=True)
    init.set_defaults(handler=command_init)

    packet = sub.add_parser("packet", help="print the compact recovery packet")
    packet.add_argument("--id", required=True)
    packet.set_defaults(handler=command_packet)

    status = sub.add_parser("status", help="show loop status")
    status.add_argument("--id", required=True)
    status.add_argument("--json", action="store_true")
    status.set_defaults(handler=command_status)

    finish = sub.add_parser("finish", help="complete active slice and activate the next")
    finish.add_argument("--id", required=True)
    finish.add_argument("--evidence", action="append", required=True)
    finish.add_argument("--validation", action="append", required=True)
    finish.add_argument("--next")
    finish.set_defaults(handler=command_finish)

    block = sub.add_parser("block", help="record a real execution blocker")
    block.add_argument("--id", required=True)
    block.add_argument("--reason", required=True)
    block.add_argument("--next", required=True)
    block.set_defaults(handler=command_block)

    resume = sub.add_parser("resume", help="clear a resolved blocker")
    resume.add_argument("--id", required=True)
    resume.add_argument("--next", required=True)
    resume.set_defaults(handler=command_resume)

    replan = sub.add_parser("replan", help="record an exceptional replan without rewriting the goal")
    replan.add_argument("--id", required=True)
    replan.add_argument("--reason", required=True)
    replan.add_argument("--next", required=True)
    replan.set_defaults(handler=command_replan)

    close = sub.add_parser("close", help="close a loop after all slices are finished")
    close.add_argument("--id", required=True)
    close.add_argument("--criterion-evidence", action="append", required=True)
    close.set_defaults(handler=command_close)

    listing = sub.add_parser("list", help="list loops for the current repository")
    listing.set_defaults(handler=command_list)
    return result


def main() -> None:
    args = parser().parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
