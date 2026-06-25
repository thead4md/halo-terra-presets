# HALO + TERRA — Lightroom Preset System

A modular, professional-grade Lightroom preset library in two halves:

- **HALO** — influencer / portrait grades, engineered around skin-tone accuracy and feed consistency.
- **TERRA** — landscape grades, engineered around believable foliage, dramatic skies, and atmospheric depth.

**49 importable `.xmp` presets**, plus the full design documentation they were built from.

| | Looks | Toolkit | Total |
|---|---|---|---|
| **HALO** | 9 looks × 3 skin tones = **27** | 6 | 33 |
| **TERRA** | **8** | 8 | 16 |
| | | | **49** |

---

## Read this first — how these presets behave

Three deliberate engineering choices, so nothing surprises you:

1. **Lightroom presets *set* values, they don't *add* them.** Applying a second preset overwrites the sliders it contains. That's why:
   - **Looks are complete files** (the HALO skin variants are pre-summed into the HSL/calibration — apply one and you're done).
   - **Toolkit presets are partial** (each touches only the sliders it fixes, so they're safe to apply *after* a look).
   - The **lighting / sky / foliage / exposure modifiers are NOT shipped as `.xmp`** — as files they'd overwrite a look instead of stacking on it. They live in the design docs (`docs/`) as exact manual slider moves. This is intentional, not missing.

2. **No white balance is baked in.** The presets don't set Temperature/Tint, so they respect your corrected/as-shot WB and work across different cameras and phones. The `+/-` temp and tint nudges in the docs are optional manual adjustments. **Always set white balance per photo before applying a look** — it's the #1 reason presets look "off."

3. **Process Version 15.4 / current.** Built for recent Lightroom Classic and Lightroom (CC) with Texture, Dehaze, and the Color Grading panel. Camera profiles used: Adobe Color, Adobe Landscape, Adobe Vivid (available for all cameras).

---

## Install

### Lightroom Classic (desktop)
1. Switch to the **Develop** module.
2. In the **Presets** panel (left), click the **+** → **Import Presets…**
3. Select the `.xmp` files (or the whole `presets/` folder, or a zip of it).
4. They appear under the groups **HALO**, **HALO Toolkit**, **TERRA**, **TERRA Toolkit**.

### Lightroom (CC / desktop cloud app)
1. Open a photo → press **E** (Edit) → open the **Presets** panel (bottom right).
2. Click the **…** menu → **Import Presets…**
3. Select the `.xmp` files or a zip. Presets sync to all your devices via Creative Cloud.

### Lightroom Mobile
- Easiest path: import on Lightroom **desktop (CC)** as above — they sync to mobile automatically.
- Direct import: in the mobile editor open **Presets → … (three dots) → Import Presets** and select the `.xmp` files or a zip from your device.

> Tip: zip the `presets/` folder first (`presets.zip`) — most Lightroom versions accept a zip of `.xmp` files in one import.

---

## Catalog

### HALO — looks (each ships in Fair / Medium / Deep)
| Look | Aesthetic |
|---|---|
| **Daydream** | Bright & airy / clean minimal |
| **Honeywash** | Warm film / nostalgic |
| **Noir Lumiere** | Moody cinematic / dark luxury |
| **Wanderlust** | Orange & teal / travel viral |
| **TrueGlow** | Natural no-filter realism |
| **Analog 400** | Film emulation (cross-processed) |
| **Sugar** | Feminine pastel / cotton candy |
| **Flashback** | Digicam / direct-flash candid |
| **Bronze** | Sun-kissed / fitness |

### HALO — toolkit (partial / masked)
`Skin Tone Rescue` · `Background Color Balancer` · `Highlight Recovery` · `Shadow Lift` · `Glow Soft` · `Grid Harmonizer`

### TERRA — looks
| Look | Scene / mood |
|---|---|
| **Vista** | Clean natural daylight |
| **Goldveil** | Golden hour / sunrise |
| **Alpine** | Mountains / moody peaks |
| **Verdant** | Forest / jungle (greens done right) |
| **Tide** | Coast / tropical water |
| **Ember** | Desert / canyon / autumn |
| **Frost** | Snow / winter |
| **Nocturne** | Blue hour / night / astro |

### TERRA — toolkit (partial / masked)
`Sky Enhancer` · `Foliage Fix` · `Water Pop` · `Atmospheric Depth` · `Sky Recovery` · `Foreground Lift` · `Orton Dreamy` · `Grid Harmonizer`

---

## How to use the system

1. **Correct exposure**, then **set white balance** (these presets leave WB to you).
2. **Apply a look.** For portraits pick the skin-tone variant that matches the subject (Fair / Medium / Deep). For landscapes pick by biome/mood.
3. **Adapt to the light** using the manual lighting/sky/foliage deltas in `docs/` (Sunny / Cloudy / Indoor / Golden, etc.). Remember these are slider *moves*, applied by hand on top of the look.
4. **Refine with the toolkit.** Most toolkit presets are meant to be **masked** — e.g. `Sky Enhancer` on the AI Sky mask, `Skin Tone Rescue` on the subject, `Foliage Fix` on greenery. Landscape work especially expects you to grade **sky and land separately** (AI Sky mask + a foreground gradient).
5. **Unify the feed** by applying the matching **Grid Harmonizer** at low strength to any outliers.

Full per-preset recipes, the adaptive deltas, the decision trees, and the realism/limitations notes are in:
- `docs/HALO_Preset_System.md`
- `docs/TERRA_Landscape_Set.md`

---

## Push this to your own GitHub

This folder is **already a git repository with an initial commit**, so publishing it takes one of two routes.

**With the GitHub CLI (`gh`):**
```bash
gh repo create halo-terra-presets --public --source=. --remote=origin --push
```

**Or manually** — create an empty repo at github.com (no README), then:
```bash
git remote add origin https://github.com/<your-username>/halo-terra-presets.git
git branch -M main
git push -u origin main
```

That's it — your preset library is live.

---

## Repository structure
```
halo-terra-presets/
├── README.md
├── LICENSE
├── .gitignore
├── generate_presets.py        # reproducible generator for every .xmp
├── docs/
│   ├── HALO_Preset_System.md  # full portrait design doc + manual deltas
│   └── TERRA_Landscape_Set.md # full landscape design doc + manual deltas
└── presets/
    ├── HALO/                  # 27 look files + Toolkit/
    └── TERRA/                 # 8 look files + Toolkit/
```

## Regenerating the presets
All `.xmp` files are produced from a single data model:
```bash
python3 generate_presets.py
```
Edit the values in `generate_presets.py` and re-run to tune the whole set consistently.

## License
See `LICENSE`. These are original color configurations — set the license to whatever fits your plans (the default is a proprietary "all rights reserved" placeholder; swap in MIT or CC-BY if you'd rather share them openly).
