---
name: content-recycle
description: Automated content recycling — identify evergreen content worth re-sharing, generate reframed versions with new hooks and angles, and schedule re-posts. Different from refresh (which updates data) — recycle creates new content from old insights without changing the original.
---

# Content Recycle

Your best content deserves a second (and third) life — with fresh angles every time.

## When to Activate

- User says `/recycle` or `/recycle suggest`
- User says `/recycle {file_path}`
- User asks "what old content should I re-share?"
- User asks "repost this with a new angle"

## Prerequisites

- `~/.content-autopilot/content-history.json` with entries 30+ days old
- `~/.content-autopilot/profile.json`

## Commands

### `/recycle` — Suggest content to recycle + auto-generate
### `/recycle suggest` — Only suggest, don't generate
### `/recycle {file_path}` — Recycle a specific piece
### `/recycle schedule` — Create a monthly recycling calendar

## How Recycle Differs from Refresh and Repurpose

| Feature | Refresh | Repurpose | Recycle |
|---------|---------|-----------|---------|
| Goal | Update old content | Change platform | Re-share with new angle |
| Changes original? | Yes | No | No |
| New content created? | Updated version | New platform version | New post referencing old |
| Best for | Outdated data | Platform expansion | Evergreen content revival |
| Timing | When content is stale | Anytime | 30+ days after original |

## Workflow

### Step 1: Identify Recycle Candidates

Scan content-history.json for entries that are:
1. **30+ days old** (enough time gap)
2. **Evergreen** (not time-sensitive/trending)
3. **Not recently recycled** (no recycle within 60 days)
4. **Strong topic** (matches content DNA sweet spots if available)

Score each candidate:
```
Recycle Score:
  +3: Evergreen category
  +3: 60+ days old (more forgotten = more recyclable)
  +2: Matches content DNA sweet spot
  +2: Multiple platform potential
  +1: A/B title winner exists (proven title)
  -3: Already recycled in last 60 days
  -2: Trending/time-sensitive category
  -1: Very recent (< 30 days)
```

### Step 2: Present Candidates

```
============================================
  Content Recycle Candidates
  (sorted by recycle potential)
============================================

1. [Score: 11] "{title}" ({date}, {days} days ago)
   Category: evergreen | Stage: {MOFU}
   Original platform: note
   Recycle strategy: New X thread with fresh hook + link back
   New angle: "{suggested_new_angle}"

2. [Score: 9] "{title}" ({date}, {days} days ago)
   Category: overseas | Stage: {TOFU}
   Original platform: X thread
   Recycle strategy: Instagram carousel + note article expansion
   New angle: "{suggested_new_angle}"

3. [Score: 8] "{title}" ({date}, {days} days ago)
   ...

Recycle which? (1/2/3/all):
```

### Step 3: Generate Reframed Content

For each selected candidate, create NEW content with a FRESH angle:

**Reframing strategies:**

| Strategy | What Changes | Example |
|----------|-------------|---------|
| New hook | Different opening/angle, same content | Data hook → Story hook |
| New format | Same insights, different structure | Article → Thread → Carousel |
| Updated context | Same advice, new relevance | "Still true in {month}" |
| Different audience | Same topic, different persona | Advanced → Beginner version |
| Compilation | Combine multiple old pieces | "Best of {topic} collection" |
| Contrarian flip | Challenge your own old take | "I was wrong about {topic}" |

```
Recycled version of "{original_title}":

Original angle: {original_hook/approach}
New angle: {fresh_hook/approach}
Strategy: {strategy_name}

--- New Content ---

{Complete new content piece with fresh hook, structure,
and angle — but using the core insights from the original.
NOT a copy — a genuinely new piece that happens to cover
similar ground.}

--- Attribution ---
"Based on my earlier article: '{original_title}'"
→ Link back to original (drives new traffic to old content)
```

### Step 4: Recycle Calendar (`/recycle schedule`)

Create a monthly calendar of content to recycle:

```
============================================
  Monthly Recycle Calendar
  {month} {year}
============================================

Week 1:
  {date}: Recycle "{title}" as X thread (new hook: {hook})

Week 2:
  {date}: Recycle "{title}" as Instagram carousel

Week 3:
  {date}: Recycle "{title}" as note article (beginner version)

Week 4:
  {date}: "Best of {month}" compilation from top 3 pieces

Rules applied:
  - Max 2 recycles per week (mixed with fresh content)
  - No two recycles from the same original week
  - Varied platforms across the month
  - Fresh content still makes up 70%+ of output
============================================
```

### Step 5: Record in History

Add to content-history.json:
```json
{
  "source": "recycle",
  "recycle_of": "{original_entry_id}",
  "recycle_strategy": "{strategy_name}",
  "new_angle": "{description}"
}
```

## 30-60-90 Day Recycle Cadence

| Age | Action | Strategy |
|-----|--------|----------|
| 30 days | First recycle | New hook, same platform |
| 60 days | Second recycle | Different platform |
| 90 days | Third recycle | Different persona or compilation |
| 120+ days | Consider /refresh instead | Update data + recycle |

## Integration with Other Skills

- **content-analytics**: Shows recycle candidates in dashboard
- **batch-generator**: Includes 1-2 recycles per weekly batch
- **content-dna**: Recycled content uses DNA-optimized angles
- **persona-switcher**: Old content recycled for different personas
- **quote-card**: Extract new quote cards from old content
- **weekly-report**: Tracks recycle usage and effectiveness

## Quality Gate

- [ ] Recycled content is genuinely reframed (not just reposted)
- [ ] New hook is different from the original
- [ ] Attribution to original is included (drives traffic)
- [ ] 30+ day gap respected (audience has forgotten)
- [ ] Not over-recycling (max 30% of output is recycled)
- [ ] Recycle strategy matches the content type
- [ ] Recorded in history with correct source and recycle_of fields
