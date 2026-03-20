---
name: visual-creator
description: Brand-consistent image generation for note OGP, X cards, and Instagram posts. Uses profile.json brand colors and generates platform-correct image sizes. Supports gemini-image MCP with text-prompt fallback. Includes optional note referral banner for funnel-enabled profiles.
---

# Visual Creator

Generate brand-consistent images for your content across note, X, and Instagram.

## When to Activate

- User says `/visual-creator`
- Called automatically by `daily-autopilot` after content generation
- User wants thumbnails, OGP images, or social media visuals
- User asks "create images for this content"

## Prerequisites

- `~/.content-autopilot/profile.json` must exist (for brand colors)
- Content title and platform(s) from `content-writer` or user input

## Platform Image Specifications

| Platform | Type | Size (px) | Aspect Ratio |
|----------|------|-----------|-------------|
| note | OGP / thumbnail | 1200 x 630 | 1.91:1 |
| X | Card image | 1200 x 675 | 16:9 |
| Instagram | Post (default) | 1080 x 1080 | 1:1 |

## Workflow

### Step 1: Load Brand Settings

Read `~/.content-autopilot/profile.json` and extract:
- `brand.primary_color` — main color for backgrounds/accents
- `brand.secondary_color` — text or complementary elements
- `brand.logo_path` — logo overlay (if provided)
- `funnel.enabled` — whether to include note referral elements
- `funnel.note_url` — for referral banner (if funnel enabled)
- Content title from `content-writer` output

### Step 2: Design the Image

For each platform, create a prompt or design specification:

**Design principles:**
- Clean, minimal composition
- Title text as the focal point
- Brand colors as background gradient or accent
- High contrast for readability
- Professional typography feel

**Prompt template for image generation:**
```
A clean, modern social media graphic with the following specifications:
- Background: gradient from {primary_color} to {secondary_color}
- Text overlay: "{title}" in bold, white sans-serif font, centered
- Style: minimalist, professional, high contrast
- Size: {width}x{height} pixels
- No stock photos, no clip art
- Clean negative space around text
```

### Step 3: Generate Images

**Level 2 — With Image MCP (gemini-image or fal.ai):**

If `gemini-image` MCP is available, use `generate_image`:
```
Generate images for each platform size using the design prompt.
Save each to ~/Desktop/content-autopilot-output/
```

File naming:
- `note_ogp_{date}.png`
- `x_card_{date}.png`
- `instagram_{date}.png`

If `fal.ai` MCP is available, use the equivalent image generation endpoint with the same prompt.

**Level 1 — Fallback (No Image MCP):**

If no image generation MCP is available, output detailed prompts that the user can paste into their preferred tool:

```
Image generation is not available (no gemini-image or fal.ai MCP configured).

Here are copy-paste prompts for your preferred image tool:

--- note OGP (1200x630) ---
Prompt: A clean, modern blog thumbnail with a {primary_color} to
{secondary_color} gradient background. Bold white text reads:
"{title}". Minimalist style, professional, high contrast.
Size: 1200x630px.

--- X Card (1200x675) ---
Prompt: [same style, adjusted for 1200x675]

--- Instagram Post (1080x1080) ---
Prompt: [same style, adjusted for 1080x1080, consider vertical text layout]

Recommended tools:
- Canva (canva.com) — free, template-based
- Midjourney — AI image generation
- DALL-E — AI image generation
- Figma — for precise layout control
```

### Step 4: Logo Overlay (Optional)

If `brand.logo_path` is set and the file exists:
1. Note the logo placement instruction: bottom-right corner, 10% of image width
2. If using gemini-image, include logo placement in the prompt
3. If fallback mode, add logo placement instructions to the prompt

### Step 5: Output

Save all generated images to `~/Desktop/content-autopilot-output/`:

```bash
mkdir -p ~/Desktop/content-autopilot-output
```

Display results:
```
Images generated:

1. note OGP: ~/Desktop/content-autopilot-output/note_ogp_2026-03-18.png
   Size: 1200x630 | Colors: #FF6B35 → #1A1A2E

2. X Card: ~/Desktop/content-autopilot-output/x_card_2026-03-18.png
   Size: 1200x675 | Colors: #FF6B35 → #1A1A2E

3. Instagram: ~/Desktop/content-autopilot-output/instagram_2026-03-18.png
   Size: 1080x1080 | Colors: #FF6B35 → #1A1A2E
```

## Advanced: Text-Heavy Thumbnails

For note OGP and X cards where the title IS the visual:

**Japanese text layout guidelines:**
- Max 2 lines of text
- Font size: large enough to read at thumbnail size (~60px equivalent)
- Line break at natural phrase boundaries
- Avoid splitting words across lines

**Title text treatment:**
```
Line 1: {first phrase of title}
Line 2: {second phrase of title}

Background: solid {primary_color} or gradient
Text color: white or {secondary_color} (whichever has higher contrast)
Optional: subtle pattern or geometric shapes as background texture
```

## Note Referral Banner (Funnel Mode)

When `funnel.enabled = true`, add a subtle note referral element to X and Instagram images:

**X card image:**
- Small banner at bottom: "続きはnoteで → {note_url}" in semi-transparent overlay
- Font size: ~18px equivalent (readable but not dominant)
- Position: bottom-right corner

**Instagram post image:**
- Small text: "noteで完全版公開中" as watermark
- Position: bottom-left corner, low opacity (60-70%)

**Prompt addition for image generation:**
```
Additional element (funnel mode):
- Small semi-transparent banner at the bottom reading "{note_url}"
- Font: clean sans-serif, 18px equivalent
- Opacity: 70%
- This should be subtle, not the main focus of the image
```

**When funnel is disabled:** Skip this step entirely. No referral elements on images.

## Quality Gate

Before delivering:
- [ ] Images match platform size specifications exactly
- [ ] Brand colors from profile.json are applied
- [ ] Title text is readable at thumbnail size
- [ ] High contrast between text and background
- [ ] Consistent visual style across all platform variants
- [ ] Files saved with correct naming convention
- [ ] Logo included if logo_path is set in profile
- [ ] If funnel enabled: X/Instagram images include subtle note referral banner
- [ ] If funnel disabled: no referral elements on images

## Troubleshooting

| Issue | Solution |
|-------|----------|
| gemini-image MCP not responding | Fall back to text prompt output |
| Logo file not found at logo_path | Skip logo, notify user |
| Title too long for image | Auto-truncate with "..." or split to 3 lines |
| Colors have low contrast | Adjust text color to white or black based on background luminance |
