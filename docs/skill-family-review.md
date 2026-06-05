# Skill Family Review

This note records why this scaffold uses multiple project skills.

## What We Learned From The First Scaffold Iteration

The first single research skill was directionally good, but it mixed
four different jobs:

```text
experiment execution
belief/claim maintenance
branch synthesis
paper/reference handling
```

Those jobs have different failure modes. Experiment work needs concrete
manifest/run-record mechanics. Claim work needs epistemic discipline. Synthesis
needs compression and stop/continue/pivot decisions. Reference work needs paper
cards and caveats.

## New Shape

```text
research-workspace    router and shared evidence-graph rules
research-experiment   experiment cards, commands, manifests, run records
research-claims       open questions, claims, decisions
research-synthesis    batch/branch compression
research-references   paper cards and external evidence
plan-research-goal    `/goal` prompt planning for autonomous research loops
```

This follows progressive disclosure: future agents load only the skill needed
for the task.

## Tooling Added

- `tools/create_run_record.py` drafts a run record from a manifest, command,
  and `summary.json`.
- `tools/validate_research_workspace.py` now checks required skills, completed
  experiment run records, index folders, question links, claim links, and
  decision links.

## Remaining Risk

Too many skills can become their own navigation problem. The router skill must
stay short, and sub-skills should stay focused. If agents repeatedly open every
skill for every task, merge or simplify.

## Verdict

The skill family is better than one monolithic skill for long-running AI
research workload, but it should stay boring: the router stays short, the
sub-skills stay focused, and experiment-specific lessons belong in experiment
folders or `research-log/`, not in this scaffold note.
