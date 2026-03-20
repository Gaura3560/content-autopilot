---
name: carousel-generator
description: Instagram carousel content generator — creates 10-slide carousel scripts with text per slide, design direction, and swipe-stopping hooks. Converts existing note/X content or generates from scratch. Carousels have the highest Instagram engagement rate.
---

# Carousel Generator

Create high-engagement Instagram carousels — the format with the best reach and saves.

## When to Activate

- User says `/carousel` or `/carousel {file_path}`
- User says `/carousel {topic}`
- User asks "create an Instagram carousel"
- User wants to repurpose content as a carousel

## Prerequisites

- `~/.content-autopilot/profile.json` must exist (for brand colors and style)

## Commands

### `/carousel {topic}` — Generate carousel from a topic
### `/carousel {file_path}` — Convert existing content to carousel
### `/carousel templates` — Show available carousel structures

## Carousel Structures

| Structure | Slides | Best For | Engagement |
|-----------|--------|----------|-----------|
| Listicle | 10 | Tips, tools, habits | High saves |
| Story Arc | 8-10 | Before/after, case study | High shares |
| How-To | 7-10 | Step-by-step guide | High saves |
| Myth Buster | 8 | Common misconceptions | High comments |
| Comparison | 6-8 | A vs B, old vs new | High shares |
| Data Reveal | 8-10 | Stats with insights | High saves |
| Checklist | 7-10 | Actionable list | Highest saves |
| Quote Series | 5-7 | Inspirational/educational | High shares |

## Workflow

### Step 1: Determine Source

**From topic (`/carousel {topic}`):**
1. Research the topic briefly (WebSearch if needed)
2. Select the best carousel structure for the topic
3. Generate content from scratch

**From existing content (`/carousel {file_path}`):**
1. Read the source file
2. Extract key points, data, steps
3. Auto-select the best carousel structure
4. Condense into slide format

### Step 2: Select Structure

If not auto-detected:
```
Best carousel structure for "{topic}":

1. Listicle — "7 {topic} tips you need to know"
2. How-To — "Step-by-step: how to {topic}"
3. Myth Buster — "5 {topic} myths debunked"

Recommended: {recommendation} (highest engagement for this topic type)
Select (1/2/3):
```

### Step 3: Generate Slide Content

**Slide-by-slide template:**

```
============================================
  Instagram Carousel: "{title}"
  Structure: {type} | Slides: {count}
============================================

--- Slide 1: COVER ---
Headline: "{attention-grabbing title}"
Subtext: "{supporting line or credential}"
Design: {brand_primary_color} background, bold white text, centered
Purpose: Stop the scroll — this must work as a standalone image

--- Slide 2: HOOK ---
Text: "{expand on the promise — why should they keep swiping?}"
Design: Clean, minimal text, {accent_color} highlight on key phrase
Purpose: Convince them to swipe

--- Slide 3: Point 1 ---
Heading: "{point_1_title}"
Body: "{2-3 lines of specific, actionable content}"
Icon/Visual: {suggested icon or visual element}
Design: Consistent layout, left-aligned text

--- Slide 4: Point 2 ---
Heading: "{point_2_title}"
Body: "{2-3 lines}"
Icon/Visual: {suggestion}

--- Slide 5: Point 3 ---
...

--- Slide 6: Point 4 ---
...

--- Slide 7: Point 5 ---
...

--- Slide 8: Data/Proof ---
Text: "{surprising statistic or case study result}"
Design: Large number/stat as focal point, supporting text below
Purpose: Build credibility

--- Slide 9: Summary ---
Text: "Recap:
1. {point_1}
2. {point_2}
3. {point_3}
4. {point_4}
5. {point_5}"
Design: Checklist format, clean layout

--- Slide 10: CTA ---
Text: "{call to action}"
Options:
  - "Save this for later" (highest engagement action)
  - "Share with someone who needs this"
  - "Follow @{handle} for more {theme}"
  - "Full guide on note — link in bio" (funnel CTA)
Design: {brand_primary_color} background, clear CTA button style

============================================

Caption:
{Instagram caption for the carousel — 300-500 chars}
{Line breaks for readability}
{CTA repeated in text}
.
.
{30 hashtags in 3 tiers}
```

### Step 4: Design Direction

For each slide, provide design specifications:

```
Design Specs:
  Size: 1080 x 1080 px (square) or 1080 x 1350 px (portrait, recommended)
  Font: Bold sans-serif for headlines, regular for body
  Colors: {primary_color} (background) + white (text) + {secondary_color} (accents)
  Consistency: Same layout template across all slides
  Text limit: Max 3 lines per slide for readability
  Logo: Small logo watermark bottom-right on each slide
```

If `gemini-image` MCP is available:
- Generate slide cover image
- Provide detailed prompts for each slide

### Step 5: Save Output

Save to `~/Desktop/content-autopilot-output/`:
```
carousel_{date}.md           # Full carousel script
carousel_caption_{date}.md   # Caption + hashtags only
```

### Step 6: Record in History

Add to `content-history.json`:
```json
{
  "platforms": {
    "instagram": {
      "title": "{carousel_title}",
      "file": "carousel_{date}.md",
      "format": "carousel",
      "slide_count": 10,
      "hashtag_count": 30
    }
  }
}
```

## Carousel Best Practices (built into generation)

1. **Cover slide**: Must work as a standalone post in the feed
2. **Swipe trigger**: Slide 2 must give a reason to keep swiping
3. **One idea per slide**: Never cram multiple points
4. **Large text**: Must be readable without zooming
5. **Visual consistency**: Same colors, fonts, layout across slides
6. **Save-worthy content**: Actionable tips get saved → algorithm boost
7. **CTA on last slide**: Always ask for a specific action

## Quality Gate

- [ ] Cover slide is scroll-stopping on its own
- [ ] Each slide has one clear point (not overcrowded)
- [ ] Text is large enough to read on mobile
- [ ] Brand colors consistently applied
- [ ] Caption includes relevant hashtags
- [ ] CTA is clear and specific
- [ ] Structure matches the topic type
- [ ] 8-10 slides (sweet spot for engagement)
