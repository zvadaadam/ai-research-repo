# Agent Instructions

This repo is a research workspace. Treat it like a lab notebook with runnable
code, not like a normal app repo.

This repository is also intended to be used as a GitHub template. When working
in this repo directly, improve the scaffold, skills, templates, and tooling.
Put domain-specific research in child repos created from the template.

## Start Sequence

Before experiment or research-note work:

1. Read `.agents/skills/research-workspace/SKILL.md`.
2. Load the task-specific sub-skill when needed:
   - `research-experiment` for experiment cards, commands, run records.
   - `research-claims` for questions, claims, decisions.
   - `research-synthesis` for batch/branch compression.
   - `research-references` for paper cards and outside evidence.
   - `plan-research-goal` for turning a research agenda into a `/goal` prompt.
3. Read `RESEARCH.md`.
4. Read `OPEN_QUESTIONS.md`, `CLAIMS.md`, and `DECISIONS.md`.
5. Read the relevant experiment folder and `experiments/index.yml`.

## Research Objects

Use stable IDs:

```text
Q###  open question
H###  hypothesis
E###  experiment
R###  run
C###  claim
D###  decision
P###  paper/reference
```

Every serious experiment must link to at least one `Q###` and one `C###`
candidate claim. Every decision must say what evidence would make us revisit
it.

## Folder Rules

- Put reusable code under `src/`.
- Put runnable entry points under `scripts/`.
- Put generated local outputs under root-level `/artifacts/`, `/data/`,
  `/runs/`, `/checkpoints/`, or `/wandb/`; keep them out of git.
- Do commit experiment run records under
  `experiments/NNN_short_name/runs/*.md`; these are notebook evidence, not
  generated bulk outputs.
- Record external source snapshots as references. If copied code becomes part
  of the research surface, put it under `src/<source-name>/` and preserve the
  upstream URL or commit in a `P###` reference card.
- Do not turn the root README into a long experiment list.

## Template Setup

When this repo is used as a starter, keep the structure and replace only the
project-specific identity and first research thread:

- update `README.md` with the new project name and purpose;
- update `RESEARCH.md` with the initial thesis or active question;
- add the first `Q001` before creating `experiments/001_short_name/`;
- run `python3 tools/validate_research_workspace.py .`.

## Experiment Rules

Create:

```text
experiments/NNN_short_name/README.md
experiments/NNN_short_name/manifest.yml
experiments/NNN_short_name/notes.md
experiments/NNN_short_name/runs/YYYY-MM-DD_HHMM_short_name.md
```

Use `README.md` for the stable experiment card. Use `runs/` for concrete run
records. Use `notes.md` for scratch thinking.

After a run, update:

- `experiments/index.yml`
- the experiment `README.md`
- the run record under `runs/`
- `CLAIMS.md` if evidence supports/weakens a belief
- `OPEN_QUESTIONS.md` if a question is answered or sharpened
- `DECISIONS.md` if a decision changes
- `RESEARCH.md` if the dashboard or next step changes
- run `tools/validate_research_workspace.py`

## Evidence Discipline

Separate:

```text
fact: measured or directly observed
hypothesis: likely explanation
decision: what we will do because of it
```

Pretty artifacts are useful, but every visual result should be tied to a
predeclared metric or a clearly stated qualitative observation.

## Batch Synthesis

After roughly five serious experiments in a branch, write a synthesis note and
make one explicit continue/stop/pivot decision. Do not let a branch grow only
chronologically without compressing what is now believed.
