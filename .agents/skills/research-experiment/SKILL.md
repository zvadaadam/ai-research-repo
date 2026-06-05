---
name: research-experiment
description: Create, run, and record AI research experiments with manifests, run records, artifact paths, metrics, and experiment index updates.
---

# Research Experiment

Use when starting or updating an experiment, running a training/eval command, or
recording metrics/artifacts.

## Before A Serious Run

- Reuse or create a `Q###` in `OPEN_QUESTIONS.md`.
- Name the falsifiable `H###`.
- Name the primary metric before seeing results.
- Create/update:

```text
experiments/NNN_short_name/README.md
experiments/NNN_short_name/manifest.yml
experiments/NNN_short_name/notes.md
experiments/index.yml
```

- Put generated outputs under ignored `artifacts/` or `data/`.

## Run Record

After a command, write:

```text
experiments/NNN_short_name/runs/YYYY-MM-DD_HHMM_short_name.md
```

Prefer `tools/create_run_record.py` when a `summary.json` exists. It drafts the
run from the manifest, command, and metrics, reducing notebook tax.

## Required Evidence

Every completed serious experiment needs:

- command;
- dataset and split;
- artifact path;
- metrics;
- interpretation with facts separated from hypotheses;
- claim updates or a statement that no claim changed;
- next step.

## Status Vocabulary

`planned`, `running`, `complete`, `failed`, `paused`, `superseded`.

## Do Not

- Bury important results only in stdout.
- Use visual artifacts without saying what to inspect.
- Change multiple major variables unless the experiment is explicitly a sweep.
