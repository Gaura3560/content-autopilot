---
name: repurpose
description: Transform existing content for different platforms — note to X thread, note to Instagram caption, X to note article, free to paid. Adapts depth, tone, and format while maintaining core insights. Records repurposed content in content-history.json.
---

# Content Repurpose

Transform existing content from one platform format to another, maximizing the value of every piece you create.

## When to Activate

- User says `/repurpose` or `/repurpose {file_path}`
- User says `/repurpose note->x` or `/repurpose note->instagram`
- User asks "convert this note article to X thread"
- User asks "turn this into Instagram content"
- User wants to reuse existing content on a different platform

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- Source content file or text to repurpose
- `~/.content-autopilot/content-history.json` (for recording output)

## Supported Conversions

| Source | Target | Depth Change | Strategy |
|--------|--------|-------------|----------|
| note (free) | X thread | 80% -> 30% | Extract most surprising hook, create curiosity gap |
| note (free) | Instagram | 80% -> 50% | Visual/emotional angle, key takeaways only |
| X thread | note (free) | 30% -> 80% | Expand hook into full article, add sections/data |
| note (free) | note (paid) | 80% -> 100% | Add templates, raw data, step-by-step details |
| note (paid) | X thread | 100% -> 30% | Tease premium insights, CTA to paid article |
| note (paid) | Instagram | 100% -> 50% | Visual summary of premium content |
| Instagram | X | 50% -> 30% | Sharpen the hook, make it tweetable |
| Instagram | note (free) | 50% -> 80% | Expand visual concept into detailed article |

## Workflow

### Step 1: Load Context

Read `~/.content-autopilot/profile.json` for:
- `style` — writing voice, tone
- `platforms` — active platforms
- `funnel` — CTA strategy (if enabled)

### Step 2: Identify Source Content

**If file path provided (`/repurpose {file_path}`):**
1. Read the file
2. Detect source platform from filename pattern:
   - `note_*.md` -> note
   - `x_*.md` -> X
   - `instagram_*.md` -> Instagram
3. Extract content and metadata

**If no file path provided (`/repurpose`):**
1. List recent files in `~/Desktop/content-autopilot-output/`
2. Ask user to select:
```
Recent content files:
1. note_2026-03-20.md — "7 Days to Transform Your AI Workflow"
2. x_2026-03-19.md — "AI Thread: 5 habits"
3. instagram_2026-03-18.md — "AI Workflow Tips"

Which content to repurpose? (number or file path)
```

**If conversion direction specified (`/repurpose note->x`):**
1. Use the most recent file of the source platform
2. Confirm with user before proceeding

### Step 3: Select Target Platform

If not already specified:
```
Repurpose "{source_title}" to which platform?

1. X (thread) — extract hook, 30% depth, curiosity gap
2. Instagram — visual/emotional angle, 50% depth
3. note (free) — expand to full article, 80% depth
4. note (paid) — add premium content, 100% depth

Select target: (1-4)
```

### Step 4: Analyze Source Content

Extract from the source:
1. **Core insight** — the single most valuable takeaway
2. **Supporting points** — data, examples, steps
3. **Hook potential** — most surprising or counterintuitive element
4. **Emotional angle** — relatable pain point or aspiration
5. **Actionable elements** — templates, checklists, steps

### Step 5: Generate Repurposed Content

Apply the conversion strategy based on source->target:

---

#### note -> X Thread (80% -> 30%)

**Strategy:** Extract the most surprising hook and create a curiosity gap.

1. **Tweet 1 (Hook):** The single most counterintuitive or surprising claim from the article
2. **Tweet 2-4 (Key Points):** 1 point per tweet — the most concrete, memorable insights
3. **Tweet 5 (CTA):**
   - If funnel enabled: "Full article with details -> {funnel.note_url}"
   - If funnel disabled: "Like + RT if this was useful"

**Rules:**
- Never summarize the entire article — leave 70% hidden
- Each tweet must stand alone as valuable
- Use the strongest data point or example
- Create explicit curiosity gap: "The surprising part is what happened next..."

---

#### note -> Instagram (80% -> 50%)

**Strategy:** Visual/emotional reframe with key takeaways.

1. **Hook line:** Emotional or relatable opening (visible before "more")
2. **Body (3-5 points):** Key takeaways in short, visual-friendly paragraphs
3. **CTA:**
   - If funnel enabled: "Details in profile link -> note"
   - If funnel disabled: "Save this for later"
4. **Hashtags:** Generate 30 relevant hashtags (10 big + 10 medium + 10 niche)

**Rules:**
- Lead with emotion, not information
- Use line breaks heavily
- Apply emoji per profile style settings
- Focus on "what" and "why", not detailed "how"

---

#### X -> note (30% -> 80%)

**Strategy:** Expand the hook into a complete article.

1. **Title:** Derived from the original tweet hook
2. **Introduction:** Expand the tweet's claim with context
3. **Sections (3-5):** Each supporting point becomes a full section with:
   - Explanation and context
   - Data or research backing
   - Real-world example
   - Practical application
4. **Conclusion:** Actionable summary + CTA

**Rules:**
- Research additional data to fill the depth gap
- Add at least 2 data points not in the original tweets
- Include a "how-to" section if the tweets only covered "what"
- Use WebSearch to find supporting evidence

---

#### note free -> note paid (80% -> 100%)

**Strategy:** Add premium depth layers.

Add the following to the free content:
1. **Step-by-step templates** — downloadable or copy-paste ready
2. **Raw data/research** — original analysis, spreadsheets, datasets
3. **Detailed case study** — full before/after with specific numbers
4. **Advanced techniques** — expert-level methods for experienced readers
5. **Resource list** — curated tools, links, further reading

**Split point recommendation:**
```
--- Free section (40% of total) ---
[Introduction + Problem + Overview]
--- Paid section (60% of total) ---
[Templates + Data + Case study + Advanced methods]
```

---

### Step 6: Save Output

Save repurposed content to `~/Desktop/content-autopilot-output/`:

```bash
mkdir -p ~/Desktop/content-autopilot-output
```

Filename: `repurpose_{target}_{date}.md`
- Example: `repurpose_x_2026-03-20.md`
- Example: `repurpose_instagram_2026-03-20.md`

### Step 7: Record in History

Add entry to `~/.content-autopilot/content-history.json`:

```json
{
  "id": "{date}-{seq}",
  "date": "{today}",
  "topic": "{source topic}",
  "category": "{source category}",
  "funnel_stage": "{target funnel stage}",
  "platforms": {
    "{target_platform}": {
      "title": "{repurposed title}",
      "file": "repurpose_{target}_{date}.md",
      ...
    }
  },
  "title_logics_used": [],
  "content_pillar": "{source pillar}",
  "source_url": null,
  "source": "repurpose",
  "series_id": null,
  "ab_titles": null
}
```

### Step 8: Display Result

```
============================================
  Content Repurposed
============================================

Source: {source_platform} — "{source_title}"
Target: {target_platform}
Depth: {source_depth}% -> {target_depth}%
Strategy: {strategy description}

Output: ~/Desktop/content-autopilot-output/repurpose_{target}_{date}.md

--- Content Preview ---
{first 500 chars of repurposed content}
...

Full content saved to file. Copy-paste ready content displayed below.

============================================
```

Then display the full repurposed content for copy-paste.

## Batch Repurpose

If user says `/repurpose all` or "repurpose to all platforms":
1. Take the source content
2. Generate versions for ALL target platforms (excluding the source platform)
3. Save each with appropriate filename
4. Record each in content-history.json

## Backward Compatibility

When `funnel.enabled = false`:
- Use traditional CTAs instead of funnel CTAs
- Depth differentiation rules still apply (they improve content regardless)
- No note referral CTAs in X/Instagram output

## Quality Gate

Before delivering:
- [ ] Repurposed content is genuinely different from source (not just shortened/lengthened)
- [ ] Depth matches the target platform's expected level
- [ ] CTAs match funnel settings (or traditional if disabled)
- [ ] Platform format conventions are followed (thread structure, hashtags, etc.)
- [ ] Content recorded in content-history.json with `"source": "repurpose"`
- [ ] User's writing style from profile is maintained across transformations
- [ ] No information from the source is fabricated or exaggerated in the repurpose
