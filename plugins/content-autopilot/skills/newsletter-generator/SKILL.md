---
name: newsletter-generator
description: Email newsletter and weekly digest generator — creates engaging newsletters from recent content, behind-the-scenes insights, and curated recommendations. Supports welcome sequences, weekly digests, and standalone editions. A new funnel entry point.
---

# Newsletter Generator

Turn your content into a newsletter that builds deeper audience relationships.

## When to Activate

- User says `/newsletter` or `/newsletter weekly`
- User says `/newsletter welcome` for welcome sequence
- User asks "create a newsletter"
- User asks "write a weekly digest email"

## Prerequisites

- `~/.content-autopilot/profile.json` must exist
- `~/.content-autopilot/content-history.json` (for weekly digest)

## Commands

### `/newsletter weekly` — Generate weekly digest from this week's content
### `/newsletter {topic}` — Generate standalone newsletter on a topic
### `/newsletter welcome` — Generate 5-email welcome sequence
### `/newsletter templates` — Show available newsletter formats

## Newsletter Formats

| Format | Frequency | Content | Best For |
|--------|-----------|---------|----------|
| Weekly Digest | Weekly | Curated highlights + personal note | Consistency, low effort |
| Deep Dive | Bi-weekly | One topic in depth | Authority building |
| Curated Links | Weekly | 5-10 links with commentary | Curation-based newsletters |
| Behind the Scenes | Monthly | Process, learnings, personal stories | Community building |
| Welcome Sequence | One-time | 5-email onboarding series | New subscriber retention |

## Workflow: Weekly Digest

### Step 1: Gather This Week's Content

Read `content-history.json` for the last 7 days:
- Extract titles, topics, platforms, funnel stages
- Identify the top-performing piece (if data available)
- Note any series in progress

### Step 2: Generate Newsletter

```markdown
# {Newsletter Name} — Week of {date}

{Personal greeting — 1-2 sentences setting the context for this week}

---

## This Week's Highlights

### {Top Article Title}
{2-3 sentence summary of the key insight}
{Why this matters to the reader}
[Read the full article on note →]({note_url})

### {Second Article Title}
{2-3 sentence summary}
[Read on note →]({note_url})

### {X Thread Summary}
{The core thread in 2-3 sentences}
{Key takeaway}

---

## Behind the Scenes

{1-2 paragraphs of personal insight, process notes, or lessons learned this week}
{What you're working on, what surprised you, what's coming next}

---

## One Thing to Try This Week

{Single actionable tip or challenge for the reader}
{Make it specific and achievable in 5 minutes}

---

## Coming Next Week

{Teaser for next week's content}
{If series is active: "Part {N} of {series_title} drops on {day}"}

---

{Sign-off in your style}
{Name}

P.S. {Personal note, question to readers, or bonus link}
```

### Step 3: Subject Line Options

Generate 3 subject line options:

```
Subject Line Options:
1. "{curiosity-driven subject}" [Question + Numbers]
2. "{value-driven subject}" [Simplicity + Secret]
3. "{urgency-driven subject}" [Urgency + Paradox]

Recommended: #1 (highest open rate pattern for your audience)
```

## Workflow: Welcome Sequence

### 5-Email Welcome Sequence

```
Email 1 (Day 0): Welcome + Immediate Value
  Subject: "{welcome_subject}"
  Content:
  - Thank you for subscribing
  - Who you are and what they'll get
  - ONE immediate actionable tip (deliver value fast)
  - Lead magnet delivery (if applicable)
  CTA: Read your first article on note

Email 2 (Day 2): Your Best Content
  Subject: "{best_content_subject}"
  Content:
  - "Here's my most popular article..."
  - Summary of your top-performing content
  - Why readers love it
  CTA: Read the article

Email 3 (Day 5): Your Story
  Subject: "{story_subject}"
  Content:
  - Your origin story (why you create content on {theme})
  - Personal touch — make it human
  - Connect your journey to the reader's goals
  CTA: Reply and tell me your story

Email 4 (Day 8): Exclusive Insight
  Subject: "{exclusive_subject}"
  Content:
  - Something you only share with subscribers
  - Could be a framework, resource, or behind-the-scenes
  - Make them feel special for subscribing
  CTA: Share this with a friend who'd benefit

Email 5 (Day 12): Soft Pitch
  Subject: "{pitch_subject}"
  Content:
  - Recap the value they've received
  - Introduce your paid offering naturally
  - "If you've been getting value from these emails..."
  CTA: Check out {paid_content/membership}
```

## Personalization

All newsletters are personalized using `profile.json`:
- **Tone**: Match `style.tone`
- **Emoji**: Match `style.emoji_usage`
- **Theme references**: Use `theme.main` and `theme.keywords`
- **Funnel CTAs**: If funnel enabled, all links point to note
- **Lead magnet**: Reference in welcome sequence

## Save Output

```
~/Desktop/content-autopilot-output/
  newsletter_weekly_{date}.md
  newsletter_welcome_1.md through newsletter_welcome_5.md
  newsletter_{topic}_{date}.md
```

## Quality Gate

- [ ] Subject lines follow proven open-rate patterns
- [ ] Content is scannable (headers, short paragraphs, bold key phrases)
- [ ] Every newsletter delivers at least one concrete value
- [ ] CTA is clear and single-focused per email
- [ ] Personal tone maintained (not corporate)
- [ ] Welcome sequence has escalating engagement
- [ ] Links to note content are included (funnel integration)
