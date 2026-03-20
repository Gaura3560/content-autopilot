---
name: poll-generator
description: Interactive content generator — create X polls, Instagram story polls, note surveys, and quiz-style content. 3-5x higher engagement than standard posts. Includes result-to-content pipeline to turn poll results into follow-up content.
---

# Poll & Quiz Generator

Create interactive content that gets 3-5x more engagement — then turn results into new content.

## When to Activate

- User says `/poll` or `/poll {topic}`
- User says `/quiz {topic}`
- User asks "create a poll about {topic}"
- User asks "make interactive content"
- User wants to boost engagement metrics

## Prerequisites

- `~/.content-autopilot/profile.json` must exist

## Commands

### `/poll {topic}` — Generate poll content for all platforms
### `/poll x {topic}` — X poll specifically
### `/poll instagram {topic}` — Instagram story poll
### `/quiz {topic}` — Generate quiz-style content
### `/poll results {topic}` — Generate follow-up content from poll results

## Poll Types

| Type | Platform | Engagement | Best For |
|------|----------|-----------|----------|
| Binary (A/B) | X, IG Stories | High votes | Debate, preference |
| Multiple choice | X | High votes | Knowledge, opinions |
| Scale (1-10) | IG Stories | Medium | Sentiment, rating |
| "This or That" | IG Stories | Very High | Quick engagement |
| Quiz (right answer) | X, IG | High shares | Education, fun |
| Open question | X, note | High replies | Research, community |

## Workflow

### Step 1: Generate Poll Content

**X Poll:**
```
Tweet text: "{engaging question about {topic}}"

Options:
  A) {option_1}
  B) {option_2}
  C) {option_3} (optional)
  D) {option_4} (optional)

Duration: 24 hours (recommended)

Follow-up tweet (post after poll closes):
"Results are in! {X}% said {winning_option}.
Here's why that's {interesting/surprising/exactly right}:
{brief insight}
Full analysis → {note_url if funnel enabled}"
```

**Instagram Story Poll:**
```
Story 1: Hook
  Background: {brand_color}
  Text: "{question}"
  Sticker: Poll — "{option_A}" vs "{option_B}"

Story 2: Context
  Text: "{why this question matters}"
  Sticker: Slider — "How much do you agree? 0-100"

Story 3: Reveal (post 24h later)
  Text: "{X}% of you said {option}! Here's my take..."
  Sticker: Link — {note_url if funnel enabled}
```

**Quiz Style (X thread):**
```
Tweet 1: "Pop quiz: {topic} edition"
  "{question}"
  A) {wrong_answer}
  B) {right_answer}
  C) {wrong_answer}
  D) {wrong_answer}

Tweet 2 (reply): "The answer is {letter}!"
  "{explanation why}"
  "Did you get it right? RT if you did"

Tweet 3: "Here's why this matters:
  {deeper insight connecting to your content}
  Full breakdown → {note_url}"
```

**note Survey/Question:**
```
At the end of a note article, add:

---
## 読者アンケート

{topic}について、あなたの経験を教えてください：

1. {option_1}
2. {option_2}
3. {option_3}

コメント欄で番号と理由を教えていただけると、
次回の記事の参考にさせていただきます！
```

### Step 2: Result-to-Content Pipeline

After a poll closes, turn results into new content:

```
/poll results "{topic}"

Poll Result Analysis:
  Question: "{question}"
  Results: A: {X}% / B: {Y}% / C: {Z}%

Content opportunities from these results:

1. [X thread] "I asked {N} people about {topic}. {X}% said {surprising_result}."
   → Data-driven thread analyzing the results

2. [note article] "Why {Y}% of people are wrong about {topic}"
   → Contrarian take on the majority opinion

3. [Instagram carousel] "{topic}: What {N} people think vs reality"
   → Visual comparison of poll results vs data

4. [Follow-up poll] "Based on the results, new question: {follow_up}"
   → Chain polls for ongoing engagement

Generate which content? (1/2/3/4/all)
```

### Step 3: Save and Record

Save poll content to output directory.
Record in content-history.json with format: "poll" or "quiz".

## Poll Topic Ideas (auto-generated from profile)

When user says `/poll` without a topic:
```
Poll topic suggestions for {theme.main}:

1. [Debate] "{controversial question in your niche}"
2. [Preference] "{A} or {B} for {goal}?"
3. [Knowledge] "True or false: {common misconception}"
4. [Experience] "Have you ever {common situation}?"
5. [Prediction] "By {year}, will {prediction}?"

Select a topic or provide your own:
```

## Integration with Other Skills

- **content-writer**: Suggests adding a poll CTA to boost engagement
- **niche-monitor**: Poll topics informed by current niche conversations
- **engagement-templates**: Poll follow-up templates for responding to voters
- **content-analytics**: Tracks poll/quiz content performance
- **weekly-report**: Includes poll engagement in weekly summary

## Quality Gate

- [ ] Poll question is genuinely engaging (not boring yes/no)
- [ ] Options are balanced (no obvious "right" answer unless quiz)
- [ ] Follow-up content plan exists for after poll closes
- [ ] Platform-specific format conventions followed
- [ ] Result-to-content pipeline generates genuinely valuable content
- [ ] Poll connects to user's broader content strategy
