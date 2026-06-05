---
name: plan-research-goal
description: Turn a research agenda into one cold-readable `/goal` prompt for autonomous AI research loops, with evidence-graph notebook rules, experiment cadence, verification, scope edges, and a clear Done condition.
argument-hint: "[optional: research agenda, hypothesis, or constraints]"
---

# Plan Research Goal

Craft one prompt to hand to a coding agent's `/goal` loop when the work is
research, not a normal feature ticket. The prompt is re-injected on every turn,
so it must stand alone without conversation memory.

## Topic

$ARGUMENTS

## Read First

Use the current conversation, then inspect the research workspace enough to
understand the dashboard, open questions, claims, decisions, experiment index,
and relevant experiment/reference areas. If the repo has the standard scaffold,
honor its evidence graph:

```text
Q question -> H hypothesis -> E experiment -> R run -> C claim -> D decision
```

## What To Produce

Write one `/goal` prompt under 4000 characters with these anchors:

- **Objective**: the research state that should be true when the loop stops.
- **Research Taste**: two or three vivid sentences about the quality bar.
- **Notebook Rules**: which evidence files must stay synchronized.
- **Experiment Loop**: how the agent should choose, run, compare, and synthesize
  experiments without sprawling.
- **Close The Loop**: concrete verification commands, artifact expectations,
  and what counts as real evidence.
- **Scope Edges**: include a `Not:` list for adjacent temptations.
- **Where To Look**: durable zones, not brittle line numbers.
- **Done = ...**: one boolean completion condition.

## Research-Specific Guidance

The prompt should make the agent skeptical and productive. Prefer a small chain
of decisive experiments over a broad sweep. Require exact commands, metrics,
artifact paths, failed-run notes, and interpretation that separates facts from
hypotheses.

Require branch synthesis after about five serious experiments or when a result
changes direction. The synthesis must update claims/questions/decisions, not
only summarize chronology.

## Goal Shape

One goal, one branch, one stopping condition. If the agenda contains multiple
research programs, split it and write the first goal only. Avoid step-by-step
implementation recipes unless the user explicitly requires them.

## Output Protocol

Cold-read the prompt before showing it. Measure it with `wc -m` and state the
character count. Then show only the final prompt in one fenced code block so it
can be pasted straight into `/goal`.
