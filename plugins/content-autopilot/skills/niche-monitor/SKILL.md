---
name: niche-monitor
description: Social listening and niche monitoring — continuously scan X, note, and industry sources for conversations, questions, and trends in your niche. Identifies content opportunities, audience pain points, and emerging topics. The always-on version of trend-scout.
---

# Niche Monitor

Stay on top of every conversation in your niche — find content opportunities before anyone else.

## When to Activate

- User says `/listen` or `/listen {keyword}`
- User asks "what's happening in my niche?"
- User asks "what questions are people asking about {topic}?"
- User wants real-time niche intelligence

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Commands

### `/listen` — Scan all tracked keywords and topics
### `/listen {keyword}` — Monitor a specific keyword
### `/listen questions` — Find questions your audience is asking
### `/listen viral` — Find viral content in your niche
### `/listen add {keyword}` — Add a keyword to monitor
### `/listen remove {keyword}` — Remove a keyword

## Data: monitor-keywords.json

Location: `~/.content-autopilot/monitor-keywords.json`

```json
{
  "version": "1.0",
  "keywords": [
    {
      "keyword": "AI automation",
      "source": "profile",
      "added_at": "2026-03-20"
    },
    {
      "keyword": "ChatGPT business",
      "source": "manual",
      "added_at": "2026-03-20"
    }
  ],
  "last_scan": "2026-03-20"
}
```

Auto-populated from `profile.json` keywords on first run.

## Workflow

### Step 1: Gather Keywords

Read monitor-keywords.json (or create from profile.json keywords on first run).

### Step 2: Multi-Source Scan

**2a. X Conversations:**
```
Search: "{keyword}" — recent, high engagement
Search: "{keyword} ?" — questions being asked
Search: "{keyword}" filter:replies — active discussions
```
Extract: Hot discussions, questions, complaints, praise

**2b. note Trends:**
```
Search: "site:note.com {keyword}" — recent articles
Search: "note.com {keyword} trending"
```
Extract: Popular articles, trending topics, content gaps

**2c. Industry Sources:**
```
Search: "{keyword} news {year}"
Search: "{keyword} announcement"
Search: "{keyword} update"
```
Extract: News, product launches, regulatory changes

**2d. Questions People Ask:**
```
Search: "{keyword} とは"
Search: "{keyword} やり方"
Search: "{keyword} おすすめ"
Search: "{keyword} 比較"
Search: "People Also Ask" results for "{keyword}"
```
Extract: Frequently asked questions → content opportunities

### Step 3: Analyze and Categorize

```
============================================
  Niche Monitor Report
  Scanned: {date} | Keywords: {count}
============================================

--- Hot Conversations ---
1. {conversation_summary}
   Source: X | Engagement: {high/medium}
   Opportunity: {how to join or create content about this}

2. {conversation_summary}
   Source: note | Engagement: {high/medium}
   Opportunity: {content angle}

--- Questions Your Audience Is Asking ---
1. "{question}"
   Source: X / Google
   Content idea: "{article title that answers this}"
   Format: {note article / X thread / carousel}

2. "{question}"
   Source: note comments
   Content idea: "{title}"

3. "{question}"
   ...

--- Emerging Trends ---
1. {trend_description}
   Signal strength: {early/growing/established}
   Content opportunity: "{title idea}"
   Timing: Write within {N} days for first-mover advantage

--- Viral Content in Your Niche ---
1. "{title}" by {author} ({platform})
   Why it went viral: {analysis}
   Your angle: "{how to cover this differently}"

2. "{title}" by {author}
   Why it went viral: {analysis}
   Your angle: "{differentiation}"

--- Sentiment Overview ---
Positive buzz: {topics people are excited about}
Frustrations: {pain points people are complaining about}
Gaps: {questions with no good answers yet}

============================================

Top 3 Content Opportunities:
1. {highest priority opportunity with suggested format}
2. {second priority}
3. {third priority}

Feed these into /trend-scout or /content-writer to create content.
============================================
```

### Step 4: Save Report

Save to `~/.content-autopilot/monitor-reports/`:
```
monitor_{date}.json
```

## Integration with Other Skills

- **trend-scout**: Uses monitor data for more targeted topic suggestions
- **content-writer**: Audience questions become content hooks
- **competitor-scout**: Combines competitive data with niche conversations
- **series-designer**: Trending conversations can inspire series topics
- **engagement-templates**: Join conversations identified by the monitor

## Quality Gate

- [ ] All scanned conversations are real (not fabricated)
- [ ] Opportunities are specific and actionable
- [ ] Questions reflect actual audience needs
- [ ] Trend signals distinguish between early/established trends
- [ ] Viral content analysis explains WHY it worked
- [ ] Report is concise enough to be useful (not overwhelming)
