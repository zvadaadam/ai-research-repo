# BATCH: Experiment Sprint Template

Objective: run a bounded batch of related experiments that can decide one
research question, pressure one claim, or choose the next branch direction.

Research taste: the batch should be small enough to finish and rich enough to
change belief. Prefer two to five decisive experiments over a broad sweep. Each
run must either answer/sharpen a question, strengthen/weaken a claim, expose a
blocker, or choose the next sharper test.

Notebook rules: after every run, update the relevant experiment card, run
record, `experiments/index.yml`, `factory/queue.yml`, `RESEARCH.md`,
`OPEN_QUESTIONS.md`, `CLAIMS.md`, and `DECISIONS.md` if evidence changes
beliefs. Record exact commands, metrics, artifact paths, failed-run notes, and
facts vs hypotheses. Run `python3 tools/validate_research_workspace.py .`
after structural or belief updates.

Batch plan:

1. Read the dashboard, live questions, claims, decisions, queue, scorecards,
   and relevant experiment/run records.
2. Select two to five related experiments with one shared decision pressure.
   If the batch is not obvious, use `research-director` to rank candidates and
   document what should not run in this batch.
3. For each experiment, create or update the card, manifest, run record,
   artifact plan, and stop/pivot gate before running.
4. Run or monitor each experiment with durable logs and metrics.
5. Update the evidence graph after each experiment, not only at the end.
6. Write one synthesis note that compresses the batch into lessons, claim
   updates, and an explicit continue/stop/pivot recommendation.

Done = all planned batch experiments are recorded or explicitly skipped with
reasons, the workspace validates, and the synthesis chooses the next single,
batch, or continuous goal.

Not: adding unrelated experiments mid-batch, running broad sweeps without a
decision gate, waiting until the end to update notebook files, or continuing
past the synthesis without a new goal.

Where to look: the evidence graph files, `factory/`, relevant `experiments/`,
`research-log/`, and durable artifact summaries.
