---
name: slide-deck
description: Convert articles and threads into presentation slide decks — generate slide-by-slide content, speaker notes, and design directions for seminars, webinars, and conference talks. One article becomes a 20-minute presentation.
---

# Slide Deck Generator

Turn your articles into presentations — one article = one talk.

## When to Activate

- User says `/slide-deck {file}` or `/slides {file}`
- User asks "turn this into a presentation"
- User has a speaking engagement or webinar

## Commands

### `/slides {file}` — Convert article to slide deck
### `/slides {file} {minutes}` — Target specific duration
### `/slides template` — Show available slide structures

## Workflow

### Step 1: Extract Key Points

From the article, extract:
- Core message (1 sentence)
- 5-7 key points (one per section)
- Data/stats for visual slides
- Stories/examples for narrative slides
- CTA for closing slide

### Step 2: Generate Slide Deck

```
Slide Deck: "{title}"
Duration: ~{minutes} min | Slides: {count}
============================================

Slide 1: TITLE
  Text: "{title}"
  Subtitle: "{speaker_name} | {date}"
  Notes: "Thank the host, introduce yourself briefly"

Slide 2: HOOK
  Text: "{surprising stat or question}"
  Visual: {large number / question mark}
  Notes: "{what to say — 30 sec}"

Slide 3: AGENDA
  Text: "Today's 3 takeaways:
    1. {point}
    2. {point}
    3. {point}"
  Notes: "Set expectations"

Slides 4-6: POINT 1
  Slide 4: "{point_1 headline}"
  Slide 5: "{supporting data/visual}"
  Slide 6: "{example/story}"
  Notes: "{speaker notes for each}"

Slides 7-9: POINT 2...
Slides 10-12: POINT 3...

Slide 13: SUMMARY
  Text: "3 things to remember"
  Notes: "Recap"

Slide 14: CTA
  Text: "{call to action}"
  Notes: "{funnel CTA if applicable}"

Slide 15: Q&A
  Text: "Questions?"
  Notes: "Prepare for common questions: {list}"

============================================

Speaker notes total: ~{word_count} words ({minutes} min at normal pace)
```

## Quality Gate

- [ ] One idea per slide (not overcrowded)
- [ ] Speaker notes provide enough guidance to present
- [ ] Duration matches target (±2 minutes)
- [ ] Visual suggestions are specific
- [ ] CTA matches funnel strategy
