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
    ".agents/skills/plan-research-goal/SKILL.md",
    "experiments/index.yml",
]


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


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    problems: list[str] = []

    for rel in REQUIRED_ROOT:
        if not (root / rel).exists():
            problems.append(f"missing {rel}")

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
    for decision_id in sorted(decision_ids):
        line = next((l for l in decisions_text.splitlines() if decision_id in l and "|" in l), "")
        if line and ("|" not in line.strip("|").split("|")[-1].strip()):
            revisit_cell = line.strip().split("|")[-2].strip() if line.endswith("|") else line.strip().split("|")[-1].strip()
            if not revisit_cell or revisit_cell == "---":
                problems.append(f"{decision_id} appears to lack a revisit condition")

    if problems:
        print("Research workspace validation failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(f"Research workspace validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
