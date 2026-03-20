---
name: instant-react
description: Rapid response content for breaking news and viral moments — generate a hot take, analysis thread, or commentary within 15 minutes. The fastest reaction gets the most followers. Includes pre-built response templates for common event types in your niche.
---

# Instant React

Breaking news just dropped. You have 15 minutes to be the first expert voice. Go.

## When to Activate

- User says `/instant-react {event}` or `/react {event}`
- User says "breaking news about {topic}"
- User pastes a URL or headline and wants to react fast

## Commands

### `/react {event}` — Generate rapid response content
### `/react {url}` — React to a specific article/post
### `/react templates` — Pre-built templates for common events

## Speed Tiers

| Tier | Time | Output | When |
|------|------|--------|------|
| Flash | 2 min | Single X tweet with hot take | First 30 min of news |
| Quick | 10 min | X thread (5 tweets) with analysis | First 2 hours |
| Deep | 30 min | X thread + note article skeleton | First 24 hours |

## Workflow

### Flash Tier (2 min)

```
EVENT: "{event_description}"

Your angle (from profile + content-dna):
  "{your unique perspective on this event}"

--- Flash Tweet ---
"{hot take that only someone with your expertise can make}"

Post NOW → edit later if needed.
```

### Quick Tier (10 min)

```
--- Rapid Thread (5 tweets) ---

Tweet 1: [BREAKING] "{headline reaction}"
  {Your immediate take — bold, specific}

Tweet 2: "Here's what this means for {your_audience}:"
  {Practical implication #1}

Tweet 3: "What most people are missing:"
  {Your unique insight from content-dna intersection}

Tweet 4: "My prediction:"
  {Where this goes next — be specific}

Tweet 5: "I'll write a deep analysis on note within 24h.
  Follow to catch it. {handle}"

Post time: {optimal based on best-times}
```

### Deep Tier (30 min)

Thread (above) + note article skeleton:
```markdown
# {Event}: What It Means for {Audience}

## What Happened
{Brief factual summary — 2-3 paragraphs}

## Why It Matters
{Your expert analysis}

## What to Do Now
{Actionable advice for your audience}

## What's Next
{Prediction}

[Flesh out within 24 hours, publish while still relevant]
```

## Pre-Built Templates

| Event Type | Template | Reaction Style |
|-----------|----------|---------------|
| Product launch | Feature analysis + impact | Informative |
| Industry controversy | Balanced take + your position | Thought leadership |
| Research/data release | Key findings + implications | Data commentary |
| Competitor move | Strategic analysis | Expert insight |
| Policy/regulation change | What it means + action steps | Practical guide |
| Viral post in niche | Agree/disagree + your angle | Discussion entry |

## Quality Gate

- [ ] Reaction is FAST (templates pre-loaded, minimal research)
- [ ] Hot take is genuinely insightful (not generic "wow this is big")
- [ ] Your unique angle (from content-dna) is present
- [ ] Follow-up content planned (thread → note article)
- [ ] Fact-check after posting if needed (speed > perfection for flash tier)
