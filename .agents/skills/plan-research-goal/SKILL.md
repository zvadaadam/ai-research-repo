---
name: plan-research-goal
description: Turn a research agenda into one cold-readable `/goal` prompt for autonomous AI research loops, with evidence-graph notebook rules, experiment cadence, verification, scope edges, and either a finite Done condition or a continuous factory-loop contract.
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

## Goal Type

Choose the goal shape from the user's intent:

- **Finite experiment goal**: default. Use when the user asks for one
  experiment, one branch segment, a smoke test, a repair, a comparison, or a
  specific scorecard candidate.
- **Continuous factory loop**: use only when the user explicitly asks to keep a
  research program running, to loop indefinitely, to keep choosing next
  experiments, or to continue until a major research thesis is settled.

Do not blur these shapes. A finite goal should stop cleanly. A continuous loop
should not stop after a successful experiment, a useful synthesis, or "some
progress."

## What To Produce For A Finite Goal

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

If `factory/scorecards/` already contains a selected candidate, preserve its
stop/pivot gate and "Not next" list in the goal prompt.

## What To Produce For A Continuous Factory Loop

Write one `/goal` prompt under 4000 characters with these anchors:

- **Objective**: the major research state that would make the whole loop worth
  stopping.
- **Research Taste**: two or three vivid sentences about the evidence bar.
- **Notebook Rules**: which evidence files must stay synchronized every cycle.
- **Loop Contract**: a numbered cycle for choosing, running, recording,
  validating, synthesizing, and selecting the next experiment.
- **Turn Exit Rule**: before any turn ends, the agent must have one of:
  an active/monitored run, a selected next experiment with scorecard and goal,
  or a documented hard blocker with a smallest repair.
- **Batch Synthesis**: after about five serious experiments, update
  claims/questions/decisions and make a continue/stop/pivot decision.
- **Stop Only When**: the full research thesis is credibly supported,
  falsified, or blocked by a documented external constraint.
- **Not Done When**: list the common false stops, such as one completed
  experiment, one useful artifact, one synthesis note, or a local improvement.
- **Not:** adjacent temptations.
- **Where To Look**: durable zones, not brittle line numbers.

Name continuous loop prompts by the research end-state, not by the first
experiment. Prefer names like `LOOP_<program>_research_factory.md` or a title
starting with `LOOP:`, for example `LOOP: NAC + Le-WM SOTA Evidence Factory`.

## Research-Specific Guidance

The prompt should make the agent skeptical and productive. Prefer a small chain
of decisive experiments over a broad sweep. Require exact commands, metrics,
artifact paths, failed-run notes, and interpretation that separates facts from
hypotheses.

Require branch synthesis after about five serious experiments or when a result
changes direction. The synthesis must update claims/questions/decisions, not
only summarize chronology.

## Goal Shape

For finite goals: one goal, one branch, one stopping condition. If the agenda
contains multiple research programs, split it and write the first goal only.

For continuous factory loops: one goal, one research program, one thesis-level
stop condition, many experiment cycles. The loop must keep selecting the next
highest-information experiment after each cycle until the thesis-level stop
condition is met.

Avoid step-by-step implementation recipes unless the user explicitly requires
them.

## Output Protocol

Cold-read the prompt before showing it. Measure it with `wc -m` and state the
character count. Then show only the final prompt in one fenced code block so it
can be pasted straight into `/goal`.
