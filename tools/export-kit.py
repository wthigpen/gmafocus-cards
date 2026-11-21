#!/usr/bin/env python3
"""Build the GMA Focus Website Kit: one folder (and .zip) with everything needed to run and update the site.

    python3 tools/export-kit.py [output-folder]

Paste files are .txt so they open in Notepad: Ctrl+A, Ctrl+C, then paste into Airo.
"""
import csv, io, pathlib, re, shutil, subprocess, sys, zipfile, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_PARENT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist"
KIT = OUT_PARENT / "GMA-Focus-Website-Kit"
TODAY = datetime.date.today().isoformat()

subprocess.run([sys.executable, str(ROOT / "tools/build-airo.py")], check=True, stdout=subprocess.DEVNULL)
if KIT.exists(): shutil.rmtree(KIT)

def put(rel, text=None, src=None):
    p = KIT / rel; p.parent.mkdir(parents=True, exist_ok=True)
    if src: shutil.copyfile(ROOT / src, p)
    else: p.write_text(text.replace("\r\n", "\n").replace("\n", "\r\n"), encoding="utf-8")  # Windows line endings for Notepad

def md2txt(src):
    t = (ROOT / src).read_text()
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t); t = re.sub(r"`([^`]+)`", r"\1", t)
    return t

# 1 · Airo paste files
A = "1-Airo-Copy-Paste/"
put(A + "1 - Game Photos  (paste on gmafocus.com-games).txt", (ROOT / "airo/game-photos.html").read_text())
put(A + "2 - Recruit list  (paste on gmafocus.com-recruit).txt", (ROOT / "airo/recruit.html").read_text())
put(A + "3 - Ricky Groff profile  (paste on gmafocus.com-recruit-ricky-groff).txt", (ROOT / "airo/recruit-ricky-groff.html").read_text())
put(A + "0 - HOW TO PASTE + Airo AI prompts.txt", md2txt("AIRO-INSTALL.md"))

# 2 · Google Sheet
G = "2-Google-Sheet/"
put(G + "Apps Script - paste into Extensions, Apps Script.txt", (ROOT / "google-sheet/Code.gs").read_text())
put(G + "Games tab.csv", src="games-template.csv")
prof = (ROOT / "profiles-template.csv").read_text().splitlines()
put(G + "Profiles tab.csv", "\n".join([prof[0],
    'Ricky Groff,2027,Basketball,,Davenport High,,,,,https://gmafocus.com/airo-assets/images/athletes/ricky-groff-spotlight,,,,,Committed to UT Dallas,,,,,,,,,live,UT Dallas',
    prof[1].replace(",live,", ",draft,")]) + "\n")
put(G + "Roster tab.csv", src="roster-template.csv")
put(G + "README - which file goes where.txt", """GOOGLE SHEET "GMA Focus Cards": ONE SHEET RUNS EVERYTHING

Tab name     Import this file      Used by
----------   -------------------   ----------------------------------------------
Submissions  (created by setup)    Card Studio submissions and approvals
Games        Games tab.csv         Game Photos page (one row per ShootProof gallery)
Profiles     Profiles tab.csv      Recruit list + every athlete profile
Roster       Roster tab.csv        Card Studio auto-fill (optional)

To import a tab: in the Sheet, add the tab, then File > Import > Upload the .csv >
"Replace current sheet".

To connect a tab to the website: File > Share > Publish to web > pick the tab >
Comma-separated values (.csv) > Publish > copy the link. Paste that link into the
matching setting in the Airo code:
  Games tab    -> "gamesCsvUrl"    in 1 - Game Photos
  Profiles tab -> "profilesCsvUrl" in 2 - Recruit list AND 3 - Ricky Groff profile

GAMES TAB: gallery_url = the link to that GAME'S ALBUM in ShootProof
(Davenport > season > sport > game). Open the album and copy the address bar.
The season is worked out from the date, so you don't need to type it.

The Profiles tab includes a "Sample Athlete" row set to draft (hidden). Delete it whenever you like.
Ricky Groff's row only has confirmed facts. Fill in the blanks (see the Update Queue).
""")
put(G + "Apps Script setup guide.txt", md2txt("SETUP-SUBMISSIONS.md"))

# 3 · Full pages (hosted copy on cards.gmafocus.com, or for opening on your computer)
F = "3-Full-Pages (cards.gmafocus.com)/"
for f in ["games.html", "athlete.html", "card-studio.html", "cards-gallery.html", "index.html"]:
    put(F + f, src=f)
put(F + "THIRD_PARTY_LICENSE-holospot.txt", src="THIRD_PARTY_LICENSE-holospot.txt")

# 4 · Guides
for f in ["SETUP-GAMES.md", "SETUP-PROFILES.md", "SETUP-SUBMISSIONS.md", "AIRO-INSTALL.md", "README.md", "COMPARISON.md"]:
    put("4-Guides/" + f.replace(".md", ".txt"), md2txt(f))

# 5 · Update queue
Q = [
 ("1", "Now", "ShootProof", "Confirm Buy 4 Get 1 Free works at checkout (it is a Cart Bundle; also 5 Digital Photos package $39.99)", "ShootProof > Cart Bundles", "", "Done"),
 ("2", "Now", "Google Sheet", "Add Games and Profiles tabs, publish both as CSV", "2-Google-Sheet", "README - which file goes where.txt", "To do"),
 ("3", "Now", "Airo", "Create /games page and paste Game Photos code; add Game Photos to menu", "1-Airo-Copy-Paste", "1 - Game Photos", "To do"),
 ("4", "Now", "Airo", "Create /recruit page and paste Recruit list code; add Recruit to menu", "1-Airo-Copy-Paste", "2 - Recruit list", "To do"),
 ("5", "Now", "Airo", "Create /recruit/ricky-groff page and paste Ricky's profile code", "1-Airo-Copy-Paste", "3 - Ricky Groff profile", "To do"),
 ("6", "Now", "Airo", "Paste the Games and Profiles CSV links into gamesCsvUrl / profilesCsvUrl, re-paste", "1-Airo-Copy-Paste", "", "To do"),
 ("7", "This week", "Ricky Groff", "Fill in position, #, height, weight, GPA", "Google Sheet > Profiles", "", "To do"),
 ("8", "This week", "Ricky Groff", "Add highlight reel link (YouTube/Vimeo) and last season's stats", "Google Sheet > Profiles", "", "To do"),
 ("9", "This week", "Ricky Groff", "Add honors and scouting note; parent + coach email with family's OK (UT Dallas commitment is in)", "Google Sheet > Profiles", "", "To do"),
 ("10", "This week", "Airo site fixes", "Link the dead Reserve My Spot and Sign Up for Season Coverage buttons", "Airo homepage", "", "To do"),
 ("11", "This week", "Airo site fixes", "Pick one booking system; point every Book button at it", "Airo", "", "To do"),
 ("12", "This week", "Airo site fixes", "Add Contact to menu; add College Scout starting price; remove 'v1.0 Platform'", "Airo homepage", "", "To do"),
 ("13", "This week", "Airo", "Homepage College Scout section: add 'Ricky Groff \u2192 committed to UT Dallas' proof + 'See College Scout profiles' button to /recruit", "Airo homepage", "", "To do"),
 ("14", "This week", "Freefield", "On the MSI: Claude Code session in GMA Focus folder; make Freefield output ShootProof / social / per-athlete folders", "MSI", "", "To do"),
 ("15", "After every game", "Routine", "Upload to ShootProof album: Davenport > season > sport > vs Opponent · Date", "ShootProof", "", "Repeat"),
 ("16", "After every game", "Routine", "Add one row to Games tab with that album's link", "Google Sheet > Games", "", "Repeat"),
 ("17", "After every game", "Routine", "Post 3-5 teasers within 24h with gmafocus.com/games link; tag players + school", "Instagram / Facebook / X", "", "Repeat"),
 ("18", "After every game", "Routine", "2 days before deal ends: post Last Chance reminder", "Social", "", "Repeat"),
 ("19", "Weekly", "Routine", "Update College Scout stats + photos; pitch Season Coverage to families who bought 2+ games", "Google Sheet > Profiles", "", "Repeat"),
 ("20", "Monthly", "Routine", "Send each College Scout family their profile link to forward to coaches", "Email", "", "Repeat"),
]
buf = io.StringIO(); w = csv.writer(buf)
w.writerow(["#", "When", "Area", "Task", "Where", "Kit file", "Status"]); w.writerows(Q)
put("5-Update-Queue/UPDATE-QUEUE.csv", buf.getvalue())

# START HERE
put("00-START-HERE.txt", f"""GMA FOCUS WEBSITE KIT   (exported {TODAY})
=====================================================================
Keep this folder at:  Documents\\GMA Focus\\Website-Kit
Get a fresh copy any time: ask Claude to "export the website kit" again.

WHAT'S IN HERE
  1-Airo-Copy-Paste\\      Paste-ready code for gmafocus.com (one file = one Airo page)
  2-Google-Sheet\\         The Apps Script + CSV files for each Sheet tab
  3-Full-Pages\\           Standalone pages for cards.gmafocus.com (double-click to preview)
  4-Guides\\               Setup guides for every piece
  5-Update-Queue\\         UPDATE-QUEUE.csv: every task in order. Open it in Excel or
                          Google Sheets and change Status to Done as you go.

HOW TO PASTE INTO AIRO
  1. Open the .txt file in 1-Airo-Copy-Paste (it opens in Notepad).
  2. Ctrl+A, then Ctrl+C.
  3. In Airo, open the page, add a full-width Custom code / HTML section, Ctrl+V, Save, Publish.
  4. Check it on your phone.

WHERE THINGS LIVE
  Website pages ........ gmafocus.com/games, /recruit, /recruit/ricky-groff
  Data (games, athletes) Google Sheet "GMA Focus Cards" (Games and Profiles tabs)
  Photo sales .......... ShootProof (one gallery per game)
  Source code .......... github.com/wthigpen/gmafocus-cards
  Media automation ..... Freefield, on the MSI

ONCE THE SHEET IS CONNECTED, YOU STOP EDITING AIRO
  New game?            Add a row to the Games tab.
  New stats or photo?  Edit the athlete's row in the Profiles tab.
  The website updates by itself within a few minutes.

ONLY RE-PASTE INTO AIRO WHEN
  - you add a new athlete profile page (copy file 3, change "athlete": "Ricky Groff")
  - you change a setting (links, scout price, CSV links)
  - Claude gives you an updated kit after a design change

THE ONE LINK TO SHARE EVERYWHERE:  gmafocus.com/games
""")

zpath = OUT_PARENT / "GMA-Focus-Website-Kit.zip"
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(KIT.rglob("*")):
        if p.is_file(): z.write(p, p.relative_to(OUT_PARENT))
print(zpath)
