---
name: funnel-designer
description: Design cross-platform content funnels (X/Instagram → note → monetization). Creates content pillars, TOFU/MOFU/BOFU stage plans, lead magnets, content calendars, and KPI targets. Reads profile.json funnel settings.
---

# Funnel Designer

Design a complete cross-platform content funnel: X/Instagram for reach → note for trust → monetization.

## When to Activate

- User says `/funnel-designer` or `/funnel`
- User wants to design a content funnel strategy
- User asks "how should I monetize my content?"
- User asks "how do I drive traffic from X to note?"
- Profile has `funnel.enabled = true` but no funnel plan exists yet

## Prerequisites

- `~/.content-autopilot/profile.json` must exist with funnel section
- If `funnel.enabled` is false, suggest enabling it first via `/setup-profile`

## Workflow

### Step 1: Load Profile & Funnel Settings

Read `~/.content-autopilot/profile.json` and extract:
- `theme.main` and `theme.keywords` — content domain
- `audience` — target reader profile
- `platforms` — active platforms
- `funnel` — note URL, handles, monetization type, lead magnet

### Step 2: Design Content Pillars

Based on the user's theme and audience, propose 3-5 content pillars:

```
Your content pillars:

1. {Pillar Name} — {description}
   Audience need: {what pain point this addresses}
   Content ratio: {suggested % of total content}

2. {Pillar Name} — {description}
   Audience need: {what pain point this addresses}
   Content ratio: {suggested % of total content}

3. {Pillar Name} — {description}
   Audience need: {what pain point this addresses}
   Content ratio: {suggested % of total content}

(Optional 4-5 pillars if the niche supports it)

Do these pillars look right? (yes / edit / suggest more)
```

**Pillar design principles:**
- Each pillar should map to a specific audience pain point
- Pillars should have natural TOFU → MOFU → BOFU progressions
- At least one pillar should directly support the monetization strategy
- Pillars should be distinct but complementary

### Step 3: Design Funnel Stages per Pillar

For each content pillar, create a TOFU → MOFU → BOFU content plan:

```
## Pillar 1: {Name}

### TOFU (Top of Funnel) — Awareness & Reach
Platform: X / Instagram
Goal: Maximize impressions, followers, and note click-throughs
Content types:
  - Hot takes on trending topics in {pillar}
  - "Did you know?" facts and surprising statistics
  - Visual tips and infographics
  - Relatable problems (audience pain points)
Example titles:
  1. "{example TOFU title for X}"
  2. "{example TOFU title for Instagram}"

### MOFU (Middle of Funnel) — Trust & Expertise
Platform: note (free articles)
Goal: Build trust, demonstrate expertise, grow note followers
Content types:
  - Step-by-step guides and tutorials
  - Case studies and real-world examples
  - Overseas insights localized for Japanese audience
  - Comparison articles and frameworks
Example titles:
  1. "{example MOFU title for note}"
  2. "{example MOFU title for note}"

### BOFU (Bottom of Funnel) — Conversion & Monetization
Platform: note (paid articles / membership)
Goal: Convert readers to paying customers
Content types:
  - Detailed templates and tools
  - Original research and data analysis
  - Premium tutorials with source files
  - Exclusive interviews and expert insights
Example titles:
  1. "{example BOFU title for note}"
  2. "{example BOFU title for note}"
```

### Step 4: Design Lead Magnet (if not set)

If `funnel.monetization.lead_magnet` is "none" or empty:

```
You need a lead magnet — a free, high-value resource that makes
readers want to follow you and come back for more.

Based on your theme ({theme.main}) and audience ({audience description}),
here are 3 lead magnet ideas:

1. {Lead Magnet Idea} — {format: PDF/checklist/template/mini-course}
   Why it works: {reason this appeals to target audience}
   Production effort: {low/medium/high}

2. {Lead Magnet Idea} — {format}
   Why it works: {reason}
   Production effort: {effort level}

3. {Lead Magnet Idea} — {format}
   Why it works: {reason}
   Production effort: {effort level}

Which one? (1 / 2 / 3 / custom idea)
```

After selection, update `profile.json` with the chosen lead magnet.

**Lead magnet best practices:**
- Solves one specific problem completely
- Can be consumed in under 15 minutes
- Demonstrates your expertise without giving away everything
- Naturally leads to wanting more (your paid content)

### Step 5: Generate Content Calendar

Create a 7-day content calendar showing which funnel stage to target each day:

```
## 7-Day Content Calendar

| Day | Platform | Funnel Stage | Pillar | Content Idea |
|-----|----------|-------------|--------|--------------|
| Mon | X (thread) | TOFU | {P1} | {title idea} |
| Tue | note (free) | MOFU | {P2} | {title idea} |
| Wed | Instagram | TOFU | {P1} | {title idea} |
| Thu | X (single) | TOFU | {P3} | {title idea} |
| Fri | note (free) | MOFU | {P1} | {title idea} |
| Sat | note (paid) | BOFU | {P2} | {title idea} |
| Sun | Instagram | TOFU | {P3} | {title idea} |

Funnel balance: TOFU 57% / MOFU 29% / BOFU 14%
Target balance: TOFU 50% / MOFU 30% / BOFU 20%
```

**Calendar design rules:**
- Never post BOFU content on X or Instagram (it doesn't convert there)
- TOFU content should alternate between X and Instagram
- MOFU content goes on note (free) 2-3 times per week
- BOFU content goes on note (paid) 1-2 times per week
- Maintain the ideal balance: TOFU 50% / MOFU 30% / BOFU 20%

### Step 6: Set KPI Targets

Based on current follower counts (ask user if unknown) and the funnel design:

```
## KPI Targets (30-Day Goals)

### Reach (TOFU)
- X followers: {current} → {target} (+{growth %})
- X avg impressions per post: {target}
- Instagram followers: {current} → {target}
- Instagram avg reach: {target}

### Engagement (MOFU)
- note followers: {current} → {target}
- note avg PV per article: {target}
- note "like" rate: {target %}
- Email/lead magnet signups: {target}

### Conversion (BOFU)
- note paid article purchases: {target}
- note membership subscribers: {target}
- Revenue target: ¥{amount}

### Funnel Metrics
- X → note click-through rate: {target %}
- Instagram → note referral rate: {target %}
- note free → paid conversion rate: {target %}
```

## Output

Save the complete funnel plan to:
```bash
mkdir -p ~/Desktop/content-autopilot-output
```

File: `~/Desktop/content-autopilot-output/funnel-plan.md`

Contents:
- Content pillars with descriptions
- TOFU/MOFU/BOFU content plan per pillar
- Lead magnet design
- 7-day content calendar
- KPI targets

Also update `~/.content-autopilot/profile.json`:
- Set `funnel.monetization.lead_magnet` if newly designed
- Optionally store pillar names for use by other skills

## Integration with Other Skills

- **trend-scout**: Uses funnel stages to tag content ideas
- **content-writer**: Uses funnel CTAs and depth differentiation
- **visual-creator**: Adds note referral banners when funnel enabled
- **daily-autopilot**: Shows funnel balance check and stage recommendations

## Optional: 30-Day Extended Calendar

If user requests `/funnel 30days`:
- Generate a full 30-day calendar
- Include weekly themes aligned with content pillars
- Plan a "launch sequence" for the lead magnet (Week 1: tease, Week 2: launch, Week 3-4: promote)
- Include review checkpoints at Day 7, 14, 21, 30

## Quality Gate

Before delivering:
- [ ] 3-5 content pillars, each with clear audience need
- [ ] TOFU/MOFU/BOFU plan for each pillar with example titles
- [ ] Lead magnet designed (or confirmed from profile)
- [ ] 7-day calendar with correct funnel balance
- [ ] KPI targets are realistic and measurable
- [ ] Calendar never places BOFU content on X/Instagram
- [ ] All content ideas align with theme and audience from profile.json
