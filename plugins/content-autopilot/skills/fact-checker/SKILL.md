---
name: fact-checker
description: Verify every claim, statistic, and data point in your content before publishing — WebSearch-powered source verification, URL validation, recency check, and citation formatting. The single most important precision skill — everything else assumes facts are correct.
---

# Fact Checker

Every number, every claim, every "according to..." — verified before it goes live.

## When to Activate

- User says `/fact-check {file_path}` or `/fact-check`
- User asks "verify the facts in this"
- User asks "are these numbers accurate?"
- Auto-suggested by content-grader and pre-publish for any content with data claims

## Prerequisites

- Content file to verify

## Commands

### `/fact-check {file_path}` — Verify all claims in a file
### `/fact-check quick {file_path}` — Verify numbers and stats only
### `/fact-check url {file_path}` — Verify all URLs are live and correct

## Claim Types to Verify

| Claim Type | Example | Verification Method |
|-----------|---------|-------------------|
| Statistic | "87% of AI projects fail" | WebSearch for original source |
| Fact | "GPT-4 was released in March 2023" | WebSearch for date/fact |
| Quote | "As Steve Jobs said..." | Verify attribution |
| URL | "[source](https://...)" | WebFetch to check if live |
| Recency | "The latest data shows..." | Check if data is actually recent |
| Comparison | "X is faster than Y" | Verify benchmark source |
| Number | "saves 3 hours per day" | Check if claim is substantiated |

## Workflow

### Step 1: Extract All Claims

Scan content and extract every verifiable claim:
```
Extracted {N} verifiable claims from "{title}":

1. [STAT] "87% of AI projects fail" (line 15)
2. [FACT] "OpenAI released GPT-4 in March 2023" (line 23)
3. [NUMBER] "saves an average of 3 hours per day" (line 31)
4. [URL] "https://example.com/study" (line 35)
5. [QUOTE] "As Peter Drucker said: '...'" (line 42)
6. [RECENCY] "According to the latest 2026 report..." (line 48)

Verifying...
```

### Step 2: Verify Each Claim

For each claim, run WebSearch:

```
Search: "{exact claim}" source
Search: "{statistic}" original study
Search: "{quote}" attribution
```

### Step 3: Present Results

```
============================================
  Fact Check Report: "{title}"
  Claims verified: {N}
============================================

VERIFIED (source confirmed):
  1. [STAT] "87% of AI projects fail"
     Source: Gartner 2023 Report
     Status: VERIFIED — but data is from 2023, consider noting the year
     Suggested citation: "87% (Gartner, 2023)"

  2. [FACT] "GPT-4 released March 2023"
     Source: OpenAI blog, March 14, 2023
     Status: VERIFIED

UPDATED NEEDED:
  3. [NUMBER] "saves 3 hours per day"
     Source: Found similar claim at 2.5 hours (McKinsey 2024)
     Status: INACCURATE — update to "saves up to 2.5 hours"
     Fix: Replace "3 hours" with "2.5 hours (McKinsey, 2024)"

  4. [RECENCY] "latest 2026 report"
     Source: Report found but dated January 2026
     Status: OUTDATED — newer data available (March 2026)
     Fix: Update to latest version

UNVERIFIABLE:
  5. [NUMBER] "productivity increases by 5x"
     Source: No credible source found for this specific claim
     Status: UNVERIFIABLE — add qualifier or remove
     Fix: "productivity can significantly increase" or cite a specific study

BROKEN LINKS:
  6. [URL] "https://example.com/study"
     Status: 404 NOT FOUND
     Fix: Find updated URL or remove link

--- Summary ---
  Verified: {count}/{total}
  Needs update: {count}
  Unverifiable: {count}
  Broken links: {count}

  Accuracy score: {percentage}%
  Action required: {yes/no}

============================================

Auto-fix all issues? (yes / select / no)
```

### Step 4: Auto-Fix

For each issue:
- Replace inaccurate numbers with verified ones
- Add citations in "(Source, Year)" format
- Update broken URLs or remove them
- Add qualifiers to unverifiable claims
- Update "latest" to specific dates

### Step 5: Citation Formatting

Format all citations consistently:
```
Citation style options:
1. Inline: "87% of projects fail (Gartner, 2023)"
2. Footnote: "87% of projects fail [1]" → References section
3. Link: "87% of projects fail ([source](url))"

Select style (1/2/3):
```

## Integration with Other Skills

- **content-writer**: Fact-check data points gathered during research
- **content-grader**: Accuracy score included in overall grade
- **pre-publish**: Mandatory fact-check for content with statistics
- **affiliate-writer**: Verify product claims
- **compliance-checker**: Fact accuracy supports legal compliance
- **content-refresh**: Re-verify facts when refreshing old content

## Quality Gate

- [ ] Every statistic has a verified source
- [ ] All URLs are live and point to correct content
- [ ] Quotes are correctly attributed
- [ ] "Latest" claims reference actually recent data
- [ ] Unverifiable claims are flagged (not silently passed)
- [ ] Citations are formatted consistently
- [ ] Disclaimer: WebSearch verification has limits — critical claims warrant manual verification
