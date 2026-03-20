---
name: trend-predictor
description: Predict upcoming trends before they peak — analyze early signals from overseas markets, search volume trajectories, niche conversations, and technology adoption curves. Get first-mover advantage by publishing before the wave hits.
---

# Trend Predictor

Write about tomorrow's trends today — be the first, not the tenth.

## When to Activate

- User says `/trend-predict` or `/predict`
- User asks "what's going to be big next month?"
- User asks "what trends should I watch?"
- User wants first-mover advantage on emerging topics

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Commands

### `/predict` — Predict trends for the next 30 days
### `/predict {niche}` — Predict for a specific niche
### `/predict signals` — Show raw signals being tracked
### `/predict track {keyword}` — Add a keyword to trend tracking

## Prediction Methodology

### Signal Sources (ranked by predictive power)

| Source | Lead Time | Reliability | How to Detect |
|--------|-----------|-------------|---------------|
| Overseas English content | 2-6 months | High | English articles on topic not yet in Japanese |
| Academic papers | 3-12 months | High | New research being discussed on X by experts |
| VC/funding news | 1-3 months | Medium | Companies raising money in the space |
| Search volume trajectory | 2-4 weeks | High | Rising search interest (not yet peaked) |
| X expert conversations | 1-3 weeks | Medium | Early adopters discussing a new concept |
| Product launches | 1-2 weeks | High | New tool/product announcement |
| Reddit/HackerNews buzz | 1-4 weeks | Medium | Early tech adopter discussions |

## Workflow

### Step 1: Scan Prediction Signals

**1a. Overseas-to-Japan pipeline:**
```
Search: "{keyword} new trend" (English)
Search: "{keyword} emerging" (English)
Search: "{keyword} 2026 predictions" (English)
```
Filter: Topics discussed in English but NOT YET in Japanese media.

**1b. Search volume signals:**
```
Search: "{keyword} rising searches"
Search: "Google Trends {keyword}"
Search: "{keyword} とは" — if this is rising, people are discovering it
```

**1c. Expert signal:**
```
Search: Leading voices in {niche} on X — what are they talking about NOW
Search: "{keyword}" from:known_expert accounts
```

**1d. Product/funding signals:**
```
Search: "{niche} startup funding {year}"
Search: "{niche} product launch {month} {year}"
Search: "Product Hunt {keyword}"
```

### Step 2: Score and Rank Predictions

For each detected signal:

```
Prediction Score:
  Signal strength: {1-5} (how many independent sources)
  Lead time: {1-5} (how much time before mainstream)
  Relevance: {1-5} (how well it fits your niche)
  Content potential: {1-5} (can you write something valuable?)
  Competition: {1-5} (how few Japanese creators cover this)
  Total: {sum}/25
```

### Step 3: Present Predictions

```
============================================
  Trend Predictions — Next 30 Days
  Your niche: {theme.main}
============================================

--- High Confidence (score 20+) ---

1. [Score: 23/25] "{predicted_trend}"
   Signal: {primary_signal_source}
   Lead time: ~{weeks} weeks before mainstream
   Why now: {explanation}
   Japanese coverage: {none / minimal / growing}
   Content opportunity:
     Week 1: [TOFU] X thread — "What is {trend}?"
     Week 2: [MOFU] note article — "How {trend} works"
     Week 3: [BOFU] note (paid) — "Complete {trend} guide"
   First-mover advantage: {HIGH / MEDIUM}

2. [Score: 21/25] "{predicted_trend}"
   ...

--- Medium Confidence (score 15-19) ---

3. [Score: 17/25] "{predicted_trend}"
   Signal: {source}
   Lead time: ~{weeks} weeks
   Risk: {what could make this prediction wrong}
   Content opportunity: {brief suggestion}

4. [Score: 15/25] "{predicted_trend}"
   ...

--- Watch List (score 10-14) ---
5. "{emerging_topic}" — too early to write, but monitor
6. "{emerging_topic}" — needs more signals

============================================

Recommendation:
  Publish NOW on prediction #1 — estimated {N} days
  before Japanese mainstream coverage.

  Use /content-writer to create the content.
  Use /series 7 to build authority on this topic.

============================================
```

### Step 4: Save Predictions

Save to `~/.content-autopilot/trend-predictions.json`:
```json
{
  "version": "1.0",
  "predicted_at": "2026-03-21",
  "predictions": [
    {
      "trend": "...",
      "score": 23,
      "lead_time_weeks": 3,
      "signals": [],
      "status": "predicted",
      "outcome": null
    }
  ]
}
```

Track outcomes: When a prediction comes true, update `status` to `"confirmed"` for calibration.

## Integration with Other Skills

- **trend-scout**: Includes high-confidence predictions as 5th category
- **batch-generator**: Prioritizes predicted trends for first-mover content
- **seasonal-calendar**: Predicted trends added to upcoming events
- **series-designer**: Build series around predicted trends before competition
- **niche-monitor**: Feeds raw signals into prediction engine

## Quality Gate

- [ ] Predictions based on multiple independent signals
- [ ] Lead time is realistic (not too late, not too speculative)
- [ ] Risk/uncertainty clearly stated for each prediction
- [ ] Content opportunity is actionable and specific
- [ ] Japanese coverage gap is verified (not already mainstream)
- [ ] Previous predictions tracked for accuracy calibration
