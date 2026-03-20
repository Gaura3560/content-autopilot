---
name: voice-script
description: Convert written content to voice/podcast scripts — transform note articles, X threads, and blog posts into natural spoken-word scripts for stand.fm, Voicy, podcasts, and YouTube narration. Adjusts tone from "reading" to "speaking" while preserving key insights.
---

# Voice Script Converter

Turn your written content into natural, engaging audio scripts.

## When to Activate

- User says `/voice` or `/voice {file_path}`
- User says `/voice {file_path} standfm` or `/voice {file_path} podcast`
- User asks "convert this to a podcast script"
- User asks "make this into audio content"
- User wants to create stand.fm, Voicy, or podcast content

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- Source content file or text to convert

## Commands

### `/voice {file_path}` — Convert specific file to voice script
### `/voice` — Interactive: choose source and format
### `/voice {file_path} {format}` — Convert with specific format

## Supported Formats

| Format | Duration | Style | Best For |
|--------|----------|-------|----------|
| standfm | 5-10 min | Casual, personal, monologue | stand.fm daily broadcasts |
| voicy | 10-15 min | Semi-professional, educational | Voicy shows |
| podcast | 15-30 min | Professional, structured, interviewer tone | Podcast episodes |
| youtube | 5-15 min | Engaging, visual references, hook-heavy | YouTube narration |
| short | 1-3 min | Punchy, key-points-only | Instagram Reels, TikTok, Shorts |

## Workflow

### Step 1: Load Source Content

**If file path provided (`/voice {file_path}`):**
1. Read the file
2. Extract: title, structure, key points, data, examples

**If no file path (`/voice`):**
1. List recent content from `~/Desktop/content-autopilot-output/`
2. Ask user to select source
3. Ask for target format

### Step 2: Analyze Source

Extract from written content:
1. **Core message**: The one thing listeners should remember
2. **Key points**: 3-5 main takeaways
3. **Data/stats**: Numbers that need to be spoken naturally
4. **Examples**: Stories and cases to narrate
5. **Structure**: Logical flow to follow

### Step 3: Transform to Spoken Word

Apply these transformations:

**Writing → Speaking Conversions:**

| Written Style | Spoken Style |
|--------------|-------------|
| "Furthermore," | "And here's the thing —" |
| "In conclusion," | "So what does all this mean?" |
| Bullet points | "First... Second... And third..." |
| Statistics: "87%" | "Nearly 9 out of 10" |
| Long sentences (40+ chars) | Split into 2-3 short sentences |
| Passive voice | Active voice |
| Technical jargon | Plain language + brief explanation |
| Parenthetical notes | "And by the way..." or remove |
| Written CTA | Spoken CTA ("If this was helpful, hit follow") |
| Section headings | Transition phrases ("Now let's talk about...") |

**Add spoken elements:**
- **Pauses**: `[pause]` markers for emphasis
- **Emphasis**: `*word*` for words to stress
- **Asides**: Personal comments in `(aside: ...)` markers
- **Audience address**: "You might be thinking..." / "Here's what I mean..."
- **Recap markers**: "So to recap..." / "The key takeaway here is..."

### Step 4: Generate Script

**Script Template (stand.fm / 5-10 min):**

```markdown
# Voice Script: "{title}"
# Format: stand.fm | Duration: ~{estimated_minutes} min
# Source: {source_file}

---

## Opening (30 sec)

こんにちは、{name}です。
今日は「{topic}」について話します。

{hook — spoken version of the article's opening}

[pause]

## Main Content ({N} min)

### Point 1: {key_point_1}

{spoken version of the first section}

で、ここがポイントなんですけど —
{key insight in conversational tone}

[pause]

### Point 2: {key_point_2}

{spoken version}

面白いのが、{data point spoken naturally}
つまり、10人中9人が{implication}ということなんです。

[pause]

### Point 3: {key_point_3}

{spoken version}

(aside: 実はこれ、私自身も{personal connection}なんですよね)

[pause]

## Closing (30 sec)

というわけで、今日のまとめです。

1つ目: {takeaway 1}
2つ目: {takeaway 2}
3つ目: {takeaway 3}

{spoken CTA}

もし参考になったら、いいねとフォローお願いします。
{funnel CTA if enabled: "もっと詳しい内容はnoteに書いてるので、プロフィールからチェックしてみてください"}

それでは、また次回。ありがとうございました。

---
# Estimated reading time: {time} min at normal speaking pace (300 chars/min)
# Character count: {count} chars
```

**Format-specific adjustments:**

**podcast (15-30 min):**
- Add intro/outro music cues: `[INTRO MUSIC]` / `[OUTRO MUSIC]`
- Add segment transitions: `[TRANSITION SOUND]`
- More structured with clear segments
- Include "episode notes" section at the end

**youtube (5-15 min):**
- Add visual cues: `[SHOW: screenshot of X]` / `[SHOW: diagram]`
- Hook in first 10 seconds (critical for retention)
- Pattern interrupts every 2-3 minutes: `[VISUAL CHANGE]`
- End screen CTA: "Watch this next → {related_video}"

**short (1-3 min):**
- Only the single most impactful point
- Start with the punchline: `[HOOK: 3 seconds]`
- Fast pace, no filler
- End with CTA in last 3 seconds

### Step 5: Estimate Duration

Calculate estimated speaking time:
- Japanese: ~300 characters per minute (moderate pace)
- Include pauses: add 10% to total time
- Adjust for format-specific pacing

```
Estimated duration: {minutes}:{seconds}
  Content: {chars} chars @ 300 chars/min = {base_time}
  Pauses: +{pause_count} × 2 sec = +{pause_time}
  Opening/closing: +{outro_time}

  Target: {format_target_range}
  Status: {within range / too long — suggest cuts / too short — suggest additions}
```

### Step 6: Save Output

Save to `~/Desktop/content-autopilot-output/`:
```
voice_{format}_{date}.md
```

Example: `voice_standfm_2026-03-20.md`

### Step 7: Record in History

Add entry to `content-history.json`:
```json
{
  "source": "voice",
  "platforms": {
    "voice": {
      "title": "{title}",
      "file": "voice_{format}_{date}.md",
      "format": "{standfm/voicy/podcast/youtube/short}",
      "estimated_duration": "{minutes}:{seconds}"
    }
  }
}
```

## Integration with Other Skills

- **repurpose**: `/repurpose note→voice` calls voice-script internally
- **batch-generator**: Can include voice script generation in weekly batch
- **content-analytics**: Tracks voice content in history
- **daily-autopilot**: Can suggest "also create a voice version?" after content generation

## Quality Gate

Before delivering:
- [ ] Script sounds natural when read aloud (not like reading an article)
- [ ] Pauses are placed at natural emphasis points
- [ ] Technical terms are explained in plain language
- [ ] Duration estimate is within format target range
- [ ] Opening hook is strong (especially for YouTube/short)
- [ ] CTA is spoken naturally, not forced
- [ ] Format-specific elements are included (music cues, visual cues, etc.)
- [ ] Personal tone is maintained throughout
