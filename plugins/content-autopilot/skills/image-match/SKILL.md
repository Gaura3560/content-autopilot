---
name: image-match
description: Image-text alignment checker — verify that OGP images, thumbnails, and social cards match the content's message, tone, and topic. Catches mismatches between visual and textual content that confuse audiences and reduce click-through rates.
---

# Image-Text Match Checker

Ensure your images actually match what your content is about — mismatches kill click-through rates.

## When to Activate

- User says `/image-match {content_file} {image_file}`
- User asks "does this image match my article?"
- User asks "check my thumbnail"
- Auto-suggested after visual-creator generates images

## Prerequisites

- Content file and corresponding image file(s)
- Image reading capability (Read tool for images)

## Commands

### `/image-match {content_file} {image_file}` — Check specific pair
### `/image-match {content_file}` — Auto-find and check associated images
### `/image-match audit` — Check all recent content-image pairs

## Workflow

### Step 1: Load Content and Image

Read both:
1. Content file — extract title, topic, key message, tone
2. Image file — analyze using Read tool (multimodal)

### Step 2: Analyze Alignment

```
Image-Text Match Analysis:
============================================

Content: "{title}"
Image: {image_filename}

--- Alignment Checks ---

1. Topic match:
   Content topic: {topic}
   Image conveys: {what the image shows/suggests}
   Match: {YES / PARTIAL / NO}

2. Title visibility:
   Title text in image: {present / absent / different}
   Readable at thumbnail size: {yes / no}
   Match: {YES / NO}

3. Tone/mood match:
   Content tone: {professional / casual / urgent / inspiring}
   Image mood: {professional / playful / dark / bright}
   Match: {YES / MISMATCH}

4. Brand consistency:
   Expected colors: {primary} + {secondary}
   Image colors: {detected colors}
   Match: {YES / OFF-BRAND}

5. Platform fit:
   Target platform: {platform}
   Expected dimensions: {WxH}
   Image dimensions: {WxH}
   Match: {YES / WRONG SIZE}

--- Overall ---

Alignment score: {score}/100

Issues:
  {list of specific mismatches}

============================================
```

### Step 3: Recommendations

```
Recommendations:

{If topic mismatch}:
  The image suggests "{image_topic}" but the content is about "{content_topic}".
  Fix: Regenerate with prompt focused on "{content_topic}"
  Suggested prompt: "{improved_image_prompt}"

{If title unreadable}:
  Title text is too small / wrong color / missing.
  Fix: Increase font size to {size}px minimum, use {color} for contrast

{If tone mismatch}:
  Content is {tone} but image feels {different_tone}.
  Fix: Use {color_palette} and {style} to match {tone}

{If off-brand}:
  Image uses {detected_colors} instead of brand colors {expected}.
  Fix: Regenerate with brand colors specified in prompt
```

## Integration with Other Skills

- **visual-creator**: Run image-match after image generation
- **content-grader**: Image alignment included in Platform Fit score
- **pre-publish**: Image check included in checklist
- **carousel-generator**: Check cover slide alignment
- **quote-card**: Verify quote text matches the visual

## Quality Gate

- [ ] Image analyzed using multimodal capability
- [ ] All alignment dimensions checked
- [ ] Specific fixes suggested (not just "doesn't match")
- [ ] Brand color check uses actual profile.json values
- [ ] Platform dimension requirements are current
