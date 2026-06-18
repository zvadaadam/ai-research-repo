#!/usr/bin/env python3
"""Draft a research run record from a manifest, command, and summary JSON."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


def parse_manifest(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw in path.read_text(errors="ignore").splitlines():
        line = raw.strip()
        if ":" not in line or line.startswith("#") or line.startswith("-"):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment-dir", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--command", help="Command text. Prefer --command-file for long commands.")
    parser.add_argument("--command-file")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--commit", default="pending local working tree")
    parser.add_argument("--status", default="complete")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def scalar_metric(value: object) -> bool:
    return value is None or isinstance(value, (str, int, float, bool))


def flatten_metrics(data: dict, *, prefix: str = "", max_lines: int = 80) -> list[str]:
    lines: list[str] = []
    for key, value in data.items():
        name = f"{prefix}.{key}" if prefix else str(key)
        if scalar_metric(value):
            if isinstance(value, float):
                lines.append(f"{name}: {value:.6f}")
            else:
                lines.append(f"{name}: {value}")
        elif isinstance(value, dict):
            lines.extend(flatten_metrics(value, prefix=name, max_lines=max_lines))
        if len(lines) >= max_lines:
            lines.append("... truncated metric draft; inspect summary.json for full details")
            return lines[: max_lines + 1]
    return lines


def metric_lines(summary: dict) -> list[str]:
    metrics = (
        summary.get("final_metrics")
        or summary.get("overall")
        or summary.get("key_results", {}).get("overall")
        or summary
    )
    lines = flatten_metrics(metrics)
    if "parameters" in summary and "parameters" not in metrics:
        lines.append(f"parameters: {summary['parameters']}")
    if "runtime_seconds" in summary and "runtime_seconds" not in metrics:
        lines.append(f"runtime_seconds: {summary['runtime_seconds']:.2f}")
    return lines


def main() -> int:
    args = parse_args()
    exp_dir = Path(args.experiment_dir)
    manifest = parse_manifest(exp_dir / "manifest.yml")
    summary_path = Path(args.summary)
    summary = json.loads(summary_path.read_text())
    command = args.command or ""
    if args.command_file:
        command = Path(args.command_file).read_text().strip()
    if not command:
        raise SystemExit("provide --command or --command-file")

    date = datetime.now().strftime("%Y-%m-%d_%H%M")
    out = exp_dir / "runs" / f"{date}_{args.name}.md"
    artifact_path = summary.get("config", {}).get("out_dir") or summary_path.parent
    dataset = manifest.get("dataset") or summary.get("dataset") or "unknown"
    metrics = "\n".join(metric_lines(summary))

    text = f"""# Run {args.run_id}

- Date: {datetime.now().strftime("%Y-%m-%d")}
- Experiment: `{manifest.get("id", "E###")}`
- Commit: {args.commit}
- Command:

```bash
{command}
```

- Dataset: {dataset}
- Split: see `summary.json`
- Artifact path: `{artifact_path}`
- Status: {args.status}

## Metrics

```text
{metrics}
```

## Visual / Qualitative Evidence

- Artifact: `{summary.get("artifacts", {}).get("sample_predictions", "TBD")}`
- Observation: TBD

## Interpretation

Facts:

- TBD

Hypotheses:

- TBD

## Claim Updates

- TBD

## Next Step

- TBD
"""

    if args.dry_run:
        print(text)
        return 0
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
