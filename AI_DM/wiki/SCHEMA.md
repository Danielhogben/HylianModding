# Wiki Schema

## Domain
**Silicon Life** — The science, engineering, and philosophy of creating sentient artificial beings. Covers consciousness, sentience, self-awareness, model training, neural architectures, alignment, embodied AI, world models, and the path from narrow AI to artificial general intelligence with subjective experience.

## Conventions
- File names: lowercase, hyphens (e.g., `emergent-sentience.md`)
- Every wiki page starts with YAML frontmatter
- Use `[[wikilinks]]` for cross-references (min 2 outbound links per page)
- Bump `updated` date on every change
- Every new page must be added to `index.md`
- Every action appended to `log.md`

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/papers/source-name.md]
confidence: high | medium | low
---
```

## Tag Taxonomy
- **Core**: consciousness, sentience, self-awareness, subjective-experience, qualia
- **Architecture**: transformer, moe, mla, world-model, recurrent, neuro-symbolic
- **Training**: pretraining, fine-tuning, rlhf, dpo, distillation, scaling-laws
- **Embodiment**: robotics, simulation, sensorimotor, physical-grounding
- **Philosophy**: hard-problem-of-consciousness, chinese-room, turing-test, panpsychism
- **Safety**: alignment, corrigibility, containment, chip
- **Actors**: person, company, lab, open-source
- **Meta**: comparison, timeline, controversy, open-question

## Page Thresholds
- Create page: entity/concept appears in 2+ sources OR is central to one source
- Add to existing: source mentions something already covered
- DON'T create: passing mentions, minor details
- Split page: over ~200 lines
- Archive: fully superseded content → `_archive/`

## Update Policy (contradictions)
1. Newer sources generally supersede older
2. Genuine contradictions → note both with dates and sources
3. Mark `contradictions: [page-name]` in frontmatter
4. Flag for human review