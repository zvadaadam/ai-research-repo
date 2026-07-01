# Factory Goals

Store cold-readable `/goal` prompts here when a research loop is ready to run.

There are three valid shapes:

- single experiment goals, usually named `G###_short_name.md`;
- batch experiment goals, named by the evidence decision, such as
  `BATCH_<theme>_experiments.md`;
- continuous factory-loop goals, named by the desired research end-state, such
  as `LOOP_<program>_research_factory.md`.

Each prompt should stand alone without chat history and should name:

- objective;
- evidence files to keep synchronized;
- experiment loop;
- verification command;
- scope edges;
- done condition for single goals, synthesis stop for batch goals, or
  stop-only/turn-exit rules for continuous loops.

A batch goal should run a bounded set of related experiments, update evidence
after each run, then write a synthesis note that chooses the next single,
batch, or continuous goal. It is not a forever loop.

A continuous loop goal must include a contract that after every serious run the
agent updates evidence, validates the workspace, synthesizes when the batch is
large enough, selects the next highest-information experiment, and continues.
It is not done when it merely records one run, writes one useful artifact, or
makes some progress.

Use `plan-research-goal` to draft the prompt, ideally after `research-director`
has ranked the candidate experiments.
