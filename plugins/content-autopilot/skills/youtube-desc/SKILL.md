---
name: youtube-desc
description: YouTube video description optimizer — SEO-optimized descriptions with timestamps, keyword placement, links, and cards/end screen strategy. Integrates with voice-script for complete video content pipeline.
---

# YouTube Description Optimizer

Maximize YouTube search visibility with SEO-optimized descriptions, timestamps, and metadata.

## When to Activate

- User says `/youtube-desc` or `/youtube-desc {title}`
- User says `/youtube-desc {script_file}` to generate from voice script
- User asks "write a YouTube description"
- User wants to optimize video SEO

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- Video title and/or script content

## Commands

### `/youtube-desc {title}` — Generate description for a video title
### `/youtube-desc {script_file}` — Generate from voice script file
### `/youtube-desc seo {keyword}` — Research YouTube SEO for a keyword

## Workflow

### Step 1: Gather Video Info

```
Video details:
1. Title: {title or suggest optimized title}
2. Topic: {main topic}
3. Duration: {approximate length}
4. Script file: {path if available}
5. Key points covered: {list}
```

### Step 2: Generate Optimized Description

```markdown
{Hook line — first 150 chars visible in search results, include primary keyword}

{2-3 sentence summary of what viewers will learn}

--- Timestamps ---
0:00 Introduction
{M:SS} {Section title with keyword}
{M:SS} {Section title}
{M:SS} {Section title}
{M:SS} {Section title}
{M:SS} Summary & Next Steps

--- Links ---
{Primary CTA link — note article, lead magnet, etc.}
{Secondary link — related video or resource}
{Social links}

--- About ---
{Brief channel/creator description with keywords}
{Subscription CTA}

--- Tags ---
{10-15 relevant tags, comma-separated}

--- Hashtags ---
#{hashtag1} #{hashtag2} #{hashtag3}
```

### Step 3: YouTube SEO Analysis

```
YouTube SEO for "{keyword}":

Title optimization:
  Primary keyword: "{keyword}" — place in first 60 chars
  Power words to include: {list}
  Suggested title: "{optimized title}"

Description optimization:
  Keyword in first sentence: required
  Keyword density: 2-3 mentions naturally
  Related keywords: {list to include}

Tags: {15 tags ranked by relevance}

Thumbnail text suggestion: "{3-5 word overlay}"

Estimated competition: {low/medium/high}
```

### Step 4: Cards & End Screen Strategy

```
Cards (clickable links during video):
  {timestamp}: Card to "{related video/playlist}"
  {timestamp}: Card to "{note article}" (if external links enabled)

End screen (last 20 seconds):
  Element 1: Subscribe button
  Element 2: Best related video
  Element 3: Playlist
```

## Integration with Other Skills

- **voice-script**: Script → Description pipeline
- **seo-optimizer**: Shared keyword research methodology
- **reels-script**: Shorts version links to full video
- **content-writer**: Article version links to video and vice versa

## Quality Gate

- [ ] Primary keyword in title (first 60 chars) and description (first sentence)
- [ ] Timestamps are accurate and descriptive
- [ ] First 150 chars are compelling (visible in search results)
- [ ] Links are correctly placed and working
- [ ] Tags are relevant (10-15)
- [ ] Description provides standalone value (not just "watch the video")
