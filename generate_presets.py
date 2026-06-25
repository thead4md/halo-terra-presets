#!/usr/bin/env python3
"""
HALO + TERRA preset generator.

Emits Adobe Camera Raw / Lightroom .xmp develop presets from a compact data
model so every value stays consistent and the whole set is reproducible.

Design notes baked into the output:
  * No white balance is written (no Temperature/Tint). Presets respect the
    user's as-shot / corrected WB. The +/- temp & tint nudges from the design
    docs are intentional MANUAL adjustments, documented in the README.
  * Look presets are COMPLETE (skin variants summed into HSL/Calibration).
  * Toolkit presets are PARTIAL (only the fields they fix), since Lightroom
    SETS values rather than adding them.
  * Color Grading is written across the SplitToning* (shadow/highlight hue+sat,
    balance) and ColorGrade* (midtone h/s/l, shadow/highlight lum, blending)
    fields, which is how Lightroom Classic stores the 3-way panel.
"""

import os, uuid

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "presets")

COLORS = ["Red", "Orange", "Yellow", "Green", "Aqua", "Blue", "Purple", "Magenta"]


def clamp(v):
    return max(-100, min(100, v))


def huecl(v):
    # Color Grading hue is a 0-360 degree wheel, NOT a -100..100 slider.
    return max(0, min(360, int(v)))


def xesc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def fmt(v):
    if isinstance(v, float):
        return f"{v:.2f}"
    return str(int(v))


def scalar_attrs(pairs):
    """pairs: list of (crsKey, value or None). Skip None."""
    out = []
    for k, v in pairs:
        if v is None:
            continue
        out.append(f'\n   crs:{k}="{fmt(v) if not isinstance(v, str) else v}"')
    return "".join(out)


def curve_block(tag, points):
    lis = "".join(f"\n      <rdf:li>{x}, {y}</rdf:li>" for x, y in points)
    return (f"\n   <crs:{tag}>\n    <rdf:Seq>{lis}\n    </rdf:Seq>\n   </crs:{tag}>")


XMP = '''<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="HALO+TERRA Generator 1.0">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
   xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"
   crs:PresetType="Normal"
   crs:Cluster=""
   crs:UUID="{uuid}"
   crs:SupportsAmount="False"
   crs:SupportsColor="True"
   crs:SupportsMonochrome="False"
   crs:SupportsHighDynamicRange="True"
   crs:SupportsNormalDynamicRange="True"
   crs:SupportsSceneReferred="True"
   crs:SupportsOutputReferred="True"
   crs:CameraModelRestriction=""
   crs:Copyright=""
   crs:ContactInfo=""
   crs:Version="16.0"
   crs:ProcessVersion="15.4"
   crs:HasSettings="True"{attrs}>
   <crs:Name>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{name}</rdf:li>
    </rdf:Alt>
   </crs:Name>
   <crs:Group>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{group}</rdf:li>
    </rdf:Alt>
   </crs:Group>
   <crs:Description>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{desc}</rdf:li>
    </rdf:Alt>
   </crs:Description>{elements}
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
'''

BASIC_MAP = [
    ("exposure", "Exposure2012"), ("contrast", "Contrast2012"),
    ("highlights", "Highlights2012"), ("shadows", "Shadows2012"),
    ("whites", "Whites2012"), ("blacks", "Blacks2012"),
    ("texture", "Texture"), ("clarity", "Clarity2012"),
    ("dehaze", "Dehaze"), ("vibrance", "Vibrance"), ("saturation", "Saturation"),
]
PARAM_MAP = [
    ("shadows", "ParametricShadows"), ("darks", "ParametricDarks"),
    ("lights", "ParametricLights"), ("highlights", "ParametricHighlights"),
]
CALIB_MAP = [
    ("tint", "ShadowTint"), ("RedHue", "RedHue"), ("RedSat", "RedSaturation"),
    ("GreenHue", "GreenHue"), ("GreenSat", "GreenSaturation"),
    ("BlueHue", "BlueHue"), ("BlueSat", "BlueSaturation"),
]


def build(name, group, desc, s):
    pairs = []
    if "profile" in s:
        pairs.append(("CameraProfile", s["profile"]))

    b = s.get("basic", {})
    for key, crs in BASIC_MAP:
        if key in b:
            v = b[key]
            pairs.append((crs, float(v) if key == "exposure" else clamp(int(v))))

    for sub, suffix in (("hue", "HueAdjustment"), ("sat", "SaturationAdjustment"),
                        ("lum", "LuminanceAdjustment")):
        d = s.get(sub, {})
        for c in COLORS:
            if c in d:
                pairs.append((f"{suffix}{c}", clamp(int(d[c]))))

    if "cg" in s:
        cg = s["cg"]
        sh, mid, hi = cg.get("sh", (0, 0, 0)), cg.get("mid", (0, 0, 0)), cg.get("hi", (0, 0, 0))
        pairs += [
            ("SplitToningShadowHue", huecl(sh[0])),
            ("SplitToningShadowSaturation", clamp(int(sh[1]))),
            ("SplitToningHighlightHue", huecl(hi[0])),
            ("SplitToningHighlightSaturation", clamp(int(hi[1]))),
            ("SplitToningBalance", clamp(int(cg.get("balance", 0)))),
            ("ColorGradeMidtoneHue", huecl(mid[0])),
            ("ColorGradeMidtoneSat", clamp(int(mid[1]))),
            ("ColorGradeMidtoneLum", clamp(int(mid[2]))),
            ("ColorGradeShadowLum", clamp(int(sh[2]))),
            ("ColorGradeHighlightLum", clamp(int(hi[2]))),
            ("ColorGradeGlobalHue", 0), ("ColorGradeGlobalSat", 0),
            ("ColorGradeGlobalLum", 0),
            ("ColorGradeBlending", clamp(int(cg.get("blending", 50)))),
        ]

    if "calib" in s:
        cal = s["calib"]
        for key, crs in CALIB_MAP:
            if key in cal:
                pairs.append((crs, clamp(int(cal[key]))))

    if "param" in s:
        p = s["param"]
        for key, crs in PARAM_MAP:
            if key in p:
                pairs.append((crs, clamp(int(p[key]))))
        pairs += [("ParametricShadowSplit", 25),
                  ("ParametricMidtoneSplit", 50),
                  ("ParametricHighlightSplit", 75)]

    if "grain" in s and any(s["grain"]):
        a, sz, fr = s["grain"]
        pairs += [("GrainAmount", clamp(int(a))), ("GrainSize", clamp(int(sz))),
                  ("GrainFrequency", clamp(int(fr)))]

    if s.get("vignette"):
        pairs += [("PostCropVignetteAmount", clamp(int(s["vignette"]))),
                  ("PostCropVignetteMidpoint", 50), ("PostCropVignetteFeather", 50),
                  ("PostCropVignetteRoundness", 0), ("PostCropVignetteStyle", 1),
                  ("PostCropVignetteHighlightContrast", 0)]

    if "sharpening" in s:
        pairs += [("Sharpness", clamp(int(s["sharpening"]))),
                  ("SharpenRadius", "+1.0"), ("SharpenDetail", 25),
                  ("SharpenEdgeMasking", 0)]

    if "nr_lum" in s:
        pairs.append(("LuminanceSmoothing", clamp(int(s["nr_lum"]))))

    elements = ""
    if "curve" in s:
        elements += curve_block("ToneCurvePV2012", s["curve"])
    if "curve_red" in s:
        elements += curve_block("ToneCurvePV2012Red", s["curve_red"])
    if "curve_green" in s:
        elements += curve_block("ToneCurvePV2012Green", s["curve_green"])
    if "curve_blue" in s:
        elements += curve_block("ToneCurvePV2012Blue", s["curve_blue"])

    return XMP.format(uuid=uuid.uuid4().hex.upper(), attrs=scalar_attrs(pairs),
                      name=xesc(name), group=xesc(group), desc=xesc(desc), elements=elements)


def write(folder, name, group, desc, s):
    os.makedirs(folder, exist_ok=True)
    safe = name.replace("/", "-")
    with open(os.path.join(folder, f"{safe}.xmp"), "w", encoding="utf-8") as f:
        f.write(build(name, group, desc, s))


# ----------------------------------------------------------------------------
# SKIN MODULE deltas (summed into each HALO look to make Fair/Medium/Deep)
# ----------------------------------------------------------------------------
SKIN = {
    "Fair":   {"hue": {"Red": 2, "Orange": -2}, "sat": {"Red": -8, "Orange": -6},
               "lum": {"Red": 2, "Orange": 4}, "basic": {"highlights": -8},
               "calib": {"RedHue": 4}},
    "Medium": {"hue": {"Orange": 2, "Yellow": 4},
               "sat": {"Orange": -2, "Yellow": -8, "Green": -10},
               "lum": {"Orange": 2}, "calib": {"tint": -2}},
    "Deep":   {"hue": {"Red": 1, "Orange": 1, "Yellow": 2},
               "sat": {"Red": 4, "Orange": 4}, "lum": {"Orange": 1},
               "basic": {"blacks": 6, "shadows": 10, "dehaze": -6},
               "calib": {"tint": 2, "RedSat": 6}},
}


def merge_skin(base, delta):
    import copy
    out = copy.deepcopy(base)
    for sub in ("hue", "sat", "lum", "basic", "calib"):
        if sub in delta:
            out.setdefault(sub, {})
            for k, v in delta[sub].items():
                out[sub][k] = clamp(out[sub].get(k, 0) + v)
    return out


# ----------------------------------------------------------------------------
# HALO LOOKS (master recipes, referenced to medium skin)
# ----------------------------------------------------------------------------
HALO = {
"Daydream": {"desc":"Bright & airy. Weightless clean light; glowing skin, muted environment.",
 "profile":"Adobe Color",
 "basic":{"exposure":0.35,"contrast":-12,"highlights":-35,"shadows":45,"whites":18,"blacks":12,"texture":-8,"clarity":-6,"dehaze":-3,"vibrance":14,"saturation":-8},
 "curve":[(0,18),(64,68),(128,135),(192,205),(255,250)],
 "param":{"highlights":-10,"lights":5,"darks":12,"shadows":20},
 "hue":{"Red":2,"Orange":4,"Yellow":-6,"Green":10,"Blue":6},
 "sat":{"Red":-8,"Orange":-10,"Yellow":-18,"Green":-30,"Aqua":-15,"Blue":-12},
 "lum":{"Red":4,"Orange":12,"Yellow":10,"Green":8,"Aqua":5,"Blue":6},
 "cg":{"sh":(220,6,2),"mid":(0,0,0),"hi":(45,8,0),"balance":10,"blending":60},
 "calib":{"tint":4,"RedHue":6,"GreenHue":12,"GreenSat":5,"BlueSat":18},
 "grain":(0,0,0),"vignette":0,"sharpening":35},

"Honeywash": {"desc":"Warm film / nostalgic. Golden highlights, faded matte shadows, olive greens.",
 "profile":"Adobe Color",
 "basic":{"exposure":0.15,"contrast":-8,"highlights":-28,"shadows":35,"whites":6,"blacks":8,"texture":4,"clarity":5,"dehaze":4,"vibrance":10,"saturation":-4},
 "curve":[(0,16),(60,60),(128,132),(200,210),(255,248)],
 "param":{"highlights":-8,"lights":4,"darks":8,"shadows":16},
 "hue":{"Red":-2,"Orange":6,"Yellow":-10,"Green":18,"Aqua":-12,"Blue":8},
 "sat":{"Red":-6,"Orange":-6,"Yellow":4,"Green":-22,"Aqua":-10,"Blue":-8},
 "lum":{"Red":2,"Orange":8,"Yellow":4,"Green":-4,"Blue":-4},
 "cg":{"sh":(195,7,-3),"mid":(40,6,0),"hi":(42,14,0),"balance":5,"blending":55},
 "calib":{"tint":6,"RedHue":8,"RedSat":4,"GreenHue":20,"BlueSat":20},
 "grain":(14,22,50),"vignette":-6},

"Noir Lumiere": {"desc":"Moody cinematic / dark luxury. Muted frame, deep blacks, skin kept alive.",
 "profile":"Adobe Color",
 "basic":{"exposure":-0.25,"contrast":22,"highlights":-45,"shadows":-10,"whites":-8,"blacks":-18,"texture":12,"clarity":14,"dehaze":10,"vibrance":6,"saturation":-16},
 "curve":[(0,8),(48,30),(128,128),(208,222),(255,252)],
 "param":{"highlights":4,"lights":6,"darks":-6,"shadows":-12},
 "hue":{"Red":3,"Orange":2,"Yellow":6,"Green":14,"Aqua":-8,"Blue":-10},
 "sat":{"Red":-8,"Orange":-12,"Yellow":-28,"Green":-40,"Aqua":-10,"Blue":6},
 "lum":{"Red":-4,"Orange":2,"Yellow":-6,"Green":-10,"Aqua":-6,"Blue":-10},
 "cg":{"sh":(215,18,-4),"mid":(30,5,0),"hi":(38,10,0),"balance":-8,"blending":50},
 "calib":{"tint":8,"RedHue":4,"RedSat":2,"GreenHue":14,"GreenSat":-6,"BlueHue":6,"BlueSat":30},
 "grain":(12,25,50),"vignette":-22},

"Wanderlust": {"desc":"Orange & teal travel viral. Vivid complementary split; protect skin separately.",
 "profile":"Adobe Vivid",
 "basic":{"exposure":0.1,"contrast":20,"highlights":-30,"shadows":30,"whites":12,"blacks":-8,"texture":14,"clarity":12,"dehaze":16,"vibrance":22,"saturation":-6},
 "curve":[(0,10),(56,42),(128,130),(196,212),(255,250)],
 "hue":{"Red":4,"Orange":6,"Yellow":-14,"Green":30,"Aqua":-16,"Blue":-10},
 "sat":{"Red":-4,"Orange":6,"Yellow":-10,"Green":-20,"Aqua":18,"Blue":20},
 "lum":{"Orange":6,"Yellow":2,"Green":-4,"Aqua":4,"Blue":-4},
 "cg":{"sh":(195,22,-2),"mid":(200,6,0),"hi":(38,16,0),"balance":0,"blending":50},
 "calib":{"tint":6,"RedHue":6,"RedSat":6,"GreenHue":22,"GreenSat":-4,"BlueHue":10,"BlueSat":35},
 "grain":(6,20,50),"vignette":-14},

"TrueGlow": {"desc":"Natural no-filter realism. Honest skin with a faint healthy glow.",
 "profile":"Adobe Color",
 "basic":{"exposure":0.1,"contrast":6,"highlights":-18,"shadows":18,"whites":6,"blacks":-4,"texture":6,"clarity":6,"dehaze":3,"vibrance":12,"saturation":0},
 "curve":[(0,2),(64,62),(128,130),(192,198),(255,254)],
 "hue":{"Red":1,"Orange":2,"Green":6,"Blue":2},
 "sat":{"Red":-3,"Orange":-4,"Yellow":-6,"Green":-10,"Blue":-4},
 "lum":{"Red":2,"Orange":6,"Blue":2},
 "cg":{"sh":(210,4,0),"mid":(0,0,0),"hi":(45,4,0),"balance":0,"blending":70},
 "calib":{"tint":2,"BlueSat":12}},

"Analog 400": {"desc":"Film emulation. Faded, grainy, cross-processed channel curves.",
 "profile":"Adobe Color",
 "basic":{"exposure":0.1,"contrast":-6,"highlights":-20,"shadows":28,"whites":-6,"blacks":12,"texture":-4,"clarity":0,"dehaze":-6,"vibrance":6,"saturation":-10},
 "curve":[(0,22),(50,55),(128,128),(205,206),(255,242)],
 "curve_red":[(0,8),(128,128),(255,255)],
 "curve_blue":[(0,18),(128,128),(255,238)],
 "hue":{"Red":-4,"Orange":4,"Yellow":-12,"Green":24,"Aqua":-10,"Blue":6,"Magenta":6},
 "sat":{"Red":-10,"Orange":-8,"Yellow":-6,"Green":-30,"Aqua":-16,"Blue":-10,"Magenta":-8},
 "lum":{"Red":2,"Orange":6,"Yellow":2,"Green":-6,"Blue":-6},
 "cg":{"sh":(200,12,-2),"mid":(40,4,0),"hi":(46,12,0),"balance":6,"blending":50},
 "calib":{"tint":6,"RedHue":6,"GreenHue":24,"GreenSat":-4,"BlueHue":-6,"BlueSat":22},
 "grain":(28,28,55),"vignette":-10},

"Sugar": {"desc":"Feminine pastel / cotton candy. High-key, low saturation, pink+lavender grade.",
 "profile":"Adobe Color",
 "basic":{"exposure":0.4,"contrast":-18,"highlights":-30,"shadows":50,"whites":14,"blacks":18,"texture":-12,"clarity":-10,"dehaze":-4,"vibrance":8,"saturation":-22},
 "curve":[(0,24),(64,72),(128,138),(192,206),(255,246)],
 "param":{"darks":10,"shadows":24},
 "hue":{"Red":6,"Orange":8,"Yellow":8,"Green":14,"Aqua":6,"Blue":14,"Purple":6,"Magenta":4},
 "sat":{"Red":-16,"Orange":-18,"Yellow":-24,"Green":-36,"Aqua":-18,"Blue":-10,"Purple":-6,"Magenta":-8},
 "lum":{"Red":6,"Orange":10,"Yellow":6,"Green":6,"Aqua":6,"Blue":8,"Purple":6,"Magenta":8},
 "cg":{"sh":(250,12,4),"mid":(320,4,0),"hi":(350,12,4),"balance":4,"blending":55},
 "calib":{"tint":10,"RedHue":4,"RedSat":-2,"GreenHue":10,"BlueHue":14,"BlueSat":14},
 "grain":(8,20,50),"vignette":0},

"Flashback": {"desc":"Digicam / direct flash. Y2K candid with recovered hotspots and sensor crunch.",
 "profile":"Adobe Color",
 "basic":{"exposure":-0.1,"contrast":18,"highlights":-50,"shadows":20,"whites":-12,"blacks":-6,"texture":16,"clarity":10,"dehaze":8,"vibrance":14,"saturation":-2},
 "curve":[(0,6),(60,46),(128,132),(196,214),(255,250)],
 "hue":{"Red":2,"Yellow":4,"Green":8,"Aqua":-6,"Blue":-4,"Magenta":4},
 "sat":{"Red":-6,"Orange":-8,"Yellow":-10,"Green":-20,"Aqua":6,"Blue":10,"Magenta":4},
 "lum":{"Red":-2,"Green":-4,"Blue":-4},
 "cg":{"sh":(220,10,0),"mid":(0,0,0),"hi":(40,6,0),"balance":0,"blending":50},
 "calib":{"tint":4,"GreenHue":8,"BlueSat":20},
 "grain":(18,18,60),"vignette":-8},

"Bronze": {"desc":"Sun-kissed / fitness. Golden tan, defined detail, deep blues behind.",
 "profile":"Adobe Color",
 "basic":{"exposure":0.1,"contrast":14,"highlights":-30,"shadows":20,"whites":8,"blacks":-8,"texture":12,"clarity":14,"dehaze":8,"vibrance":16,"saturation":-4},
 "curve":[(0,8),(60,48),(128,130),(196,210),(255,250)],
 "hue":{"Red":-2,"Orange":5,"Yellow":-8,"Green":14,"Aqua":-8,"Blue":4},
 "sat":{"Red":-2,"Orange":4,"Yellow":2,"Green":-24,"Aqua":4,"Blue":12},
 "lum":{"Red":-2,"Orange":2,"Green":-6,"Blue":-6},
 "cg":{"sh":(205,8,0),"mid":(35,8,0),"hi":(40,16,0),"balance":6,"blending":55},
 "calib":{"tint":6,"RedHue":8,"RedSat":4,"GreenHue":18,"BlueHue":8,"BlueSat":28},
 "grain":(6,20,50),"vignette":-10},
}

# ----------------------------------------------------------------------------
# TERRA LOOKS (landscape, no skin variants)
# ----------------------------------------------------------------------------
TERRA = {
"Vista": {"desc":"Clean natural daylight. True-to-a-great-day, deep sky, lush-but-real foliage.",
 "profile":"Adobe Landscape",
 "basic":{"exposure":0.0,"contrast":12,"highlights":-30,"shadows":30,"whites":14,"blacks":-10,"texture":12,"clarity":12,"dehaze":10,"vibrance":18,"saturation":-2},
 "curve":[(0,4),(60,46),(128,130),(196,210),(255,252)],
 "hue":{"Red":2,"Orange":4,"Yellow":4,"Green":-8,"Aqua":2,"Blue":4},
 "sat":{"Red":2,"Orange":4,"Yellow":-2,"Green":6,"Aqua":8,"Blue":12},
 "lum":{"Red":-2,"Yellow":2,"Green":6,"Blue":-8},
 "cg":{"sh":(210,6,-2),"mid":(0,0,0),"hi":(48,6,0),"balance":0,"blending":50},
 "calib":{"tint":4,"RedHue":4,"GreenHue":-6,"GreenSat":6,"BlueHue":6,"BlueSat":22},
 "grain":(0,0,0),"vignette":-6,"sharpening":45},

"Goldveil": {"desc":"Golden hour / sunrise. Warm light wrapping the whole scene.",
 "profile":"Adobe Landscape",
 "basic":{"exposure":0.1,"contrast":8,"highlights":-25,"shadows":28,"whites":8,"blacks":-6,"texture":8,"clarity":8,"dehaze":6,"vibrance":16,"saturation":0},
 "curve":[(0,8),(60,50),(128,130),(196,210),(255,250)],
 "hue":{"Red":-2,"Orange":4,"Yellow":-6,"Green":-10,"Aqua":2,"Blue":-4},
 "sat":{"Red":4,"Orange":8,"Yellow":6,"Green":-4,"Aqua":4,"Blue":8,"Magenta":6},
 "lum":{"Orange":4,"Yellow":4,"Green":2,"Blue":-4},
 "cg":{"sh":(35,8,0),"mid":(40,8,0),"hi":(45,16,0),"balance":6,"blending":55},
 "calib":{"tint":6,"RedHue":6,"RedSat":4,"GreenHue":-8,"BlueHue":4,"BlueSat":18},
 "grain":(8,20,50),"vignette":-8},

"Alpine": {"desc":"Mountains / moody peaks. Cold valleys, warm-lit summits, deep atmospheric sky.",
 "profile":"Adobe Color",
 "basic":{"exposure":-0.15,"contrast":18,"highlights":-40,"shadows":-8,"whites":-6,"blacks":-14,"texture":18,"clarity":16,"dehaze":18,"vibrance":10,"saturation":-12},
 "curve":[(0,8),(50,34),(128,128),(206,220),(255,252)],
 "hue":{"Red":2,"Orange":2,"Yellow":4,"Green":8,"Aqua":-2,"Blue":6,"Purple":4},
 "sat":{"Red":-6,"Orange":-8,"Yellow":-16,"Green":-18,"Aqua":8,"Blue":18,"Purple":6},
 "lum":{"Red":-4,"Yellow":-2,"Green":-6,"Aqua":-4,"Blue":-16},
 "cg":{"sh":(220,20,-4),"mid":(210,6,0),"hi":(40,10,0),"balance":-10,"blending":45},
 "calib":{"tint":8,"RedHue":4,"RedSat":2,"GreenHue":10,"GreenSat":-6,"BlueHue":6,"BlueSat":34},
 "grain":(10,22,50),"vignette":-20},

"Verdant": {"desc":"Forest / jungle. Deep immersive foliage done right, with warm light shafts.",
 "profile":"Adobe Landscape",
 "basic":{"exposure":0.05,"contrast":12,"highlights":-28,"shadows":24,"whites":6,"blacks":-10,"texture":14,"clarity":12,"dehaze":10,"vibrance":14,"saturation":-4},
 "curve":[(0,10),(58,44),(128,128),(196,210),(255,250)],
 "hue":{"Red":2,"Orange":4,"Yellow":8,"Green":-6,"Blue":2},
 "sat":{"Red":-2,"Yellow":-4,"Green":10,"Aqua":4,"Blue":6},
 "lum":{"Red":-2,"Green":-4,"Aqua":-2,"Blue":-8},
 "cg":{"sh":(180,10,-2),"mid":(120,4,0),"hi":(50,8,0),"balance":-4,"blending":50},
 "calib":{"tint":6,"RedHue":4,"GreenHue":-8,"GreenSat":10,"BlueHue":2,"BlueSat":24},
 "grain":(8,20,50),"vignette":-16},

"Tide": {"desc":"Coast / tropical. Turquoise water, bright clean sky, warm sand.",
 "profile":"Adobe Landscape",
 "basic":{"exposure":0.1,"contrast":14,"highlights":-30,"shadows":26,"whites":14,"blacks":-8,"texture":10,"clarity":12,"dehaze":14,"vibrance":20,"saturation":-2},
 "curve":[(0,6),(58,46),(128,132),(196,212),(255,252)],
 "hue":{"Red":2,"Orange":4,"Yellow":-4,"Green":-6,"Aqua":-4,"Blue":-8},
 "sat":{"Orange":4,"Green":6,"Aqua":18,"Blue":18},
 "lum":{"Orange":4,"Yellow":2,"Green":4,"Aqua":6,"Blue":-4},
 "cg":{"sh":(195,14,-2),"mid":(200,6,0),"hi":(50,10,0),"balance":2,"blending":50},
 "calib":{"tint":4,"RedHue":6,"RedSat":4,"GreenHue":-6,"GreenSat":4,"BlueHue":-4,"BlueSat":32},
 "grain":(4,20,50),"vignette":-10},

"Ember": {"desc":"Desert / canyon / autumn. Red-gold earth against a deep complementary blue sky.",
 "profile":"Adobe Landscape",
 "basic":{"exposure":0.0,"contrast":16,"highlights":-28,"shadows":24,"whites":8,"blacks":-10,"texture":16,"clarity":14,"dehaze":14,"vibrance":14,"saturation":0},
 "curve":[(0,8),(58,46),(128,130),(196,210),(255,250)],
 "hue":{"Red":-2,"Orange":2,"Yellow":-8,"Green":-14,"Aqua":2,"Blue":8},
 "sat":{"Red":10,"Orange":12,"Yellow":8,"Green":-12,"Aqua":4,"Blue":14,"Magenta":4},
 "lum":{"Red":-2,"Orange":2,"Yellow":2,"Green":-4,"Blue":-10},
 "cg":{"sh":(35,10,0),"mid":(38,8,0),"hi":(42,16,0),"balance":6,"blending":55},
 "calib":{"tint":6,"RedHue":10,"RedSat":8,"GreenHue":-10,"BlueHue":8,"BlueSat":24},
 "grain":(8,20,50),"vignette":-12},

"Frost": {"desc":"Snow / winter. Clean cool whites, crisp detail, blue shadows.",
 "profile":"Adobe Color",
 "basic":{"exposure":0.2,"contrast":12,"highlights":-35,"shadows":20,"whites":12,"blacks":-8,"texture":12,"clarity":10,"dehaze":12,"vibrance":10,"saturation":-8},
 "curve":[(0,4),(58,44),(128,130),(196,210),(255,252)],
 "hue":{"Red":2,"Orange":2,"Yellow":4,"Green":6,"Aqua":-2,"Blue":4,"Purple":4},
 "sat":{"Red":-4,"Orange":-6,"Yellow":-18,"Green":-20,"Aqua":8,"Blue":16,"Purple":6},
 "lum":{"Red":-2,"Yellow":4,"Green":-2,"Aqua":-4,"Blue":-10},
 "cg":{"sh":(220,18,-2),"mid":(215,4,0),"hi":(45,6,0),"balance":-6,"blending":45},
 "calib":{"tint":6,"RedHue":2,"GreenHue":6,"GreenSat":-6,"BlueHue":4,"BlueSat":28},
 "grain":(6,20,50),"vignette":-10},

"Nocturne": {"desc":"Blue hour / night / astro. Deep night sky with a warm foreground anchor.",
 "profile":"Adobe Color",
 "basic":{"exposure":0.1,"contrast":14,"highlights":-20,"shadows":10,"whites":-6,"blacks":-16,"texture":6,"clarity":8,"dehaze":10,"vibrance":14,"saturation":-6},
 "curve":[(0,8),(48,30),(128,128),(206,218),(255,250)],
 "hue":{"Red":2,"Orange":2,"Yellow":4,"Green":6,"Aqua":-4,"Blue":4,"Purple":2},
 "sat":{"Red":-4,"Orange":-6,"Yellow":-14,"Green":-16,"Aqua":10,"Blue":20,"Purple":12,"Magenta":6},
 "lum":{"Red":-4,"Yellow":-4,"Green":-4,"Aqua":-4,"Blue":-14,"Purple":-4},
 "cg":{"sh":(230,22,-4),"mid":(225,8,0),"hi":(40,8,0),"balance":-12,"blending":40},
 "calib":{"tint":8,"RedHue":4,"GreenHue":6,"GreenSat":-6,"BlueHue":6,"BlueSat":30},
 "grain":(4,20,50),"vignette":-18,"nr_lum":25},
}

# ----------------------------------------------------------------------------
# TOOLKIT (PARTIAL presets - only the fields they fix)
# ----------------------------------------------------------------------------
HALO_TOOLKIT = {
"Skin Tone Rescue": {"desc":"Even and calm skin. Apply on a subject mask; pair with Point Color.",
 "hue":{"Orange":2}, "sat":{"Red":-10,"Orange":-10}, "lum":{"Orange":6}},
"Background Color Balancer": {"desc":"Mute competing colors so the subject pops. Best on a background mask.",
 "sat":{"Green":-25,"Aqua":-15,"Blue":-15}},
"Highlight Recovery": {"desc":"Rescue blown highlights and skies.",
 "basic":{"highlights":-60,"whites":-25,"dehaze":6}},
"Shadow Lift": {"desc":"Open crushed shadows cleanly (adds light luminance NR).",
 "basic":{"shadows":50,"blacks":15},"curve":[(0,16),(128,128),(255,255)],"nr_lum":12},
"Glow Soft": {"desc":"Dreamy soft skin and light. Brush onto skin only.",
 "basic":{"texture":-15,"clarity":-10}},
"Grid Harmonizer": {"desc":"Low-strength glue layer to unify a mixed feed into one fingerprint.",
 "basic":{"blacks":6,"vibrance":6},
 "cg":{"sh":(215,6,0),"mid":(0,0,0),"hi":(42,6,0),"balance":0,"blending":50}},
}

TERRA_TOOLKIT = {
"Sky Enhancer": {"desc":"Deepen and recover sky. Apply on the AI Sky mask.",
 "basic":{"highlights":-25,"dehaze":6}, "hue":{"Blue":4}, "sat":{"Aqua":8,"Blue":12}, "lum":{"Blue":-10}},
"Foliage Fix": {"desc":"De-neon greens: merge yellows, deepen and warm foliage.",
 "hue":{"Yellow":8,"Green":-8}, "sat":{"Yellow":-4,"Green":-8}, "lum":{"Green":4}},
"Water Pop": {"desc":"Turquoise water. Apply on a water mask.",
 "hue":{"Aqua":-4}, "sat":{"Aqua":16,"Blue":12}, "lum":{"Aqua":4}},
"Atmospheric Depth": {"desc":"Cut haze for depth. For aerial perspective also cool the distance and warm the foreground with gradient masks (see docs).",
 "basic":{"dehaze":10,"clarity":6}},
"Sky Recovery": {"desc":"Recover a blown white sky. Apply on the Sky mask, then pull exposure.",
 "basic":{"highlights":-60,"whites":-25,"dehaze":8}},
"Foreground Lift": {"desc":"Open a dark foreground. Apply on a lower linear-gradient mask.",
 "basic":{"shadows":50,"blacks":15},"nr_lum":12},
"Orton Dreamy": {"desc":"Soft landscape glow. Apply masked at low opacity.",
 "basic":{"exposure":0.15,"texture":-12,"clarity":-18}},
"Grid Harmonizer": {"desc":"Low-strength glue layer to unify a landscape feed.",
 "basic":{"blacks":4,"vibrance":6},
 "cg":{"sh":(215,6,0),"mid":(0,0,0),"hi":(46,6,0),"balance":0,"blending":50}},
}


def main():
    n = 0
    # HALO looks x 3 skin variants
    for look, s in HALO.items():
        for tone in ("Fair", "Medium", "Deep"):
            variant = s if tone == "Medium" and False else merge_skin(s, SKIN[tone])
            d = dict(variant); d["desc"] = s["desc"] + f" [{tone} skin]"
            write(os.path.join(OUT, "HALO"), f"{look} - {tone}", "HALO", d["desc"], d)
            n += 1
    for tool, s in HALO_TOOLKIT.items():
        write(os.path.join(OUT, "HALO", "Toolkit"), tool, "HALO Toolkit", s["desc"], s)
        n += 1
    # TERRA looks
    for look, s in TERRA.items():
        write(os.path.join(OUT, "TERRA"), look, "TERRA", s["desc"], s)
        n += 1
    for tool, s in TERRA_TOOLKIT.items():
        write(os.path.join(OUT, "TERRA", "Toolkit"), tool, "TERRA Toolkit", s["desc"], s)
        n += 1
    print(f"Generated {n} .xmp presets into {OUT}")


if __name__ == "__main__":
    main()
