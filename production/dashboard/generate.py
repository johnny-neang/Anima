#!/usr/bin/env python3
"""Dashboard generator for the Anima production pipeline.

Renders production/dashboard/index.html from the coherence registry, git
activity, and a few hand-tuned project signals. Open the HTML in a
browser; it's static, no server needed.

Usage:
    python production/dashboard/generate.py
    open production/dashboard/index.html
"""

from __future__ import annotations

import datetime as dt
import html
import json
import os
import subprocess
import sys
from pathlib import Path

DASHBOARD_DIR = Path(__file__).resolve().parent
REPO_ROOT = DASHBOARD_DIR.parents[1]
COHERENCE_DIR = REPO_ROOT / "production" / "coherence"
REGISTRY_PATH = COHERENCE_DIR / "registry.json"
OUT_PATH = DASHBOARD_DIR / "index.html"

# GitHub link configuration. Override with env vars when deploying.
GITHUB_REPO = os.environ.get("GITHUB_REPO", "johnny-neang/Anima")
GITHUB_BRANCH_OVERRIDE = os.environ.get("GITHUB_BRANCH")  # default: detect from git


def link_for(path: str, branch: str) -> str:
    """Build a GitHub blob URL for a repo-relative path."""
    return f"https://github.com/{GITHUB_REPO}/blob/{branch}/{path}"

# Import coherence module
sys.path.insert(0, str(COHERENCE_DIR))
import coherence  # noqa: E402

STAGES = [
    "synopsis",
    "outline",
    "script",
    "shotlist",
    "animatic",
    "lookdev",
    "production",
    "edit",
    "color",
    "delivery",
]
EPISODES = [
    ("ep01", "Hunger"),
    ("ep02", "Almost"),
    ("ep03", "Morrow"),
    ("ep04", "The Constitution"),
    ("ep05", "Witness"),
    ("ep06", "The Distance"),
]
STATUS_COLORS = {
    "missing": "gray",
    "draft": "yellow",
    "in_review": "blue",
    "approved": "green",
    "locked": "green",
    "stale": "red",
}
STATUS_LABELS = {
    "missing": "—",
    "draft": "draft",
    "in_review": "review",
    "approved": "approved",
    "locked": "locked",
    "stale": "stale",
}


# ─── git helpers ─────────────────────────────────────────────────────────────

def get_recent_commits(n: int = 8) -> list[dict]:
    try:
        out = subprocess.check_output(
            ["git", "log", "-n", str(n), "--format=%h%x09%cr%x09%s"],
            cwd=REPO_ROOT, text=True, stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return []
    items = []
    for line in out.strip().splitlines():
        parts = line.split("\t", 2)
        if len(parts) == 3:
            items.append({"hash": parts[0], "when": parts[1], "subject": parts[2]})
    return items


def get_branch() -> str:
    if GITHUB_BRANCH_OVERRIDE:
        return GITHUB_BRANCH_OVERRIDE
    # Vercel sets VERCEL_GIT_COMMIT_REF to the deploying branch
    if os.environ.get("VERCEL_GIT_COMMIT_REF"):
        return os.environ["VERCEL_GIT_COMMIT_REF"]
    try:
        b = subprocess.check_output(
            ["git", "branch", "--show-current"],
            cwd=REPO_ROOT, text=True, stderr=subprocess.DEVNULL,
        ).strip()
        return b or "main"
    except subprocess.CalledProcessError:
        return "main"


# ─── Status logic ────────────────────────────────────────────────────────────

def status_for(artifact: dict, stale_ids: set[str]) -> str:
    if not (REPO_ROOT / artifact["path"]).exists():
        return "missing"
    if artifact["id"] in stale_ids:
        return "stale"
    return artifact.get("status", "draft")


def episode_cell(reg: dict, ep_id: str, stage: str, stale_ids: set[str]) -> tuple[str, str | None]:
    for a in reg["artifacts"]:
        if a.get("episode") == ep_id and a.get("stage") == stage:
            return status_for(a, stale_ids), a["path"]
    return "missing", None


def awaiting_approval(reg: dict, stale_ids: set[str]) -> list[dict]:
    items = []
    for a in reg["artifacts"]:
        st = status_for(a, stale_ids)
        if st == "in_review":
            items.append((a, st))
        if st == "draft" and a.get("stage") in {
            "logline", "one_pager", "treatment", "beat_sheet", "episodes", "synopsis"
        }:
            # First-pass drafts are implicitly awaiting initial review.
            items.append((a, "draft"))
    return items


# ─── Rendering ───────────────────────────────────────────────────────────────

def esc(s) -> str:
    return html.escape(str(s)) if s is not None else ""


def render_html(reg: dict, stale: list[dict], commits: list[dict], branch: str) -> str:
    stale_ids = {s["artifact"] for s in stale if s["reason"] == "dependency_newer"}
    awaiting = awaiting_approval(reg, stale_ids)
    artifact_count = len(reg["artifacts"])

    # Episode matrix
    rows = []
    for ep_id, ep_title in EPISODES:
        cells = []
        for stage in STAGES:
            st, path = episode_cell(reg, ep_id, stage, stale_ids)
            color = STATUS_COLORS.get(st, "gray")
            tooltip = f"{stage}: {st}"
            if path is None:
                cells.append(
                    f'<td class="cell {color}" title="{esc(tooltip)}">'
                    f'<span class="dot"></span></td>'
                )
            else:
                cells.append(
                    f'<td class="cell {color}" title="{esc(tooltip)}">'
                    f'<a href="{esc(link_for(path, branch))}" class="dot-link" target="_blank" rel="noopener">'
                    f'<span class="dot"></span></a></td>'
                )
        rows.append(
            f'<tr><th class="ep-row">'
            f'<span class="ep-id">{esc(ep_id)}</span>'
            f'<span class="ep-title">{esc(ep_title)}</span>'
            f'</th>{"".join(cells)}</tr>'
        )
    head_cells = "".join(f'<th class="stage-col">{esc(s)}</th>' for s in STAGES)

    # Awaiting cards
    if awaiting:
        cards = []
        for a, st in awaiting:
            badge_color = STATUS_COLORS.get(st, "gray")
            cards.append(
                f'<a class="card" href="{esc(link_for(a["path"], branch))}" target="_blank" rel="noopener">'
                f'<div class="card-header">'
                f'<span class="badge {badge_color}">{esc(STATUS_LABELS.get(st, st))}</span>'
                f'<span class="card-id">{esc(a["id"])}</span>'
                f'</div>'
                f'<div class="card-stage">{esc(a.get("stage", ""))}'
                f'{" · " + esc(a["episode"]) if a.get("episode") else ""}</div>'
                f'<div class="card-path">{esc(a["path"])}</div>'
                + (f'<div class="card-notes">{esc(a["notes"])}</div>' if a.get("notes") else "")
                + "</a>"
            )
        awaiting_html = '<div class="cards">' + "".join(cards) + "</div>"
    else:
        awaiting_html = '<div class="empty">Nothing awaiting your review.</div>'

    # Stale list
    if stale:
        items = []
        for s in stale:
            if s["reason"] == "missing":
                items.append(
                    f'<li><strong>{esc(s["artifact"])}</strong> '
                    f'<span class="muted">— file missing: {esc(s["path"])}</span></li>'
                )
            elif s["reason"] == "unknown_dependency":
                items.append(
                    f'<li><strong>{esc(s["artifact"])}</strong> '
                    f'<span class="muted">— unknown dependency:</span> '
                    f'<code>{esc(s["dependency"])}</code></li>'
                )
            else:
                items.append(
                    f'<li><strong>{esc(s["artifact"])}</strong> '
                    f'<span class="muted">— dependency</span> '
                    f'<code>{esc(s["dependency"])}</code> '
                    f'<span class="muted">updated after this</span></li>'
                )
        stale_html = "<ul>" + "".join(items) + "</ul>"
    else:
        stale_html = '<div class="empty">No stale artifacts. ✓</div>'

    # Commits
    if commits:
        commits_html = "<ul class='commits'>" + "".join(
            f'<li><code>{esc(c["hash"])}</code> '
            f'<span class="when">{esc(c["when"])}</span> '
            f'{esc(c["subject"])}</li>'
            for c in commits
        ) + "</ul>"
    else:
        commits_html = '<div class="empty">No git history available.</div>'

    # Counts by status
    counts: dict[str, int] = {}
    for a in reg["artifacts"]:
        st = status_for(a, stale_ids)
        counts[st] = counts.get(st, 0) + 1
    counts_html = "".join(
        f'<div class="counter"><span class="dot {STATUS_COLORS.get(st, "gray")}"></span>'
        f'<span class="num">{n}</span><span class="lbl">{esc(STATUS_LABELS.get(st, st))}</span></div>'
        for st, n in sorted(counts.items())
    )

    now = dt.datetime.now(tz=dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Footer links
    src_link = link_for("docs/story.md", branch)
    readme_link = link_for("production/README.md", branch)
    director_link = link_for("production/DIRECTOR.md", branch)
    questions_link = link_for("production/QUESTIONS.md", branch)
    queue_link = link_for("production/REVIEW_QUEUE.md", branch)
    repo = GITHUB_REPO

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Anima — Production Dashboard</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="topbar">
    <div class="title">
      <h1>Anima — <em>The Second Dawn</em></h1>
      <div class="subtitle">Lasseter Cut · 6 episodes · Series limited</div>
    </div>
    <div class="meta">
      <div><span class="meta-label">Branch</span><code>{esc(branch)}</code></div>
      <div><span class="meta-label">Artifacts</span>{artifact_count}</div>
      <div><span class="meta-label">Updated</span>{esc(now)}</div>
    </div>
  </header>

  <div class="counters">{counts_html}</div>

  <section class="awaiting">
    <h2>Awaiting your review</h2>
    {awaiting_html}
  </section>

  <section class="matrix">
    <h2>Series matrix</h2>
    <p class="hint">Six episodes (rows) × ten production stages (columns). Click any dot to open the underlying file.</p>
    <table>
      <thead><tr><th class="ep-col"></th>{head_cells}</tr></thead>
      <tbody>{"".join(rows)}</tbody>
    </table>
    <div class="legend">
      <span class="dot gray"></span>missing&nbsp;&nbsp;
      <span class="dot yellow"></span>draft&nbsp;&nbsp;
      <span class="dot blue"></span>in review&nbsp;&nbsp;
      <span class="dot green"></span>approved/locked&nbsp;&nbsp;
      <span class="dot red"></span>stale
    </div>
  </section>

  <section class="stale-section">
    <h2>Stale artifacts</h2>
    <p class="hint">Triggered when a dependency was updated after this artifact's <code>last_updated</code>. Run <code>python production/coherence/coherence.py touch &lt;artifact_id&gt;</code> after re-review to clear.</p>
    {stale_html}
  </section>

  <section class="activity">
    <h2>Recent activity</h2>
    {commits_html}
  </section>

  <footer>
    <p>Auto-regenerated after every Claude turn (via the Stop hook in <code>.claude/settings.json</code>) and on every push to Vercel. Manual: <code>python3 production/dashboard/generate.py</code>.</p>
    <p>
      <a href="{src_link}" target="_blank" rel="noopener">docs/story.md</a> ·
      <a href="{readme_link}" target="_blank" rel="noopener">README</a> ·
      <a href="{director_link}" target="_blank" rel="noopener">DIRECTOR</a> ·
      <a href="{questions_link}" target="_blank" rel="noopener">QUESTIONS</a> ·
      <a href="{queue_link}" target="_blank" rel="noopener">REVIEW_QUEUE</a> ·
      <a href="https://github.com/{repo}" target="_blank" rel="noopener">repo</a>
    </p>
  </footer>
</body>
</html>
"""


def main() -> int:
    if not REGISTRY_PATH.exists():
        print(f"Registry not found: {REGISTRY_PATH}", file=sys.stderr)
        return 1
    reg = coherence.load_registry()
    stale = coherence.check_stale(reg)
    commits = get_recent_commits(8)
    branch = get_branch()
    out = render_html(reg, stale, commits, branch)
    OUT_PATH.write_text(out)
    print(f"Wrote {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
