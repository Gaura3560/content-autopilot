---
name: ab-test-runner
description: Systematic A/B testing framework for all content elements — not just titles but hooks, structures, CTAs, posting times, hashtags, and formats. Design controlled experiments, track results, and auto-update content-dna with findings. The scientific approach to content optimization.
---

# A/B Test Runner

Stop guessing. Test everything systematically — one variable at a time.

## When to Activate

- User says `/ab-test` or `/ab-test {element}`
- User asks "should I test this?"
- User asks "which approach works better?"
- User wants to optimize a specific content element

## Prerequisites

- `~/.content-autopilot/content-history.json` with performance data (from /perf-log)
- `~/.content-autopilot/profile.json`

## Data: ab-tests.json

Location: `~/.content-autopilot/ab-tests.json`

```json
{
  "version": "1.0",
  "tests": [
    {
      "id": "test-001",
      "element": "hook_type",
      "hypothesis": "Data hooks outperform question hooks on X",
      "variant_a": { "type": "data_hook", "content_id": "2026-03-20-001" },
      "variant_b": { "type": "question_hook", "content_id": "2026-03-22-001" },
      "control_variables": ["topic", "posting_time", "format", "length"],
      "metric": "engagement_rate",
      "status": "running",
      "started_at": "2026-03-20",
      "results": null,
      "winner": null,
      "confidence": null
    }
  ]
}
```

## Testable Elements

| Element | How to Test | Minimum Tests |
|---------|------------|---------------|
| Hook type | Same topic, different opening | 3 pairs |
| Title logic | Same content, different title | 3 pairs |
| Posting time | Same content type, different time | 5 tests |
| CTA type | Same content, different CTA | 3 pairs |
| Thread length | Same topic, different tweet count | 3 pairs |
| Content depth | Same topic, TOFU vs MOFU | 3 pairs |
| Hashtag set | Same post, different hashtags | 3 pairs |
| Format | Same topic, thread vs single | 3 pairs |
| Emoji usage | With vs without emoji | 3 pairs |
| First person vs third | Same insight, different voice | 3 pairs |

## Commands

### `/ab-test` — Show active tests and suggest new ones
### `/ab-test new {element}` — Design a new test
### `/ab-test results` — Show completed test results
### `/ab-test apply` — Apply winning findings to content-dna

## Workflow

### Step 1: Design Test (`/ab-test new hook_type`)

```
============================================
  A/B Test Design
============================================

Element to test: Hook type
Hypothesis: "{suggested hypothesis based on content-dna}"

--- Test Design ---

Variable: Hook opening type
  Variant A: Data hook — "87% of..."
  Variant B: Question hook — "What if...?"

Controlled variables (keep the same):
  [x] Topic: {same topic for both}
  [x] Platform: {same platform}
  [x] Posting time: {same time window}
  [x] Content length: {similar length}
  [x] CTA: {same CTA}

Success metric: {engagement_rate / likes / saves / link_clicks}

Test duration: {N} content pairs over {N} weeks
  Pair 1: Data hook (Mon) vs Question hook (Wed)
  Pair 2: Data hook (next Mon) vs Question hook (next Wed)
  Pair 3: Data hook (following Mon) vs Question hook (following Wed)

Minimum sample: 3 pairs needed for meaningful results

Start this test? (yes / modify / different element)
```

### Step 2: Track During Test

When generating content during an active test:
```
Active A/B test: Hook type
  This content should use: Variant {A/B} (data hook)
  Controlled variables: {checklist}

Content-writer will use the specified variant.
Log performance with /perf-log after publishing.
```

### Step 3: Analyze Results (`/ab-test results`)

```
============================================
  A/B Test Results
============================================

Test: Hook type — Data vs Question hooks
Status: COMPLETE (3 pairs tested)

--- Results ---

Variant A (Data hooks):
  Avg engagement rate: {rate}%
  Avg likes: {count}
  Avg saves: {count}
  Results: {pair1}, {pair2}, {pair3}

Variant B (Question hooks):
  Avg engagement rate: {rate}%
  Avg likes: {count}
  Avg saves: {count}
  Results: {pair1}, {pair2}, {pair3}

--- Winner ---

Winner: Variant {A/B} ({type} hooks)
  Margin: +{difference}% engagement
  Confidence: {high/medium/low} (based on {N} tests)
  Consistency: Won {N}/{total} pairs

--- Insight ---

"{hook_type} hooks generate {X}% higher engagement on {platform}
for {topic} content. This pattern was consistent across {N} tests."

Apply to content-dna? (yes / need more data / no)

============================================
```

### Step 4: Apply Findings (`/ab-test apply`)

When applying winning findings:
```
Applying A/B test results to content-dna:

Updated: content-dna.json
  hook_dna.strongest: "data" (confirmed by A/B test, {N} pairs)
  Previously: "data" (estimated from history)
  Change: Estimate → Confirmed (confidence: high)

Updated: smart-cta preferences (if CTA test)
Updated: best-times adjustment (if timing test)
Updated: content-writer defaults (if format test)

All future content generation will use these confirmed findings.
```

### Step 5: Suggest Next Test

```
Suggested next A/B test:

Based on your data, the highest-impact untested element is: {element}
  Current assumption: {what we assume}
  Test hypothesis: "{hypothesis}"
  Expected insight: This could improve {metric} by ~{estimate}%

Design this test with /ab-test new {element}
```

## Testing Calendar

```
A/B Testing Schedule:
  Week 1-2: Test hook types (3 pairs)
  Week 3-4: Test posting times (5 tests)
  Week 5-6: Test CTA types (3 pairs)
  Week 7-8: Test thread lengths (3 pairs)

  After 8 weeks: content-dna will be data-confirmed, not estimated.
```

## Integration with Other Skills

- **performance-log**: REQUIRED — A/B tests need real performance data
- **content-dna**: Test results confirm or override DNA estimates
- **content-writer**: Uses active test variants when generating
- **engagement-predictor**: Predictions calibrated by test results
- **smart-cta**: CTA tests improve CTA recommendations
- **best-time**: Timing tests improve posting time recommendations
- **weekly-report**: Active tests and results included in report

## Quality Gate

- [ ] Only ONE variable changes per test (everything else controlled)
- [ ] Minimum 3 pairs for meaningful results
- [ ] Performance data is actual (from /perf-log, not estimated)
- [ ] Confidence level honestly reflects sample size
- [ ] Findings applied to content-dna with test evidence
- [ ] Next test suggested based on highest-impact untested element
