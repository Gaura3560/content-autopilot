---
name: setup-profile
description: Initial setup for Content Autopilot — collects user preferences (theme, audience, platforms, writing style, brand colors, funnel configuration, competitor accounts) and generates a reusable profile.json. Run once before using other content-autopilot skills.
---

# Setup Profile

Create your Content Autopilot profile so all generated content matches your voice, brand, and audience.

## When to Activate

- First time using any content-autopilot skill
- User says `/setup-profile`
- `~/.content-autopilot/profile.json` does not exist
- User wants to update their content profile

## Workflow

### Step 1: Ask 7 Questions

Ask the user the following questions one at a time. Wait for each answer before proceeding.

**Question 1 — Theme & Keywords**
```
What is your main content theme?
Examples: AI x business, cooking for beginners, personal finance, programming tutorials

Also provide 3-5 keywords that describe your niche.
```

**Question 2 — Target Audience**
```
Who is your target reader?
Describe their profile:
- Age range
- Occupation or interests
- Pain points or goals
- Knowledge level (beginner / intermediate / advanced)
```

**Question 3 — Platforms**
```
Which platforms do you publish on? (Select all that apply)
1. note
2. X (Twitter)
3. Instagram
4. All of the above
```

**Question 4 — Writing Style**
Choose one method to capture style:

```
How should I learn your writing style? Pick one:

A) Paste 3 URLs of your past posts (best accuracy)
B) Choose a preset:
   - casual: friendly, conversational, uses spoken language
   - professional: polished, authoritative, data-driven
   - storytelling: narrative-driven, personal anecdotes, emotional
   - educational: structured, step-by-step, clear explanations
   - provocative: bold opinions, contrarian, debate-sparking
C) Provide a reference account URL whose style you want to emulate
```

If the user chooses option A:
1. Use WebFetch to retrieve the URLs
2. Analyze tone, sentence length, vocabulary, paragraph structure
3. Generate a `style_profile` object summarizing patterns

If the user chooses option B:
1. Map the preset to a predefined style profile

If the user chooses option C:
1. Use WebSearch/WebFetch to analyze the reference account
2. Extract style patterns

**Question 5 — Brand Visual**
```
What are your brand colors and logo?

- Brand color: hex code (e.g., #FF6B35) or color name (e.g., navy blue)
- Secondary color (optional): hex code or color name
- Logo file path (optional, or type "none")
```



**Question 6 — Funnel Configuration**
```
Do you want to set up a cross-platform funnel? (X/Instagram → note → monetization)

If yes, provide the following:
- note URL (e.g., https://note.com/username)
- X handle (e.g., @username)
- Instagram handle (e.g., @username)
- Monetization method:
  A) note paid articles
  B) note membership (monthly magazine)
  C) External product/service referral
  D) Not decided yet (build followers first)
- Lead magnet (free value offering):
  e.g., "5-step guide to ○○", "○○ checklist"
  (type "none" if not ready — you can design one later with /funnel-designer)
- Membership URL (optional, if using note membership):
  e.g., https://note.com/username/membership
- Lead magnet URL (optional, if you already have one):
  e.g., URL to a note article or external page with your free resource

If no, funnel features will be disabled and content will be generated
independently per platform (traditional mode).
```

If the user enables funnel:
1. Validate the note URL format
2. Store all funnel settings in profile.json
3. All subsequent content generation will include cross-platform CTAs

If the user declines:
1. Set `funnel.enabled` to `false`
2. Content generation works as before (no cross-platform CTAs)

**Question 7 — Competitor Accounts (Optional)**
```
Do you want to track competitor accounts? (optional — you can add them later)

If yes, provide up to 5 competitors:
- Name (display name)
- note URL (optional): https://note.com/...
- X handle (optional): @...
- Instagram handle (optional): @...

You can also add competitors later with /competitor add {handle}

If no, type "skip"
```

If the user provides competitors:
1. Store each in the `competitors` array in profile.json
2. Set `added_at` to today's date

If the user skips:
1. Set `competitors` to an empty array `[]`

### Step 2: Generate Profile

After collecting all answers, create the profile file:

```bash
mkdir -p ~/.content-autopilot
```

Write `~/.content-autopilot/profile.json` with this structure:

```json
{
  "version": "1.0",
  "created_at": "2026-03-18T00:00:00Z",
  "updated_at": "2026-03-18T00:00:00Z",
  "theme": {
    "main": "AI x business",
    "keywords": ["AI", "automation", "productivity", "business growth", "tools"]
  },
  "audience": {
    "age_range": "25-45",
    "occupation": "business owners, marketers, freelancers",
    "pain_points": ["time-consuming content creation", "inconsistent posting"],
    "knowledge_level": "intermediate"
  },
  "platforms": ["note", "x", "instagram"],
  "style": {
    "method": "preset",
    "preset": "professional",
    "tone": "authoritative yet approachable",
    "sentence_length": "medium",
    "vocabulary": "accessible technical terms",
    "paragraph_style": "short paragraphs with line breaks",
    "emoji_usage": "minimal",
    "first_person": true,
    "sample_urls": []
  },
  "brand": {
    "primary_color": "#FF6B35",
    "secondary_color": "#1A1A2E",
    "logo_path": null,
    "font_preference": null
  },
  "funnel": {
    "enabled": true,
    "note_url": "https://note.com/username",
    "x_handle": "@username",
    "instagram_handle": "@username",
    "monetization": {
      "type": "paid_articles",
      "lead_magnet": "AI仕事術の5ステップ無料ガイド",
      "membership_url": null,
      "lead_magnet_url": null
    }
  },
  "competitors": [
    {
      "name": "Competitor A",
      "note_url": "https://note.com/competitor_a",
      "x_handle": "@competitor_a",
      "instagram_handle": null,
      "added_at": "2026-03-20"
    }
  ]
}
```

### Step 3: Confirm

Display the generated profile as a formatted summary and ask the user to confirm or edit:

```
Your Content Autopilot Profile:

Theme: AI x business
Keywords: AI, automation, productivity, business growth, tools
Audience: Business owners and marketers (25-45), intermediate level
Platforms: note, X, Instagram
Style: Professional — authoritative yet approachable
Brand: #FF6B35 (primary), #1A1A2E (secondary)

Funnel: Enabled — X/Instagram → note → paid articles
Lead Magnet: AI仕事術の5ステップ無料ガイド

Competitors: {N} registered ({names list}) — or "none"

Is this correct? (yes / edit [field name])
```

## Updating an Existing Profile

If `~/.content-autopilot/profile.json` already exists:
1. Read and display the current profile
2. Ask which field(s) to update
3. Update only the specified fields
4. Update the `updated_at` timestamp
5. Save and confirm

## Output

- File: `~/.content-autopilot/profile.json`
- No MCP dependencies — pure text-based interaction

## Error Handling

- If user provides invalid hex color: suggest common alternatives
- If URL fetch fails: fall back to asking for manual style description
- If directory creation fails: report the error and suggest manual creation
