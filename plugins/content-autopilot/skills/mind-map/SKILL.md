---
name: mind-map
description: Content ideation mind map — expand one topic into 20-30 branching content ideas across different angles, formats, audiences, and platforms. Turn one seed idea into a month of content. The creative expansion engine.
---

# Mind Map

One topic. Thirty ideas. A month of content from a single seed.

## When to Activate

- User says `/mind-map {topic}` or `/ideas {topic}`
- User asks "what can I write about {topic}?"
- User asks "give me content ideas"
- User feels stuck on a single topic angle

## Prerequisites

- `~/.content-autopilot/profile.json`

## Commands

### `/mind-map {topic}` — Generate full ideation map
### `/mind-map {topic} quick` — 10 ideas only
### `/mind-map expand {idea}` — Expand a specific branch further

## Workflow

### Step 1: Generate Mind Map

```
============================================
  Content Mind Map: "{topic}"
  {count} ideas generated
============================================

                        ┌── Beginner: "{idea}"
               ┌─ By   ├── Advanced: "{idea}"
               │  Level └── Executive: "{idea}"
               │
               │        ┌── Data/stat angle: "{idea}"
               ├─ By    ├── Story angle: "{idea}"
               │  Angle ├── Contrarian angle: "{idea}"
               │        ├── How-to angle: "{idea}"
               │        └── Prediction angle: "{idea}"
               │
  "{TOPIC}" ───┤        ┌── X thread: "{idea}"
               │        ├── note article: "{idea}"
               ├─ By    ├── IG carousel: "{idea}"
               │  Format├── Reels script: "{idea}"
               │        ├── Newsletter: "{idea}"
               │        └── Poll/quiz: "{idea}"
               │
               │        ┌── Problem: "{pain point idea}"
               ├─ By    ├── Solution: "{tool/method idea}"
               │  Stage ├── Comparison: "{A vs B idea}"
               │        └── Case study: "{result idea}"
               │
               │        ┌── {adjacent_niche_1}: "{crossover idea}"
               └─ Cross ├── {adjacent_niche_2}: "{crossover idea}"
                 Niche  └── {unexpected_niche}: "{surprising connection}"

============================================

Top 5 ideas (by novelty × demand):
  1. "{idea}" — {why this is high potential}
  2. "{idea}" — {reason}
  3. "{idea}" — {reason}
  4. "{idea}" — {reason}
  5. "{idea}" — {reason}

Save all to pipeline? (yes / select / no)
============================================
```

### Step 2: Expand a Branch

`/mind-map expand "contrarian angle"`:
```
Expanding: Contrarian angle on "{topic}"

1. "{specific contrarian take 1}"
   Hook: "Everyone says X. Here's why that's wrong."
   Evidence needed: {what data would support this}
   Risk level: {safe contrarian / actually controversial}

2. "{contrarian take 2}"
   Hook: "I stopped doing X. Results surprised me."
   Evidence: {personal experience + data}
   Risk: {level}

3. "{contrarian take 3}"
   ...
```

### Step 3: Connect to Content System

Each idea maps to skills:
```
Idea: "{selected idea}"

Execution plan:
  1. /trend-scout — verify demand for this angle
  2. /content-writer — generate the content
  3. /persuasion pas — apply PAS framework
  4. /grade — quality check
  5. Save to /pipeline as idea

Or add to /batch for next week's content.
```

## Integration with Other Skills

- **trend-scout**: Mind map ideas validated by trend data
- **content-writer**: Ideas feed directly into writing
- **pipeline-view**: Ideas saved to pipeline as "idea" stage
- **batch-generator**: Ideas used for topic selection
- **persona-switcher**: "By Level" branch matches personas
- **series-designer**: Connected ideas become series

## Quality Gate

- [ ] At least 20 genuinely different ideas generated
- [ ] Ideas span multiple dimensions (angle, format, level, niche)
- [ ] Cross-niche ideas are surprising but relevant
- [ ] Top 5 selection reflects actual novelty and demand
- [ ] Ideas are specific enough to write from (not vague)
