# Research Repo Review Checklist

Use this after every batch of experiments.

## Navigation

- Can a new researcher find the current thesis in under one minute?
- Can they find the next experiment in under one minute?
- Can they find the evidence for the most important claim?

## Reproducibility

- Does every serious run have a command?
- Does every serious run name the dataset and split?
- Are artifact paths recorded and ignored by git?
- Is the primary metric named before interpretation?

## Epistemics

- Are facts separated from hypotheses?
- Are negative results preserved?
- Are stale claims marked `superseded` instead of silently forgotten?
- Does each decision have a revisit condition?
- Does every claim cite concrete evidence IDs?
- Has the branch had a synthesis note after about five serious experiments?

## Scope

- Is reusable code in `src/` instead of growing forever in scripts?
- Are references summarized as paper cards?
- Is the dashboard short enough to stay useful?
- Can `tools/create_run_record.py` draft run records from artifacts instead of
  making agents rewrite boilerplate?
