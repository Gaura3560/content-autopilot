---
name: competitor-scout
description: Competitive content analysis — scan competitors' note/X/Instagram content, analyze topics and title patterns, identify content gaps and differentiation opportunities. Manages competitor profiles in profile.json and stores analysis in competitor-analysis.json.
---

# Competitor Scout

Analyze your competitors' content strategy and find gaps you can exploit.

## When to Activate

- User says `/competitor-scout` or `/competitor`
- User says `/competitor add {handle}` to register a new competitor
- User asks "what are my competitors posting about?"
- User asks "what topics am I missing?"
- User wants competitive content analysis

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- At least one competitor registered in `profile.competitors` (or add one now)

## Profile Schema Addition: competitors

Added to `~/.content-autopilot/profile.json`:

```json
{
  "competitors": [
    {
      "name": "Competitor A",
      "note_url": "https://note.com/competitor_a",
      "x_handle": "@competitor_a",
      "instagram_handle": "@competitor_a_ig",
      "added_at": "2026-03-20"
    }
  ]
}
```

## Analysis Data: competitor-analysis.json

Location: `~/.content-autopilot/competitor-analysis.json`

```json
{
  "version": "1.0",
  "last_scan": "2026-03-20",
  "competitors": [
    {
      "name": "Competitor A",
      "last_scanned": "2026-03-20",
      "topics": [
        {
          "topic": "AI productivity tools",
          "frequency": "weekly",
          "platforms": ["note", "x"],
          "sample_titles": ["Title 1", "Title 2"],
          "title_patterns": ["Numbers", "Simplicity"]
        }
      ],
      "posting_frequency": {
        "note": "3/week",
        "x": "daily",
        "instagram": "2/week"
      },
      "strengths": ["Deep technical content", "Consistent posting"],
      "gaps": ["No paid content", "Weak Instagram presence"]
    }
  ],
  "gap_analysis": {
    "only_me": ["Topic A", "Topic B"],
    "only_competitors": ["Topic C", "Topic D"],
    "both_cover": ["Topic E", "Topic F"],
    "opportunities": [
      {
        "topic": "Topic C",
        "reason": "High engagement on competitor's post, not covered by you",
        "suggested_angle": "Your unique perspective on Topic C"
      }
    ]
  }
}
```

## Commands

### `/competitor add {handle}` — Register a competitor

```
Adding competitor: {handle}

Please provide:
- Name (display name):
- note URL (optional): https://note.com/...
- X handle (optional): @...
- Instagram handle (optional): @...
```

Save to `profile.json` under `competitors` array.

### `/competitor remove {name}` — Remove a competitor

Remove from `profile.json` and `competitor-analysis.json`.

### `/competitor list` — List registered competitors

```
Registered Competitors:
1. Competitor A — note: yes | X: yes | Instagram: no
   Added: 2026-03-20 | Last scanned: 2026-03-20
2. Competitor B — note: yes | X: yes | Instagram: yes
   Added: 2026-03-15 | Last scanned: 2026-03-18
```

### `/competitor-scout` — Run full analysis (default)

Execute the full competitor analysis workflow below.

## Workflow (Full Analysis)

### Step 1: Load Data

Read:
1. `~/.content-autopilot/profile.json` — user's theme, keywords, competitors
2. `~/.content-autopilot/content-history.json` — user's own content topics
3. `~/.content-autopilot/competitor-analysis.json` — previous analysis (if exists)

### Step 2: Scan Competitors

For each registered competitor:

**2a. Scan note content (if note_url provided):**
```
WebSearch: "site:note.com/{username}" — last 30 days
```
Extract:
- Recent article titles (up to 10)
- Topics and categories
- Free vs paid content split
- Posting frequency

**2b. Scan X content (if x_handle provided):**
```
WebSearch: "from:{x_handle}" — last 30 days
WebSearch: "site:x.com/{handle}" — recent popular posts
```
Extract:
- Recent tweet topics
- Thread topics
- Engagement patterns (if visible)
- Posting frequency

**2c. Scan Instagram content (if instagram_handle provided):**
```
WebSearch: "{instagram_handle} instagram" — recent activity
WebSearch: "site:instagram.com/{handle}" — recent posts
```
Extract:
- Recent post topics
- Hashtag usage
- Content format (image/carousel/reel)

### Step 3: Analyze Patterns

For each competitor:
1. **Topic clustering** — group their content into 3-5 topic categories
2. **Title pattern analysis** — identify which bestseller title logics they use
3. **Posting frequency** — how often they post on each platform
4. **Content depth** — surface-level vs. in-depth content ratio
5. **Strengths** — what they do well
6. **Weaknesses** — gaps or missed opportunities

### Step 4: Gap Analysis

Compare competitor topics vs. your own content (from content-history.json):

```
Content Gap Analysis:
============================================

Topics ONLY YOU cover:
  - {Topic A} — your competitive advantage, keep investing
  - {Topic B} — unique angle, no competition

Topics ONLY COMPETITORS cover:
  - {Topic C} ({Competitor A}, {Competitor B})
    Opportunity: {suggested angle for you}
    Suggested funnel stage: {TOFU/MOFU/BOFU}
  - {Topic D} ({Competitor A})
    Opportunity: {suggested angle}
    Suggested funnel stage: {stage}

Topics BOTH cover (competitive):
  - {Topic E} — differentiate with {your unique angle}
  - {Topic F} — differentiate with {your unique angle}

UNTAPPED topics (neither you nor competitors):
  - {Topic G} — emerging trend in {niche}
  - {Topic H} — cross-niche opportunity

============================================
```

### Step 5: Competitive Strategy

Generate 3-5 strategic recommendations:

```
Competitive Strategy Recommendations:

1. [Quick Win] Cover "{Topic C}" — competitors get high engagement,
   you haven't touched it yet. Use your {pillar} angle.

2. [Differentiation] For "{Topic E}" where you both compete,
   differentiate by {specific strategy — deeper data, different format,
   unique perspective}.

3. [Gap Exploit] {Competitor A} has no Instagram presence. Dominate
   Instagram with {theme} content to capture that audience.

4. [Title Strategy] Competitors overuse "Numbers" logic. Stand out
   with "Coined Term" or "Paradox" titles.

5. [Funnel Advantage] Competitors don't use a funnel strategy.
   Your X->note->paid pipeline is a structural advantage — lean into it.
```

### Step 6: Save Analysis

Save to `~/.content-autopilot/competitor-analysis.json` with the schema above.

### Step 7: Display Results

```
============================================
  Competitor Analysis Report
  Scanned: {date} | Competitors: {count}
============================================

{Competitor 1 name}:
  Topics: {topic1}, {topic2}, {topic3}
  Frequency: note {X}/week | X {Y}/week | Instagram {Z}/week
  Title patterns: {logic1}, {logic2}
  Strength: {key strength}
  Weakness: {key weakness}

{Competitor 2 name}:
  ...

--- Gap Analysis ---
Your exclusive topics: {count}
Competitor-only topics: {count} (opportunities!)
Competitive topics: {count}

--- Top 3 Opportunities ---
1. {opportunity with suggested action}
2. {opportunity with suggested action}
3. {opportunity with suggested action}

Full analysis saved to:
~/.content-autopilot/competitor-analysis.json

============================================
```

## Integration with Other Skills

- **trend-scout**: Adds `[Competitor Gap]` as 4th category using opportunities from gap_analysis
- **content-writer**: Can use competitor title patterns to differentiate
- **content-analytics**: Shows competitive coverage metrics
- **daily-autopilot**: Factors in competitor gaps when suggesting topics

## Backward Compatibility

- If no competitors are registered, all competitor-related features are silently skipped
- Existing skills work without changes if `competitors` array is empty or missing
- The `competitors` field in profile.json is optional

## Quality Gate

Before delivering:
- [ ] All registered competitors were scanned
- [ ] Topics are accurately extracted from search results (not fabricated)
- [ ] Gap analysis compares against actual content-history.json data
- [ ] Recommendations are specific and actionable
- [ ] competitor-analysis.json is saved with correct schema
- [ ] No private or non-public data is scraped (only public content)
