# HALO — The Influencer Grade System
### A modular Lightroom preset library engineered for skin-tone accuracy, color harmony, and feed-level consistency

> **What this is.** Not a bag of random filters. HALO is a *system*: 9 signature looks, each shipping with adaptive lighting and skin-tone variants, plus a utility toolkit and a decision layer that tells you which preset to use and how to adapt it. It is designed around the two failures that sink almost every commercial influencer pack: presets that only work on one skin tone (usually fair), and presets that only work in one lighting condition (usually the seller's golden-hour test shots).

---

## HOW TO READ THE SETTINGS

All numeric values use Lightroom's native slider ranges.

- **Basic:** Exposure in stops (−5…+5). Everything else −100…+100.
- **Tone Curve points:** written as `(input, output)` on a 0–255 scale. `(0,18)` means the black point is *lifted* to 18 → matte shadows. Parametric regions (Highlights/Lights/Darks/Shadows) are −100…+100.
- **HSL:** `H` = Hue shift, `S` = Saturation, `L` = Luminance, each −100…+100, per color channel.
- **Color Grading:** `H` = hue angle 0–360°, `S` = saturation 0–100, `L` = luminance −100…+100, for Shadows / Midtones / Highlights. `Balance` −100…+100 (negative favors shadows), `Blending` 0–100.
- **Calibration:** Shadows Tint −100…+100, then per-primary `H`/`S`.
- **Effects:** Grain Amount/Size/Roughness 0–100; Vignette −100…+100.

**Golden rule baked into the whole system:** the master recipe is the *look*. Skin variant + lighting variant + exposure correction are *deltas you stack on top*. This is how you get hundreds of usable combinations from 9 packs without 81 separate files.

---

# PHASE 1 — MARKET RESEARCH & TREND ANALYSIS (2024–2026)

## 1.1 Dominant aesthetics

### A. Bright & Airy / Clean Minimal
- **Color grading:** Lifted black point (matte, but subtle), desaturated greens and blues so foliage/sky never compete with the subject, raised orange luminance for glowing skin. Highlights pulled to retain detail; whites pushed.
- **Lighting:** Low-to-negative contrast, generous exposure, soft highlights, lifted shadows. High-key.
- **Skin strategy:** Brighten orange luminance, *reduce* orange saturation to avoid an orange cast, neutralize ruddiness in red.
- **Emotional effect:** Clean, expensive, calm, aspirational. "Effortlessly put-together."
- **Use cases:** Fashion flatlays, bright cafés, interiors, lifestyle, beauty close-ups.

### B. Warm Film / Nostalgic (Kodak Portra / Gold lineage)
- **Color grading:** Warm white balance, faded matte shadows, greens shifted toward olive/yellow, golden highlights, often a faint teal in the shadows for a split.
- **Lighting:** Soft contrast, gentle roll-off, warmth in midtones.
- **Skin strategy:** Golden orange, slightly desaturated reds so warmth reads as glow, not sunburn.
- **Emotional effect:** Cozy, romantic, memory-like, intimate.
- **Use cases:** Golden-hour portraits, couples, coffee/cooking, slow-living lifestyle.

### C. Moody Cinematic / Dark Luxury
- **Color grading:** Desaturated overall but with *deliberate* rich color — teal/blue shadows, restrained warm highlights, deep (not clipped) blacks.
- **Lighting:** Higher contrast, lower exposure, dramatic shadow weight, often a vignette.
- **Skin strategy:** Pull saturation everywhere *except* red/orange; keep skin alive against a muted frame.
- **Emotional effect:** Luxury, mystery, editorial authority, "quiet wealth."
- **Use cases:** Evening fashion, watches/jewelry, architecture, editorial portraits.

### D. Orange & Teal / Travel Viral
- **Color grading:** The blockbuster split — aquas and blues pushed toward teal and saturated; oranges (skin, sand, terracotta) warmed and punched. Strong complementary contrast.
- **Lighting:** Punchy contrast, positive dehaze, high vibrance.
- **Skin strategy:** The danger zone. Done wrong, skin goes orange/jaundiced. Done right, you push *environmental* orange and protect skin hue separately.
- **Emotional effect:** Adventurous, vivid, escapist, thumb-stopping.
- **Use cases:** Travel, landscapes, pools/beaches, drone/wide shots.

### E. Natural "No-Filter" Realism
- **Color grading:** Minimal. Accurate WB, gentle S-curve, vibrance over saturation, a *whisper* of skin glow.
- **Lighting:** True-to-life, light contrast, light clarity.
- **Skin strategy:** Tiny orange luminance lift; otherwise leave it honest.
- **Emotional effect:** Trustworthy, relatable, authentic — increasingly the highest-converting "real" look.
- **Use cases:** UGC, everyday creators, "get ready with me," skincare honesty content.

### F. Vintage / Film Emulation
- **Color grading:** Stronger matte, visible grain, cross-processed channel curves (cool shadows / warm highlights), faded color.
- **Lighting:** Reduced extremes, soft haze.
- **Skin strategy:** Muted but warm; protect from going green.
- **Emotional effect:** Artistic, retro, "shot on film," collectible.
- **Use cases:** Creative portraits, music/band aesthetics, analog-leaning brands.

### G. Feminine Pastel / "Cotton Candy"
- **Color grading:** High-key, very low saturation, pastel split toning — pink highlights, lavender/blue shadows.
- **Lighting:** Lifted everything, low contrast, soft.
- **Skin strategy:** Reds toward pink, soft luminance, no harsh edges.
- **Emotional effect:** Sweet, dreamy, soft, "coquette."
- **Use cases:** Beauty, soft fashion, florals, youthful lifestyle.

### H. (Emergent 2024–2026) Digicam / Direct-Flash Candid
- **Color grading:** Slightly cool/clinical base, recovered flash hotspots, crunchy texture, faint Y2K magenta. The deliberate "early-2000s point-and-shoot" revival.
- **Lighting:** Hard frontal light feel, contrast, sensor-noise grain.
- **Emotional effect:** Candid, un-precious, in-the-moment, Gen-Z native.
- **Use cases:** Parties, behind-the-scenes, candid street, group shots.

## 1.2 Common denominators of high-performing feeds
1. **Consistency is the brand.** Recognition in the first half-second of a scroll is what converts a viewer into a follower. A coherent palette *is* the logo.
2. **Natural skin beats heavy color.** Top accounts edit the *environment* hard and the *skin* gently.
3. **Restraint reads as quality.** Subtle, considered grading signals "premium"; obvious filters signal "amateur."
4. **The grid is the unit, not the photo.** Strong individual edits that clash on the 9-tile grid underperform cohesive edits that are individually less dramatic.
5. **Contrast and clarity are doing the scroll-stopping**, but tone and warmth are doing the *liking* — vivid stops the thumb, flattering earns the engagement.

## 1.3 Gaps in the current preset market (the design brief)
- **Single-skin-tone development.** Most packs are built and tested on fair skin. On medium/olive skin they go sallow; on deep skin they go ashy, grey, or crush detail. → *HALO ships a dedicated Skin Module with Fair/Medium/Deep deltas for every look.*
- **Single-lighting-condition development.** They shine on the seller's golden-hour shots and collapse indoors. → *HALO ships Sunny/Cloudy/Indoor/Golden-Hour deltas.*
- **Skin sacrificed to the look.** Orange-teal packs especially turn skin orange. → *HALO isolates environmental color from skin hue.*
- **No repair layer.** A look but no way to fix a blown highlight or a green fluorescent cast. → *Micro-Adjustment Toolkit.*
- **No feed strategy.** Looks, but no system for grid cohesion across mixed lighting and subjects. → *Grid Harmonizer + Phase 4 strategy.*
- **No "which one, when."** Users are handed 40 presets and no logic. → *Smart Logic decision tree.*
- **Baked-in extreme WB that assumes one camera.** Breaks on other bodies/phones. → *HALO uses relative WB guidance, not hard Kelvin locks.*

---

# PHASE 2 — SYSTEM DESIGN

## 2.1 Architecture overview

```
HALO SYSTEM
├── CORE PACKS (9 signature looks) ........... the "look"
│     └── each ships as 3 skin-calibrated files (Fair / Medium / Deep)
├── ADAPTIVE LAYERS (stacked on top)
│     ├── Lighting deltas (Sunny / Cloudy / Indoor / Golden Hour)
│     └── Exposure-correction deltas (Under / Over)
├── MICRO-ADJUSTMENT TOOLKIT (utility fixes)
└── SMART LOGIC LAYER (decision tree + LR AI features)
```

## 2.2 Core packs (signature looks)

| # | Name | Aesthetic | Primary use case | One-line identity |
|---|------|-----------|------------------|-------------------|
| 1 | **Daydream** | Bright & airy | Lifestyle, fashion, interiors | Clean, expensive, weightless light |
| 2 | **Honeywash** | Warm film | Portraits, golden hour, slow living | Sun-soaked nostalgia |
| 3 | **Noir Lumière** | Dark luxury | Editorial, evening, jewelry | Cinematic restraint |
| 4 | **Wanderlust** | Orange & teal | Travel, landscapes, water | Vivid escapism |
| 5 | **TrueGlow** | Natural realism | UGC, everyday, skincare | "Did they even edit?" |
| 6 | **Analog 400** | Film emulation | Creative, retro brands | Shot-on-film character |
| 7 | **Sugar** | Pastel | Beauty, soft fashion, florals | Cotton-candy dream |
| 8 | **Flashback** | Digicam flash | Candid, party, Gen-Z | Un-precious, in-the-moment |
| 9 | **Bronze** | Sun-kissed | Fitness, beach, summer | Golden, defined, warm |

Full technical breakdowns in **Phase 3**.

## 2.3 Adaptive variants (the critical layer)

Variants are **deltas**, applied on top of the master. This is the professional, scalable model and mirrors how colorists actually work.

### Skin Tone Module (universal — layer on any pack)

| Channel / Setting | **Fair** | **Medium / Olive** | **Deep** |
|---|---|---|---|
| Red H / S / L | +2 / −8 / +2 | 0 / −2 / 0 | +1 / **+4** / 0 |
| Orange H / S / L | **−2** / −6 / +4 | +2 / −2 / +2 | +1 / **+4** / **0 to +2 only** |
| Yellow H / S | 0 / 0 | **+4 / −8** | +2 / 0 |
| Green S (extra) | 0 | **−10** | 0 |
| Blacks / Shadows (extra) | 0 / 0 | 0 / 0 | **+6 / +10** |
| Dehaze (extra) | 0 | 0 | **−6** |
| Calibration Tint | 0 | **−2** | **+2** |
| Calibration Red primary | H +4 | — | **S +6** |
| Highlights (extra) | **−8** | 0 | 0 |

**Why these moves:**
- **Fair:** the failure mode is *ruddiness and blotchy red*. Cool the orange hue slightly (no fake tan), pull red saturation, hold highlights so skin doesn't blow out pink.
- **Medium/Olive:** the failure mode is *sallow/green*. Shift yellow toward warm and pull yellow + green saturation; subtract a touch of green via tint.
- **Deep:** the failure mode is *ashy, grey, crushed detail, and washed-out richness*. **Lift** blacks and shadows so texture survives, **reduce** dehaze (dehaze greys deep skin), **add** red/orange saturation to preserve richness, and — critically — **do not** raise orange luminance the way you would for fair skin, which flattens and washes deep tones. Warmth comes from tint and red primary, not from blowing out luminance.

### Lighting Module (universal deltas)

| Setting | **Sunny / Harsh** | **Cloudy / Flat** | **Indoor / Artificial** | **Golden Hour** |
|---|---|---|---|---|
| Temp | +2 | **+4** | **−10** | **+6** |
| Tint | +2 | 0 | **+4** | 0 |
| Contrast | −6 | **+10** | 0 | −4 |
| Highlights | **−15** | 0 | −10 | −10 |
| Shadows | +12 | −4 | +8 | +8 |
| Whites | −6 | +6 | 0 | 0 |
| Dehaze | −4 | **+8** | +2 | 0 |
| Clarity / Texture | −4 / −4 | +6 / +4 | 0 / 0 | 0 / 0 |
| Vibrance | 0 | **+8** | +6 | 0 |
| Orange S | 0 | 0 | **−6** | 0 |
| Orange L | 0 | 0 | 0 | **+4** |

**Why:**
- **Sunny/harsh:** kill highlight clipping, open shadows, soften over-crisp midday texture.
- **Cloudy/flat:** rebuild the contrast and color the gray sky stole; warm it slightly.
- **Indoor/artificial:** *cool* the temp to neutralize tungsten orange, add tint to fight fluorescent green, and pull orange saturation so skin isn't jaundiced under warm bulbs.
- **Golden hour:** lean *into* the warmth instead of correcting it.

### Exposure-Correction Module

| Setting | **Underexposed** | **Overexposed** |
|---|---|---|
| Exposure | **+0.6 to +1.0** | **−0.5 to −0.9** |
| Highlights | 0 | **−40** |
| Whites | +6 | **−20** |
| Shadows | +20 | 0 |
| Blacks | +8 | −4 |
| Dehaze | 0 | +6 |
| Vibrance | +6 | **+8** |
| Noise Reduction (Luminance) | **+15** | 0 |

**Why:** lifting an underexposed file reveals shadow noise → add NR. Overexposed files lose color along with the highlights → recover whites/highlights *and* add vibrance to restore the bleached tones. Always check skin isn't clipped in the overexposed case.

## 2.4 Micro-Adjustment Toolkit (utility presets)

| Tool | What it does | Settings (apply, often masked/brushed) |
|---|---|---|
| **Skin Tone Rescue** | Even out and calm skin | Orange H +2 / S −10 / L +6; Red S −10; pair with **Point Color** sampled on skin; brush at 70% |
| **Background Color Balancer** | Make subject pop by muting the frame | Green S −25; Blue S −15; Aqua S −15 (or mask the *background* and apply) |
| **Highlight Recovery** | Save blown skies / hotspots | Highlights −60; Whites −25; Dehaze +6 |
| **Shadow Lift** | Open crushed shadows cleanly | Shadows +50; Blacks +15; curve toe (0,16); NR +12 |
| **WB Fix — Warm Killer** | Neutralize orange cast | Temp −10 |
| **WB Fix — Cool Killer** | Neutralize blue cast | Temp +10 |
| **WB Fix — Green Killer** | Fluorescent/LED cast | Tint +8 |
| **Glow / Soft** | Dreamy skin & light | Texture −15; Clarity −10 (brush on skin only) |
| **Grid Harmonizer** ⭐ | "Glue" mixed photos into one feed | Blacks +6; Color Grade Highlights H42 S6 / Shadows H215 S6; Vibrance +6 — apply at **low strength** across an inconsistent feed to unify it |

⭐ The **Grid Harmonizer** is the secret weapon. When a feed mixes Daydream cafés with Wanderlust travel shots, this thin unifying layer gives them a shared "fingerprint" without forcing one look on everything.

## 2.5 Smart Logic Layer (decision system)

This layer is **conceptual rules + Lightroom's real AI features**. Lightroom already ships *Adaptive Presets* (presets containing AI subject/sky masks), *Auto* tone/WB, AI *Denoise*, *Lens Blur*, and *Point Color* — HALO is built to ride those.

### The pipeline (always in this order)
1. **Correct exposure first.** Run Auto as a first pass or set manually. If the histogram clips highlights → apply **Highlight Recovery** before anything else.
2. **Neutralize white balance.** Identify the light source. If there's a color cast → apply the matching **WB Fix** utility. *You cannot grade on top of a wrong WB.*
3. **Identify the dominant skin tone** in frame → load the **Fair / Medium / Deep** file of your chosen pack.
4. **Choose the pack** by content + mood goal (tree below).
5. **Apply the lighting delta** matching the scene.
6. **Refine:** mask the subject (AI Select Subject), apply Skin Tone Rescue if needed, check skin against the rest of the frame, optional Lens Blur for separation.

### Pack-selection decision tree (by intent)

```
What's the goal?
├─ Clean / bright / aspirational ............ lifestyle, fashion, interiors → DAYDREAM
├─ Cozy / romantic / golden ................. portraits, couples, slow-living → HONEYWASH
├─ Luxury / dramatic / editorial ............ evening, jewelry, architecture → NOIR LUMIÈRE
├─ Vivid / escapist / scroll-stopping ....... travel, landscapes, water → WANDERLUST
├─ Authentic / relatable / barely-edited .... UGC, skincare, everyday → TRUEGLOW
├─ Artistic / retro / film .................. creative portraits, music → ANALOG 400
├─ Soft / sweet / feminine .................. beauty, florals, coquette → SUGAR
├─ Candid / party / Gen-Z ................... events, BTS, group shots → FLASHBACK
└─ Tanned / defined / summer ................ fitness, beach, sun → BRONZE
```

### Condition-adaptation rules (if → then)

| Condition detected | Action |
|---|---|
| Histogram clipping right (blown) | Highlight Recovery *before* the pack |
| Histogram bunched left (dark) | Underexposed delta + AI Denoise |
| Orange cast / indoor bulbs | WB Warm Killer, then *Indoor* lighting delta |
| Greenish cast / office light | WB Green Killer first |
| Deep skin + crushed shadows | Deep skin file + Shadow Lift, reduce Dehaze |
| Skin reads orange after grading | Skin Tone Rescue + Point Color on skin |
| Busy, colorful background | Background Color Balancer + Lens Blur |
| Feed looks inconsistent | Grid Harmonizer at low strength on outliers |

---

# PHASE 3 — PRESET CREATION (FULL SETTINGS)

Each master below is the **look at base** (neutral lighting, designed against medium skin as the reference). Stack the Phase 2 deltas for skin / lighting / exposure.

---

## 1 · DAYDREAM — Bright & Airy
**Intention:** weightless, gallery-clean light; skin glows, environment recedes.
**Profile:** Adobe Color.

**Basic:** Temp +5, Tint +2 · Exposure +0.35 · Contrast −12 · Highlights −35 · Shadows +45 · Whites +18 · Blacks +12 · Texture −8 · Clarity −6 · Dehaze −3 · Vibrance +14 · Saturation −8

**Tone Curve (point):** (0,18) (64,68) (128,135) (192,205) (255,250) → lifted toe + pulled top = soft airy matte.
**Parametric:** Highlights −10, Lights +5, Darks +12, Shadows +20.

**HSL:**
- Red H+2 S−8 L+4 · Orange H+4 S−10 **L+12** (skin glow) · Yellow H−6 S−18 L+10
- Green H+10 **S−30** L+8 (mute foliage) · Aqua S−15 L+5 · Blue H+6 S−12 L+6
- Purple/Magenta: negligible

**Color Grading:** Highlights H45 S8 (warm cream) · Midtones neutral · Shadows H220 S6 L+2 (cool) · Balance +10 · Blending 60
**Calibration:** Shadows Tint +4 · Red H+6 · Green H+12 S+5 · Blue S+18
**Effects:** Grain 0 · Vignette 0 · Sharpening 35

**Before → after:** flat bright snapshot → luminous, clean, "expensive interiors" image where skin is the warmest thing in frame.
**Viewer psychology:** calm, order, aspiration, trust.

---

## 2 · HONEYWASH — Warm Film
**Intention:** sun-soaked memory; Portra/Gold warmth with a faint teal shadow.
**Profile:** Adobe Color (or a camera Standard base).

**Basic:** Temp +14, Tint +4 · Exposure +0.15 · Contrast −8 · Highlights −28 · Shadows +35 · Whites +6 · Blacks +8 · Texture +4 · Clarity +5 · Dehaze +4 · Vibrance +10 · Saturation −4

**Tone Curve:** (0,16) (60,60) (128,132) (200,210) (255,248) — faded matte.
**Parametric:** Shadows +16, Darks +8, Lights +4, Highlights −8.

**HSL:**
- Red H−2 S−6 L+2 · Orange **H+6** S−6 L+8 (golden) · Yellow H−10 S+4 L+4
- Green **H+18 S−22** L−4 (olive Portra greens) · Aqua H−12 S−10 · Blue H+8 S−8 L−4

**Color Grading:** Highlights H42 **S14** (golden) · Midtones H40 S6 · Shadows H195 S7 L−3 (teal split) · Balance +5 · Blending 55
**Calibration:** Shadows Tint +6 · Red H+8 S+4 · Green H+20 · Blue S+20
**Effects:** Grain 14 / 22 / 50 · Vignette −6

**Before → after:** neutral daytime portrait → warm, intimate, film-like frame with creamy golden highlights and cool-teal shadow separation.
**Viewer psychology:** nostalgia, comfort, closeness.

---

## 3 · NOIR LUMIÈRE — Dark Luxury
**Intention:** cinematic restraint; muted frame, rich blacks, skin kept alive.
**Profile:** Adobe Color.

**Basic:** Temp −4, Tint +3 · Exposure −0.25 · Contrast +22 · Highlights −45 · Shadows −10 · Whites −8 · Blacks −18 (rich, *not* clipped) · Texture +12 · Clarity +14 · Dehaze +10 · Vibrance +6 · Saturation −16

**Tone Curve:** (0,8) (48,30) (128,128) (208,222) (255,252) — deep S with a hair of film lift.
**Parametric:** Shadows −12, Darks −6, Lights +6, Highlights +4.

**HSL:**
- Red H+3 S−8 L−4 · Orange H+2 **S−12** L+2 (protect skin) · Yellow H+6 S−28 L−6
- Green H+14 **S−40** L−10 · Aqua H−8 S−10 L−6 · Blue **H−10** S+6 **L−10** (deep) · Magenta/Purple deepened

**Color Grading:** Shadows H215 **S18** L−4 (teal-blue) · Midtones H30 S5 · Highlights H38 S10 (restrained warm) · Balance −8 · Blending 50
**Calibration:** Shadows Tint +8 · Red H+4 S+2 · Green H+14 S−6 · Blue H+6 **S+30**
**Effects:** Grain 12 · Vignette −22

**Before → after:** ordinary evening shot → moody editorial frame; everything desaturates and deepens *except* the subject, who pops with warmth.
**Viewer psychology:** luxury, intrigue, authority.

---

## 4 · WANDERLUST — Orange & Teal
**Intention:** maximum vivid scroll-stop, with skin protected from the orange push.
**Profile:** Adobe Vivid (or Color).

**Basic:** Temp +6, Tint −2 · Exposure +0.1 · Contrast +20 · Highlights −30 · Shadows +30 · Whites +12 · Blacks −8 · Texture +14 · Clarity +12 · Dehaze +16 · Vibrance +22 · Saturation −6

**Tone Curve:** (0,10) (56,42) (128,130) (196,212) (255,250) — punchy.

**HSL:**
- Red H+4 S−4 · Orange H+6 S+6 L+6 (warm pop, *environmental*) · Yellow H−14 S−10 L+2
- Green **H+30** S−20 L−4 (toward teal) · Aqua **H−16 S+18** L+4 (teal water/sky) · Blue H−10 S+20 L−4

**Color Grading:** Shadows H195 **S22** L−2 (teal) · Midtones H200 S6 · Highlights H38 **S16** (orange) · Balance 0 · Blending 50
**Calibration:** Shadows Tint +6 · Red H+6 S+6 · Green H+22 S−4 · Blue H+10 **S+35** (drives the orange/teal separation)
**Effects:** Grain 6 · Vignette −14

**Skin safeguard:** because the global teal/orange split fights skin, *always* finish with Skin Tone Rescue on the subject. The split should live in sand, water, sky, and buildings — not faces.
**Before → after:** flat travel snap → vivid, complementary, postcard-grade image.
**Viewer psychology:** wanderlust, energy, "I want to be there."

---

## 5 · TRUEGLOW — Natural Realism
**Intention:** invisible editing; honest skin with a faint healthy glow.
**Profile:** Adobe Color (or camera Standard for max realism).

**Basic:** Temp +3, Tint +1 · Exposure +0.1 · Contrast +6 · Highlights −18 · Shadows +18 · Whites +6 · Blacks −4 · Texture +6 · Clarity +6 · Dehaze +3 · Vibrance +12 · Saturation 0

**Tone Curve:** (0,2) (64,62) (128,130) (192,198) (255,254) — gentle S, no lift.

**HSL:** Red H+1 S−3 L+2 · Orange H+2 S−4 **L+6** · Yellow S−6 · Green H+6 S−10 · Blue H+2 S−4 L+2 (everything else untouched)

**Color Grading:** Highlights H45 S4 · Shadows H210 S4 · Balance 0 · Blending 70 (barely there)
**Calibration:** Shadows Tint +2 · Blue S+12
**Effects:** Grain 0 · Vignette 0

**Before → after:** raw file → the same photo, just *better* — true colors, clean skin, nothing that screams "filter."
**Viewer psychology:** authenticity, trust, relatability (often the strongest converter for personal-brand creators).

---

## 6 · ANALOG 400 — Film Emulation
**Intention:** genuine film character — faded, grainy, cross-processed channels.
**Profile:** Adobe Color.

**Basic:** Temp +10, Tint +5 · Exposure +0.1 · Contrast −6 · Highlights −20 · Shadows +28 · Whites −6 · Blacks +12 (strong matte) · Texture −4 · Clarity 0 · Dehaze −6 (film softness) · Vibrance +6 · Saturation −10

**Tone Curve (point):** (0,22) (50,55) (128,128) (205,206) (255,242) — heavy fade.
**Per-channel (the film signature):**
- **Blue channel:** lift shadow (0,18) → cool/teal shadows; pull highlight (255,238) → warm/yellow highlights = classic cross-process.
- **Red channel:** slight shadow lift (0,8).

**HSL:** Red H−4 S−10 L+2 · Orange H+4 S−8 L+6 · Yellow H−12 S−6 · Green **H+24 S−30** L−6 (olive) · Aqua H−10 S−16 · Blue H+6 S−10 L−6 · Magenta H+6 S−8

**Color Grading:** Shadows H200 S12 L−2 (teal) · Midtones H40 S4 · Highlights H46 S12 (yellow-cream) · Balance +6 · Blending 50
**Calibration:** Shadows Tint +6 · Red H+6 · Green H+24 S−4 · Blue H−6 S+22
**Effects:** Grain **28 / 28 / 55** (visible) · Vignette −10

**Before → after:** clinical digital file → believable analog frame with grain, lifted blacks, and split-tinted channels.
**Viewer psychology:** artistry, nostalgia, "collectible" feel.

---

## 7 · SUGAR — Feminine Pastel
**Intention:** soft, high-key, cotton-candy palette.
**Profile:** Adobe Color.

**Basic:** Temp +6, Tint +6 · Exposure +0.4 · Contrast −18 · Highlights −30 · Shadows +50 · Whites +14 · Blacks +18 (high matte) · Texture −12 · Clarity −10 · Dehaze −4 · Vibrance +8 · Saturation −22 (pastel = low sat)

**Tone Curve:** (0,24) (64,72) (128,138) (192,206) (255,246) — very lifted, low contrast.
**Parametric:** Shadows +24, Darks +10.

**HSL:**
- Red **H+6** S−16 L+6 (toward pink) · Orange H+8 S−18 L+10 · Yellow H+8 S−24 L+6
- Green H+14 **S−36** L+6 · Aqua H+6 S−18 L+6 · Blue **H+14** S−10 L+8 (toward lavender) · Purple H+6 L+6 · Magenta H+4 S−8 L+8

**Color Grading:** Highlights **H350 (pink)** S12 L+4 · Midtones H320 S4 · Shadows **H250 (lavender)** S12 L+4 · Balance +4 · Blending 55
**Calibration:** Shadows Tint +10 (magenta) · Red H+4 · Green H+10 · Blue H+14 S+14
**Effects:** Grain 8 · Vignette 0

**Before → after:** normal portrait → airy pastel dream with pink highlights and lavender shadows.
**Viewer psychology:** sweetness, softness, youthful charm.

---

## 8 · FLASHBACK — Digicam / Direct Flash
**Intention:** deliberate early-2000s point-and-shoot revival.
**Profile:** Adobe Color (or Standard for a flatter base).

**Basic:** Temp −6, Tint +2 · Exposure −0.1 · Contrast +18 · Highlights **−50** (tame flash hotspots) · Shadows +20 · Whites −12 · Blacks −6 · Texture +16 (crunch) · Clarity +10 · Dehaze +8 · Vibrance +14 · Saturation −2

**Tone Curve:** (0,6) (60,46) (128,132) (196,214) (255,250) — contrasty with a slight toe lift.

**HSL:** Red H+2 S−6 L−2 · Orange H0 S−8 L0 (flash skin stays natural, not orange) · Yellow H+4 S−10 · Green H+8 S−20 L−4 · Aqua H−6 S+6 · Blue H−4 S+10 L−4 · Magenta H+4 S+4 (faint Y2K cast)

**Color Grading:** Shadows H220 S10 (slight cool) · Highlights H40 S6 · Midtones neutral · Balance 0 · Blending 50
**Calibration:** Shadows Tint +4 · Green H+8 · Blue S+20
**Effects:** Grain **18 / 18 / 60** (sensor-noise feel) · Vignette −8

**Before → after:** flat flash snap → punchy, candid "found-photo" frame with believable digicam crunch.
**Viewer psychology:** spontaneity, fun, un-curated cool.

---

## 9 · BRONZE — Sun-Kissed / Fitness
**Intention:** golden tan, defined detail, summer warmth.
**Profile:** Adobe Color (or Vivid for beach).

**Basic:** Temp +12, Tint +4 · Exposure +0.1 · Contrast +14 · Highlights −30 · Shadows +20 · Whites +8 · Blacks −8 · Texture +12 (muscle/skin definition) · Clarity +14 · Dehaze +8 · Vibrance +16 · Saturation −4

**Tone Curve:** (0,8) (60,48) (128,130) (196,210) (255,250) — warm S.

**HSL:** Red H−2 S−2 L−2 · Orange **H+5** S+4 L+2 (golden tan) · Yellow H−8 S+2 · Green H+14 S−24 L−6 · Aqua H−8 S+4 · Blue H+4 S+12 L−6 (deep pool/sky) · Magenta minor

**Color Grading:** Highlights H40 **S16** (gold) · Midtones H35 S8 · Shadows H205 S8 (subtle teal) · Balance +6 · Blending 55
**Calibration:** Shadows Tint +6 · Red H+8 S+4 · Green H+18 · Blue H+8 **S+28**
**Effects:** Grain 6 · Vignette −10

**Before → after:** pale gym/beach shot → warm, defined, sun-kissed frame with golden skin and rich blues behind.
**Viewer psychology:** vitality, health, summer aspiration.

---

# PHASE 4 — INFLUENCER OPTIMIZATION STRATEGY

## 4.1 How HALO maximizes engagement and perceived attractiveness
- **Scroll-stop is engineered separately from likeability.** Contrast, clarity, dehaze, and the orange-teal/vivid packs *stop the thumb*; the warm, glowing, skin-flattering grading *earns the like and follow*. HALO does both jobs with different sliders so they don't fight.
- **Skin is the hero, always.** Every look brightens or warms skin while muting competing colors (greens, busy blues). The eye lands on the face within the first fixation.
- **Restraint signals premium.** Subtle matte + targeted HSL reads as "professional photographer," which raises perceived value of the person and anything they're selling.

> **Honest framing:** grading correlates with performance but does not *guarantee* it. Reach is also driven by content, hook, timing, audio, and format. HALO removes the *visual* reasons a strong post underperforms; it doesn't replace strategy.

## 4.2 Enhancing skin and facial features
- Orange/red HSL tuning per skin tone for healthy, accurate complexion (see Skin Module).
- **Glow / Soft** utility (negative texture/clarity, brushed on skin) smooths without the plastic "beauty-filter" look.
- Highlight control keeps cheekbones and foreheads from blowing out; gentle shadow lift keeps under-eyes and jawlines from going muddy.
- Lens Blur (AI) adds subject separation that flatters the face by softening busy backgrounds.

## 4.3 Building a recognizable personal brand
- **Pick a "home" pack** that matches your niche and personality — this becomes your signature (e.g., a slow-living creator lives in Honeywash; a fitness creator in Bronze).
- Use 1–2 *supporting* packs for variety, unified by the **Grid Harmonizer**.
- Recognition compounds: a consistent palette means followers identify your post before they read the handle. That half-second of recognition is the entire game.

## 4.4 Maintaining consistency across a 9–12 grid
- **Plan the grid, not the post.** Preview tiles in a planner before posting.
- Keep a stable **brightness rhythm** (don't alternate very dark and very bright tiles randomly) and a stable **temperature** (don't mix icy and golden tiles unless intentional).
- Run mixed-lighting outliers through the **Grid Harmonizer** at low strength so the whole grid shares one fingerprint.
- Reserve high-vibrance packs (Wanderlust) for ~1 in 3 tiles; used every tile, they exhaust the eye and the feed reads "loud" rather than "curated."

## 4.5 Cross-niche mapping

| Niche | Primary pack | Support | Notes |
|---|---|---|---|
| Fashion | Daydream / Noir Lumière | Honeywash | Clean for day, dark-lux for editorial |
| Fitness | Bronze | TrueGlow | Definition + glow; keep skin honest |
| Travel | Wanderlust | Honeywash | Vivid hero shots, warm portraits between |
| Lifestyle | Honeywash / Daydream | Sugar | Cozy + clean core |
| Beauty | Sugar / TrueGlow | Daydream | Soft, accurate skin is non-negotiable |
| Creative / music | Analog 400 | Noir Lumière | Film character + drama |
| Gen-Z / candid | Flashback | TrueGlow | Un-precious, real-time energy |

---

# PHASE 5 — REALISM & LIMITATIONS

A premium pack tells you the truth. Here it is.

1. **Presets are starting points, not one-click magic.** They are tuned against a *reference* exposure and skin tone. Every real photo needs the stacked deltas and a final manual nudge. Anyone selling "one-click perfect every time" is selling a fantasy.

2. **RAW vs JPEG matters enormously.** These recipes assume RAW. On a JPEG, the file has less latitude — lifts get noisy and pulls clip faster. Reduce the strength of shadow/highlight moves on JPEG.

3. **Camera and phone profiles render color differently.** A Sony, a Canon, a Fuji, and an iPhone produce different reds and greens from the *same* scene. That's exactly why HALO uses **relative WB guidance** instead of hard Kelvin locks — but you may still need to adjust the **Calibration** primaries per camera. Build a per-camera baseline once, then apply HALO on top.

4. **White balance must be set per image — first.** No grade survives a wrong WB. Neutralize the cast (WB Fix utilities) before applying a look. This is the single most common reason presets "don't work."

5. **Exposure must be corrected before grading.** A look applied to a 1-stop-under file will look nothing like the same look on a correct exposure. Fix exposure, *then* grade.

6. **Skin varies within a tone category.** "Deep," "medium," "fair" are starting buckets, not absolutes. Undertone (warm/cool/neutral) still needs a Skin Tone Rescue pass per person.

7. **Calibrate your monitor.** If you grade on an uncalibrated, over-saturated, over-bright screen, your edits will look wrong on everyone else's phone. This silently ruins more feeds than any slider.

8. **Mobile vs desktop Lightroom differ slightly.** A few sliders and AI features behave differently across platforms; check a look on the device your audience actually uses (phones).

9. **Over-editing is the real risk.** The failure mode of *good* tools is heavy-handedness — orange skin, crushed blacks, HDR-flat midtones. When in doubt, pull strength back 15–20%. Restraint is the look.

### Best practice — refining after applying
1. Apply pack → skin variant → lighting delta → exposure delta.
2. Re-check WB on the *graded* result; fine-tune Temp/Tint ±a few points.
3. Mask the subject (AI) and apply **Skin Tone Rescue**; confirm skin hue against the frame.
4. Adjust **Exposure** to taste (this is the slider you'll touch most; presets rarely nail it).
5. Tame any newly-clipped highlights; lift any newly-muddy shadows.
6. Optional: Lens Blur for separation, light Denoise on lifted shadows.
7. **Compare to the previous post** before publishing — does it belong on the grid?

---

# APPENDIX A — SKU / FILE MAP

```
HALO/
├─ 01_Daydream/        Daydream_Fair  Daydream_Medium  Daydream_Deep
├─ 02_Honeywash/       Honeywash_Fair  ...  _Deep
├─ 03_NoirLumiere/     ...
├─ 04_Wanderlust/      ...
├─ 05_TrueGlow/        ...
├─ 06_Analog400/       ...
├─ 07_Sugar/           ...
├─ 08_Flashback/       ...
├─ 09_Bronze/          ...
├─ _Lighting/          Sunny  Cloudy  Indoor  GoldenHour   (apply on top)
├─ _Exposure/          Under  Over
└─ _Toolkit/           SkinRescue  BackgroundBalancer  HighlightRecovery
                       ShadowLift  WB-Warm  WB-Cool  WB-Green
                       Glow-Soft  GridHarmonizer
```
**Naming convention for stacking:** the three skin files per pack are full presets; everything in the underscore folders is a *delta* preset designed to be applied *after* a pack (Lightroom applies the most recently chosen settings on top).

# APPENDIX B — ONE-PAGE CHEAT SHEET

```
1. EXPOSURE  → Auto/manual; if blown, Highlight Recovery
2. WHITE BAL → neutralize cast (WB Fix utility)
3. SKIN      → load Fair / Medium / Deep file of your pack
4. PACK      → pick by intent (see decision tree)
5. LIGHTING  → stack Sunny / Cloudy / Indoor / Golden delta
6. REFINE    → mask subject, Skin Rescue, tweak exposure, check grid
```

*HALO is built so that the look is the easy part — and the skin and the grid are the parts that actually win.*
