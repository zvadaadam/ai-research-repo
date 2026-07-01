# Research Factory

This folder is the small operating layer above the evidence graph.

The evidence graph remembers what happened. The factory queue decides what to
try next, what not to try, and when a branch should stop or keep looping.

Use this layer when a project has more possible experiments than attention or
compute.

## Files

- `queue.yml`: ranked candidate experiments and goal prompts.
- `scorecards/`: one-page rationale for why a candidate deserves a run.
- `goals/`: cold-readable `/goal` prompts for autonomous research loops.
- `audits/`: periodic checks for bloat, stale branches, and weak evidence.

## Factory Rule

Before a new autonomous goal loop starts, write down:

```text
why this experiment now
what should not be run next
what result would stop or pivot the branch
```

If those are unclear, use the `research-director` skill before spending
experiment time.

## Goal Shapes

Use a single experiment goal when the next unit of work is one experiment,
smoke test, repair, comparison, or scorecard candidate. It should have a
concrete `Done = ...` condition and stop when that evidence is recorded.

Use a batch experiment goal when the next unit of work is a bounded sprint of
two to five related experiments. It should update evidence after every run,
then stop after a synthesis note chooses the next single, batch, or continuous
goal.

Use a continuous factory-loop goal only when the intent is to keep the research
program running across many experiment cycles. It should not stop after one
experiment or one synthesis note. It stops only when the thesis-level evidence
target is reached, the thesis is falsified, or a documented external blocker
prevents the next smallest repair.
