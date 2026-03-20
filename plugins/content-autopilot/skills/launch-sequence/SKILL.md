---
name: launch-sequence
description: Product/course launch campaign planner — designs a 14-day multi-channel launch sequence with pre-launch teasers, launch day content, post-launch follow-up, and urgency escalation. Covers X, Instagram, note, and email across TOFU/MOFU/BOFU stages.
---

# Launch Sequence

Plan and execute a high-converting product or course launch across all your channels.

## When to Activate

- User says `/launch` or `/launch {product_name}`
- User asks "plan my product launch"
- User asks "how should I launch my course/ebook/membership?"
- User is preparing to release paid content

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- Product/service details from the user

## Commands

### `/launch {product_name}` — Design a full launch sequence
### `/launch status` — Check active launch progress
### `/launch templates` — Show available launch frameworks

## Launch Frameworks

| Framework | Duration | Best For |
|-----------|----------|----------|
| Quick Launch | 7 days | Simple product, existing audience |
| Standard Launch | 14 days | Courses, ebooks, memberships |
| Extended Launch | 30 days | High-ticket products, large campaigns |

## Workflow

### Step 1: Gather Product Details

```
Let's plan your launch! Tell me about your product:

1. Product name:
2. Product type: (paid article / ebook / course / membership / service)
3. Price: ¥___
4. Launch date:
5. Target audience (or use profile.json):
6. Key benefit (one sentence):
7. What makes it different from free content:
8. Any bonuses or limited-time offers:
9. Scarcity element: (limited seats / early bird / launch price)
```

### Step 2: Design 14-Day Sequence

```
============================================
  Launch Sequence: "{product_name}"
  Launch Date: {date} | Duration: 14 days
============================================

=== Phase 1: Pre-Launch (Day -14 to Day -8) ===
Theme: Problem Awareness + Curiosity

Day -14 | X thread + Instagram
  TOFU: "{problem-focused title}"
  Goal: Highlight the pain point your product solves
  Hook: "Most people struggle with {problem}..."
  NO mention of the product yet

Day -13 | note (free article)
  MOFU: "{deep dive into the problem}"
  Goal: Establish expertise on this topic
  CTA: "I'm working on something to solve this. Stay tuned."

Day -12 | X single tweet
  TOFU: "{surprising stat about the problem}"
  Goal: Build curiosity

Day -11 | Instagram carousel
  TOFU: "{5 signs you have this problem}"
  Goal: Reader self-identification

Day -10 | X thread
  MOFU: "{your journey solving this problem}"
  Goal: Personal story → credibility

Day -9 | note (free article)
  MOFU: "{partial solution — free version of your method}"
  Goal: Deliver value, show expertise, create desire for more

Day -8 | X + Instagram
  TOFU: "{teaser — something big is coming}"
  Goal: Build anticipation
  CTA: "Announcement coming this week..."

=== Phase 2: Launch Week (Day -7 to Day 0) ===
Theme: Solution Reveal + Social Proof

Day -7 | X thread + note
  MOFU: "I've been working on {product} for {time}..."
  Goal: Behind-the-scenes, build connection
  Show: Process, early results, beta feedback

Day -5 | X + Instagram
  MOFU: "{testimonial or beta user result}"
  Goal: Social proof
  CTA: "Launch in 5 days..."

Day -3 | note (free article)
  MOFU: "{final free value bomb — best content yet}"
  Goal: Peak trust before asking for money
  CTA: "On {date}, I'm releasing the complete system..."

Day -1 | X + Instagram
  TOFU: "Tomorrow: {product_name} goes live"
  Goal: Maximum anticipation
  Include: What's inside, price, bonuses

=== Phase 3: Launch Day (Day 0) ===
Theme: The Offer

Day 0 | ALL platforms
  BOFU: "{product_name} is LIVE"
  X: Launch announcement thread (10 tweets)
  Instagram: Carousel with product overview
  note: Sales article (free intro + paid content)
  Email: Launch email to subscribers

  Thread structure:
  1. "It's here: {product_name}"
  2. "What's inside:" (feature list)
  3. "Who it's for:" (target audience)
  4-6. "Here's what you'll learn:" (key benefits)
  7. Social proof (testimonials/results)
  8. Bonuses (limited time)
  9. Price + link
  10. "Early bird price ends {date}" (urgency)

=== Phase 4: Post-Launch (Day +1 to Day +7) ===
Theme: Urgency + Social Proof + Objection Handling

Day +1 | X + note
  BOFU: "{first buyer results/reactions}"
  Goal: FOMO from social proof

Day +2 | Instagram + X
  BOFU: "FAQ: {common objection addressed}"
  Goal: Remove friction

Day +3 | note (free article)
  MOFU: "{related valuable content — not a sales pitch}"
  Goal: Keep delivering value, subtle reminder

Day +5 | X + Instagram
  BOFU: "Bonus expires in 48 hours"
  Goal: Urgency escalation

Day +7 | ALL platforms
  BOFU: "Last chance: {product_name} at launch price"
  Goal: Final push, cart close energy
  X: Countdown thread
  Instagram: Final carousel with key benefits
  note: Updated sales article with testimonials
  Email: "Final hours" email

============================================
```

### Step 3: Generate Content for Each Day

For each day in the sequence:
1. Generate the actual content (not just titles)
2. Follow content-writer platform conventions
3. Apply funnel CTAs
4. Use appropriate thread templates from thread-templates skill

### Step 4: Save Launch Plan

Save to `~/.content-autopilot/launch-plans/`:
```
launch_{product_name}_{date}.md — Full launch plan
```

Save individual day content to:
```
~/Desktop/content-autopilot-output/launch/
  day_-14_x.md
  day_-14_instagram.md
  day_-13_note.md
  ...
  day_0_all.md
  ...
  day_+7_all.md
```

### Step 5: Track Progress

Active launch tracking via `/launch status`:
```
Launch: "{product_name}"
Phase: {current_phase}
Progress: Day {current} / Day +7

[x] Day -14: Problem awareness (X + IG) — published
[x] Day -13: Deep dive (note) — published
[ ] Day -12: Stats tweet (X) — TODAY
[ ] Day -11: Carousel (IG) — tomorrow
...

Next action: Post "{content_title}" on {platform}
```

## Integration with Other Skills

- **content-writer**: Generates actual content for each launch day
- **visual-creator**: Creates launch images and graphics
- **thread-templates**: Uses proven thread structures for launch threads
- **carousel-generator**: Creates launch carousels
- **newsletter-generator**: Creates launch email sequence
- **engagement-templates**: Reply templates for launch day comments
- **monetize-report**: Track launch revenue

## Quality Gate

- [ ] Launch builds gradually (no hard sell before Day -7)
- [ ] Free value delivered before asking for money
- [ ] Social proof included where possible
- [ ] Urgency is genuine (real deadlines, real scarcity)
- [ ] Every platform has appropriate content format
- [ ] CTA is clear on launch day and post-launch
- [ ] Objections are addressed proactively
