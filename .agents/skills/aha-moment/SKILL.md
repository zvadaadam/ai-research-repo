---
name: aha-moment
description: Capture personal "now it clicked" learning notes in AHA/ when the user says a concept clicked, asks to remember an explanation, or wants a durable note of what they did not understand and what they learned.
---

# Aha Moment

Use this when the user says a concept clicked, asks to remember an explanation,
or wants to store a personal learning snapshot for later rereading.

This is not an experiment run record and not a formal research claim. It is a
personal understanding note.

## Destination

Write notes under:

```text
AHA/YYYY-MM-DD_short_slug.md
```

If `AHA/README.md` does not exist, create it with a short purpose statement and
an index.

## Required Shape

Each note should include:

```text
# Short Concept Name

- Date: YYYY-MM-DD
- Related research: `E###`, `C###`, `P###` or none
- Status: clicked | open | needs-follow-up

## What I Did Not Understand

Synthesize the user's confusion from their questions. Prefer the user's mental
framing over textbook wording, but clean up typos.

## What I Was Asking

State the underlying question in one concise block.

## What Clicked

Preserve the explanation, analogy, diagram, CLI visual, or wording that made it
land.

## The Clean Mental Model

The reusable version of the idea.

## Next Time I Forget

The shortest reminder that can restore the understanding.
```

## Writing Rules

- Start with the confusion, not the answer.
- Make it tailored to the user's actual questions.
- Use first person when describing the confusion if that helps future recall.
- Include ASCII diagrams when they were part of the click.
- Keep it concise enough to reread quickly.
- Do not put aha notes in `research-log/`.
- Update `AHA/README.md` with a link to the new note.

If the aha changes the research state, separately update `CLAIMS.md`,
`OPEN_QUESTIONS.md`, `DECISIONS.md`, or an experiment record using the relevant
research skill.
