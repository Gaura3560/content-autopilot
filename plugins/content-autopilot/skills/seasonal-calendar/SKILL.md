---
name: seasonal-calendar
description: Seasonal and event-based content calendar — maps industry events, holidays, seasonal trends, and cultural moments to content opportunities. Auto-suggests timely topics for trend-scout and batch-generator integration.
---

# Seasonal Calendar

Never miss a timely content opportunity — plan around events, seasons, and cultural moments.

## When to Activate

- User says `/seasonal` or `/seasonal {month}`
- User asks "what events are coming up?"
- User asks "what should I write about this month?"
- Referenced by batch-generator and trend-scout for topic suggestions

## Prerequisites

- `~/.content-autopilot/profile.json` must exist (for theme and niche)

## Commands

### `/seasonal` — Show next 30 days of events and opportunities
### `/seasonal {month}` — Show events for a specific month (e.g., `/seasonal april`)
### `/seasonal add {date} {event}` — Add a custom event
### `/seasonal year` — Show full year overview

## Workflow

### Step 1: Load Context

Read `profile.json` for:
- `theme.main` and `theme.keywords` — to filter relevant events
- `audience` — to prioritize audience-relevant events

### Step 2: Build Event Calendar

Combine three event sources:

**2a. Universal Japanese Calendar Events:**
```
January: New Year, Coming of Age Day, year-start planning
February: Valentine's Day, tax season starts
March: Graduation, year-end, cherry blossom forecasts
April: New fiscal year, new school year, new hires
May: Golden Week, Mother's Day, spring cleanup
June: Rainy season, Father's Day, mid-year review
July: Summer begins, Obon prep, summer sales
August: Obon, summer vacation, back-to-school prep
September: Silver Week, autumn begins, Q3 review
October: Halloween, sports day, reading season
November: Black Friday, year-end prep, 七五三
December: Year-end reviews, Christmas, New Year prep
```

**2b. Niche-Specific Events (via WebSearch):**
```
Search: "{theme} conferences {year}"
Search: "{theme} events Japan {year}"
Search: "{keyword} product launches {year}"
Search: "{niche} industry trends {month} {year}"
```

Extract:
- Industry conferences and expos
- Product launches and announcements
- Regulatory changes and deadlines
- Seasonal trends specific to the niche

**2c. Custom Events (from seasonal-calendar.json):**
- User-added events via `/seasonal add`
- Recurring events from previous years

### Step 3: Map Events to Content Opportunities

For each event, suggest content angles:

```
============================================
  Seasonal Content Calendar
  {start_date} — {end_date} (30 days)
============================================

--- Week 1 ({date range}) ---

{date} ({weekday}) — {Event Name}
  Content angle: "{suggested topic connecting event to your niche}"
  Platform: {best platform for this topic}
  Funnel stage: {TOFU/MOFU/BOFU}
  Timing: Post {N} days before event for maximum relevance
  Priority: {High/Medium/Low}

{date} ({weekday}) — {Event Name}
  Content angle: "{suggested topic}"
  Platform: {platform}
  Funnel stage: {stage}
  Timing: {timing advice}
  Priority: {priority}

--- Week 2 ({date range}) ---
...

--- Niche Events ---

{date} — {Industry Conference/Launch}
  Content angle: "{pre-event analysis / live coverage / post-event takeaways}"
  Platform: X (real-time) + note (deep dive)
  Timing: Pre-event (1 week before), during, post-event (2-3 days after)

--- Monthly Theme ---
Overarching theme: "{monthly theme connecting events}"
Suggested pillar focus: {content pillar that aligns}

============================================
```

### Step 4: Content Timing Strategy

For each event, recommend a content timeline:

```
Event: {event_name} ({event_date})

Timeline:
  -7 days: [TOFU] Awareness post on X — "Did you know {event} is coming?"
  -3 days: [MOFU] note article — "How to prepare for {event}"
  -1 day:  [TOFU] Instagram post — Visual countdown/checklist
   0 days: [TOFU] X live thread — Real-time coverage/commentary
  +1 day:  [MOFU] note article — "Key takeaways from {event}"
  +3 days: [BOFU] note (paid) — "Complete {event} action plan"
```

### Step 5: Save Calendar

Save to `~/.content-autopilot/seasonal-calendar.json`:
```json
{
  "version": "1.0",
  "generated_at": "2026-03-20",
  "events": [
    {
      "date": "2026-04-01",
      "name": "New Fiscal Year",
      "type": "national",
      "niche_relevance": "high",
      "content_angles": [
        {
          "topic": "AI tools for the new fiscal year",
          "platform": "note",
          "funnel_stage": "MOFU",
          "timing": "post 2 days before"
        }
      ],
      "custom": false
    }
  ],
  "custom_events": []
}
```

## Custom Event Management

### `/seasonal add {date} {event}`

```
Added custom event:
  Date: 2026-04-15
  Event: "Product X Launch"

  Auto-generated content angles:
  1. Pre-launch teaser (X, 3 days before)
  2. Launch day coverage (X thread + Instagram)
  3. Deep analysis (note, 2 days after)

  Save these angles? (yes / edit)
```

## Integration with Other Skills

- **trend-scout**: Checks seasonal-calendar.json for upcoming events when generating ideas
- **batch-generator**: Includes seasonal events in weekly topic selection
- **daily-autopilot**: Mentions upcoming events in topic suggestions
- **series-designer**: Can build series around major events

## Quality Gate

Before delivering:
- [ ] Events are accurate and correctly dated
- [ ] Content angles are specific to user's niche (not generic)
- [ ] Timing recommendations account for content creation lead time
- [ ] Both national/cultural events and niche events are included
- [ ] Custom events are preserved and included
- [ ] Calendar data is saved for other skills to reference
