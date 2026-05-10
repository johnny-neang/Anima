#!/usr/bin/env python3
"""Coherence engine for the Anima production pipeline.

Walks the registry, detects stale artifacts (whose dependencies have been
modified since the artifact's own last_updated), and reports them. Also
serves the dashboard generator with a JSON-shaped status of the project.

Usage
-----
    python production/coherence/coherence.py check
    python production/coherence/coherence.py report > report.json
    python production/coherence/coherence.py touch <artifact_id>
    python production/coherence/coherence.py status

The registry lives at production/coherence/registry.json. Schema is
documented in registry_schema.md.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = Path(__file__).resolve().parent / "registry.json"


# ─── Registry I/O ────────────────────────────────────────────────────────────

def load_registry() -> dict:
    with REGISTRY_PATH.open() as f:
        return json.load(f)


def save_registry(data: dict) -> None:
    with REGISTRY_PATH.open("w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


# ─── Helpers ─────────────────────────────────────────────────────────────────

def file_mtime(path: Path) -> dt.datetime | None:
    if not path.exists():
        return None
    return dt.datetime.fromtimestamp(path.stat().st_mtime, tz=dt.timezone.utc)


def parse_date(s) -> dt.datetime | None:
    if not s:
        return None
    if isinstance(s, dt.datetime):
        return s if s.tzinfo else s.replace(tzinfo=dt.timezone.utc)
    if isinstance(s, dt.date):
        return dt.datetime(s.year, s.month, s.day, tzinfo=dt.timezone.utc)
    if isinstance(s, str):
        try:
            if len(s) == 10:
                s = s + "T00:00:00+00:00"
            return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except ValueError:
            return None
    return None


def expand_deps(reg: dict, dep: str) -> list[str]:
    """Expand wildcards like 'source.character.*' to concrete artifact IDs."""
    if "*" not in dep:
        return [dep]
    prefix = dep.replace("*", "")
    return [a["id"] for a in reg["artifacts"] if a["id"].startswith(prefix)]


# ─── Core check ──────────────────────────────────────────────────────────────

def check_stale(reg: dict) -> list[dict]:
    """Return a list of stale artifact records.

    An artifact is stale if any of its dependencies has been modified after
    the artifact's own last_updated date. Missing files are also reported.
    """
    by_id = {a["id"]: a for a in reg["artifacts"]}
    stale: list[dict] = []

    for a in reg["artifacts"]:
        path = REPO_ROOT / a["path"]
        artifact_time = file_mtime(path)

        if artifact_time is None:
            stale.append({
                "artifact": a["id"],
                "reason": "missing",
                "path": a["path"],
            })
            continue

        # Compare against authoritative last_updated when present (handles
        # edits where mtime advanced but the artifact itself wasn't
        # conceptually updated — e.g. trailing-whitespace fix).
        last_updated = parse_date(a.get("last_updated")) or artifact_time

        deps: list[str] = []
        for d in a.get("depends_on", []) or []:
            deps.extend(expand_deps(reg, d))

        for dep_id in deps:
            dep = by_id.get(dep_id)
            if dep is None:
                stale.append({
                    "artifact": a["id"],
                    "reason": "unknown_dependency",
                    "dependency": dep_id,
                })
                continue

            dep_path = REPO_ROOT / dep["path"]
            dep_time = file_mtime(dep_path)
            dep_last_updated = parse_date(dep.get("last_updated")) or dep_time

            if dep_last_updated is None:
                continue
            if dep_last_updated > last_updated:
                stale.append({
                    "artifact": a["id"],
                    "reason": "dependency_newer",
                    "dependency": dep_id,
                    "dep_last_updated": dep_last_updated.isoformat(),
                    "this_last_updated": last_updated.isoformat(),
                })

    return stale


# ─── Subcommands ─────────────────────────────────────────────────────────────

def cmd_check(_args) -> int:
    reg = load_registry()
    stale = check_stale(reg)
    if not stale:
        print("All artifacts coherent.")
        return 0
    print(f"{len(stale)} stale artifact(s):\n")
    for s in stale:
        if s["reason"] == "missing":
            print(f"  [missing] {s['artifact']:34s}  {s['path']}")
        elif s["reason"] == "unknown_dependency":
            print(f"  [unknown] {s['artifact']:34s}  -> {s['dependency']}")
        else:
            print(f"  [stale]   {s['artifact']:34s}  <- {s['dependency']} updated after this")
    return 1


def cmd_report(_args) -> int:
    reg = load_registry()
    stale = check_stale(reg)
    out = {
        "version": reg.get("version", 1),
        "project": reg.get("project", "anima"),
        "checked_at": dt.datetime.now(tz=dt.timezone.utc).isoformat(),
        "artifact_count": len(reg["artifacts"]),
        "stale_count": len(stale),
        "stale": stale,
        "artifacts": reg["artifacts"],
    }
    print(json.dumps(out, indent=2, default=str))
    return 0


def cmd_touch(args) -> int:
    reg = load_registry()
    found = False
    for a in reg["artifacts"]:
        if a["id"] == args.artifact_id:
            a["last_updated"] = dt.datetime.now(tz=dt.timezone.utc).date().isoformat()
            found = True
            break
    if not found:
        print(f"Artifact not found: {args.artifact_id}", file=sys.stderr)
        return 1
    save_registry(reg)
    print(f"Touched: {args.artifact_id}")
    return 0


def cmd_status(_args) -> int:
    reg = load_registry()
    by_stage: dict[str, list] = {}
    by_status: dict[str, int] = {}
    for a in reg["artifacts"]:
        by_stage.setdefault(a.get("stage", "?"), []).append(a)
        by_status[a.get("status", "?")] = by_status.get(a.get("status", "?"), 0) + 1

    print(f"Project: {reg.get('project', 'anima')}")
    print(f"Total artifacts: {len(reg['artifacts'])}\n")
    print("By stage:")
    for stage in sorted(by_stage):
        print(f"  {stage:18s} {len(by_stage[stage]):3d}")
    print("\nBy status:")
    for status in sorted(by_status):
        print(f"  {status:18s} {by_status[status]:3d}")
    print()
    return cmd_check(_args)


# ─── Entry point ─────────────────────────────────────────────────────────────

def main() -> int:
    p = argparse.ArgumentParser(description="Coherence engine for the Anima production pipeline.")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("check", help="Detect stale artifacts.")
    sp.set_defaults(func=cmd_check)

    sp = sub.add_parser("report", help="Emit JSON report (for the dashboard).")
    sp.set_defaults(func=cmd_report)

    sp = sub.add_parser("touch", help="Mark an artifact as freshly updated.")
    sp.add_argument("artifact_id")
    sp.set_defaults(func=cmd_touch)

    sp = sub.add_parser("status", help="Full project status + coherence check.")
    sp.set_defaults(func=cmd_status)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
