---
name: trend-scout
description: Trend research and topic suggestion engine — searches the web for trending topics in the user's niche, analyzes overseas articles, and proposes 3-4 content ideas categorized as trending, overseas-sourced, evergreen, or competitor gap with funnel stage tags (TOFU/MOFU/BOFU). Reads profile.json and content-history.json for personalized, non-repeating results.
---

# Trend Scout

Find trending topics in your niche and propose 3 ready-to-write content ideas.

## When to Activate

- User says `/trend-scout`
- Called automatically by `daily-autopilot`
- User asks "what should I write about today?"
- User wants content ideas or topic research

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- If missing, instruct user to run `/setup-profile` first

## Workflow

### Step 1: Load Profile

Read `~/.content-autopilot/profile.json` and extract:
- `theme.keywords` — search terms
- `theme.main` — primary topic area
- `audience` — who the content is for
- `platforms` — which platforms to optimize for
- `funnel.enabled` — whether funnel mode is active

### Step 1.5: Load Content History (NEW — Dedup)

Read `~/.content-autopilot/content-history.json` (if it exists) and extract:
- Topics from the last 30 days
- Build a dedup list of recent topics

**Dedup rules:**
- Exact topic match within 14 days → skip
- Similar topic (>70% keyword overlap) within 7 days → skip
- Same category used 3+ times in last 7 days → prefer other categories

If content-history.json doesn't exist, skip dedup (first run).

Also load `~/.content-autopilot/competitor-analysis.json` (if it exists) for competitor gap opportunities.

### Step 2: Research (3 Parallel Searches)

Run these searches concurrently using WebSearch:

**Search A — Trending Topics (Japanese)**
```
Search queries (use theme keywords):
- "{keyword} 最新 2026"
- "{keyword} トレンド"
- "{keyword} 話題"
```
Look for: news articles, trending discussions, viral posts from the last 7 days.

**Search B — Overseas Articles (English)**
```
Search queries:
- "{keyword} latest trends 2026"
- "{keyword} new research"
- "{keyword} industry report"
```
Look for: articles, research papers, case studies not yet covered in Japanese media.

**Search C — X (Twitter) Trends**
```
Search queries:
- "{keyword}" (filter by recent, high engagement)
- "site:x.com {keyword}"
```
Look for: viral posts, debates, announcements in the niche.

### Step 3: Analyze and Filter

For each search result:
1. Score relevance to the user's theme (0-10)
2. Check recency (prefer last 7 days for trending, any time for evergreen)
3. Check if the topic has been covered to death (avoid saturated topics)
4. **Check against content-history.json dedup list** (NEW) — skip topics already covered in the last 14 days
5. Identify a unique angle the user can take

If a high-scoring topic was recently covered, note it but suggest a different angle:
```
Note: "{topic}" was covered on {date}. Suggesting a fresh angle instead.
```

### Step 4: Propose 3 Ideas

Present exactly 3 content ideas in this format:

```
## Today's Content Ideas

### 1. [Trending] [TOFU] {Title Idea}
- Cut: {unique angle or perspective}
- Why now: {why this is timely}
- Source: {reference URL}
- Platforms: {recommended platforms for this topic}
- Funnel: X/Instagramで拡散向き、noteへの誘導に最適

### 2. [Overseas] [MOFU] {Title Idea}
- Cut: {unique angle — translate/localize overseas insight for Japanese audience}
- Why now: {why Japanese audience would care}
- Source: {reference URL}
- Platforms: {recommended platforms}
- Funnel: note無料記事で信頼構築向き

### 3. [Evergreen] [BOFU] {Title Idea}
- Cut: {unique angle on a timeless topic}
- Why now: {evergreen but with a fresh twist}
- Source: {reference URL or "original insight"}
- Platforms: {recommended platforms}
- Funnel: note有料記事でマネタイズ向き

### 4. [Competitor Gap] [TOFU/MOFU] {Title Idea} (NEW — if competitor data exists)
- Cut: {your unique angle on a topic competitors cover but you don't}
- Why now: {competitor gets engagement on this, your audience would benefit}
- Source: Competitor analysis ({competitor name})
- Platforms: {recommended platforms}
- Funnel: {funnel recommendation based on topic depth}

Which one would you like to write about? (1 / 2 / 3 / 4)
```

> **Note**: The 4th idea `[Competitor Gap]` appears only when `~/.content-autopilot/competitor-analysis.json` exists and has gap opportunities.
> If no competitor data exists, present 3 ideas as before.

> **Note**: Funnel stage tags ([TOFU]/[MOFU]/[BOFU]) and "Funnel:" lines appear only when `funnel.enabled = true`.
> When funnel is disabled, omit the `[TOFU]`/`[MOFU]`/`[BOFU]` tags from headings and remove the "Funnel:" line from each idea.
> The rest of the format remains identical.

### Step 5: User Selection

Wait for the user to choose one of the 3 ideas. Store the selection for use by `content-writer`.

If called by `daily-autopilot`, pass the selection forward automatically.

## Funnel Stage Assignment (when funnel.enabled = true)

Each content idea receives a funnel stage tag based on these criteria:

| Stage | Tag | Content Characteristics | Best Platforms |
|-------|-----|------------------------|----------------|
| TOFU (Top of Funnel) | `[TOFU]` | Broad appeal, trending, beginner-friendly, SNS-optimized | X, Instagram |
| MOFU (Middle of Funnel) | `[MOFU]` | Intermediate depth, specific methods, case studies | note (free) |
| BOFU (Bottom of Funnel) | `[BOFU]` | Advanced, templates/tools, original data, detailed guides | note (paid) |

**Assignment rules:**
- Trending topics → usually TOFU (high virality, broad reach)
- Overseas insights → usually MOFU (unique value, builds expertise credibility)
- Evergreen topics → usually BOFU (deep, actionable, worth paying for)
- Override the default if the specific angle suggests a different stage

## Category Definitions

| Category | Definition | Source Priority |
|----------|-----------|----------------|
| Trending | Hot topic in the last 7 days, high social engagement | Japanese news, X trends |
| Overseas | Insight from English-language sources not yet covered in Japanese | English articles, research, case studies |
| Evergreen | Timeless topic with a fresh angle or new data | Any, with a current hook |
| Competitor Gap | Topic competitors cover successfully but you haven't addressed | competitor-analysis.json gap_analysis |

## Fallback Behavior

If WebSearch returns insufficient results:
1. Broaden search queries (remove specific keywords, use theme.main only)
2. If still insufficient, generate ideas from domain knowledge with a note:
   ```
   Note: Web search returned limited results. These ideas are based on
   domain knowledge of {theme.main}. Consider running again later for
   fresher trends.
   ```

## Optional: Deep Research with firecrawl

If `firecrawl` MCP is available:
- Use `firecrawl_scrape` to extract full article content from promising URLs
- Summarize key points for richer content ideas
- Extract data/statistics that can be cited in the content

If firecrawl is not available, rely on WebSearch snippets only.

## Output

- 3 content ideas with titles, angles, sources, and platform recommendations
- User's selected idea (passed to content-writer)

## Quality Gate

Before presenting ideas:
- [ ] All 3 ideas are genuinely different (not variations of the same topic)
- [ ] Each idea has a specific, actionable angle (not just a broad topic)
- [ ] Sources are real and accessible
- [ ] Ideas match the user's theme and audience from profile.json
- [ ] At least one idea leverages overseas content (differentiation advantage)
- [ ] No idea duplicates a topic from the last 14 days (content-history.json dedup)
- [ ] If competitor data exists: at least one [Competitor Gap] idea is included
- [ ] If funnel enabled: each idea has a funnel stage tag (TOFU/MOFU/BOFU)
- [ ] If funnel enabled: funnel recommendations explain the strategic fit
