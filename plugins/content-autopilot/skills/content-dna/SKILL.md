---
name: content-dna
description: Analyze your own content history to discover what makes YOUR content work — extract patterns from high-performing pieces including hook structure, topic type, title logic combos, posting time, depth, and platform. Generates a personal "Content DNA" profile that content-writer uses to maximize future performance.
---

# Content DNA Analyzer

Discover what makes YOUR content uniquely effective — then replicate it.

## When to Activate

- User says `/dna`
- User asks "what type of content works best for me?"
- User asks "why did that post do well?"
- User wants to understand their content success patterns

## Prerequisites

- `~/.content-autopilot/content-history.json` with 10+ entries (more data = better insights)
- `~/.content-autopilot/profile.json`

## Commands

### `/dna` — Full DNA analysis
### `/dna hooks` — Analyze hook patterns only
### `/dna topics` — Analyze topic patterns only
### `/dna update` — Refresh DNA profile with latest data

## Workflow

### Step 1: Load Content History

Read `content-history.json` and gather:
- All entries with their metadata
- A/B title winners (if recorded)
- Platform-specific data (format, length, hashtag count)
- Funnel stage distribution

If fewer than 10 entries:
```
Content DNA requires 10+ entries for meaningful patterns.
Current entries: {N}. Keep creating with /daily-autopilot to build your dataset.
```

### Step 2: Pattern Extraction

**2a. Hook DNA — What openings work for you:**
```
Analyze first lines/paragraphs of all content.
Classify each hook by category (surprise/empathy/question/data/story/authority/urgency).
Cross-reference with performance signals (A/B winners, if available).

Your Hook DNA:
  Strongest type: {category} — used {N} times, {win_rate}% win rate
  Second best: {category} — used {N} times
  Weakest: {category} — used {N} times, lowest engagement
  Unused: {categories you've never tried}

  Your signature hook pattern:
  "{extracted pattern}" — this structure appears in your best content
```

**2b. Topic DNA — What subjects resonate:**
```
Cluster all topics into categories.
Identify which categories have the most entries with positive signals.

Your Topic DNA:
  Sweet spot topic: "{topic_cluster}" — {N} posts, consistently strong
  Rising topic: "{topic_cluster}" — recent trend in your content, gaining traction
  Declining topic: "{topic_cluster}" — fewer posts recently, consider refreshing angle
  Untapped: "{topic_cluster}" — adjacent to your sweet spot, haven't explored yet
```

**2c. Title Logic DNA — What title patterns convert:**
```
Analyze title_logics_used across all entries.
Cross-reference with A/B winners.

Your Title Logic DNA:
  Winning combo: {Logic A} + {Logic B} — {win_rate}% when used together
  Safe bet: {Logic C} — consistent performer, never loses badly
  Overused: {Logic D} — you use this {N}% of the time, diminishing returns
  Secret weapon: {Logic E} — rarely used but highest win rate when you do

  Recommendation: Increase {Logic E} usage from {current}% to {target}%
```

**2d. Format DNA — What structures work:**
```
Analyze content formats (thread vs single, long vs short, free vs paid).

Your Format DNA:
  X: Threads ({N}) outperform singles ({N}) — use more threads
  note: {char_range} char articles perform best
  Instagram: Carousels ({N}) vs single posts ({N}) — {recommendation}
  Optimal thread length: {N} tweets
  Optimal note length: {N} chars
```

**2e. Timing DNA — When you perform best:**
```
Analyze posting dates and days of week.
Cross-reference with best-times.json if available.

Your Timing DNA:
  Best day: {weekday} — {reason based on data}
  Best category per day: {weekday}: {category}
  Posting consistency: {score}% (affects algorithm favor)
```

**2f. Depth DNA — How deep should you go:**
```
Analyze content depth (TOFU/MOFU/BOFU) performance.

Your Depth DNA:
  TOFU content: {count} posts — {engagement_level}
  MOFU content: {count} posts — {engagement_level}
  BOFU content: {count} posts — {conversion_level}
  Ideal depth distribution: TOFU {X}% / MOFU {Y}% / BOFU {Z}%
  (May differ from default 50/30/20 based on YOUR data)
```

### Step 3: Generate DNA Profile

```
============================================
  Your Content DNA Profile
  Based on {N} content entries
  Last updated: {date}
============================================

SIGNATURE STRENGTHS:
  1. {strength_1} — "{supporting evidence}"
  2. {strength_2} — "{supporting evidence}"
  3. {strength_3} — "{supporting evidence}"

GROWTH OPPORTUNITIES:
  1. {opportunity_1} — try this in your next {N} posts
  2. {opportunity_2} — experiment with this format
  3. {opportunity_3} — this adjacent topic could be your next sweet spot

YOUR CONTENT FORMULA:
  Hook: {best_hook_type} opening
  + Topic: {sweet_spot_topic}
  + Title: {winning_logic_combo}
  + Format: {best_format} on {best_day}
  + Depth: {optimal_depth}
  = Your highest-performing content recipe

DNA SCORE: {score}/100 (how well-defined your content identity is)
  <50: Still exploring — keep experimenting
  50-70: Emerging patterns — start doubling down
  70-90: Clear identity — optimize and scale
  90+: Distinctive voice — you have a recognizable brand

============================================
```

### Step 4: Save DNA Profile

Save to `~/.content-autopilot/content-dna.json`:
```json
{
  "version": "1.0",
  "analyzed_at": "2026-03-21",
  "entries_analyzed": 45,
  "hook_dna": { "strongest": "data", "win_rate": 72, "signature_pattern": "..." },
  "topic_dna": { "sweet_spot": "AI automation", "rising": "...", "untapped": "..." },
  "title_dna": { "winning_combo": ["Numbers", "Paradox"], "secret_weapon": "Coined Term" },
  "format_dna": { "x_best": "thread", "note_optimal_length": 3200, "thread_optimal": 6 },
  "timing_dna": { "best_day": "tuesday", "best_category_per_day": {} },
  "depth_dna": { "ideal_tofu": 45, "ideal_mofu": 35, "ideal_bofu": 20 },
  "content_formula": "...",
  "dna_score": 68
}
```

## Integration with Other Skills

- **content-writer**: References content-dna.json for hook type, title logic, and format selection
- **batch-generator**: Plans the week using DNA-optimized topic/format distribution
- **trend-scout**: Prioritizes topics matching your sweet spot DNA
- **content-grader**: Bonus points when content aligns with your DNA strengths
- **hook-library**: Highlights hooks matching your strongest hook type

## Quality Gate

- [ ] Patterns extracted from actual data (not assumed)
- [ ] Sample size noted for each insight
- [ ] Low-confidence patterns flagged as "emerging" not "definitive"
- [ ] Recommendations are actionable (not just descriptive)
- [ ] DNA profile saved for other skills to reference
