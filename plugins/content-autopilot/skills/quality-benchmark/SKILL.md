---
name: quality-benchmark
description: Benchmark content quality against your OWN best work — not generic standards. Uses your top-performing content as the gold standard, comparing structure, hook, depth, and technique. The grader scores against rules; the benchmark scores against YOUR proven best.
---

# Quality Benchmark

Your best content is the standard — new content should meet or exceed it.

## When to Activate

- User says `/benchmark {file_path}`
- User asks "is this as good as my best work?"
- User asks "compare this to my top content"
- Auto-suggested by content-grader for score calibration

## Prerequisites

- `~/.content-autopilot/content-history.json` with performance data
- At least 5 entries with performance data (to establish benchmarks)

## Commands

### `/benchmark {file_path}` — Compare against your best
### `/benchmark calibrate` — Establish benchmark standards
### `/benchmark top5` — Show your top 5 benchmark pieces

## Workflow

### Step 1: Establish Benchmarks (`/benchmark calibrate`)

From performance-logged content, identify your top performers:

```
Benchmark Calibration:
============================================

Analyzing {N} content pieces with performance data...

Your Gold Standard (top 10% by engagement):

note:
  Benchmark: "{title}" ({date}) — {rate}% engagement, {PV} PV
  What makes it great:
    Hook: {hook_type} — "{first_line}"
    Structure: {sections} sections, {chars} chars
    Depth: {MOFU}, {data_points} data points
    CTA: {cta_type} — {cta_rate}% click-through

X:
  Benchmark: "{title}" ({date}) — {rate}% engagement
  What makes it great:
    Hook: {analysis}
    Thread: {tweet_count} tweets
    CTA: {analysis}

Instagram:
  Benchmark: "{title}" ({date}) — {saves} saves
  What makes it great:
    Hook: {analysis}
    Format: {carousel/single/reel}
    Hashtags: {strategy}

Benchmarks saved to benchmark-standards.json
============================================
```

### Step 2: Compare New Content (`/benchmark {file}`)

```
============================================
  Quality Benchmark: "{new_title}"
  vs Your Gold Standard: "{benchmark_title}"
============================================

--- Structural Comparison ---

| Element | Benchmark | This Content | Gap |
|---------|-----------|-------------|-----|
| Hook type | {type} | {type} | {match/differ} |
| Hook strength | {score}/10 | {score}/10 | {+/-N} |
| Word count | {count} | {count} | {+/-N} |
| Sections | {count} | {count} | {+/-N} |
| Data points | {count} | {count} | {+/-N} |
| Examples | {count} | {count} | {+/-N} |
| CTA clarity | {score}/10 | {score}/10 | {+/-N} |

--- Technique Comparison ---

Benchmark uses:
  [x] {technique_1} — you also used this
  [x] {technique_2} — you also used this
  [ ] {technique_3} — MISSING in your new content
  [ ] {technique_4} — MISSING in your new content

--- Quality Gap ---

Benchmark score: {score}/100 (your proven best)
This content: {score}/100
Gap: {difference} points

Areas to improve to reach benchmark:
  1. Add {technique_3}: "{specific suggestion}"
  2. Strengthen hook: "{benchmark_hook}" vs yours
  3. Add {N} more data points for credibility

--- Predicted Performance ---

If published as-is: ~{predicted}% of benchmark engagement
If improvements applied: ~{predicted}% of benchmark engagement

============================================
```

## Integration with Other Skills

- **content-grader**: Benchmark score complements the generic grade
- **performance-log**: Benchmarks based on actual performance data
- **content-dna**: Benchmark techniques feed into DNA
- **engagement-predictor**: Benchmark comparison improves predictions
- **post-mortem**: Why benchmark pieces outperform — lessons captured

## Quality Gate

- [ ] Benchmarks based on actual top-performing content (not assumed)
- [ ] Comparison is element-by-element (not just overall score)
- [ ] Missing techniques are specifically identified
- [ ] Improvement suggestions are actionable
- [ ] Platform-specific benchmarks (note vs X vs IG)
