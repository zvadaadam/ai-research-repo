# Research System

This repo uses a two-layer notebook.

## Layer 1: Evidence

Evidence is concrete:

- experiment cards;
- run records;
- metrics files;
- plots and visuals;
- paper cards.

Evidence should be reproducible and boring.

## Layer 2: Belief

Belief is compressed:

- claims;
- decisions;
- open questions;
- current dashboard.

Belief should be easy to inspect and easy to revise.

## Layer 3: Factory

The factory layer chooses what to run next:

- scorecards;
- ranked queue;
- goal prompts;
- audits.

Factory state should be small. It should say why the next experiment is worth
running and what should not be run next.

Factory goals come in two shapes. A finite experiment goal should stop when one
evidence-producing unit is recorded. A continuous factory-loop goal should keep
selecting, running, recording, validating, and synthesizing experiments until a
thesis-level evidence target is reached, falsified, or externally blocked.

## Anti-Pattern

Avoid one giant chronological diary where every file is equally important.
That creates memory but not judgment.

## Good Pattern

After every serious run, ask:

```text
Did this support or weaken a claim?
Did this answer or sharpen a question?
Did this change a decision?
What would change our mind next?
```

If the answer is "no," the run may still be useful, but it should not dominate
the research state.

## Skill Family

The repo uses a small skill family instead of one large instruction file:

- `research-workspace`: router and shared rules.
- `research-experiment`: experiment/run mechanics.
- `research-claims`: questions, claims, decisions.
- `research-synthesis`: branch compression after a batch.
- `research-references`: paper cards and external evidence.
- `research-director`: next-experiment ranking and factory queue maintenance.
- `plan-research-goal`: `/goal` prompt planning for autonomous research loops.

This keeps routine experiment work from loading synthesis or reference details
unless they are needed.
