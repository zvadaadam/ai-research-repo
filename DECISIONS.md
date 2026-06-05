# Decisions

Decisions record what the project will do because of evidence. They should be
few, explicit, and reversible when possible.

| ID | Date | Status | Decision | Rationale | Evidence | Revisit If |
| --- | --- | --- | --- | --- | --- | --- |
| `D001` | 2026-06-05 | active | Use an evidence graph instead of long duplicated README ledgers. | Long-running research needs linked claims/questions more than chronological lists. | repo-design review | Researchers cannot answer "what do we believe now?" in under five minutes. |
| `D002` | 2026-06-05 | active | Split the research workflow into a router skill plus focused experiment, claims, synthesis, and references skills. | Different research jobs need different instructions; one large skill would either be vague or too costly to load. | `docs/skill-family-review.md` | Agents cannot find the right procedure or the skill family becomes harder to maintain than one file. |
| `D003` | 2026-06-05 | active | Commit experiment run records, but ignore only root-level generated run folders. | Run records under `experiments/*/runs/*.md` are durable notebook evidence, while root-level `/runs/` is for generated local output. | scaffold gitignore review | Experiment run records become bulky generated logs rather than concise evidence files. |

## Decision Rules

A decision is not a thought. It changes future behavior.

Every decision needs:

- rationale;
- evidence;
- revisit condition.
