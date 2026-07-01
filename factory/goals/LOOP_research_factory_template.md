# LOOP: Research Factory Template

Objective: run the research factory continuously until the active thesis is
credibly supported, falsified, or blocked by a documented external constraint.

Research taste: prefer decisive evidence over activity. Every cycle should
pressure a claim, answer or sharpen a question, expose a blocker, or choose the
next sharper experiment. Do not treat local progress, nice artifacts, or one
successful run as the end of the research program.

Notebook rules: keep `RESEARCH.md`, `OPEN_QUESTIONS.md`, `CLAIMS.md`,
`DECISIONS.md`, `experiments/index.yml`, `factory/queue.yml`, the relevant
experiment cards, run records, scorecards, and goal prompts synchronized.
Record exact commands, metrics, artifact paths, failed-run notes, and facts vs
hypotheses. Run `python3 tools/validate_research_workspace.py .` after
structural or belief updates.

Loop contract:

1. Read the dashboard, questions, claims, decisions, experiment index, queue,
   and latest relevant experiment/run records.
2. Select the highest-information next experiment from the evidence graph. If
   it is not obvious, use `research-director` to update a scorecard and
   `factory/queue.yml`.
3. Create or update the experiment card, manifest, notes, run record, and goal
   prompt before spending serious compute.
4. Run or monitor the experiment with bounded commands, durable logs, metrics,
   and artifact paths.
5. Update claims, questions, decisions, the dashboard, experiment index, queue,
   and run record from the evidence.
6. After about five serious experiments or any direction-changing result, write
   a synthesis note and make an explicit continue/stop/pivot decision.
7. Choose the next decisive experiment and continue the loop.

Turn exit rule: before ending any turn, leave the project with one of: an
active monitored run, a selected next experiment with scorecard and goal, or a
documented hard blocker plus the smallest repair/audit that should run next.

Stop only when: the thesis-level evidence target is met, the thesis is
falsified strongly enough to stop the branch, or an external blocker prevents
the smallest next repair after being documented with exact commands and paths.

Not done when: one experiment completes, one useful artifact exists, a synthesis
note is written, a local metric improves, or the queue merely has a plausible
next item.

Not: broad sweeps without a decision gate, unrecorded generated artifacts,
claims without linked evidence, or starting new branches from vibes.

Where to look: the evidence graph files, `factory/`, relevant `experiments/`,
`research-log/`, `references/`, `papers/`, and durable artifact summaries.
