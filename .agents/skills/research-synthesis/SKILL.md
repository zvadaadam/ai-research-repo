---
name: research-synthesis
description: Compress an AI research experiment batch or branch into lessons, updated claims/questions, and a continue/stop/pivot decision.
---

# Research Synthesis

Use after about five serious experiments, at branch end, or when the user asks
what the research has learned.

## Inputs

Read only what is needed:

- `RESEARCH.md`
- `experiments/index.yml`
- relevant experiment run records
- affected `CLAIMS.md`, `OPEN_QUESTIONS.md`, `DECISIONS.md`
- artifact summaries if claims depend on exact metrics

## Synthesis Questions

Answer:

- What did this branch test?
- What facts are now established?
- Which hypotheses failed?
- Which claim changed most?
- What should stop?
- What should continue?
- What is the next sharper question?

## Required Output

Update or create:

- a `research-log/YYYY-MM-DD-branch-synthesis.md` note;
- `CLAIMS.md`;
- `OPEN_QUESTIONS.md`;
- `DECISIONS.md` with one continue/stop/pivot decision if behavior changes;
- `RESEARCH.md` dashboard.

## Discipline

Prefer one strong conclusion over many loose observations. Mark stale claims or
questions `superseded` instead of leaving them quietly misleading.
