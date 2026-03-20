---
name: strategy-test
description: Test entire content strategies — not individual elements like A/B tests, but holistic approaches. "TOFU-heavy vs BOFU-heavy for 2 weeks" or "daily posting vs 3x/week." The forest-level experiment that determines your overall direction.
---

# Strategy Test

A/B tests tweak the tree. Strategy tests redesign the forest.

## When to Activate

- User says `/strategy-test` or `/strategy-test new`
- User asks "should I post daily or 3x a week?"
- User wants to compare fundamentally different approaches

## Commands

### `/strategy-test new` — Design a new strategy experiment
### `/strategy-test status` — Active experiment status
### `/strategy-test results` — Analyze completed experiments

## Testable Strategies

| Strategy Pair | Duration | Key Metric |
|--------------|----------|-----------|
| Daily posting vs 3x/week | 4 weeks | Total engagement + revenue |
| TOFU-heavy vs BOFU-heavy | 4 weeks | Revenue + follower growth |
| Thread-focused vs article-focused | 4 weeks | Engagement + traffic |
| Original vs curated mix (70/30 vs 50/50) | 4 weeks | Authority + engagement |
| Single platform vs cross-platform | 4 weeks | Total reach + conversions |
| Short-form vs long-form focus | 4 weeks | Audience growth rate |

## Workflow

### Step 1: Design Experiment

```
Strategy Experiment Design:
============================================

Hypothesis: "{strategy_A} will generate more {metric} than {strategy_B}"

Strategy A (weeks 1-2): {detailed description}
  Posting: {frequency}
  Focus: {platform/format/stage}
  Content mix: {ratio}

Strategy B (weeks 3-4): {detailed description}
  Posting: {frequency}
  Focus: {platform/format/stage}
  Content mix: {ratio}

Controlled variables:
  [x] Total effort/time per week (equal)
  [x] Topic quality (similar)
  [x] Posting times (same schedule)

Success metrics:
  Primary: {metric} (e.g., total revenue)
  Secondary: {metric} (e.g., follower growth)
  Tertiary: {metric} (e.g., engagement rate)

Duration: 4 weeks (2 per strategy)
Start date: {date}

============================================
```

### Step 2: Track During Experiment

```
Strategy Test: Week {N} of 4
Active strategy: {A or B}

Week 1 results (Strategy A):
  {metric_1}: {value}
  {metric_2}: {value}
  Notes: {observations}

Week 2 results (Strategy A):
  {metric_1}: {value}
  {metric_2}: {value}

[Switching to Strategy B on {date}]
```

### Step 3: Analyze Results

```
============================================
  Strategy Test Results
============================================

Strategy A: {name}
  Revenue: ¥{total}
  Followers gained: {N}
  Avg engagement: {rate}%

Strategy B: {name}
  Revenue: ¥{total}
  Followers gained: {N}
  Avg engagement: {rate}%

Winner: Strategy {A/B}
  Primary metric: {A/B} wins by {margin}
  Secondary: {A/B} wins by {margin}

Confidence: {level} (4-week test, {conditions})

Recommendation:
  Adopt Strategy {winner} as your default.
  Next test: {suggested follow-up experiment}

============================================
```

## Integration

- **ab-test-runner**: Element tests (tree); strategy tests (forest)
- **weekly-report**: Strategy test progress in report
- **content-dna**: Winning strategy updates DNA recommendations
- **advisor**: Strategy test results inform all future advice
- **workflow-chain**: Winning strategy becomes a workflow

## Quality Gate

- [ ] Only ONE strategy variable changes (not multiple)
- [ ] Equal effort/time invested in both strategies
- [ ] Duration sufficient for meaningful comparison (4+ weeks)
- [ ] Multiple metrics tracked (not just one)
- [ ] External factors noted (seasonal, platform changes)
