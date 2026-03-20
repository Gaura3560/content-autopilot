---
name: trending-audio
description: Trending audio and sound finder for Instagram Reels and TikTok — research currently trending sounds, match them to your niche, and suggest how to use them in your content. Using trending audio can 3-10x your Reels reach.
---

# Trending Audio Finder

Use the right sound and your Reels reach explodes — find what's trending NOW.

## When to Activate

- User says `/trending-audio` or `/audio`
- User asks "what sounds are trending on Reels?"
- User asks "what audio should I use for my Reel?"
- Auto-referenced by reels-script for audio suggestions

## Prerequisites

- `~/.content-autopilot/profile.json` (for niche context)

## Commands

### `/audio` — Show current trending audio
### `/audio {niche}` — Trending audio for a specific niche
### `/audio match {topic}` — Find audio that matches a content topic
### `/audio original` — Tips for using original audio effectively

## Workflow

### Step 1: Research Trending Audio

```
Search: "trending Reels audio {month} {year}"
Search: "trending TikTok sounds {month} {year}"
Search: "Instagram Reels trending music this week"
Search: "トレンド BGM リール {year}"
```

### Step 2: Categorize and Present

```
============================================
  Trending Audio — {date}
  Platform: Instagram Reels + TikTok
============================================

--- Trending Sounds This Week ---

1. "{sound_name}" by {artist}
   Trend level: {viral / rising / steady}
   Best for: {content types that use this sound}
   Your niche fit: {high / medium / low}
   How to use: {specific suggestion for your content}
   Example: "{how others in your niche are using it}"

2. "{sound_name}" by {artist}
   Trend level: {level}
   Best for: {types}
   Your niche fit: {fit}
   How to use: {suggestion}

3. "{sound_name}" by {artist}
   ...

--- Trending Audio Categories ---

Voiceover sounds (talk over them):
  - "{sound}" — good for tips/tutorials
  - "{sound}" — good for storytelling

Transition sounds (visual transitions):
  - "{sound}" — good for before/after
  - "{sound}" — good for reveals

Music (background for text-heavy Reels):
  - "{sound}" — upbeat, good for positive content
  - "{sound}" — dramatic, good for surprising reveals

--- For Your Niche ({theme.main}) ---

Recommended audio this week:
  1st choice: "{sound}" — {why it fits your content}
  2nd choice: "{sound}" — {backup option}
  For tutorials: "{sound}"
  For storytelling: "{sound}"

--- Original Audio Tips ---

When to use original audio:
  - Educational/tutorial content (your voice IS the content)
  - When no trending sound fits naturally
  - For building recognizable brand audio

Tips for original audio:
  - Clear voice, minimal background noise
  - Add captions (80% of users watch without sound)
  - Keep talking pace natural (not too fast for Reels)

============================================

Note: Trending audio changes weekly. Run /audio again
before creating new Reels for the freshest recommendations.
============================================
```

## Integration with Other Skills

- **reels-script**: Audio suggestion included in every script
- **algorithm-guide**: Audio trends reflect algorithm preferences
- **batch-generator**: Match audio to batch Reels content
- **content-calendar**: Note audio trends when planning Reels days

## Quality Gate

- [ ] Audio recommendations are current (this week/month)
- [ ] Niche relevance assessed for each sound
- [ ] Usage suggestions are specific (not just "use this sound")
- [ ] Both trending and original audio options provided
- [ ] Platform differences noted (Reels vs TikTok vs Shorts)
