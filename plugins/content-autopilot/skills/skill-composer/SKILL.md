---
name: skill-composer
description: Fuse multiple skills into a single new custom skill — not sequential like workflow-chain, but MERGED into one unified output. "morning-lite" = advisor + recycle + micro fused into one streamlined result.
---

# Skill Composer

Workflows chain skills sequentially. Composer FUSES them into one.

## Commands

### `/compose {name} = {skill1} + {skill2} + ...` — Create a composed skill
### `/compose list` — List your composed skills
### `/compose {name}` — Run a composed skill

## Difference from Workflow

| Feature | Workflow Chain | Skill Composer |
|---------|--------------|---------------|
| Execution | Sequential (1→2→3) | Fused (combined output) |
| Output | Multiple outputs | Single merged output |
| Example | grade, THEN publish | grade+publish = one checklist |

## Examples

```
/compose quick-publish = grade + fact-check + pre-publish + brand-voice

Running "quick-publish":
  Combined quality gate (from 4 skills in 1 pass):

  Grade: 84/100
  Facts: 3/3 verified
  Pre-publish: 11/12 passed (1 fix: missing hashtag)
  Voice: 92% match

  Overall: READY (1 minor fix)
  Apply fix and publish? (yes / no)

Time: 30 seconds (vs 4 separate skill runs)
```

```
/compose idea-storm = mind-map + trend-predict + comment-mine + arbitrage

Running "idea-storm":
  Combined ideation from 4 sources:

  Top 10 ideas (deduplicated, ranked):
  1. "{idea}" — source: trend-predict + mind-map overlap
  2. "{idea}" — source: comment-mine (3 people asked)
  3. "{idea}" — source: arbitrage (English→Japanese gap)
  ...
```

Integrates with: ALL skills (any can be composed), meta-learning (tracks which compositions work), workflow-chain (compositions can be chained).
