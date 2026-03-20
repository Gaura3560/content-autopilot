---
name: challenge-designer
description: Community challenge designer — create 7-day or 30-day challenges that engage your audience, generate UGC (user-generated content), and grow followers through participation. Includes daily prompts, hashtag strategy, participation templates, and progress tracking.
---

# Challenge Designer

Build community through shared challenges — the highest-engagement content format.

## When to Activate

- User says `/challenge` or `/challenge 7` or `/challenge 30`
- User asks "create a challenge for my audience"
- User asks "how do I get my audience to participate?"
- User wants to boost engagement and community feeling

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Commands

### `/challenge 7` — Design a 7-day challenge
### `/challenge 30` — Design a 30-day challenge
### `/challenge status` — Check active challenge progress
### `/challenge day {N}` — Generate today's challenge content

## Workflow

### Step 1: Design the Challenge

```
Let's design your challenge!

1. Challenge theme: (related to {theme.main})
   Suggested: "{N}-Day {topic} Challenge"

2. Duration: 7 days / 30 days

3. Difficulty level:
   A) Easy — anyone can do it (5 min/day)
   B) Medium — requires some effort (15 min/day)
   C) Advanced — real commitment (30+ min/day)

4. Primary platform: X / Instagram / Both

5. Challenge hashtag:
   Suggested: #{YourName}{Topic}Challenge
   e.g., #7DayAIChallenge
```

### Step 2: Generate Challenge Plan

**7-Day Challenge:**

```
============================================
  {Challenge Name}
  Duration: 7 days | Difficulty: {level}
  Hashtag: #{hashtag}
============================================

--- Pre-Launch (Day -3 to -1) ---

Day -3: Announcement post
  "Starting {date}: {Challenge Name}!
  7 days. 1 simple task per day. Big results.
  Who's in? Reply with {emoji} to join.
  #{hashtag}"

Day -1: Rules + expectations
  "Tomorrow we start! Here's how it works:
  1. Each day I post a task
  2. Complete it and share your result with #{hashtag}
  3. I'll feature the best responses
  Ready? #{hashtag}"

--- Challenge Days ---

Day 1: "{task_title}" — Easy warm-up
  Task: {specific, achievable task}
  Time required: ~{N} min
  Post template for participants:
    "Day 1 of #{hashtag}: {what they did/learned}
    {their result/screenshot/insight}"
  Your post: {content introducing day 1 task}

Day 2: "{task_title}" — Building on Day 1
  Task: {task}
  Callback: "Yesterday you {day 1 task}. Today, take it further..."
  Post template: "Day 2..."

Day 3: "{task_title}" — Introducing the core concept
  Task: {task}
  Mid-point energy boost

Day 4: "{task_title}" — Deep dive
  Task: {task — slightly harder}

Day 5: "{task_title}" — Application
  Task: {apply what they've learned}

Day 6: "{task_title}" — Share results
  Task: {share their progress/results publicly}
  Community element: "Reply to someone else's Day 6 post with encouragement"

Day 7: "{task_title}" — Celebration + next steps
  Task: {final task — synthesis}
  Your post: "You did it! 7 days of {topic}. Here's what we accomplished:
  - {community highlight 1}
  - {community highlight 2}

  Want to go deeper? {CTA to paid content/membership}"

--- Post-Challenge ---

Day +1: Results roundup
  Feature the best participant results
  Link to resources for continuing the journey
  CTA to paid content or next challenge

Day +3: "What we learned" article
  note article summarizing challenge insights
  Include participant quotes (with permission)

============================================
```

### Step 3: Generate Daily Content

For each challenge day, generate:
1. **Your daily post** — the task announcement
2. **Participant template** — what they should post
3. **Engagement plan** — how to interact with participants
4. **Reminder post** — evening check-in

### Step 4: Hashtag and UGC Strategy

```
Challenge Hashtag Strategy:

Primary: #{hashtag} — all posts use this
Secondary: #{hashtag}Day{N} — daily tracking
Community: Encourage participants to use both

UGC (User Generated Content) plan:
  - Repost/quote the best daily responses
  - Create "challenge highlight" stories (Instagram)
  - Thread of best responses (X)
  - Feature participants in day +1 roundup article

  Permission template:
  "素晴らしい！あなたの投稿を紹介してもいいですか？ #{hashtag}"
```

### Step 5: Save Challenge Plan

Save to `~/.content-autopilot/active-challenges.json`:
```json
{
  "challenges": [
    {
      "name": "7-Day AI Challenge",
      "hashtag": "#7DayAIChallenge",
      "start_date": "2026-03-25",
      "duration": 7,
      "status": "active",
      "days": [...]
    }
  ]
}
```

Daily content saved to:
```
~/Desktop/content-autopilot-output/challenge/
  challenge_day_1.md
  challenge_day_2.md
  ...
```

## Integration with Other Skills

- **engagement-templates**: Reply templates for participant responses
- **content-writer**: Challenge posts use content-writer conventions
- **hashtag-optimizer**: Challenge hashtag optimized for discovery
- **poll-generator**: Mid-challenge polls to boost engagement
- **testimonial-framework**: Collect testimonials from challenge completers
- **weekly-report**: Challenge engagement tracked in weekly summary
- **content-analytics**: Challenge content recorded in history

## Quality Gate

- [ ] Tasks are achievable in stated time (not overwhelming)
- [ ] Difficulty escalates gradually (easy → hard)
- [ ] Each day builds on the previous
- [ ] Participant templates make it easy to join
- [ ] CTA to paid content is natural (earned, not forced)
- [ ] UGC strategy respects participant privacy
- [ ] Challenge hashtag is unique and memorable
