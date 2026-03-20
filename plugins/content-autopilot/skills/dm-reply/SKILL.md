---
name: dm-reply
description: DM auto-reply template generator — pre-built responses for common direct message types across X, Instagram, and note. Covers questions, collab requests, product inquiries, praise, criticism, and spam. Includes funnel-aware responses that guide DM conversations toward monetization.
---

# DM Reply Templates

Handle every DM professionally and quickly — with templates that save time and drive results.

## When to Activate

- User says `/dm-reply` or `/dm`
- User says `/dm {category}` for specific DM type
- User asks "how should I reply to this DM?"
- User gets a lot of DMs and needs efficiency

## Prerequisites

- `~/.content-autopilot/profile.json` (for tone and funnel settings)

## Commands

### `/dm` — Show all DM template categories
### `/dm {category}` — Templates for specific DM type
### `/dm quick` — Top 5 most-used templates
### `/dm funnel` — Funnel-aware DM response flows

## DM Categories

| Category | Frequency | Template Count |
|----------|-----------|---------------|
| Questions | High | 5 templates |
| Praise/Thanks | High | 3 templates |
| Collab requests | Medium | 4 templates |
| Product inquiries | Medium | 3 templates |
| Criticism/Complaints | Low | 3 templates |
| Spam/Irrelevant | High | 2 templates |
| Media/Interview | Low | 3 templates |
| Hiring/Job offers | Low | 2 templates |

## Templates

### Questions

```
Template 1 (Quick answer + content link):
ありがとうございます！
{topic}については、こちらの記事で詳しく解説しています：
→ {note_url}
他にも質問があればお気軽にどうぞ！

Template 2 (Detailed question — defer to content):
いい質問ですね！
実は{topic}についてちょうど記事を書こうと思っていたので、
詳しくnoteにまとめますね。
フォローしていただければ公開時に通知が届きます！

Template 3 (Question beyond your scope):
ありがとうございます！
{topic}は私の専門外なので正確なお答えが難しいのですが、
{alternative_resource}が参考になるかもしれません。
{your_topic}に関するご質問はいつでもどうぞ！
```

### Collab Requests

```
Template 1 (Interested):
ありがとうございます！コラボのご提案、嬉しいです。
具体的にどんな形式をお考えですか？
（対談記事、相互紹介、共同企画など）
お互いの読者に価値を届けられるならぜひ！

Template 2 (Polite decline):
お声がけありがとうございます！
現在のスケジュール的に難しいのですが、
今後機会があればぜひお願いしたいです。
引き続きよろしくお願いします！

Template 3 (Evaluate first):
ありがとうございます！
{their_content}拝見しました。{specific_positive_note}ですね。
コラボの詳細を教えていただけますか？
・想定形式
・ターゲット読者
・スケジュール感
前向きに検討させていただきます！
```

### Funnel-Aware DM Flows

When `funnel.enabled = true`, DM responses guide toward monetization:

```
DM Question → Answer + note article link (MOFU)
  → "もっと詳しくはnoteで → {url}"

DM "How do I get started?" → Lead magnet (MOFU)
  → "まずはこちらの無料ガイドがおすすめです → {lead_magnet_url}"

DM "What's in your paid content?" → Value preview (BOFU)
  → "無料記事では{overview}を、有料では{premium_detail}をカバーしています"
  → "{paid_url}"

DM Praise → Deepen relationship + upsell
  → "嬉しいです！{specific_response}"
  → "もしよければ、こちらの記事もおすすめです → {next_article}"
```

### Step-by-Step Flow

```
DM received → Classify type:

Question?
  → Can answer quickly → Template 1 (answer + link)
  → Complex question → Template 2 (defer to content)
  → Out of scope → Template 3 (redirect)

Praise?
  → Thank + deepen + suggest next content

Collab?
  → Interested → Template 1 (explore)
  → Not sure → Template 3 (evaluate)
  → Not interested → Template 2 (polite decline)

Product inquiry?
  → Answer + link to paid content

Spam?
  → Ignore or block (no response needed)
```

## Personalization

All templates use:
- `style.tone` from profile.json
- `style.emoji_usage` setting
- `funnel` settings for link placement
- `theme.main` for topic references

## Integration with Other Skills

- **engagement-templates**: Comments = public, DMs = private
- **lead-magnet-creator**: Lead magnet link in DM responses
- **collab-planner**: Handle collab DMs with structured evaluation
- **testimonial-framework**: Request testimonials via DM template

## Quality Gate

- [ ] Templates match the user's tone
- [ ] Response is helpful (not just promotional)
- [ ] Funnel links are natural (not every DM is a sales pitch)
- [ ] Decline templates are respectful
- [ ] Spam handling is clear (don't waste time)
