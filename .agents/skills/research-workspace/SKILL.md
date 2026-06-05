---
name: research-workspace
description: Route AI research workspace work across the evidence graph. Use for broad research tasks, choosing which research sub-skill applies, or updating the dashboard after experiment, claims, synthesis, or reference work.
---

# Research Workspace

## Role

This is the router skill. Use it first for broad research work, then load the
smallest sub-skill that matches the task:

- `research-experiment`: creating experiments, running commands, recording
  run evidence.
- `research-claims`: updating `OPEN_QUESTIONS.md`, `CLAIMS.md`, and
  `DECISIONS.md`.
- `research-synthesis`: batch/branch review after several experiments.
- `research-references`: paper cards and outside evidence.
- `plan-research-goal`: drafting a `/goal` prompt for autonomous research.

Keep this skill small. Detailed procedures live in the sub-skills.

## Read Order

1. `RESEARCH.md`
2. `OPEN_QUESTIONS.md`
3. `CLAIMS.md`
4. `DECISIONS.md`
5. `experiments/index.yml`
6. relevant experiment folders

## Evidence Graph

```text
Q question -> H hypothesis -> E experiment -> R run -> C claim -> D decision
```

## Quality Bar

Each experiment should make one of these moves:

- answer a question;
- falsify a hypothesis;
- strengthen/weaken a claim;
- expose a blocker;
- choose the next sharper experiment.

If none of those happened, record it as a scratch run, not a serious
experiment.

## Always Do

- Keep `RESEARCH.md` short.
- Never use the root README as an experiment ledger.
- Separate facts, hypotheses, and decisions.
- Prefer linked evidence IDs over narrative memory.
- Run `tools/validate_research_workspace.py` after structural changes.

## Periodic Compression

After about five serious experiments in a branch, use `research-synthesis`.
The branch should get an explicit continue/stop/pivot decision.
