---
name: content-inheritance
description: Extract value from "dead" content — harvest data points, frameworks, quotes, examples, and structures from underperforming or outdated articles and transplant them into new content. Nothing is wasted. Every piece of content has reusable parts.
---

# Content Inheritance

Dead content has living parts. Harvest them.

## When to Activate

- User says `/inherit` or `/content-inheritance`
- User says `/inherit {file}` to harvest a specific piece
- Auto-suggested by content-network for dead nodes
- Auto-suggested by content-expiry for expired content

## Commands

### `/inherit` — Scan for harvestable dead content
### `/inherit {file}` — Harvest specific content
### `/inherit transplant {source} {target}` — Move parts between content

## Harvestable Parts

| Part | Example | Reuse Potential |
|------|---------|----------------|
| Data points | "87% of..." with source | Very High — facts don't expire |
| Frameworks | "The 3-step method" | Very High — structures are reusable |
| Examples | Case study, personal story | High — stories are timeless |
| Quotes | Expert quotes with attribution | High |
| Analogies | "AI is like a Swiss Army knife" | Medium |
| Structure | Section flow, heading pattern | Medium |
| CTAs | Well-performing call to action | High |
| Visuals | Image prompts, design specs | Medium |

## Workflow

### Step 1: Identify Dead Content

```
Dead content scan (from content-network + expiry):

Candidates for inheritance:

1. "{title}" ({date}) — DEAD ({N} PV, declining)
   Harvestable parts:
     - 3 data points with sources
     - 1 original framework ("The X Method")
     - 1 case study (still relevant)
     - 2 strong analogies
   Value: HIGH — good parts in a dead article

2. "{title}" ({date}) — EXPIRED (data outdated)
   Harvestable parts:
     - Structure/outline (still works)
     - 2 examples (timeless)
     - CTA template (proven click-through)
   Value: MEDIUM

Harvest which? (1/2/all)
```

### Step 2: Harvest Parts

```
Harvesting from: "{title}"
============================================

Extracted parts:

[DATA] "87% of AI projects fail in the first year"
  Source: Gartner, 2023
  Status: Fact-check needed (data may be updated)
  Reuse in: Any article about AI implementation challenges

[FRAMEWORK] "The 3-Step AI Adoption Framework"
  1. Assess → 2. Pilot → 3. Scale
  Status: Original framework, still valid
  Reuse in: note article, course module, slide deck

[STORY] "When Company X tried to automate..."
  Status: Timeless case study
  Reuse in: note article, X thread, newsletter

[ANALOGY] "Implementing AI without a strategy is like..."
  Status: Strong, reusable
  Reuse in: Hooks, explanations

Parts saved to: inheritance-library.json
============================================
```

### Step 3: Transplant to New Content

```
/inherit transplant bank-001 note_2026-03-25.md

Transplanting from inheritance library to "{new_title}":

Available parts for this topic:
  1. [DATA] "87% of AI projects fail" — fits Section 2
  2. [FRAMEWORK] "3-Step AI Adoption" — could be Section 3
  3. [STORY] "Company X case study" — fits Section 4

Insert which? (1/2/3/all/none)

After insertion:
  Section 2: Data point added with updated source check
  Section 3: Framework integrated with new context
  Section 4: Case study adapted for current article angle

Content enriched with {N} inherited parts.
Original dead article → value lives on.
```

### Inheritance Library

```
/inherit library

Inheritance Library: {N} parts stored

By type:
  Data points: {N} (fact-check status: {verified}/{total})
  Frameworks: {N}
  Examples/Stories: {N}
  Analogies: {N}
  CTAs: {N}

Most reused: "{part}" — used in {N} articles
Never reused: {N} parts (consider archiving)

Search: /inherit search {keyword}
```

## Integration

- **content-network**: Dead nodes identified for harvesting
- **content-expiry**: Expired content triggers inheritance scan
- **content-writer**: Suggests inherited parts during writing
- **fact-checker**: Re-verify inherited data points before reuse
- **content-vault**: Archived content still available for harvesting

## Quality Gate

- [ ] Harvested parts are genuinely reusable (not filler)
- [ ] Data points flagged for re-verification before transplant
- [ ] Frameworks and stories adapted to new context (not copy-pasted)
- [ ] Dead content source acknowledged where appropriate
- [ ] Library stays organized (not a junk drawer)
