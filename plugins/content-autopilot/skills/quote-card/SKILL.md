---
name: quote-card
description: Extract the most shareable quotes from your content and generate visual quote cards for X and Instagram. One article generates 3-5 additional micro-content pieces. Includes image generation prompts and text overlays.
---

# Quote Card Generator

Turn your best lines into shareable visual content — multiply every article into 3-5 extra posts.

## When to Activate

- User says `/quote-card {file_path}` or `/quote {file_path}`
- User says `/quote "{text}"`
- User asks "create quote cards from this article"
- User asks "make this into a shareable image"

## Prerequisites

- `~/.content-autopilot/profile.json` must exist (for brand colors)
- Source content to extract quotes from

## Commands

### `/quote {file_path}` — Extract quotes and generate cards from a file
### `/quote "{text}"` — Generate a card from a specific quote
### `/quote batch` — Generate quote cards from all this week's content

## Workflow

### Step 1: Extract Shareable Quotes

Read the source content and identify the most shareable phrases:

**Quote selection criteria (score each 1-5):**
- **Standalone value**: Makes sense without context (+5)
- **Emotional impact**: Triggers a reaction (+5)
- **Conciseness**: Under 150 characters (+5)
- **Shareability**: "Would someone screenshot this?" (+5)
- **Uniqueness**: Not a generic platitude (+5)

Select the top 3-5 quotes from each article.

```
Extracted quotes from "{article_title}":

1. [Score: 23/25] "{quote_text}"
   Why it works: {reason}
   Best for: {X / Instagram / both}

2. [Score: 21/25] "{quote_text}"
   Why it works: {reason}
   Best for: {platform}

3. [Score: 19/25] "{quote_text}"
   Why it works: {reason}
   Best for: {platform}

4. [Score: 17/25] "{quote_text}"
   Why it works: {reason}
   Best for: {platform}

5. [Score: 15/25] "{quote_text}"
   Why it works: {reason}
   Best for: {platform}

Generate cards for all 5? (yes / select numbers / edit quotes)
```

### Step 2: Design Quote Cards

For each selected quote, generate a card specification:

```
--- Quote Card #{N} ---

Quote: "{text}"
Attribution: — {author_name} (@{handle})

Design specifications:
  Size: 1080 x 1080 (Instagram) / 1200 x 675 (X)
  Background: {brand_primary_color} solid or gradient to {secondary}
  Text: White, bold sans-serif, centered
  Font size: Large enough to read at thumbnail (min 36px equivalent)
  Layout:
    [Top 20%]: Empty space or subtle pattern
    [Middle 60%]: Quote text (2-3 lines max)
    [Bottom 20%]: Attribution + logo/handle

  Alternative layouts:
  A) Minimal — solid color + white text
  B) Textured — color gradient + semi-transparent overlay + text
  C) Photo — blurred background image + text overlay

Image generation prompt:
"A clean, modern quote card graphic. Background: {primary_color} to
{secondary_color} gradient. Center text: '{quote_abbreviated}' in bold
white sans-serif font. Bottom right: small '@{handle}' text.
Minimalist, professional, high contrast. 1080x1080 pixels."
```

### Step 3: Generate Social Posts

For each quote card, generate the accompanying post text:

**X post:**
```
"{quote_text}"

{1-2 sentences of context or expansion}

{CTA: "Full article on note → {url}" or "Like if you agree"}

[Image: quote card attached]
```

**Instagram post:**
```
"{quote_text}"
.
{2-3 sentences expanding on the quote}
.
{Context from the full article}
.
{CTA}
.
{Hashtags — 10-15 relevant tags}

[Image: quote card attached]
```

### Step 4: Save Output

```
~/Desktop/content-autopilot-output/
  quote_card_1_{date}.md    # Post text + image prompt
  quote_card_2_{date}.md
  quote_card_3_{date}.md
  ...
```

If `gemini-image` MCP is available:
- Generate actual images for each card
- Save as `quote_card_1_{date}.png`

### Step 5: Display Summary

```
============================================
  Quote Cards Generated: {count}
============================================

From: "{article_title}"

Card 1: "{quote_preview}..."
  → X post + Instagram post + image prompt

Card 2: "{quote_preview}..."
  → X post + Instagram post + image prompt

Card 3: "{quote_preview}..."
  → X post + Instagram post + image prompt

Total additional content: {count} posts from 1 article
Estimated time to post: 5 minutes (copy-paste ready)

Files saved to ~/Desktop/content-autopilot-output/
============================================
```

## Batch Mode (`/quote batch`)

Process all this week's content at once:
1. Read content-history.json for this week
2. Extract top quotes from each piece
3. Generate cards for the best 10-15 quotes across all content
4. Create a posting schedule (1-2 quote cards per day)

## Integration with Other Skills

- **content-writer**: After generating content, suggest: "Extract quote cards? /quote {file}"
- **batch-generator**: Include quote card generation in weekly batch
- **visual-creator**: Uses same brand colors and design language
- **daily-autopilot**: Step 7.5 can suggest quote card creation
- **content-recycle**: Quote cards are a form of content recycling

## Quality Gate

- [ ] Extracted quotes genuinely stand alone (make sense without context)
- [ ] Quotes are attributed correctly
- [ ] Design specs match brand colors from profile
- [ ] Text is readable at thumbnail size
- [ ] Accompanying posts add value beyond the quote
- [ ] Not too many cards from one article (3-5 max)
