#!/usr/bin/env python3
"""Build paste-ready GoDaddy Airo snippets from the full pages.

    python3 tools/build-airo.py

Writes airo/*.html. Each snippet has no <html>/<head>/<body>, its CSS only touches its own section
(#gma-games or #gma-scout), and its settings are filled in for gmafocus.com. Edit the SNIPPETS list
below (or the files in airo/) to change settings. Re-run after changing games.html or athlete.html.
"""
import json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "airo"
SITE = "https://gmafocus.com"
HOSTED = "https://cards.gmafocus.com"

PROFILE_HEAD = "name,grad_year,sport,position,school,number,height,weight,gpa,photo_url,highlight_url,hudl_url,stats,measurables,achievements,bio,parent_name,parent_email,coach_name,coach_email,x_handle,instagram,photos,status,committed"
# Only facts confirmed so far. Fill the blanks (see SETUP-PROFILES.md for the format) or move this row to the Profiles tab.
RICKY = "Ricky Groff,2027,Basketball,,Davenport High,,,,," + SITE + "/airo-assets/images/athletes/ricky-groff-spotlight,,,,,Committed to UT Dallas,,,,,,,,,live,UT Dallas"
PROFILES = PROFILE_HEAD + "\n" + RICKY

SCOUT_COMMON = {
    "profilesCsvUrl": "", "profilesData": PROFILES,
    "gamesUrl": SITE + "/games", "cardsUrl": SITE + "/cards", "scoutInfoUrl": SITE + "/contact",
    "profileUrl": SITE + "/recruit/{slug}", "listUrl": SITE + "/recruit", "linkTarget": "_top",
}
SNIPPETS = [
    ("game-photos.html", "games.html", "gma-games", "Game Photos page → paste on gmafocus.com/games", {
        "gamesCsvUrl": "", "gamesData": "",
        "links": {"gameDay": "https://photos.gmafocus.com/booking/davenport", "season": SITE + "/services", "scout": SITE + "/contact"},
        "dealText": "", "scoutPrice": "", "linkTarget": "_top"}),
    ("recruit.html", "athlete.html", "gma-scout", "College Scout athlete list → paste on gmafocus.com/recruit", dict(SCOUT_COMMON)),
    ("recruit-ricky-groff.html", "athlete.html", "gma-scout", "Ricky Groff's College Scout profile → paste on gmafocus.com/recruit/ricky-groff",
        dict(SCOUT_COMMON, athlete="Ricky Groff")),
]

def split_rules(css):
    """Yield (prelude, body) for each top-level rule, keeping nested braces in body."""
    i, n = 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j < 0: break
        depth, k = 1, j + 1
        while k < n and depth:
            depth += {"{": 1, "}": -1}.get(css[k], 0); k += 1
        yield css[i:j].strip(), css[j + 1:k - 1]
        i = k

def split_selectors(pre):
    """Split a selector list on top-level commas only (not inside :is(...), :not(...))."""
    out, depth, cur = [], 0, ""
    for ch in pre:
        depth += {"(": 1, ")": -1}.get(ch, 0)
        if ch == "," and depth == 0: out.append(cur); cur = ""
        else: cur += ch
    return out + [cur]

def scope(css, rid):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out = []
    for pre, body in split_rules(css):
        if pre.startswith("@media") or pre.startswith("@supports"):
            out.append(f"{pre}{{{scope(body, rid)}}}")
        elif pre.startswith("@"):
            out.append(f"{pre}{{{body}}}")
        else:
            sels = []
            for sel in split_selectors(pre):
                sel = sel.strip()
                if sel.startswith("#gma-") or sel.startswith("body *"): sels.append(sel)     # already page-level on purpose
                elif sel in (":root", "html", "body"): sels.append(f"#{rid}")
                elif sel == "*": sels += [f"#{rid}", f"#{rid} *"]
                else: sels.append(f"#{rid} {sel}")
            out.append(f"{','.join(dict.fromkeys(sels))}{{{body.strip()}}}")
    return "\n".join(out)

def build(src, rid, cfg, title):
    s = (ROOT / src).read_text()
    fonts = "\n".join(m for m in re.findall(r'<link[^>]+fonts[^>]+>', s))
    css = re.search(r"<style>(.*?)</style>", s, re.S).group(1)
    body = re.search(r"<body>(.*?)<script>", s, re.S).group(1).strip()
    js = re.search(r"<script>(.*?)</script>\s*</body>", s, re.S).group(1)
    assert f'id="{rid}"' in body, f"{src} is missing its #{rid} wrapper"
    conf = json.dumps(cfg, indent=2, ensure_ascii=False)
    return f"""<!-- GMA Focus · {title}
     Paste ALL of this into one Airo custom code / HTML section. Settings are in GMA_CONFIG just below.
     Built from {src} by tools/build-airo.py. -->
{fonts}
<style>
{scope(css, rid)}
</style>
<script>window.GMA_CONFIG = {conf};</script>
{body}
<script>{js}</script>
"""

OUT.mkdir(exist_ok=True)
for name, src, rid, title, cfg in SNIPPETS:
    (OUT / name).write_text(build(src, rid, cfg, title))
    print("wrote", OUT / name)
