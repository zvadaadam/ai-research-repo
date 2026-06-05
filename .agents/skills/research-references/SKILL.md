---
name: research-references
description: Add or update research paper cards, reference notes, external repo links, and evidence links from papers to claims and experiments.
---

# Research References

Use when adding papers, external repos, datasets, benchmark docs, or reference
notes.

## Reference Objects

Use `P###` IDs for external evidence. Prefer concise paper cards over loose
links.

```text
references/paper-cards/P001_short_name.md
```

## Paper Card Must Say

- source;
- status: `unread`, `skimmed`, `read`, `implemented`, or `superseded`;
- core claim;
- method details we need;
- caveats/assumptions;
- related local claims;
- related experiments it motivates.

## Evidence Discipline

Papers support hypotheses; local experiments decide project claims. When a
paper changes a claim, link both the paper ID and the local experiment/blocker
that makes it relevant.
