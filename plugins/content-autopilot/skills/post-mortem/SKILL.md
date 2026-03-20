---
name: post-mortem
description: Structured post-publish analysis — understand WHY content performed well or poorly by cross-referencing actual performance data with content elements (hook, structure, topic, timing, CTA). Generates lessons that auto-feed into content-dna, hook-library, and smart-cta.
---

# Post-Mortem Analysis

Every post teaches you something — but only if you analyze it. Turn results into reusable lessons.

## When to Activate

- User says `/post-mortem {date}` or `/post-mortem`
- User asks "why did this post do well/poorly?"
- User asks "what can I learn from this week's content?"
- Auto-suggested after performance data is logged

## Prerequisites

- `~/.content-autopilot/content-history.json` with performance data
- Content files to analyze

## Commands

### `/post-mortem {date}` — Analyze a specific post
### `/post-mortem week` — Analyze this week's content
### `/post-mortem best` — Deep dive on your best-performing content
### `/post-mortem worst` — Deep dive on your worst-performing content

## Workflow

### Step 1: Select Content

```
Content with performance data available:

1. "{title}" ({date}) — engagement: {rate}% — {HIGH/AVG/LOW}
2. "{title}" ({date}) — engagement: {rate}% — {HIGH/AVG/LOW}
3. "{title}" ({date}) — engagement: {rate}% — {HIGH/AVG/LOW}

Analyze which? (number / "best" / "worst" / "all")
```

### Step 2: Element-by-Element Analysis

```
============================================
  Post-Mortem: "{title}"
  Published: {date} on {platform}
  Performance: {rate}% engagement ({percentile} percentile)
============================================

--- Element Analysis ---

Hook: "{first_line}"
  Type: {hook_type}
  Your avg for this type: {avg_rate}%
  This post: {rate}%
  Verdict: {OUTPERFORMED / UNDERPERFORMED / ON PAR}
  Lesson: {specific insight}

Title: "{title}"
  Logics: {logic_combo}
  Your avg for this combo: {avg}%
  This post: {rate}%
  Verdict: {result}
  Lesson: {insight}

Topic: "{topic}"
  Category: {category}
  Your avg for this topic: {avg}
  This post: {value}
  Verdict: {result}

Timing: {posted_at}
  Optimal for {platform}: {best_time}
  Deviation: {minutes} {early/late}
  Impact: {estimated_impact}

Structure: {format}
  Length: {chars} chars (your optimal: {optimal_range})
  Sections: {count} (your optimal: {optimal})
  Verdict: {result}

CTA: "{cta_text}"
  Type: {cta_type}
  Click-through: {rate}%
  Your avg CTA rate: {avg}%
  Verdict: {result}

Hashtags (if IG): {count} tags
  Tier distribution: {big/medium/niche counts}
  New vs repeated: {ratio}
  Verdict: {result}

--- Root Cause Analysis ---

Why this post {overperformed/underperformed}:

Primary factor: {element} — {explanation}
  Evidence: {data point}

Contributing factors:
  1. {factor} — {explanation}
  2. {factor} — {explanation}

External factors:
  - {timing event, trending topic, competitor activity, etc.}

--- Lessons Learned ---

1. KEEP: {what worked and should be repeated}
   → Auto-save to: {content-dna / hook-library / smart-cta}

2. CHANGE: {what didn't work and should be modified}
   → Auto-save to: {content-dna}

3. TEST: {hypothesis generated from this analysis}
   → Suggested A/B test: {test_description}

============================================
```

### Step 3: Auto-Feed Lessons

```
Lessons auto-saved:

1. content-dna.json updated:
   - hook_dna: {type} confirmed as {strong/weak} (+{data_point})
   - topic_dna: {topic} moved to {sweet_spot/declining}

2. hook-library.json updated:
   - "{hook}" tagged with performance: {high/low}

3. smart-cta preferences updated:
   - "{cta_type}" effectiveness: {up/down} based on this data

4. ab-tests.json updated:
   - New hypothesis added: "{hypothesis from this analysis}"

All future content generation will reflect these lessons.
```

### Step 4: Weekly Post-Mortem (`/post-mortem week`)

```
============================================
  Weekly Post-Mortem — {date_range}
============================================

Total content: {count} pieces
Avg engagement: {rate}% (vs overall avg: {overall}%)

Best: "{title}" — {rate}% (top {percentile}%)
  Key success factor: {factor}

Worst: "{title}" — {rate}% (bottom {percentile}%)
  Key failure factor: {factor}

Pattern discovered this week:
  "{insight that emerged from comparing multiple posts}"

Lessons for next week:
  1. {actionable lesson}
  2. {actionable lesson}
  3. {actionable lesson}

============================================
```

## Integration with Other Skills

- **performance-log**: REQUIRED — post-mortem needs real data
- **content-dna**: Lessons update DNA patterns
- **hook-library**: Hook performance tagged
- **smart-cta**: CTA effectiveness updated
- **ab-test-runner**: Generates new test hypotheses
- **weekly-report**: Post-mortem insights in weekly summary
- **engagement-predictor**: Calibrates prediction model

## Quality Gate

- [ ] Analysis based on actual performance data (not guesses)
- [ ] Root cause analysis is specific (not "post didn't perform well")
- [ ] Lessons are actionable and auto-saved to relevant skills
- [ ] External factors considered (not just content quality)
- [ ] Hypotheses generated for future A/B testing
- [ ] Weekly patterns identified (not just individual post analysis)
