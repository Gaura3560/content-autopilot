---
name: bio-optimizer
description: Profile and bio optimization across X, Instagram, and note — craft compelling bios with USP, social proof, CTA, and keywords. The bio is where 80% of follow decisions happen. Includes link-in-bio strategy and profile audit.
---

# Bio Optimizer

Your bio is your storefront — optimize it for follows, clicks, and trust.

## When to Activate

- User says `/bio` or `/bio {platform}`
- User asks "optimize my profile"
- User asks "write a better bio"
- User wants more profile visits to convert to follows

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Commands

### `/bio` — Optimize bios for all platforms
### `/bio {platform}` — Optimize for specific platform (x/instagram/note)
### `/bio audit` — Audit current bios for issues
### `/bio link` — Optimize link-in-bio strategy

## Bio Anatomy (Universal)

Every effective bio needs these 4 elements:

| Element | Purpose | Example |
|---------|---------|---------|
| **Who** | Identity/credential | "AI researcher" / "3x founder" |
| **What** | Value proposition | "Sharing AI tools that save 3hrs/day" |
| **Proof** | Social proof/number | "50K+ readers" / "Featured in Forbes" |
| **CTA** | Next action | "Free guide ↓" / "Latest article ↓" |

## Workflow

### Step 1: Gather Current Profile Info

```
Let's optimize your bios. Current info:

1. Your one-line identity (who are you?):
   Current: {from profile or ask}
2. Your key achievement or credential:
   Current: {from profile or ask}
3. What value do you provide to followers?
   Current: {from profile or ask}
4. Any social proof numbers?
   (follower count, article count, years of experience)
```

### Step 2: Generate Platform-Specific Bios

**X Bio (160 chars max):**
```
Option A (Achievement-led):
"{credential} | {value_prop} | {social_proof} | {CTA} ↓"

Option B (Value-led):
"{value_prop} | {who_you_are} | {proof} | Free: {lead_magnet}"

Option C (Personality-led):
"{personality_hook} | {what_you_share} | {CTA}"

Character counts: A: {N}/160 | B: {N}/160 | C: {N}/160
```

**Instagram Bio (150 chars + 5 link sections):**
```
Line 1: {identity + credential}
Line 2: {value proposition}
Line 3: {social proof}
Line 4: {emoji} {CTA}
Link: {link-in-bio URL}

Highlights suggested:
  1. "About" — your story
  2. "Tips" — best carousel saves
  3. "Free" — lead magnet
  4. "Reviews" — testimonials
  5. "{Topic}" — content category
```

**note Profile:**
```
Display name: {optimized name with keyword}

Bio (long-form allowed):
  Paragraph 1: {who you are + credential}
  Paragraph 2: {what readers get from following}
  Paragraph 3: {social proof + achievements}
  Paragraph 4: {CTA — what to read first}

Header image: {suggestion for brand-consistent header}
Pinned article: Recommend pinning "{best_article_title}"
```

### Step 3: Keyword Optimization

For each platform, ensure searchable keywords:
```
Keywords to include in your bio:
  Primary: {keyword_1} (your main topic)
  Secondary: {keyword_2}, {keyword_3}

  X: Put primary keyword in name field (searchable)
  Instagram: Put keywords in name field (searchable, separate from @handle)
  note: Keywords in bio text improve internal search ranking
```

### Step 4: Link-in-Bio Strategy (`/bio link`)

```
Link-in-Bio Optimization:

Current setup: {assessed}

Recommended structure:
  1. {Primary CTA link} — your current focus (paid article/lead magnet)
  2. {Secondary link} — your best free content
  3. {Evergreen link} — your #1 most valuable resource
  4. {Social link} — cross-platform (note URL on X, X handle on IG)

Tools: Linktree, Lit.link, or note profile page as hub

Update frequency: Change link #1 weekly to match latest content
```

### Step 5: Bio Audit (`/bio audit`)

```
Bio Audit Results:
============================================

X Bio:
  [ ] Identity clear? {yes/no — fix: ...}
  [ ] Value proposition present? {yes/no}
  [ ] Social proof included? {yes/no}
  [ ] CTA present? {yes/no}
  [ ] Keywords in name field? {yes/no}
  [ ] Link is current? {yes/no}
  Score: {score}/100

Instagram Bio:
  [ ] All 4 elements present? {yes/no}
  [ ] Highlights set up? {yes/no}
  [ ] Link-in-bio working? {yes/no}
  [ ] Profile/Reel grid consistent? {yes/no}
  Score: {score}/100

note Profile:
  [ ] Bio complete? {yes/no}
  [ ] Pinned article set? {yes/no}
  [ ] Header image brand-consistent? {yes/no}
  Score: {score}/100

Priority fix: {the single highest-impact change}
============================================
```

## Quality Gate

- [ ] Bios are within platform character limits
- [ ] All 4 elements (who/what/proof/CTA) are present
- [ ] Keywords are included for search discoverability
- [ ] Tone matches brand voice from profile.json
- [ ] Link-in-bio strategy is coherent with funnel
- [ ] Each platform bio is different (not copy-pasted)
