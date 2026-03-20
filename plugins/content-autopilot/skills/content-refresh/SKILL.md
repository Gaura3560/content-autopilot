---
name: content-refresh
description: Update and refresh existing content with new data, examples, and insights. Identify stale content from history, research current information, and generate updated versions while preserving the original structure and voice. Boosts SEO and re-engagement.
---

# Content Refresh

Breathe new life into old content — update data, add fresh examples, and improve SEO.

## When to Activate

- User says `/refresh` or `/refresh {file_path}`
- User asks "update this old article"
- User asks "which content should I refresh?"
- User wants to improve an existing piece of content

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- Source content file to refresh
- `~/.content-autopilot/content-history.json` (for identifying stale content)

## Commands

### `/refresh {file_path}` — Refresh a specific file
### `/refresh` — Interactive: suggest stale content and choose
### `/refresh suggest` — List content candidates for refresh (no action)

## Workflow

### Step 1: Identify Content to Refresh

**If file path provided (`/refresh {file_path}`):**
1. Read the file
2. Extract date, topic, key data points
3. Proceed to Step 2

**If no file path (`/refresh` or `/refresh suggest`):**
1. Read `content-history.json`
2. Score each entry for refresh potential:

```
Refresh Score Criteria:
  +3: Published 30+ days ago
  +2: Published 14-29 days ago
  +2: Contains statistics or data (likely outdated)
  +2: Evergreen category (worth updating)
  +1: High-performing topic (worth re-promoting)
  -2: Already refreshed recently
  -1: Part of a completed series (refresh the series instead)
```

3. Present top 5 candidates:
```
Content Refresh Candidates:

1. [Score: 8] "7 AI Tools That Save 3 Hours/Day" (2026-02-15)
   Reason: 33 days old, contains tool comparisons that may have changed
   Platform: note (free) | 3,200 chars

2. [Score: 7] "The State of AI Automation in 2026" (2026-02-20)
   Reason: Contains 2026 Q1 data, Q2 data now available
   Platform: note (paid) | 4,800 chars

3. [Score: 6] "Instagram Growth Hacks for Tech Creators" (2026-03-01)
   Reason: Instagram algorithm changed since publication
   Platform: note (free) | 2,900 chars

Which content to refresh? (1-5 or file path)
```

### Step 2: Analyze Current Content

Read the source file and extract:
1. **Structure**: Headings, sections, flow
2. **Data points**: Statistics, numbers, dates, claims
3. **Examples**: Case studies, tool mentions, comparisons
4. **Links**: External references (may be broken)
5. **Key insight**: Core message/thesis

### Step 3: Research Updates

Use WebSearch to find:
1. **Updated data**: New statistics, research, reports on the topic
2. **New developments**: What changed since the original was published
3. **New examples**: Recent case studies, tools, or events
4. **Fact check**: Verify claims are still accurate
5. **Competitor coverage**: How competitors covered this topic recently

Display research findings:
```
Refresh Research Results:

Updated data found:
  - Original: "AI market size: $150B (2025)"
    Update: "AI market size: $210B (2026 Q1, Statista)"
  - Original: "ChatGPT has 100M users"
    Update: "ChatGPT has 300M users (OpenAI, March 2026)"

New developments:
  - {new tool/feature/event relevant to the topic}
  - {industry change since publication}

Outdated sections:
  - Section 3: Tool comparison needs updating (2 new tools)
  - Conclusion: CTA link may be broken

Proceed with refresh? (yes / customize)
```

### Step 4: Generate Refreshed Content

Create an updated version that:
1. **Preserves**: Original structure, voice, core thesis
2. **Updates**: Data points, statistics, examples
3. **Adds**: New sections for recent developments
4. **Removes**: Outdated or irrelevant information
5. **Improves**: SEO (better headings, updated keywords)

**Refresh levels:**
| Level | Changes | When to Use |
|-------|---------|-------------|
| Light | Update data + fix links | Content is mostly current |
| Medium | Update data + add new section + improve SEO | 1-2 months old |
| Heavy | Significant rewrite with new structure | 3+ months old or topic changed a lot |

Auto-select level based on content age and amount of outdated data.

### Step 5: Show Diff

Display a summary of changes:
```
Refresh Summary:
  Level: Medium
  Changes: 12 data points updated, 1 new section added, 2 examples replaced

  Key updates:
  - Section 2: Updated AI market data (2025 → 2026)
  - Section 4: Added new tool "ToolX" to comparison
  - New section: "2026 Q1 Developments" added after Section 5
  - Conclusion: Updated CTA and lead magnet reference

  Original: 3,200 chars → Refreshed: 3,800 chars (+19%)
```

### Step 6: Save Output

Save refreshed content:
```bash
~/Desktop/content-autopilot-output/refresh_note_{date}.md
```

If the user wants to replace the original:
```
Replace original file? (yes / keep both / no)
- yes: Overwrite the original file
- keep both: Keep original + save refreshed version
- no: Only save refreshed version to output directory
```

### Step 7: Record in History

Add entry to `content-history.json`:
```json
{
  "id": "{date}-{seq}",
  "date": "{today}",
  "topic": "{same topic}",
  "category": "{original category}",
  "source": "refresh",
  "refresh_of": "{original entry id}",
  ...
}
```

### Step 8: Cross-Platform Refresh

After refreshing the main content, offer:
```
The note article has been refreshed. Would you also like to:
1. Generate a new X thread announcing the update
2. Create an Instagram post highlighting what's new
3. Both
4. Skip

These will reference the refreshed content and drive traffic back to it.
```

## Auto-Refresh Suggestions

When running `/analytics`, content-analytics can flag stale content:
```
Refresh Candidates:
  3 articles are 30+ days old with refreshable data
  Run /refresh suggest to see details
```

## Backward Compatibility

Works identically regardless of `funnel.enabled` setting. Funnel CTAs in refreshed content follow the same rules as content-writer.

## Quality Gate

Before delivering:
- [ ] All outdated data points are updated with sources
- [ ] Original voice and structure are preserved
- [ ] New information is accurate and sourced
- [ ] Refreshed content is genuinely better (not just different)
- [ ] SEO improvements are applied (headings, keywords)
- [ ] Entry recorded in content-history.json with `source: "refresh"`
- [ ] Cross-platform refresh offered
