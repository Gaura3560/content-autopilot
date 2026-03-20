---
name: micro-content
description: Micro-content mass generator — extract 10-20 bite-sized content pieces from a single article. One-liners, tips, stats, questions, and provocative statements for X singles, Instagram stories, and daily filler content. Maximum content from minimum input.
---

# Micro-Content Generator

One article → 10-20 micro posts. Never run out of content to share.

## When to Activate

- User says `/micro {file_path}` or `/micro`
- User asks "break this into smaller posts"
- User asks "give me quick posts from this article"
- User needs daily filler content without writing from scratch

## Prerequisites

- Source content file
- `~/.content-autopilot/profile.json`

## Commands

### `/micro {file_path}` — Generate micro-content from a file
### `/micro batch` — Process all this week's content
### `/micro {file_path} {count}` — Generate specific number of pieces

## Micro-Content Types

| Type | Length | Platform | Example |
|------|--------|----------|---------|
| One-liner | 1 sentence | X, IG Story | Sharp insight or tip |
| Quick tip | 2-3 sentences | X, IG | Actionable mini-advice |
| Stat callout | 1 sentence + number | X, IG | Surprising data point |
| Question | 1 sentence | X, IG Story | Thought-provoking question |
| Hot take | 1-2 sentences | X | Bold opinion from the article |
| Fill-in-blank | Template | IG Story | "The best way to _____ is _____" |
| This-or-that | 2 options | IG Story | Interactive poll content |
| Before/After | 2 lines | X, IG | Contrast statement |

## Workflow

### Step 1: Analyze Source Content

Read the article and extract:
- Key insights (every paragraph's core point)
- Data points and statistics
- Surprising claims or contrarian takes
- Actionable tips
- Questions raised
- Strong phrases and quotable lines

### Step 2: Generate Micro-Content

```
============================================
  Micro-Content from: "{article_title}"
  Generated: {count} pieces
============================================

--- One-Liners (X singles) ---
1. "{sharp insight from paragraph 3}"
2. "{another insight}"
3. "{provocative statement}"

--- Quick Tips (X / IG) ---
4. "Quick tip: {actionable advice from article}. Try it today."
5. "Pro tip: {specific technique}. Most people skip this step."

--- Stat Callouts (X / IG) ---
6. "{data point}. Let that sink in."
7. "{surprising number} — and most people don't even know it."

--- Questions (X / IG Stories) ---
8. "{thought-provoking question from the article}?"
9. "{question that challenges the reader}?"

--- Hot Takes (X) ---
10. "{bold opinion}. I'll die on this hill."
11. "Unpopular opinion: {contrarian take from article}."

--- Fill-in-Blank (IG Story) ---
12. "The most underrated {topic} skill is _______"
13. "I wish someone told me about {topic}: _______"

--- This-or-That (IG Story polls) ---
14. "{option_A} or {option_B}?" (from article's comparison)
15. "{approach_1} vs {approach_2}?"

--- Before/After (X / IG) ---
16. "Before: {old way}. After: {new way from article}."

============================================

Posting schedule (1 micro-post per day):
  Day 1: #{1} on X (one-liner)
  Day 2: #{8} on IG Story (question)
  Day 3: #{4} on X (quick tip)
  Day 4: #{14} on IG Story (this-or-that)
  ...

All micro-content saved. 1 article → {count} days of content.
============================================
```

### Step 3: Save Output

```
~/Desktop/content-autopilot-output/
  micro_{date}.md          # All micro-content pieces
  micro_schedule_{date}.md # Posting schedule
```

## Integration with Other Skills

- **content-writer**: Suggest "/micro to extract micro-content" after writing
- **batch-generator**: Include micro-content in weekly distribution plan
- **quote-card**: Overlap with quote extraction — micro focuses on text, quotes on visuals
- **daily-autopilot**: Fill gaps between major content with micro-posts
- **content-recycle**: Micro-content from old articles = effortless recycling

## Quality Gate

- [ ] Each micro piece stands alone (makes sense without the full article)
- [ ] Variety of types included (not all one-liners)
- [ ] Platform appropriateness noted for each piece
- [ ] No piece exceeds platform character limits
- [ ] Each piece delivers value or provokes thought
- [ ] Posting schedule spaces out similar types
