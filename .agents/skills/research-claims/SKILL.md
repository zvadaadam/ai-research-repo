---
name: research-claims
description: Maintain the research workspace belief layer: open questions, claims, decisions, confidence levels, evidence links, and revisit conditions.
---

# Research Claims

Use when interpreting evidence, updating beliefs, closing questions, or changing
research direction.

## Files

- `OPEN_QUESTIONS.md`: uncertainties ranked by information gain.
- `CLAIMS.md`: compressed belief state.
- `DECISIONS.md`: choices that change future behavior.
- `RESEARCH.md`: short dashboard summary.

## Claim Rules

- No claim without evidence IDs.
- No high confidence without multiple converging runs or one decisive blocker.
- Every claim needs an implication.
- Use statuses: `supported`, `weakened`, `mixed`, `superseded`, `unknown`.
- Use confidence: `low`, `medium`, `high`.

## Question Rules

Each `Q###` should have:

- measurable answer;
- next experiment or reason it is paused;
- related claims;
- status: `open`, `answered`, `paused`, or `superseded`.

## Decision Rules

A decision changes future behavior. Every `D###` needs:

- rationale;
- evidence;
- revisit condition.

Do not create a decision for every run. Create one when the next branch changes,
when a path stops, or when a default practice changes.

## Update Pattern

After evidence:

```text
facts -> claim status/confidence -> question status -> decision if behavior changes
```

Then update the `RESEARCH.md` evidence snapshot if the current thesis changes.
