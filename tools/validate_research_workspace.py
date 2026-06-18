#!/usr/bin/env python3
"""Structural validator for the AI research workspace.

This intentionally avoids third-party YAML dependencies. It validates the
simple index/manifest conventions used by this scaffold.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_ROOT = [
    "RESEARCH.md",
    "OPEN_QUESTIONS.md",
    "CLAIMS.md",
    "DECISIONS.md",
    "AGENTS.md",
    ".agents/skills/research-workspace/SKILL.md",
    ".agents/skills/research-experiment/SKILL.md",
    ".agents/skills/research-claims/SKILL.md",
    ".agents/skills/research-synthesis/SKILL.md",
    ".agents/skills/research-references/SKILL.md",
    ".agents/skills/research-director/SKILL.md",
    ".agents/skills/plan-research-goal/SKILL.md",
    "experiments/index.yml",
    "factory/README.md",
    "factory/queue.yml",
    "factory/scorecards/_template.md",
    "factory/goals/README.md",
    "factory/audits/README.md",
]


LIVE_FILE_BUDGETS = {
    # These are intentionally small enough to keep the belief layer readable.
    # Put chronology in run records and synthesis notes, not live dashboards.
    "RESEARCH.md": {"max_lines": 160, "max_chars": 18_000},
    "OPEN_QUESTIONS.md": {"max_lines": 120, "max_chars": 20_000},
    "CLAIMS.md": {"max_lines": 260, "max_chars": 32_000},
    "DECISIONS.md": {"max_lines": 180, "max_chars": 35_000},
}

MAX_ACTIVE_DECISIONS = 20
MAX_RUNNING_EXPERIMENTS = 3


def ids_in_file(path: Path, prefix: str) -> set[str]:
    if not path.exists():
        return set()
    return set(re.findall(rf"\b{prefix}[0-9]{{3}}\b", path.read_text(errors="ignore")))


def parse_index(path: Path) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for raw in path.read_text(errors="ignore").splitlines():
        line = raw.strip()
        if line.startswith("- id:"):
            if current:
                entries.append(current)
            current = {"id": line.split(":", 1)[1].strip()}
            continue
        if current is None or ":" not in line or line.startswith("#"):
            continue
        key, value = line.split(":", 1)
        current[key.strip()] = value.strip().strip('"')
    if current:
        entries.append(current)
    return entries


def parse_manifest(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data
    for raw in path.read_text(errors="ignore").splitlines():
        line = raw.strip()
        if ":" not in line or line.startswith("#") or line.startswith("-"):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def line_for_id(text: str, object_id: str) -> str:
    return next((line for line in text.splitlines() if object_id in line and "|" in line), "")


def markdown_table_rows_with_id(path: Path, prefix: str) -> list[str]:
    if not path.exists():
        return []
    pattern = re.compile(rf"\|\s*`?{prefix}[0-9]{{3}}`?\s*\|")
    return [line for line in path.read_text(errors="ignore").splitlines() if pattern.search(line)]


def markdown_table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    problems: list[str] = []

    for rel in REQUIRED_ROOT:
        if not (root / rel).exists():
            problems.append(f"missing {rel}")

    for rel, budget in LIVE_FILE_BUDGETS.items():
        path = root / rel
        if not path.exists():
            continue
        text = path.read_text(errors="ignore")
        line_count = text.count("\n") + 1
        char_count = len(text)
        if line_count > budget["max_lines"]:
            problems.append(
                f"{rel} has {line_count} lines; compress live belief files below "
                f"{budget['max_lines']} lines"
            )
        if char_count > budget["max_chars"]:
            problems.append(
                f"{rel} has {char_count} chars; move chronology into run records "
                f"or synthesis notes below {budget['max_chars']} chars"
            )

    queue_path = root / "factory/queue.yml"
    if queue_path.exists():
        queue_text = queue_path.read_text(errors="ignore")
        if "queue:" not in queue_text:
            problems.append("factory/queue.yml must contain a queue: list")
        if "require_stop_or_pivot_gate: true" not in queue_text:
            problems.append("factory/queue.yml should require stop_or_pivot gates")

    question_ids = ids_in_file(root / "OPEN_QUESTIONS.md", "Q")
    claim_ids = ids_in_file(root / "CLAIMS.md", "C")
    decision_ids = ids_in_file(root / "DECISIONS.md", "D")
    experiments_by_id: dict[str, Path] = {}

    exp_root = root / "experiments"
    for exp in sorted(exp_root.glob("[0-9][0-9][0-9]_*")):
        for rel in ["README.md", "manifest.yml", "notes.md"]:
            if not (exp / rel).exists():
                problems.append(f"missing {exp.relative_to(root)}/{rel}")
        manifest = exp / "manifest.yml"
        if manifest.exists():
            text = manifest.read_text(errors="ignore")
            manifest_data = parse_manifest(manifest)
            exp_id = manifest_data.get("id", "")
            question_id = manifest_data.get("question", "")
            if not re.search(r"^E[0-9]{3}$", exp_id):
                problems.append(f"{manifest.relative_to(root)} missing id: E###")
            else:
                experiments_by_id[exp_id] = exp
            if not re.search(r"^Q[0-9]{3}$", question_id):
                problems.append(f"{manifest.relative_to(root)} missing question: Q###")
            elif question_id not in question_ids:
                problems.append(f"{manifest.relative_to(root)} references missing {question_id}")

            for claim_id in sorted(set(re.findall(r"\bC[0-9]{3}\b", text))):
                if claim_id not in claim_ids:
                    problems.append(f"{manifest.relative_to(root)} references missing {claim_id}")

            decision_value = manifest_data.get("decision")
            if decision_value and re.search(r"^D[0-9]{3}$", decision_value):
                if decision_value not in decision_ids:
                    problems.append(f"{manifest.relative_to(root)} references missing {decision_value}")

            if manifest_data.get("status") == "complete":
                runs = list((exp / "runs").glob("*.md"))
                if not runs:
                    problems.append(f"completed {exp.relative_to(root)} has no run records")
                if len(runs) >= 5:
                    exp_id = manifest_data.get("id", "")
                    synthesis_refs = [
                        path
                        for path in (root / "research-log").glob("*.md")
                        if exp_id and exp_id in path.read_text(errors="ignore")
                    ]
                    if not synthesis_refs:
                        problems.append(
                            f"completed {exp.relative_to(root)} has {len(runs)} run records "
                            f"but no synthesis note mentions {exp_id}"
                        )

    index_path = root / "experiments/index.yml"
    for entry in parse_index(index_path):
        exp_id = entry.get("id", "")
        folder = entry.get("folder", "")
        status = entry.get("status", "")
        question = entry.get("question", "")
        if not re.search(r"^E[0-9]{3}$", exp_id):
            problems.append(f"experiments/index.yml has invalid experiment id {exp_id!r}")
        if folder and not (root / folder).exists():
            problems.append(f"experiments/index.yml references missing folder {folder}")
        if exp_id and exp_id not in experiments_by_id:
            problems.append(f"experiments/index.yml references missing manifest id {exp_id}")
        if question and question not in question_ids:
            problems.append(f"experiments/index.yml references missing question {question}")
        for claim_id in re.findall(r"\bC[0-9]{3}\b", str(entry)):
            if claim_id not in claim_ids:
                problems.append(f"experiments/index.yml references missing claim {claim_id}")
        if status == "complete" and folder:
            runs_dir = root / folder / "runs"
            if not list(runs_dir.glob("*.md")):
                problems.append(f"completed index entry {exp_id} has no run records")

    decisions_text = (root / "DECISIONS.md").read_text(errors="ignore") if (root / "DECISIONS.md").exists() else ""
    active_decisions = 0
    for decision_id in sorted(decision_ids):
        line = line_for_id(decisions_text, decision_id)
        if line and "| active |" in line:
            active_decisions += 1
        if line:
            cells = markdown_table_cells(line)
            revisit_cell = cells[-1] if cells else ""
            if not revisit_cell or revisit_cell == "---":
                problems.append(f"{decision_id} appears to lack a revisit condition")

    if active_decisions > MAX_ACTIVE_DECISIONS:
        problems.append(
            f"DECISIONS.md has {active_decisions} active decisions; supersede or compress "
            f"below {MAX_ACTIVE_DECISIONS}"
        )

    index_entries = parse_index(index_path)
    running_experiments = [entry.get("id", "") for entry in index_entries if entry.get("status") == "running"]
    if len(running_experiments) > MAX_RUNNING_EXPERIMENTS:
        problems.append(
            "experiments/index.yml has too many running experiments "
            f"({', '.join(running_experiments)}); pause, complete, or supersede stale branches"
        )

    for rel, prefix in [
        ("OPEN_QUESTIONS.md", "Q"),
        ("CLAIMS.md", "C"),
        ("DECISIONS.md", "D"),
    ]:
        rows = markdown_table_rows_with_id(root / rel, prefix)
        if len(rows) > 40:
            problems.append(
                f"{rel} has {len(rows)} {prefix} rows; split old details into cards, "
                "synthesis notes, or superseded sections"
            )

    if problems:
        print("Research workspace validation failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(f"Research workspace validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
