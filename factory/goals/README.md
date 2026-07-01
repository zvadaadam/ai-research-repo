# Factory Goals

Store cold-readable `/goal` prompts here when a research loop is ready to run.

There are two valid shapes:

- finite experiment goals, usually named `G###_short_name.md`;
- continuous factory-loop goals, named by the desired research end-state, such
  as `LOOP_<program>_research_factory.md`.

Each prompt should stand alone without chat history and should name:

- objective;
- evidence files to keep synchronized;
- experiment loop;
- verification command;
- scope edges;
- done condition for finite goals, or stop-only/turn-exit rules for continuous
  loops.

A continuous loop goal must include a contract that after every serious run the
agent updates evidence, validates the workspace, synthesizes when the batch is
large enough, selects the next highest-information experiment, and continues.
It is not done when it merely records one run, writes one useful artifact, or
makes some progress.

Use `plan-research-goal` to draft the prompt, ideally after `research-director`
has ranked the candidate experiments.
