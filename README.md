# AI Research Repo

This is a clean research-repo scaffold for long-running AI experiments. It is
meant to be used as a **GitHub template repository**: start new research repos
from it, then do the actual research in the child repo.

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
- `factory/queue.yml`: ranked next-experiment candidates and goal loop queue.
- `AHA/`: personal "now it clicked" learning notes.
- `research-log/`: durable observations and explanations.

## Repo Map

```text
.agents/skills/        project skill for coding/research agents
.github/workflows/     structural validation in GitHub Actions
docs/                  research-system docs and review checklists
experiments/           numbered experiment folders plus index.yml
AHA/                   personal aha notes and remembered explanations
research-log/          durable notes that survive one run
references/            paper cards, external repo notes, evidence summaries
papers/                source PDFs and primary paper artifacts
factory/               ranked candidates, goal prompts, and research audits
src/                   reusable research code
scripts/               runnable entry points
tools/                 small validators and maintenance helpers
artifacts/             generated outputs, ignored by git
data/                  generated/local datasets, ignored by git
```

## Start A New Research Repo

Preferred path:

```bash
gh repo create OWNER/NEW_RESEARCH_REPO \
  --template zvadaadam/ai-research-repo \
  --private \
  --clone
```

Use `--public` instead of `--private` when the new research should be open.
You can also click **Use this template** on GitHub.

Example:

```bash
gh repo create zvadaadam/imaginator-v2 \
  --template zvadaadam/ai-research-repo \
  --private \
  --clone
```

After cloning the new repo:

1. Change the title and one-sentence purpose in `README.md`.
2. Update `RESEARCH.md` with the first thesis or active question.
3. Add the first `Q001` to `OPEN_QUESTIONS.md`.
4. Copy `experiments/_template/` to `experiments/001_short_name/`.
5. Use `factory/scorecards/_template.md` before launching a long-running goal.
6. Run `python3 tools/validate_research_workspace.py .`.

Generated data, checkpoints, videos, and metrics stay under ignored root
folders such as `/data/` and `/artifacts/`. Experiment run records under
`experiments/*/runs/*.md` are evidence and should be committed.

## First Rule

Every serious experiment must answer:

```text
What question does this answer?
What claim could this change?
What evidence did it produce?
What should happen next?
```

If it cannot answer those, it is a scratch run, not a research experiment.

## Factory Layer

The factory layer is intentionally small. It exists to choose the next best
experiment before an autonomous loop spends time or compute.

Use it when there are multiple plausible next moves:

```text
research-director -> scorecard -> factory/queue.yml -> plan-research-goal
```

The most useful line in a scorecard is often "What not to run next." A research
factory should reduce thrash, not only remember more.
