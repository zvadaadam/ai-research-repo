# Research Factory

This folder is the small operating layer above the evidence graph.

The evidence graph remembers what happened. The factory queue decides what to
try next, what not to try, and when a branch should stop.

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
