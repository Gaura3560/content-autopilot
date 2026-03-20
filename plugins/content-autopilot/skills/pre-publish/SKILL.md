---
name: pre-publish
description: Pre-publish checklist for every platform — catch missing images, broken links, wrong hashtag counts, formatting issues, and CTA gaps before posting. The "one final check" that prevents embarrassing mistakes.
---

# Pre-Publish Checklist

The last check before you hit publish — catch every mistake that costs you engagement.

## When to Activate

- User says `/pre-publish {file_path}` or `/check {file_path}`
- User says `/pre-publish all` to check all today's content
- User asks "is this ready to post?"
- Auto-suggested by daily-autopilot before publishing

## Prerequisites

- Content file(s) to check

## Commands

### `/check {file_path}` — Run checklist on a specific file
### `/check all` — Check all today's content
### `/check {platform}` — Platform-specific checklist only

## Platform Checklists

### note Checklist

```
note Pre-Publish Checklist: "{title}"
============================================

Content:
  [ ] Title present and compelling
  [ ] Lead paragraph hooks within first 2 lines
  [ ] H2 headings present (3-7 recommended): {found: N}
  [ ] Content length: {chars} chars {within 2,000-5,000: yes/no}
  [ ] No orphan sentences (paragraphs ≤ 3 sentences)
  [ ] Conclusion/summary section present
  [ ] No placeholder text remaining ("{...}", "TODO", "TBD")

Media:
  [ ] OGP/thumbnail image set (1200x630)
  [ ] Images have descriptions/context
  [ ] No broken image references

Links:
  [ ] All URLs are valid and working
  [ ] Internal links to other articles present: {count}
  [ ] External source links present: {count}
  [ ] No "example.com" or placeholder URLs

SEO:
  [ ] Target keyword in title
  [ ] Keyword in first 100 chars
  [ ] Note excerpt (meta description) is compelling

CTA:
  [ ] Clear CTA present at the end
  [ ] CTA matches funnel stage
  [ ] Like/follow prompt included

Monetization (if paid):
  [ ] Free/paid split point is natural
  [ ] Free section provides enough value to demonstrate expertise
  [ ] Paid section is clearly worth the price
  [ ] Price is set correctly

Score: {passed}/{total} checks passed
Status: {READY / FIX REQUIRED}
============================================
```

### X Checklist

```
X Pre-Publish Checklist: "{title}"
============================================

Thread structure:
  [ ] Tweet 1 is a scroll-stopping hook
  [ ] Each tweet ≤ 280 chars: {all_pass: yes/no}
      {If no: Tweet {N} is {chars}/280 — trim {excess} chars}
  [ ] Thread numbering consistent (if used)
  [ ] Each tweet adds unique value (no filler)
  [ ] Last tweet has clear CTA

Content:
  [ ] No typos in first tweet (highest visibility)
  [ ] @mentions are correct
  [ ] Hashtags: {count} (recommended: 1-3 for X)
  [ ] No placeholder text
  [ ] Thread length: {N} tweets (optimal: 5-10)

Media:
  [ ] Image/card attached to tweet 1 (2-3x engagement boost)
  [ ] Image dimensions correct (1200x675)
  [ ] Alt text considered

Links:
  [ ] URLs shortened or using proper format
  [ ] note link working (if funnel CTA)
  [ ] No broken links

Score: {passed}/{total}
Status: {READY / FIX REQUIRED}
============================================
```

### Instagram Checklist

```
Instagram Pre-Publish Checklist: "{title}"
============================================

Caption:
  [ ] Hook visible before "more" fold (first 125 chars)
  [ ] Line breaks for readability
  [ ] Caption length: {chars} (recommended: 300-500)
  [ ] No placeholder text
  [ ] Emoji usage matches profile style

Hashtags:
  [ ] Hashtag count: {N}/30
  [ ] 3-tier distribution (big/medium/niche)
  [ ] No banned/restricted hashtags
  [ ] Not repeating exact set from last 3 days
  [ ] Placement: {in caption / first comment}

Media:
  [ ] Image/carousel ready
  [ ] Dimensions correct (1080x1080 or 1080x1350)
  [ ] Text readable at mobile size
  [ ] Brand colors consistent
  [ ] Carousel: cover slide works standalone in feed

CTA:
  [ ] Clear action requested (save/share/comment/link)
  [ ] Profile link updated to match CTA

Score: {passed}/{total}
Status: {READY / FIX REQUIRED}
============================================
```

## Auto-Fix

For each failed check, offer a fix:
```
Issues found: {count}

1. [X] Tweet 3 is 295/280 chars
   Fix: Remove "{suggested_words}" → 278 chars
   Apply fix? (yes / no / manual)

2. [Instagram] Only 22/30 hashtags
   Fix: Add these 8 tags: {generated tags}
   Apply fix? (yes / no / manual)

3. [note] No CTA at end
   Fix: Add: "{suggested CTA}"
   Apply fix? (yes / no / manual)

Apply all fixes? (yes / select / no)
```

## Integration with Other Skills

- **daily-autopilot**: Step 5.5 — auto-run pre-publish before saving
- **batch-generator**: Run pre-publish on all batch content
- **content-grader**: Pre-publish checks formatting; grader checks quality
- **hashtag-optimizer**: Called when Instagram hashtag count is low
- **smart-cta**: Called when CTA is missing

## Quality Gate

- [ ] Every check item is binary (pass/fail, not subjective)
- [ ] Fixes are specific and ready to apply
- [ ] Platform-specific checks are accurate and current
- [ ] No false positives (e.g., intentional short tweets flagged)
- [ ] Auto-fix doesn't change meaning or voice
