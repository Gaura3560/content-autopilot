---
name: lead-magnet-creator
description: Create actual lead magnet content — PDFs, checklists, templates, mini-guides, and cheat sheets. Funnel-designer plans the strategy, this skill builds the deliverable. Generates the complete document ready for distribution.
---

# Lead Magnet Creator

Don't just plan your lead magnet — create it. Ready to distribute in one session.

## When to Activate

- User says `/lead-magnet-create` or `/magnet`
- User asks "create my lead magnet"
- User asks "make a free PDF/checklist/template"
- User has a lead_magnet planned in profile.json but hasn't built it yet

## Prerequisites

- `~/.content-autopilot/profile.json` (for lead_magnet name and audience)

## Commands

### `/magnet` — Create lead magnet from profile settings
### `/magnet checklist {topic}` — Create a checklist
### `/magnet template {topic}` — Create a fill-in template
### `/magnet guide {topic}` — Create a mini-guide (5-10 pages)
### `/magnet cheatsheet {topic}` — Create a one-page cheat sheet

## Lead Magnet Types

| Type | Pages | Creation Time | Best For | Conversion |
|------|-------|--------------|----------|------------|
| Checklist | 1-2 | Fast | Action-oriented audiences | High |
| Cheat Sheet | 1 | Fast | Quick reference | High |
| Template | 2-5 | Medium | Practical users | Very High |
| Mini-Guide | 5-10 | Medium | Education-focused | High |
| Toolkit | 3-5 | Medium | Tool recommendations | Medium |
| Workbook | 10-20 | Slow | Deep engagement | Medium |
| Swipe File | 5-10 | Medium | Creative professionals | High |

## Workflow

### Step 1: Define the Lead Magnet

If profile.json has `funnel.monetization.lead_magnet`:
```
Your planned lead magnet: "{lead_magnet_name}"

Creating this as a: {auto-detect type from name}
Target audience: {from profile}
Topic: {from theme}

Proceed? (yes / change type / different topic)
```

If no lead magnet planned:
```
What lead magnet would you like to create?

1. Checklist — "{suggested based on theme}"
2. Template — "{suggested}"
3. Mini-guide — "{suggested}"
4. Cheat sheet — "{suggested}"
5. Custom (describe)

Select (1-5):
```

### Step 2: Research and Outline

Research the topic for the lead magnet:
```
Search: "{topic} checklist" / "{topic} template" / "{topic} guide"
Search: Best practices for {topic}
```

Generate outline:
```
Lead Magnet Outline: "{title}"
Type: {type}
Pages: {estimated}

1. {section/item 1}
2. {section/item 2}
3. {section/item 3}
...

Approve outline? (yes / edit / add sections)
```

### Step 3: Generate Content

**Checklist:**
```markdown
# {Title} Checklist

## {Category 1}
- [ ] {Item with brief explanation}
- [ ] {Item}
- [ ] {Item}

## {Category 2}
- [ ] {Item}
- [ ] {Item}

## {Category 3}
- [ ] {Item}
- [ ] {Item}

---
Created by {name} | {note_url}
Get more resources: {CTA}
```

**Template:**
```markdown
# {Title} Template

## How to Use This Template
{Brief instructions}

## Section 1: {Name}
{Description of what to fill in}

| Field | Your Input |
|-------|-----------|
| {field_1} | _____________ |
| {field_2} | _____________ |
| {field_3} | _____________ |

## Section 2: {Name}
{Fillable sections with examples}

## Example (Filled In)
{Complete example showing how to use the template}

---
Created by {name} | {note_url}
```

**Mini-Guide:**
```markdown
# {Title}
## A Quick Guide by {name}

### Introduction
{Why this matters — 1 paragraph}

### Chapter 1: {Topic}
{2-3 paragraphs of actionable content}
Key takeaway: {one-line summary}

### Chapter 2: {Topic}
{Content}

### Chapter 3: {Topic}
{Content}

### Action Plan
{Step-by-step what to do next}

### About the Author
{Brief bio + CTA to note/paid content}
```

**Cheat Sheet:**
```markdown
# {Title} — Cheat Sheet

| {Category} | {Details} |
|------------|-----------|
| {item} | {quick reference info} |
| {item} | {info} |
| {item} | {info} |

Quick formulas:
  {formula_1}: {explanation}
  {formula_2}: {explanation}

Common mistakes:
  X {mistake} → O {correct approach}

---
{name} | {note_url} | More: {CTA}
```

### Step 4: Save Output

Save to `~/Desktop/content-autopilot-output/`:
```
lead_magnet_{type}_{date}.md
```

### Step 5: Distribution Plan

```
Lead Magnet Ready!

Distribution channels:
1. note free article — embed or link to download
2. X bio — "Free: {magnet_name} ↓ {link}"
3. Instagram bio link — add to link-in-bio
4. Newsletter — welcome email attachment
5. X thread — CTA in final tweet

Suggested distribution post:
"{draft_post_announcing_the_lead_magnet}"

Update profile.json with lead magnet URL? (yes / later)
```

## Integration with Other Skills

- **funnel-designer**: Plans the strategy, this builds the deliverable
- **content-writer**: References lead magnet in CTAs
- **launch-sequence**: Lead magnet can be the "product" for a mini-launch
- **newsletter-generator**: Welcome email delivers the lead magnet
- **bio-optimizer**: Updates bio with lead magnet CTA

## Quality Gate

- [ ] Lead magnet delivers genuine value (not thin content)
- [ ] Can be consumed in under 15 minutes
- [ ] Demonstrates expertise without giving away everything
- [ ] Naturally leads to wanting more (paid content)
- [ ] Branded with name, URL, and CTA
- [ ] Format appropriate for the content type
