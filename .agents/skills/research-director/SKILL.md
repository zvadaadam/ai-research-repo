---
name: research-director
description: Rank candidate experiments, decide what not to run next, maintain the factory queue, and choose one decisive next research goal before autonomous loops spend compute.
---

# Research Director

Use when choosing the next research direction, starting a new `/goal` loop,
reviewing a branch after surprising evidence, or asking whether the research
workspace is still moving toward the right objective.

This skill does not replace `research-experiment`; it decides which experiment
deserves to be created or run.

## Read First

1. `RESEARCH.md`
2. `OPEN_QUESTIONS.md`
3. `CLAIMS.md`
4. `DECISIONS.md`
5. `experiments/index.yml`
6. `factory/queue.yml`
7. the latest relevant synthesis note under `research-log/`

## Output Shape

Produce one ranked shortlist, then choose exactly one next move.

```text
1. candidate
   expected information gain:
   cost:
   risk of fooling ourselves:
   what it would prove:
   what it would not prove:

Selected next move:
Not next:
Stop/pivot gate:
```

## Factory Queue

When a candidate is selected, update or create:

```text
factory/scorecards/F###_short_name.md
factory/queue.yml
```

If the next move is ready for autonomous execution, use `plan-research-goal`
after this skill and store the prompt in `factory/goals/`.

## Taste

- Prefer one decisive experiment over a broad sweep.
- Prefer tests that can falsify the current favorite idea.
- Penalize experiments that only rename a failed mechanism.
- Do not promote a result until it survives the stress test implied by its
  own failure mode.
- Name what should not be run next; this is part of the output, not a footnote.

## Anti-Bloat Rule

If `RESEARCH.md`, `CLAIMS.md`, or `DECISIONS.md` have become long ledgers,
choose `compress before more experiments` as the next move. The factory should
not spend compute while the belief layer is unreadable.
