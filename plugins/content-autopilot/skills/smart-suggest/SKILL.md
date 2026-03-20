---
name: smart-suggest
description: Context-aware skill suggestion — paste a URL, drop a topic, or describe a situation and get the optimal skill chain automatically. No need to know which of 129 skills to use. Just say what you want and the system figures it out.
---

# Smart Suggest

Don't learn 129 commands. Just say what you want.

## Commands

### `/suggest {anything}` — Get the right skill chain for any input

## Examples

```
/suggest https://note.com/someone/article
→ /viral-reverse + /repurpose + /quote-card

/suggest "I want to grow on Instagram"
→ /growth-hack instagram + /hashtag + /carousel templates + /reels

/suggest "I have a paid article to sell"
→ /launch + /pricing + /persuasion + /drip welcome

/suggest "I feel stuck and uninspired"
→ /unblock + /mood-write + /mind-map + /daily-capture review

/suggest "Is my content any good?"
→ /multi-review + /benchmark + /engagement-predict + /brand-voice

/suggest "quarterly planning"
→ /annual-review + /identity check + /content-dna + /strategy-test + /batch 14
```

## How It Works

1. Parse the input for intent (create/optimize/analyze/grow/monetize/fix)
2. Match intent to skill category
3. Build optimal skill chain with dependencies
4. Present as a runnable workflow

```
Your input: "{input}"
Detected intent: {intent}

Recommended skill chain:
  1. {skill} — {why}
  2. {skill} — {why}
  3. {skill} — {why}

Run this chain? (yes / modify / explain more)
```

Integrates with: ALL skills, workflow-chain (executes the chain), meta-learning (learns which suggestions you follow).
