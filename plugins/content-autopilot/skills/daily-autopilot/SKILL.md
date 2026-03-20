---
name: daily-autopilot
description: Full content automation orchestrator — runs the complete pipeline from trend research to published content in one command. Chains setup-profile, trend-scout, content-writer, and visual-creator with minimal user intervention. Includes funnel stage tracking, balance check, content history recording, series integration, engagement templates, and optional X API auto-posting.
---

# Daily Autopilot

Run the complete content pipeline in one command. From trend research to ready-to-publish content.

## When to Activate

- User says `/daily-autopilot` or `/autopilot`
- User says "today's content", "generate today's posts", or "run the content pipeline"
- Scheduled daily content workflow

## Workflow Overview

```
Step 1: Profile Check
  └─ profile.json exists? → Yes: continue / No: run setup-profile

Step 2.0: Series Check (NEW)
  └─ active-series.json has active series? → suggest next part

Step 2: Trend Scout
  └─ Research → 3-4 topic ideas with funnel stage tags

Step 2.5: Funnel Balance Check (content-history.json based)
  └─ Analyze content-history.json → recommend optimal funnel stage

Step 3: User Selection (primary human intervention)
  └─ User picks topic (from series, trend ideas, or custom)

Step 4: Content Writer
  └─ Title selection (auto-select #1 or user picks) → generate content

Step 5: Visual Creator
  └─ Generate images for each platform

Step 6: Output Summary
  └─ All files listed + copy-paste text displayed

Step 6.5: Record to Content History (NEW)
  └─ Append entry to content-history.json

Step 7: Optional Auto-Post (X only)
  └─ If X API credentials exist → confirm → post

Step 7.5: Engagement Suggestions (NEW)
  └─ Suggest engagement templates for today's content
```

## Detailed Steps

### Step 1: Profile Check

```python
# Pseudo-logic
if file_exists("~/.content-autopilot/profile.json"):
    profile = load("~/.content-autopilot/profile.json")
    print(f"Profile loaded: {profile.theme.main}")
    print(f"Platforms: {', '.join(profile.platforms)}")
else:
    print("No profile found. Starting setup...")
    # → Run setup-profile skill
    # → Return here after profile is created
```

### Step 2.0: Series Check (NEW)

Check if there is an active content series:

```python
# Pseudo-logic
if file_exists("~/.content-autopilot/active-series.json"):
    series_data = load("~/.content-autopilot/active-series.json")
    active = [s for s in series_data.series if s.status == "active"]
    if active:
        series = active[0]
        next_part = next(p for p in series.parts if p.status == "pending")
        print(f"Active series: {series.title}")
        print(f"Next: Part {next_part.part} — {next_part.title}")
        print(f"Platform: {next_part.platform} | Stage: {next_part.stage}")
        print(f"Hook: {next_part.hook}")
        print(f"Callback: {next_part.callback}")
        # Offer to continue series or pick a new topic
```

If active series exists, present the option:
```
Active series detected: "{series_title}" (Part {N}/{total})

1. Continue series — Part {N}: "{part_title}" ({platform})
2. Skip series today — pick a new topic instead

Select (1/2):
```

If user selects 1, skip Step 2 (Trend Scout) and go directly to Step 3 with the series part as the selected topic. Pass series metadata (hook, callback, cliffhanger) to content-writer for series mode.

If user selects 2, proceed with normal trend scout.

If no active series, skip this step silently.

### Step 2: Run Trend Scout

Invoke the `trend-scout` skill:
- Pass profile.json keywords and theme
- Receive 3 topic ideas (trending / overseas / evergreen)
- Display to user

### Step 2.5: Funnel Balance Check (content-history.json based)

If `funnel.enabled = true`, check the content history for funnel stage balance:

1. Read `~/.content-autopilot/content-history.json`
2. Filter entries from the last 7 days
3. Count TOFU/MOFU/BOFU entries
4. Display balance report:

```
直近7日のファネルバランス:
  TOFU: 4日 (57%) — 拡散重視
  MOFU: 2日 (29%) — 信頼構築
  BOFU: 1日 (14%) — マネタイズ

推奨: 今日はMOFU (信頼構築) コンテンツがおすすめです
理想バランス: TOFU 50% / MOFU 30% / BOFU 20%
```

**Ideal balance targets:**
| Stage | Target % | Purpose |
|-------|----------|---------|
| TOFU | 50% | Maximize reach and new followers |
| MOFU | 30% | Build trust and expertise credibility |
| BOFU | 20% | Drive monetization |

If balance is significantly off (>15% deviation), highlight the recommended stage in the topic selection.

If no history exists (first run), skip the balance check and note:
```
ファネル履歴: まだデータがありません（初回実行）
今日のおすすめ: TOFU — まずは拡散重視で始めましょう
```

### Step 3: User Selection

This is the **only point** where user input is required:

```
Which topic would you like to write about today?

1. [Trending] [TOFU] {title}
   → Funnel: X/Instagramで拡散向き、noteに誘導

2. [Overseas] [MOFU] {title}
   → Funnel: note無料記事で信頼構築向き

3. [Evergreen] [BOFU] {title}
   → Funnel: note有料記事でマネタイズ向き

Enter 1, 2, or 3:
```

> Funnel stage tags and recommendations appear only when `funnel.enabled = true`.

Wait for user response. Do not proceed without selection.

### Step 4: Run Content Writer

Invoke the `content-writer` skill with:
- Selected topic and angle
- Profile style settings
- Target platforms from profile

Content writer will:
1. Generate 3 title candidates (bestseller logic)
2. Ask user to pick a title (or auto-select #1 if user says "auto")
3. Generate platform-native content for each platform
4. Save files to `~/Desktop/content-autopilot-output/`

### Step 5: Run Visual Creator

Invoke the `visual-creator` skill with:
- Selected title
- Brand colors from profile
- Platform list

Visual creator will:
1. Generate (or provide prompts for) platform-specific images
2. Save images to `~/Desktop/content-autopilot-output/`

### Step 6: Output Summary

Display a complete summary of everything generated:

```
============================================
  Content Autopilot — Daily Output Summary
============================================

Date: 2026-03-18
Topic: {selected topic title}
Category: {trending/overseas/evergreen}
Funnel Stage: {TOFU/MOFU/BOFU}  ← only shown when funnel.enabled = true

--- Generated Files ---

note:
  Content: ~/Desktop/content-autopilot-output/note_2026-03-18.md
  Image:   ~/Desktop/content-autopilot-output/note_ogp_2026-03-18.png
  Type:    {free/paid} | Length: {X} chars
  Funnel:  {MOFU/BOFU} → {CTA target description}  ← omit if funnel disabled

X (Twitter):
  Content: ~/Desktop/content-autopilot-output/x_2026-03-18.md
  Image:   ~/Desktop/content-autopilot-output/x_card_2026-03-18.png
  Format:  {single/thread (N tweets)}
  Funnel:  TOFU → noteへ誘導CTA付き  ← omit if funnel disabled

Instagram:
  Content: ~/Desktop/content-autopilot-output/instagram_2026-03-18.md
  Image:   ~/Desktop/content-autopilot-output/instagram_2026-03-18.png
  Hashtags: {N} tags
  Funnel:  TOFU → noteへ誘導CTA付き  ← omit if funnel disabled

============================================

Copy-paste ready content is displayed below for each platform.
```

> When `funnel.enabled = false`, omit all "Funnel Stage" and "Funnel:" lines from the summary.

Then display the full text content for each platform, clearly separated, so the user can copy-paste directly.

### Step 6.5: Record to Content History (NEW)

After generating content, automatically append an entry to `~/.content-autopilot/content-history.json`:

```python
# Pseudo-logic
history = load_or_create("~/.content-autopilot/content-history.json")

entry = {
    "id": f"{today}-{next_sequence_number(history, today)}",
    "date": today,
    "topic": selected_topic,
    "category": topic_category,  # trending/overseas/evergreen/competitor_gap
    "funnel_stage": funnel_stage,  # TOFU/MOFU/BOFU or null
    "platforms": {
        # For each platform that content was generated for:
        "note": {
            "title": note_title,
            "file": f"note_{today}.md",
            "type": "free",  # or "paid"
            "char_count": len(note_content)
        },
        "x": {
            "title": x_title,
            "file": f"x_{today}.md",
            "format": "thread",  # or "single"
            "tweet_count": tweet_count
        },
        "instagram": {
            "title": instagram_title,
            "file": f"instagram_{today}.md",
            "hashtag_count": hashtag_count
        }
    },
    "title_logics_used": selected_title_logics,  # from content-writer
    "content_pillar": content_pillar,  # from funnel-designer or null
    "source_url": source_url,
    "source": "original",  # or "repurpose"
    "series_id": series_id,  # from active series or null
    "ab_titles": {
        "chosen": chosen_title,
        "alternative": runner_up_title,
        "winner": null  # set later with /title-winner
    }
}

history["entries"].append(entry)
save("~/.content-autopilot/content-history.json", history)
```

If content-history.json doesn't exist, create it with `{"version": "1.0", "entries": []}` first.

If writing for an active series, also update the series part status:
```python
if series_id:
    series_data = load("~/.content-autopilot/active-series.json")
    # Find the part and update status
    part.status = "published"
    part.content_file = output_filename
    save("~/.content-autopilot/active-series.json", series_data)
```

Display confirmation:
```
Content recorded in history (entry: {entry_id})
```

### Step 7: Optional X Auto-Post

Check for X API environment variables:

```bash
# Required env vars for auto-posting
X_API_KEY
X_API_SECRET
X_ACCESS_TOKEN
X_ACCESS_SECRET
```

**If X API credentials exist:**
```
X API credentials detected. Would you like to post to X now?

Preview:
{first tweet text}

Post now? (yes / no / edit first)
```

If user confirms:
1. Post single tweet or thread using X API v2
2. Display posted tweet URL
3. Report success/failure

**If X API credentials do NOT exist:**
```
X auto-posting is not configured.
To enable, set these environment variables:
  export X_API_KEY="your-key"
  export X_API_SECRET="your-secret"
  export X_ACCESS_TOKEN="your-token"
  export X_ACCESS_SECRET="your-secret"

For now, copy-paste the content above to post manually.
```

**note and Instagram:**
Auto-posting is not supported (no public API / complex OAuth).
Content is provided as copy-paste text + images.

### Step 7.5: Engagement Suggestions (NEW)

After content is ready, suggest engagement strategies:

```
--- Engagement Suggestions ---

Today's content: "{topic_title}" ({funnel_stage})

Suggested engagement actions:
1. Reply template for comments:
   "{thank_template based on content topic}"

2. Conversation starter to post alongside:
   "{conversation_starter based on content topic}"

3. Cross-platform nudge:
   "{funnel_nudge if funnel enabled, otherwise share prompt}"

Run /engagement for more templates.
```

This provides 1 template from each engagement category (thank, converse, funnel) tailored to today's specific content. The templates are brief — for full sets, direct user to `/engagement`.

## Quick Mode

If the user says `/autopilot quick` or "auto everything":
- Skip title selection (use the first candidate)
- Skip topic selection (use the #1 trending topic)
- Generate all content without intermediate confirmations
- Display final summary only

## Error Recovery

| Error | Recovery |
|-------|----------|
| Profile missing | Run setup-profile, then restart |
| WebSearch fails | Use domain knowledge for topic ideas, note the limitation |
| Image MCP unavailable | Output text prompts instead |
| X API post fails | Show error, save content for manual posting |
| Output directory not writable | Report error, ask user to create ~/Desktop/content-autopilot-output/ manually |

## Daily Consistency Tips

Display at the end of each run:

```
Tips for consistency:
- Run /autopilot at the same time each day
- Post note in the morning (highest engagement: 7-9 AM)
- Post X during lunch (12-1 PM) or evening (7-9 PM)
- Post Instagram in the evening (6-9 PM)
- Batch a week's content on Sunday with /autopilot x7 (coming soon)
```

## Output

- Text content files in `~/Desktop/content-autopilot-output/`
- Image files in `~/Desktop/content-autopilot-output/`
- Copy-paste ready content displayed in terminal
- Optional: posted tweet URL (if X API auto-post is used)

## Capability Levels

| Level | Requirements | Features |
|-------|-------------|----------|
| Level 1 | Claude Code + WebSearch | Text content only, image prompts |
| Level 2 | + gemini-image or fal.ai MCP | Text + auto-generated images |
| Level 3 | + X API credentials | Text + images + X auto-posting |
