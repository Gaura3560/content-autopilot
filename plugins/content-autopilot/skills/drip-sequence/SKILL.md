---
name: drip-sequence
description: Automated email drip sequence designer — create conditional email flows for different audience segments (new subscribers, purchasers, inactive readers). Goes beyond newsletters with branching logic, timing optimization, and conversion triggers.
---

# Drip Sequence Designer

Turn email into an automated conversion machine — the right message at the right time.

## When to Activate

- User says `/drip` or `/drip {sequence_type}`
- User asks "create an email sequence"
- User asks "automate my email marketing"
- User wants conditional email flows

## Prerequisites

- `~/.content-autopilot/profile.json` must exist (for funnel settings)

## Commands

### `/drip welcome` — Welcome sequence for new subscribers
### `/drip nurture` — Nurture sequence for engaged readers
### `/drip convert` — Conversion sequence for warm leads
### `/drip winback` — Win-back sequence for inactive readers
### `/drip custom` — Custom sequence with branching logic

## Sequence Types

| Type | Emails | Trigger | Goal |
|------|--------|---------|------|
| Welcome | 5-7 | New subscriber | Onboard + first purchase |
| Nurture | 7-10 | Engaged but not buying | Build trust → purchase |
| Convert | 3-5 | Viewed paid content | Close the sale |
| Win-back | 3-4 | 30+ days inactive | Re-engage |
| Post-purchase | 3-5 | After purchase | Upsell + retention |
| Launch | 7-10 | Pre-launch signup | Build to launch day |

## Workflow

### Step 1: Select Sequence Type

```
Drip sequence types:

1. Welcome — new subscriber onboarding
2. Nurture — build trust over time
3. Convert — push warm leads to buy
4. Win-back — re-engage inactive readers
5. Post-purchase — upsell and retain buyers
6. Custom — design your own flow

Select (1-6):
```

### Step 2: Generate Sequence

**Welcome Drip (7 emails, 14 days):**

```
============================================
  Welcome Drip Sequence
  Trigger: New email subscriber
  Duration: 14 days | Emails: 7
============================================

Email 1 — Immediate (Day 0)
  Subject: "{welcome_subject}"
  Purpose: Deliver lead magnet + set expectations
  Content:
    - Thank you for subscribing
    - Here's your {lead_magnet} [download link]
    - What to expect: {frequency} emails about {topic}
    - Quick win: {one actionable tip}
  CTA: Download your {lead_magnet}

Email 2 — Day 2
  Subject: "{value_subject}"
  Purpose: Deliver your #1 best content
  Content:
    - Your most popular article
    - Why readers love it
    - Key takeaway
  CTA: Read the full article
  Branch: If opened → continue / If not opened → resend with new subject on Day 4

Email 3 — Day 4
  Subject: "{story_subject}"
  Purpose: Personal connection
  Content:
    - Your origin story
    - Why you create content on {theme}
    - What drives you
  CTA: Reply and tell me your story

Email 4 — Day 7
  Subject: "{exclusive_subject}"
  Purpose: Subscriber-exclusive value
  Content:
    - Something only email subscribers get
    - Framework, template, or insider insight
  CTA: Try this today
  Branch: If clicked → tag as "engaged" / If not → keep in nurture

Email 5 — Day 9
  Subject: "{social_proof_subject}"
  Purpose: Build desire through others' results
  Content:
    - Reader testimonials
    - Case studies from your audience
    - "People like you are getting results"
  CTA: See what's possible

Email 6 — Day 11
  Subject: "{soft_pitch_subject}"
  Purpose: Introduce paid offering
  Content:
    - "You've been getting value from these emails..."
    - Natural bridge to paid content
    - What's in the paid version that's not in free
  CTA: Check out {paid_offering}
  Branch: If purchased → move to post-purchase / If not → Email 7

Email 7 — Day 14
  Subject: "{final_subject}"
  Purpose: Last chance + ongoing value
  Content:
    - Recap what they've received
    - Final soft pitch with limited-time element
    - "Either way, I'll keep sending you great content"
  CTA: {paid_offering} OR just enjoy the free content

============================================

Branching logic:
  Opened Email 2 → Standard path
  Didn't open Email 2 → Resend with new subject
  Clicked Email 4 → Tag "engaged", priority for converts
  Purchased → Exit to post-purchase sequence
  Inactive after Email 7 → Enter nurture sequence
============================================
```

### Step 3: Subject Line Variants

For each email, provide 2-3 subject options:
```
Email 1 subjects:
  A) "{option_a}" — Direct, clear
  B) "{option_b}" — Curiosity-driven
  C) "{option_c}" — Benefit-focused
```

### Step 4: Save Sequence

```
~/Desktop/content-autopilot-output/drip/
  drip_welcome_overview.md    # Sequence overview with branching
  drip_welcome_email_1.md     # Individual email content
  drip_welcome_email_2.md
  ...
  drip_welcome_email_7.md
```

## Integration with Other Skills

- **newsletter-generator**: Weekly newsletter runs parallel to drip sequences
- **lead-magnet-creator**: Lead magnet delivered in drip email 1
- **launch-sequence**: Launch drip for pre-launch signups
- **testimonial-framework**: Testimonials used in social proof emails
- **monetize-report**: Track drip sequence conversion rates

## Quality Gate

- [ ] Each email has a single clear purpose and CTA
- [ ] Timing between emails is appropriate (not too aggressive)
- [ ] Branching logic is clear and implementable
- [ ] Value is delivered before any sales pitch
- [ ] Subject lines are tested with A/B variants
- [ ] Unsubscribe-friendly (respectful, not manipulative)
