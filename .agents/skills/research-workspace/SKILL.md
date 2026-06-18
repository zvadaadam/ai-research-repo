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
- `research-director`: rank next experiments, decide what not to run, and
  update `factory/queue.yml`.
- `plan-research-goal`: drafting a `/goal` prompt for autonomous research.
- `aha-moment`: personal "now it clicked" notes in `AHA/`.

Keep this skill small. Detailed procedures live in the sub-skills.

## Read Order

1. `RESEARCH.md`
2. `OPEN_QUESTIONS.md`
3. `CLAIMS.md`
4. `DECISIONS.md`
5. `experiments/index.yml`
6. `factory/queue.yml`
7. relevant experiment folders

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
- Keep the live belief files compressed enough to inspect quickly.
- Never use the root README as an experiment ledger.
- Separate facts, hypotheses, and decisions.
- Prefer linked evidence IDs over narrative memory.
- When a concept clicks for the user, load `aha-moment` and capture it in
  `AHA/`.
- Run `tools/validate_research_workspace.py` after structural changes.

## Periodic Compression

After about five serious experiments in a branch, use `research-synthesis`.
The branch should get an explicit continue/stop/pivot decision.

Before starting a new autonomous `/goal` loop, use `research-director` if the
next experiment is not already a direct consequence of the latest decision.
