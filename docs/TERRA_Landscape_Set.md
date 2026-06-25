# TERRA — The Landscape Grade Set
### A HALO companion, engineered for nature: believable foliage, dramatic skies, atmospheric depth, and feed consistency

> **Why a separate set.** HALO *mutes* the environment so skin is the hero. Landscapes flip that: the environment **is** the subject. So the priorities invert — greens and skies must sing instead of recede, and the two failures that wreck most landscape presets are **radioactive neon foliage** and **fake over-deepened HDR skies**. TERRA is built to avoid both, and around the one habit amateurs skip: **masking the sky and the land separately**, because no single global grade serves both a bright sky and a dark foreground.

**Notation:** identical to HALO. `(input,output)` curve points on 0–255 (a lifted black point = matte). HSL/Calibration −100…+100. Color Grading: `H`=0–360°, `S`=0–100, `L`=−100…+100, with Balance (−favors shadows) and Blending (0–100).

**HSL hue directions used throughout** (so the foliage/sky moves are unambiguous):
`Yellow −→orange / +→green` · `Green −→yellow / +→aqua` · `Aqua −→green / +→blue` · `Blue −→cyan / +→purple` · `Tint −→green / +→magenta`.

---

# PHASE 1 — WHAT CHANGES FROM PORTRAITS

| Concern | Portrait (HALO) | Landscape (TERRA) |
|---|---|---|
| Hero | Skin | Sky, foliage, light, terrain |
| Greens/blues | Muted so they don't compete | Carefully *enhanced* — the whole point |
| Orange luminance | Raised for skin glow | Tuned for rock/sand/autumn, not glow |
| Workflow | Subject mask + skin protect | **Sky mask + foreground gradient**, graded apart |
| Biggest failure | Orange/ashy skin | Neon foliage, fake skies, HDR halos |
| Depth | Subject separation (blur) | Aerial perspective: cool distance / warm foreground |

**The two hard problems**
- **Greens:** sensors render foliage as a bright yellow-green that saturates into neon. The fix is hue-shaping (merge yellows into green, nudge green toward yellow for warmth or toward aqua for cinema) and *lowering green luminance* to deepen it — not cranking saturation.
- **Skies:** deepening blue too far reads fake. Real drama comes from masking the sky, holding highlights, and a controlled blue luminance pull — plus clouds carry structure (clarity/texture), not just color.

---

# PHASE 2 — SYSTEM DESIGN

```
TERRA SET
├── LOOKS (8 biome + mood signatures) ......... the grade
├── ADAPTIVE DELTAS (stack on top)
│     ├── Light / time-of-day  (Midday / Overcast / Golden / Blue-hour)
│     ├── Sky                  (Deepen clear / Save blown / Dramatize clouds)
│     ├── Foliage              (Spring / Summer-deep / Autumn / Arid)
│     └── Exposure             (Under / Over)
├── TOOLKIT (utility fixes, mostly masked)
└── SMART LOGIC (mask-first pipeline + decision tree)
```

### The 8 looks

| # | Name | Scene / mood | One-liner |
|---|------|--------------|-----------|
| 1 | **Vista** | Clean natural daylight, any scene | True-to-a-great-day, Nat-Geo clean |
| 2 | **Goldveil** | Golden hour / sunrise | Warm glow across the whole frame |
| 3 | **Alpine** | Mountains, moody peaks | Cold valleys, warm-lit summits, deep sky |
| 4 | **Verdant** | Forest, jungle, lush green | Rich foliage done right, light shafts |
| 5 | **Tide** | Coast, ocean, tropical | Turquoise water, bright clean sky |
| 6 | **Ember** | Desert, canyon, autumn | Red-gold earth vs. deep blue sky |
| 7 | **Frost** | Snow, winter | Clean cool whites, blue shadows |
| 8 | **Nocturne** | Blue hour, night, astro | Deep night sky, warm foreground glow |

---

# PHASE 3 — FULL SETTINGS

Each master is the look at base. Stack the Phase-4 deltas for light / sky / foliage / exposure. Landscape masters assume you'll **mask sky vs. land** at refine.

---

## 1 · VISTA — Clean Natural Daylight
**Intention:** the scene on its best day — punchy but believable, never HDR.
**Profile:** Adobe Landscape.

**Basic:** Temp +4, Tint +3 · Exposure 0 · Contrast +12 · Highlights −30 · Shadows +30 · Whites +14 · Blacks −10 · Texture +12 · Clarity +12 · Dehaze +10 · Vibrance +18 · Saturation −2
**Tone Curve:** (0,4) (60,46) (128,130) (196,210) (255,252) — gentle punchy S.
**HSL:**
- Red H+2 S+2 L−2 · Orange H+4 S+4 L0 · Yellow H+4 S−2 L+2
- Green **H−8** S+6 **L+6** (natural lush) · Aqua H+2 S+8 L0 · Blue **H+4 S+12 L−8** (rich daytime sky)

**Color Grading:** Shadows H210 S6 L−2 · Midtones neutral · Highlights H48 S6 (warm sun) · Balance 0 · Blending 50
**Calibration:** Shadows Tint +4 · Red H+4 · Green H−6 S+6 · Blue H+6 **S+22**
**Effects:** Grain 0 · Vignette −6 · **Sharpening 45** (landscapes reward detail)

**Before→after:** flat daytime shot → crisp, dimensional, true-color landscape with deep sky and lush-but-real foliage.

---

## 2 · GOLDVEIL — Golden Hour / Sunrise
**Intention:** warm light wrapping the whole scene.
**Profile:** Adobe Landscape.

**Basic:** Temp +14, Tint +4 · Exposure +0.1 · Contrast +8 · Highlights −25 · Shadows +28 · Whites +8 · Blacks −6 · Texture +8 · Clarity +8 · Dehaze +6 · Vibrance +16 · Saturation 0
**Tone Curve:** (0,8) (60,50) (128,130) (196,210) (255,250).
**HSL:**
- Red H−2 S+4 L0 · Orange **H+4 S+8 L+4** (golden light on terrain) · Yellow **H−6** (toward gold) S+6 L+4
- Green H−10 S−4 L+2 (foliage warms; reined in so it doesn't fight the gold) · Aqua H+2 S+4 · Blue **H−4** S+8 L−4 · Magenta S+6 (sunset pinks)

**Color Grading:** Shadows H35 S8 (warm fill) · Midtones H40 S8 · Highlights **H45 S16** (gold) · Balance +6 · Blending 55
**Calibration:** Shadows Tint +6 · Red H+6 S+4 · Green H−8 · Blue H+4 S+18
**Effects:** Grain 8 · Vignette −8

**Before→after:** ordinary light → that 20-minute golden window, glowing and aspirational.

---

## 3 · ALPINE — Mountains / Moody Peaks
**Intention:** cold valleys, warm-lit summits, deep atmospheric sky. The epic look.
**Profile:** Adobe Color (so the moodiness isn't auto-boosted away).

**Basic:** Temp −4, Tint +4 · Exposure −0.15 · Contrast +18 · Highlights −40 · Shadows −8 · Whites −6 · Blacks −14 · Texture +18 · Clarity +16 · **Dehaze +18** (cut haze on distant peaks) · Vibrance +10 · Saturation −12
**Tone Curve:** (0,8) (50,34) (128,128) (206,220) (255,252) — strong, deep, not clipped.
**HSL:**
- Red H+2 S−6 L−4 · Orange H+2 S−8 L0 (rock muted) · Yellow H+4 S−16 L−2 (alpine grass muted)
- Green **H+8 S−18 L−6** (cool, cinematic — *not* lush) · Aqua H−2 S+8 L−4 · Blue **H+6 S+18 L−16** (deep dramatic sky) · Purple H+4 S+6 (alpenglow shadow)

**Color Grading:** Shadows **H220 S20 L−4** (cold = depth) · Midtones H210 S6 · Highlights H40 S10 (warm peaks) · Balance −10 · Blending 45
**Calibration:** Shadows Tint +8 · Red H+4 S+2 · Green H+10 S−6 · Blue H+6 **S+34**
**Effects:** Grain 10 · Vignette −20

**Before→after:** flat mountain snap → cinematic range with cold air in the valleys and warm light catching the summits.

---

## 4 · VERDANT — Forest / Jungle (greens done right)
**Intention:** deep, immersive, *natural* foliage with warm light shafts.
**Profile:** Adobe Landscape.

**Basic:** Temp +6, Tint +6 (richen greens, avoid sickly yellow-green) · Exposure +0.05 · Contrast +12 · Highlights −28 · Shadows +24 · Whites +6 · Blacks −10 · Texture +14 · Clarity +12 · Dehaze +10 · Vibrance +14 · Saturation −4
**Tone Curve:** (0,10) (58,44) (128,128) (196,210) (255,250) — slight toe lift for forest mood.
**HSL — the foliage masterclass:**
- Red H+2 S−2 L−2 · Orange H+4 S0 L0 (trunks, earth)
- Yellow **H+8** (merge yellow-leaves into green) S−4 L0
- Green **H−6 S+10 L−4** (deeper, richer — *lower* luminance is the anti-neon move)
- Aqua H0 S+4 L−2 · Blue H+2 S+6 L−8 (canopy gaps kept deep) · Magenta minor

**Color Grading:** Shadows **H180 S10 L−2** (cyan-green immersion) · Midtones H120 S4 (faint green) · Highlights H50 S8 (warm light shafts) · Balance −4 · Blending 50
**Calibration:** Shadows Tint +6 · Red H+4 · Green **H−8 S+10** · Blue H+2 S+24
**Effects:** Grain 8 · Vignette −16

**Before→after:** neon-leaning forest snap → deep, dimensional woodland where greens are rich but real and light filters warm.

---

## 5 · TIDE — Coast / Tropical Water
**Intention:** turquoise seas, bright clean sky, warm sand.
**Profile:** Adobe Landscape (or Vivid for full tropical pop).

**Basic:** Temp +6, Tint −2 · Exposure +0.1 · Contrast +14 · Highlights −30 · Shadows +26 · Whites +14 · Blacks −8 · Texture +10 · Clarity +12 · Dehaze +14 · Vibrance +20 · Saturation −2
**Tone Curve:** (0,6) (58,46) (128,132) (196,212) (255,252).
**HSL:**
- Red H+2 S0 · Orange H+4 S+4 L+4 (sand; protects skin) · Yellow H−4 S0 L+2 (sand)
- Green H−6 S+6 L+4 (palms) · Aqua **H−4 S+18 L+6** (turquoise shallows) · Blue **H−8 S+18 L−4** (tropical deep water/sky)

**Color Grading:** Shadows H195 S14 L−2 (teal) · Midtones H200 S6 · Highlights H50 S10 (warm sun) · Balance +2 · Blending 50
**Calibration:** Shadows Tint +4 · Red H+6 S+4 · Green H−6 S+4 · Blue H−4 **S+32** (drives turquoise)
**Effects:** Grain 4 · Vignette −10

**Before→after:** dull coast → postcard tropics with vivid turquoise water and clean bright sky.

---

## 6 · EMBER — Desert / Canyon / Autumn
**Intention:** red-gold earth set against deep complementary blue sky.
**Profile:** Adobe Landscape (or Color).

**Basic:** Temp +12, Tint +5 · Exposure 0 · Contrast +16 · Highlights −28 · Shadows +24 · Whites +8 · Blacks −10 · Texture +16 · Clarity +14 · Dehaze +14 · Vibrance +14 · Saturation 0
**Tone Curve:** (0,8) (58,46) (128,130) (196,210) (255,250) — warm punchy S.
**HSL:**
- Red **H−2 S+10 L−2** (rich red rock) · Orange **H+2 S+12 L+2** (canyon glow) · Yellow **H−8 S+8 L+2** (sandstone / autumn leaves)
- Green H−14 S−12 L−4 (sparse scrub muted/warm) · Aqua H+2 S+4 · Blue **H+8 S+14 L−10** (deep sky — the complementary punch) · Magenta S+4

**Color Grading:** Shadows H35 S10 (warm) · Midtones H38 S8 · Highlights **H42 S16** (gold) · Balance +6 · Blending 55
**Calibration:** Shadows Tint +6 · Red **H+10 S+8** · Green H−10 · Blue H+8 S+24
**Effects:** Grain 8 · Vignette −12

**Before→after:** washed desert/autumn → warm, sculpted earth tones against a rich blue sky.
*Autumn:* add the **Foliage → Autumn** delta and this becomes a fire-foliage look.

---

## 7 · FROST — Snow / Winter
**Intention:** clean cool whites and blue shadows, crisp detail.
**Profile:** Adobe Color (Landscape can over-color sparse winter scenes).

**Basic:** Temp −6, Tint +2 · Exposure +0.2 (snow must read white, not grey) · Contrast +12 · Highlights −35 (hold snow detail) · Shadows +20 · Whites +12 · Blacks −8 · Texture +12 · Clarity +10 · Dehaze +12 · Vibrance +10 · Saturation −8
**Tone Curve:** (0,4) (58,44) (128,130) (196,210) (255,252).
**HSL:**
- Red H+2 S−4 L−2 · Orange H+2 S−6 L0
- Yellow **H+4 S−18 L+4** (kill yellow cast → cleaner snow) · Green H+6 S−20 L−2 (evergreens cool)
- Aqua H−2 S+8 L−4 · Blue **H+4 S+16 L−10** (blue snow shadows = cold + depth) · Purple H+4 S+6 (blue-hour)

**Color Grading:** Shadows **H220 S18 L−2** (cold) · Midtones H215 S4 · Highlights H45 S6 · Balance −6 · Blending 45
**Calibration:** Shadows Tint +6 · Red H+2 · Green H+6 S−6 · Blue H+4 **S+28**
**Effects:** Grain 6 · Vignette −10

**Before→after:** muddy grey-yellow snow → clean white with crisp blue shadows.
*WB is the #1 trap here — pair with the Snow WB utility.*

---

## 8 · NOCTURNE — Blue Hour / Night / Astro
**Intention:** deep night sky with a warm foreground anchor.
**Profile:** Adobe Color (Landscape amplifies night noise/color).

**Basic:** Temp −8, Tint +6 · Exposure +0.1 · Contrast +14 · Highlights −20 · Shadows +10 · Whites −6 · Blacks −16 (deep) · Texture +6 (don't sharpen noise) · Clarity +8 · Dehaze +10 · Vibrance +14 · Saturation −6
**Tone Curve:** (0,8) (48,30) (128,128) (206,218) (255,250) — deep, tiny lift to keep stars visible.
**HSL:**
- Red H+2 S−4 L−4 · Orange H+2 S−6 L0 (control warm light-pollution glow) · Yellow **H+4 S−14 L−4** (tame sodium streetlight)
- Green H+6 S−16 L−4 · Aqua H−4 S+10 L−4 · Blue **H+4 S+20 L−14** (deep night sky) · Purple **H+2 S+12 L−4** (Milky Way tones) · Magenta S+6 (airglow/aurora)

**Color Grading:** Shadows **H230 S22 L−4** (deep blue night) · Midtones H225 S8 · Highlights H40 S8 (moon / warm foreground) · Balance −12 · Blending 40
**Calibration:** Shadows Tint +8 · Red H+4 · Green H+6 S−6 · Blue H+6 **S+30**
**Effects:** Grain 4 · Vignette −18 · **Noise Reduction (Luminance) +25**

**Before→after:** noisy dark frame → deep, clean night sky with a warm-lit foreground.
*Astro: lean on AI Denoise; protect stars — over-NR or over-sharpen turns them to mush.*

---

# PHASE 4 — ADAPTIVE DELTAS

### Light / time-of-day (stack on any look)

| Setting | **Midday harsh** | **Overcast / flat** | **Golden** | **Blue hour** |
|---|---|---|---|---|
| Temp | +2 | **+4** | **+6** | **−8** |
| Contrast | −6 | **+12** | −4 | +2 |
| Highlights | **−15** | 0 | −10 | 0 |
| Shadows | +12 | −4 | +8 | +6 |
| Whites | −6 | +6 | 0 | 0 |
| Dehaze | −4 | **+10** | 0 | +4 |
| Clarity | 0 | +6 | 0 | 0 |
| Vibrance | +6 | **+10** | 0 | +6 |
| Blue L / S | 0 | 0 | −4 / 0 | **−6 / +6** |
| Green S | 0 | 0 | −4 | 0 |
| Exposure | 0 | 0 | 0 | +0.15 |
| NR (Lum) | 0 | 0 | 0 | +10 |

### Sky (apply on the AI **Sky** mask)

| Setting | **Deepen clear** | **Save blown/white** | **Dramatize clouds** |
|---|---|---|---|
| Exposure (sky) | 0 | **−0.3** | 0 |
| Highlights | 0 | **−50** | −30 |
| Whites | 0 | **−25** | −15 |
| Dehaze | +6 | +8 | **+12** |
| Clarity / Texture | 0 / 0 | 0 / 0 | **+14 / +10** (cloud structure) |
| Blue H / S / L | +4 / +12 / **−10** | 0 / +10 / 0 | +2 / +8 / −6 |
| Aqua S | +8 | 0 | +6 |

### Foliage (apply on a foliage mask, or globally with care)

| Channel | **Spring fresh** | **Summer deep** | **Autumn** | **Arid / dry** |
|---|---|---|---|---|
| Green H / S / L | −4 / +8 / **+6** | −6 / +10 / **−4** | **−24 / −10** / 0 | −18 / **−24** / +2 |
| Yellow H / S | +6 / +4 | +8 / −2 | **−10 / +10** | −8 / +4 |
| Orange S | 0 | 0 | **+12** | +4 |
| Red S | 0 | 0 | **+10** | 0 |

### Exposure

| Setting | **Underexposed** | **Overexposed** |
|---|---|---|
| Exposure | **+0.6 to +1.0** | **−0.5 to −0.9** |
| Highlights | 0 | **−40** |
| Whites | +6 | **−20** |
| Shadows / Blacks | +20 / +8 | 0 / −4 |
| Dehaze | 0 | +6 |
| Vibrance | +6 | **+8** (recover washed color) |
| NR (Lum) | **+15** | 0 |

### People in the landscape (hikers, figures for scale)
Mask the subject (AI Select Subject) and apply the **HALO Skin Module** (Fair / Medium / Deep) *inside* the mask, so the landscape grade doesn't push faces green, teal, or orange. The land gets graded as a landscape; the person gets graded as a portrait.

---

# PHASE 5 — TOOLKIT (utility, mostly masked)

| Tool | Purpose | Settings |
|---|---|---|
| **Sky Enhancer** ⭐ | Deepen + recover sky (AI Sky mask) | Blue H+4 S+12 L−10; Aqua S+8; Highlights −25; Dehaze +6 |
| **Foliage Fix** ⭐ | De-neon greens | Green H−8 S−8 L+4; Yellow H+8 S−4 (merge); raise green L if dark |
| **Water Pop** | Teal/turquoise water | Aqua H−4 S+16 L+4; Blue S+12; on a water mask |
| **Atmospheric Depth** | Aerial perspective | Dehaze +10; *cool* distance (linear grad, Temp −8) + *warm* foreground (Temp +6) |
| **Sky/Highlight Recovery** | Blown sky | Highlights −60; Whites −25; Dehaze +8; sky mask Exposure −0.3 |
| **Foreground Lift** | Open dark land | Shadows +50; Blacks +15; lower-half gradient; NR +12 |
| **Sun Glow** | Light bloom | Radial mask: Temp +8, Exposure +0.3, Clarity −10, Dehaze −10 |
| **Snow WB** | Neutralize snow cast | Temp −6 to −12; Tint +2; hold Highlights −20 |
| **Orton / Dreamy** | Soft landscape glow | Clarity −18, Texture −12, Exposure +0.15 — masked, low opacity |
| **Grid Harmonizer (Terra)** | Unify a landscape feed | Blacks +4; Highlights H46 S6 / Shadows H215 S6; Vibrance +6 — low strength on outliers |

⭐ Sky Enhancer + Foliage Fix do 80% of landscape rescue work.

---

# PHASE 6 — SMART LOGIC (mask-first pipeline)

**The pipeline — order matters:**
1. **Exposure first.** If the sky is blown → run **Sky/Highlight Recovery** before grading.
2. **White balance.** Neutralize the cast (snow goes blue, forest goes green, golden goes warm). Set per scene.
3. **Mask sky vs. land** — *the* landscape step. AI **Sky** mask + a linear gradient for the foreground. You will grade them semi-independently; one global setting rarely serves both.
4. **Choose the look** by biome + mood (tree below).
5. **Stack deltas** — light / sky / foliage / exposure.
6. **Atmospheric depth** — cool the distance, warm the foreground.
7. **People in frame?** Mask + Skin Module.
8. **Refine** — tame any neon green (Foliage Fix), confirm the sky isn't fake-deep, sharpen for detail, Denoise if night/astro.

**Pack-selection tree**
```
Bright, true-to-life, any scene ........... VISTA
Warm glow / sunrise / sunset .............. GOLDVEIL
Mountains / epic / moody .................. ALPINE
Forest / jungle / lush green .............. VERDANT
Beach / ocean / tropical .................. TIDE
Desert / canyon / red earth / autumn ...... EMBER
Snow / winter ............................. FROST
Night / blue hour / astro ................. NOCTURNE
```

**Condition → action**
| Detected | Do |
|---|---|
| Sky clipping (blown) | Sky Recovery before the look |
| Neon / radioactive foliage | Foliage Fix on a foliage mask |
| Flat overcast | Overcast delta (rebuild contrast + dehaze) |
| Hazy distant peaks | Atmospheric Depth + dehaze on the far gradient |
| Muddy/yellow snow | Snow WB + Frost |
| Night noise | Nocturne + AI Denoise, ease off sharpening |
| Person in shot | Subject mask + Skin Module |
| Feed looks inconsistent | Grid Harmonizer (Terra), low strength |

---

# PHASE 7 — FEED & ENGAGEMENT (landscape/travel)

- **Light and depth are the scroll-stoppers** — golden light, dramatic sky, leading lines, foreground anchors. Grade to amplify those, not to crank saturation.
- **A recognizable palette is the brand.** Landscape/travel feeds win hardest on cohesion; pick a "home" look (e.g., a mountain creator lives in Alpine) and unify outliers with the Grid Harmonizer.
- **Grid rhythm:** alternate wide epics with intimate details (a leaf, a ridge line, texture) so the feed breathes.
- **Mixed creators** who shoot people *and* places: run both HALO and TERRA, then glue the whole feed with a shared Grid Harmonizer fingerprint.
- **Restraint reads premium.** The over-clarity, halo'd, HDR look is the amateur tell; pulling strength back 15–20% almost always helps.

---

# PHASE 8 — REALISM & LIMITATIONS

1. **Greens and skies are per-image.** Every scene's foliage and sky differ; expect to touch Foliage Fix / Sky tuning on most photos. No preset nails foliage blind.
2. **Masking is mandatory, not optional.** Landscape dynamic range (bright sky, dark land) defeats a single global grade. If you refuse to mask, these looks will only ever be half-right.
3. **White balance swings wildly** across snow / forest / golden / blue-hour. Set it per scene before grading.
4. **Dehaze is sharp-edged.** It adds contrast and saturation and can throw halos and color shifts at the horizon and mountain edges. Use sparingly; mask it onto the distance.
5. **HDR halos = the amateur signature.** Over-clarity/over-dehaze around ridgelines and horizons. Watch for it.
6. **Camera profile compounds.** Adobe *Landscape* already boosts greens/blues — stacking a saturated preset on top can push neon. Drop to *Color* when a look goes loud, and rebuild a per-camera baseline once.
7. **These grade real skies — they don't replace them.** Sky replacement is a separate tool; TERRA enhances what you captured.
8. **Astro needs care.** Denoise and gentle sharpening, or stars turn to noise/mush. Don't treat a night sky like a daytime one.

**Refine checklist**
1. Look → light delta → sky delta → foliage delta → exposure delta.
2. Re-mask sky vs. land; tune each side's exposure/WB.
3. Foliage Fix if anything reads neon; confirm sky isn't fake-deep.
4. Atmospheric depth on the distance.
5. Person in frame → Skin Module inside subject mask.
6. Sharpen for detail; Denoise lifted shadows / night.
7. Compare to the previous tile before posting.

---

# APPENDIX — FILE MAP & CHEAT SHEET

```
TERRA/
├─ 01_Vista/  02_Goldveil/  03_Alpine/  04_Verdant/
├─ 05_Tide/   06_Ember/     07_Frost/   08_Nocturne/
├─ _Light/    Midday  Overcast  Golden  BlueHour      (stack on a look)
├─ _Sky/      DeepenClear  SaveBlown  DramatizeClouds (on Sky mask)
├─ _Foliage/  Spring  SummerDeep  Autumn  Arid        (on foliage mask)
├─ _Exposure/ Under  Over
└─ _Toolkit/  SkyEnhancer  FoliageFix  WaterPop  AtmosphericDepth
              SkyRecovery  ForegroundLift  SunGlow  SnowWB
              OrtonDreamy  GridHarmonizer
```

```
LANDSCAPE QUICK PASS
1. EXPOSURE  → fix; if sky blown, Sky Recovery first
2. WHITE BAL → neutralize per scene (snow/forest/golden differ)
3. MASK      → Sky AI mask + foreground gradient (grade apart)
4. LOOK      → pick by biome + mood
5. DELTAS    → light / sky / foliage / exposure
6. DEPTH     → cool distance, warm foreground
7. REFINE    → Foliage Fix, sharpen, Denoise, check the grid
```

*TERRA's job is to make greens and skies believable and the depth real — the look is the easy part; the mask is what wins.*
