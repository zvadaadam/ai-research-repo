# AI Research Repo

This is a clean research-repo scaffold for long-running AI experiments.

The core idea is an evidence graph:

```text
question -> hypothesis -> experiment/run -> evidence -> claim -> decision -> next question
```

Do not use the root README as an experiment ledger. The README is only a map.
The live research state lives in:

- `RESEARCH.md`: current dashboard and next move.
- `OPEN_QUESTIONS.md`: ranked uncertainties.
- `CLAIMS.md`: what the project currently believes, with evidence links.
- `DECISIONS.md`: choices we have committed to, with revisit conditions.
- `experiments/index.yml`: compact machine-readable experiment index.
- `research-log/`: durable observations and explanations.

## Repo Map

```text
.agents/skills/        project skill for coding/research agents
docs/                  research-system docs and review checklists
experiments/           numbered experiment folders plus index.yml
research-log/          durable notes that survive one run
references/            paper cards, PDFs, external repos
src/                   reusable research code
scripts/               runnable entry points
tools/                 small validators and maintenance helpers
artifacts/             generated outputs, ignored by git
data/                  generated/local datasets, ignored by git
```

## First Rule

Every serious experiment must answer:

```text
What question does this answer?
What claim could this change?
What evidence did it produce?
What should happen next?
```

If it cannot answer those, it is a scratch run, not a research experiment.
