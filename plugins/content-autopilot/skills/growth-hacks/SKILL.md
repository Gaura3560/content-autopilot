---
name: growth-hacks
description: Platform-specific growth tactics — research and generate actionable growth playbooks for X, Instagram, note, YouTube, and LinkedIn. Beyond algorithm tips — specific tactical sequences to accelerate follower growth and engagement. The execution layer of algorithm-guide.
---

# Growth Hacks

Specific, tactical growth playbooks for each platform — not theory, action steps.

## When to Activate

- User says `/growth-hack` or `/growth-hack {platform}`
- User asks "how do I grow on X/Instagram?"
- User asks "what growth tactics should I use?"
- User wants to accelerate audience growth

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- Optional: algorithm-guide.json (for current platform intelligence)

## Commands

### `/growth-hack` — Playbooks for all platforms
### `/growth-hack {platform}` — Platform-specific playbook
### `/growth-hack audit` — Audit your current growth strategy

## Workflow

### Step 1: Research Current Tactics

Use WebSearch for latest growth strategies:
```
Search: "{platform} growth strategy {year}"
Search: "{platform} follower growth tactics {year}"
Search: "{platform} {niche} growth case study"
Search: "{platform} growth hacks that still work {year}"
```

### Step 2: Generate Platform Playbooks

**X Growth Playbook:**
```
============================================
  X (Twitter) Growth Playbook
  Current follower goal: {current} → {target}
============================================

--- Daily Actions (15 min/day) ---

Morning routine:
  1. Post thread/tweet at {best_time}
  2. Reply to 5 accounts in your niche (genuine, valuable replies)
  3. Quote-tweet 1 interesting post with your take

Evening routine:
  4. Reply to all comments on your posts
  5. Engage with 3 new accounts (potential followers)

--- Weekly Tactics ---

Week 1: Authority Building
  - Post 3 threads (Mon/Wed/Fri)
  - 2 single tweets with data/insights (Tue/Thu)
  - 1 personal story tweet (Sat)
  - Engage in 2 spaces related to your niche

Week 2: Network Expansion
  - Quote-tweet 3 larger accounts (add genuine value)
  - Start a thread replying to a trending topic in your niche
  - DM 3 creators for potential collaboration
  - Host or co-host a Space

--- Growth Accelerators ---

1. "Reply guy" strategy (ethical version):
   - Identify 10 large accounts in your niche
   - Be FIRST to reply with genuinely valuable insights
   - Not "great post!" — add a specific data point or perspective
   - Their audience sees your reply → follows you

2. Thread recycling:
   - Repost best-performing threads every 45+ days
   - New hook, same insights
   - /recycle handles this automatically

3. Pinned tweet optimization:
   - Pin your single best thread
   - Change monthly
   - Include CTA to follow

Expected growth: +{estimate}/month with consistent execution
============================================
```

**Instagram Growth Playbook:**
```
============================================
  Instagram Growth Playbook
============================================

--- Content Mix (weekly) ---
  Reels: 3/week (algorithm priority)
  Carousels: 2/week (highest saves)
  Single posts: 1/week
  Stories: daily (5-10 per day)

--- Daily Actions ---
  1. Post content at {best_time}
  2. Respond to all comments within 1 hour
  3. Post 5-10 stories throughout the day
  4. Engage with 10 accounts in your niche
  5. Use question/poll stickers in stories

--- Growth Tactics ---

1. Reel → Feed → Follow flywheel:
   - Reels reach non-followers (discovery)
   - Viewers visit profile → see grid
   - Compelling bio + grid → follow
   - Key: Reels hook in 1-3 seconds

2. Carousel saves strategy:
   - Save-worthy content (checklists, tips, frameworks)
   - "Save this for later" CTA
   - Saves boost algorithm ranking significantly

3. Hashtag ladder:
   - Start with niche hashtags (< 10K posts) — rank easily
   - As post gains traction, algorithm pushes to bigger hashtags
   - /hashtag handles optimal set generation

4. Collab posts:
   - Instagram's "Collab" feature shares with both audiences
   - 2x reach guaranteed
   - /collab handles partner identification

Expected growth: +{estimate}/month
============================================
```

**note Growth Playbook:**
```
============================================
  note Growth Playbook
============================================

--- Discovery Channels ---
1. note内検索 (SEO): /seo + /cluster で最適化
2. おすすめ表示: Quality + engagement signals
3. X/Instagram → note (funnel): /daily-autopilot
4. Google検索: /seo + /content-cluster

--- Growth Tactics ---

1. First 100 followers:
   - Post consistently (3/week minimum)
   - Share every article on X with engaging thread
   - Engage with other note creators (comment on their articles)
   - Join note circles/communities

2. 100-1,000 followers:
   - SEO optimization for every article (/seo)
   - Build content clusters (/cluster)
   - Start paid content (validates expertise)
   - Guest posts on larger accounts

3. 1,000+ followers:
   - Membership/magazine launch
   - Cross-platform funnel optimization
   - Collaboration with other creators
   - Content series for retention

Expected growth: +{estimate}/month
============================================
```

### Step 3: Growth Audit

```
Growth Audit: Current Strategy
============================================

Platform: {platform}
Current followers: {ask or estimate}
Posting frequency: {from content-history}
Engagement rate: {estimate}

Strengths:
  + {what you're doing well}
  + {strength}

Gaps:
  - {missing tactic 1}: {impact if implemented}
  - {missing tactic 2}: {impact}
  - {missing tactic 3}: {impact}

Priority actions (next 7 days):
  1. {most impactful quick win}
  2. {second priority}
  3. {third priority}

============================================
```

## Integration with Other Skills

- **algorithm-guide**: Growth tactics aligned with current algorithm
- **best-time**: Posting timing optimized for growth
- **collab-planner**: Collaboration as growth tactic
- **hashtag-optimizer**: Hashtag strategy for discovery
- **content-dna**: Double down on content types that drive follows
- **weekly-report**: Track growth metrics weekly

## Quality Gate

- [ ] Tactics are current and platform-specific (not generic)
- [ ] Daily actions are realistic (15-30 min/day)
- [ ] Expected growth estimates are conservative and honest
- [ ] Ethical tactics only (no follow-unfollow, bots, or spam)
- [ ] Integrated with existing Content Autopilot skills
- [ ] Growth audit is based on actual content-history data
