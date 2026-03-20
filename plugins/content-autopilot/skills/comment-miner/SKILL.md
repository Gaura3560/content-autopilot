---
name: comment-miner
description: Extract content ideas from your audience's comments, replies, and questions — scan note comments, X replies, and Instagram comments for pain points, questions, and content gaps. Your audience is telling you what to write — listen.
---

# Comment Miner

Your audience is already telling you what to write about — mine their comments for gold.

## When to Activate

- User says `/comment-mine` or `/comments`
- User asks "what are my readers asking about?"
- User asks "find content ideas from comments"
- User wants to create audience-driven content

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- Published content with comments/replies to analyze

## Commands

### `/comments` — Scan recent comments across platforms
### `/comments {url}` — Analyze comments on a specific post
### `/comments questions` — Extract only questions from comments
### `/comments pain-points` — Extract frustrations and struggles

## Workflow

### Step 1: Gather Comments

**X replies:**
```
Search: "to:{x_handle}" — replies to your posts
Search: Review recent threads for reply content
```

**note comments:**
```
Search: "site:note.com/{username}" — find articles with comments
WebFetch: Read comment sections of recent articles
```

**Instagram (limited):**
```
Search: "{instagram_handle} comments"
Note: Instagram comments are harder to scrape — rely on user-provided screenshots or recent memory
```

### Step 2: Classify Comments

Categorize each meaningful comment:

| Category | Indicator | Content Opportunity |
|----------|-----------|-------------------|
| Question | "?", "how", "what", "why" | Direct answer article |
| Pain point | Frustration, "I struggle with" | Problem-solving content |
| Request | "Write about", "I wish", "Can you" | Demanded content |
| Disagreement | "But", "I think differently" | Debate/contrarian piece |
| Success story | "I tried this and" | Case study expansion |
| Confusion | "I don't understand" | Clarification/beginner content |

### Step 3: Present Findings

```
============================================
  Comment Mining Results
  Sources: {platforms scanned}
  Comments analyzed: {count}
============================================

--- Questions Your Audience Asks ---
1. "{question}" — asked by {N} people
   Source: {platform, article/post}
   Content idea: "{article title that answers this}"
   Format: {note article / X thread / carousel}
   Priority: HIGH (multiple people asked)

2. "{question}"
   Source: {platform}
   Content idea: "{title}"
   Priority: MEDIUM

3. "{question}"
   ...

--- Pain Points Detected ---
1. "{frustration/struggle}"
   Frequency: mentioned {N} times
   Content idea: "{how-to/solution article}"
   Angle: Address this directly — your audience needs it

2. "{pain_point}"
   ...

--- Direct Requests ---
1. "{request}" — "{exact comment}"
   From: {platform}
   Action: Write this — your audience literally asked for it

--- Disagreements (Debate Opportunities) ---
1. "{opposing viewpoint}" — {N} comments
   Content idea: "{title exploring both sides}"
   Format: Contrarian thread or balanced note article

--- Success Stories (Case Study Material) ---
1. "{reader's result}" — "{quote}"
   Content idea: Feature this as a case study
   Ask permission: Reach out to {commenter} for details

============================================

Top 5 Content Ideas from Your Audience:
1. {idea} — based on {N} comments asking about this
2. {idea} — direct request from audience
3. {idea} — addresses common pain point
4. {idea} — explores audience debate
5. {idea} — expands on reader success story

Feed these into /content-writer or /batch 7 to create content.
============================================
```

### Step 4: Save Insights

Save to `~/.content-autopilot/comment-insights.json` for other skills to reference.

## Integration with Other Skills

- **trend-scout**: Audience questions become a 5th idea category
- **content-writer**: Suggests addressing audience questions in content
- **series-designer**: Common questions can inspire multi-part series
- **poll-generator**: Turn disagreements into polls
- **engagement-templates**: Generate specific replies to mined comments
- **niche-monitor**: Combines audience comments with broader niche listening

## Quality Gate

- [ ] Comments are from actual audience (not fabricated)
- [ ] Questions genuinely represent audience needs
- [ ] Content ideas are specific (not just restating the question)
- [ ] Multiple sources checked for comprehensive coverage
- [ ] Frequency noted (popular questions > one-off questions)
- [ ] Privacy respected (no personal information exposed)
