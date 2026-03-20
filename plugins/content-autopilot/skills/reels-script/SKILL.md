---
name: reels-script
description: Generate scripts for Instagram Reels, TikTok, and YouTube Shorts — 15-90 second vertical video format with hook (0-3 sec), body, and CTA. Converts existing content or generates original scripts. Includes shot directions, text overlays, and trending audio suggestions.
---

# Reels / TikTok / Shorts Script

Create scroll-stopping short-form video scripts — the fastest-growing content format.

## When to Activate

- User says `/reels`, `/reels {file_path}`, or `/reels {topic}`
- User says `/tiktok` or `/shorts`
- User asks "create a Reels script"
- User wants short-form video content

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Commands

### `/reels {topic}` — Generate original Reels script
### `/reels {file_path}` — Convert existing content to Reels
### `/reels templates` — Show Reels structure templates
### `/reels batch` — Generate 5 Reels scripts from recent content

## Reels Structure Templates

| Template | Duration | Structure | Best For |
|----------|----------|-----------|----------|
| Quick Tip | 15-30s | Hook → 1 tip → CTA | Daily tips, tricks |
| 3-Point | 30-60s | Hook → Point 1-2-3 → CTA | Listicle content |
| Story | 45-90s | Hook → Problem → Solution → Result → CTA | Case studies |
| Tutorial | 30-60s | Hook → Step 1-2-3 → Result → CTA | How-to content |
| Myth Buster | 15-30s | "People think X" → "Actually Y" → Proof | Contrarian takes |
| Before/After | 15-45s | Before state → Transition → After state | Transformations |

## Workflow

### Step 1: Generate Script

```markdown
# Reels Script: "{title}"
# Duration: ~{seconds}s | Template: {template_name}
# Platform: Instagram Reels / TikTok / YouTube Shorts

---

## [0:00-0:03] HOOK — Stop the Scroll
Visual: {what's on screen — face/text/action}
Text overlay: "{bold text that appears}"
Audio: {speaking / trending sound / voiceover}
Script: "{what to say — must grab in 3 seconds}"

## [0:03-0:08] SETUP
Visual: {description}
Text overlay: "{supporting text}"
Script: "{expand on the hook — establish the problem/promise}"

## [0:08-0:20] POINT 1
Visual: {description}
Text overlay: "{key phrase}"
Script: "{first main point — specific and visual}"

## [0:20-0:32] POINT 2
Visual: {description}
Text overlay: "{key phrase}"
Script: "{second point}"

## [0:32-0:42] POINT 3
Visual: {description}
Text overlay: "{key phrase}"
Script: "{third point — strongest/most surprising last}"

## [0:42-0:50] RESULT / PROOF
Visual: {screenshot / data / before-after}
Text overlay: "{result/number}"
Script: "{show the outcome — specific data if possible}"

## [0:50-0:55] CTA
Visual: {point to profile / text with handle}
Text overlay: "Follow for more" / "Save this"
Script: "{spoken CTA — keep it natural}"

---

Caption: "{Instagram caption for the Reel}"
Hashtags: {15-20 relevant hashtags}
Audio suggestion: {trending audio or original}

Total script word count: {count} (~{seconds}s at normal pace)
```

### Step 2: Hook Variants

Generate 3 hook options for A/B testing:
```
Hook options (pick the strongest):
A) [Data] "{number-based hook}"
B) [Question] "{provocative question}"
C) [Contrarian] "{bold claim that challenges assumptions}"
```

### Step 3: Platform Adjustments

| Element | Instagram Reels | TikTok | YouTube Shorts |
|---------|----------------|--------|----------------|
| Ideal length | 15-30s (currently boosted) | 30-60s | 30-60s |
| Text overlays | Essential | Essential | Optional |
| CTA | "Save + Follow" | "Follow for Part 2" | "Subscribe" |
| Hashtags | 15-20 | 3-5 | 3-5 in description |
| Music | Use trending IG audio | Use trending TT sound | Original/royalty-free |
| Caption | Full caption below | Short caption | In description |

### Step 4: Save Output

```
~/Desktop/content-autopilot-output/
  reels_{date}.md       # Script with directions
  reels_caption_{date}.md  # Caption + hashtags
```

## Integration with Other Skills

- **voice-script**: Reels = visual version of short voice scripts
- **content-writer**: Suggests Reels adaptation after article creation
- **carousel-generator**: Same content, different format choice
- **algorithm-guide**: Reels optimization tips from latest algorithm data
- **quote-card**: Quote cards can become Reels with text animation

## Quality Gate

- [ ] Hook grabs attention within 3 seconds
- [ ] Script fits within target duration at normal speaking pace
- [ ] Visual directions are specific enough to film
- [ ] Text overlays are readable on mobile (large, brief)
- [ ] CTA is natural and platform-appropriate
- [ ] Content delivers value even on mute (text overlays carry the message)
