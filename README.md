# GMA Focus Card Studio (rebuild)

`card-studio.html` is the whole tool in one file. Photos are processed in the visitor's browser and never uploaded.

## What's in it
| File | What it is |
|---|---|
| `card-studio.html` | The Card Studio: build, submit, download and print cards. Also the 3D card viewer (`?view=ID`). |
| `games.html` | **Game Photos page:** every ShootProof game gallery, newest first, with the Buy 4 get 1 free offer and packages. Setup: `SETUP-GAMES.md`. |
| `cards-gallery.html` | Approved-card gallery for a Cards page or a player profile (`player: "Name"`). |
| `google-sheet/Code.gs` | Free backend in your Google Sheet: submissions, approval and gallery data. |
| `roster-template.csv` | Columns for the roster that auto-fills stats. |
| `SETUP-SUBMISSIONS.md` | **Start here:** Google Sheet setup, Airo prompts, approving and printing. |

**Card Studio features**
- **GMA Focus Season One sport templates** in an original card-game style: title, type line, two abilities, a quote, power/toughness-style ratings and a set symbol.
  - Basketball: *Hardwood* (Rainbow foil) and *Above the Rim* (Sparkle).
  - Baseball and Softball: *Diamond* (Gold Shatter, yellow leather for Softball) and *Under the Lights* (Rainbow).
  - Each sport has its own ability presets, and players can write their own.
- **Classic frames** for every sport: Varsity, Spotlight, Legend, Prism.
- **School logos and colors:** Davenport High, Danville Middle, Cibolo Steele and Smithson Valley are built in, or players can upload a logo. Add more schools in the `SCHOOLS` list at the top of the script.
- **Roster auto-fill:** a player picks their name and the card fills itself in from your Google Sheet.
- **Real 3D holographic foil** (holospot): 7 foils, the Pro foil controls, holo.spot looks pasted in, and "Save 3D shot". Phones without 3D support get a lighter foil effect automatically.
- **Submit to profile:** cards go to your approval queue, then show on the gallery and the player's profile.
- **Downloads:** a 1500×2100 PNG, and a card file (`.gmacard.json`) for edits and reprints.

## Printing on the Canon PRO-1100
The **Print at home** panel builds a true-size sheet at 600 dpi.

| Paper | Layout | Cards per sheet |
|---|---|---|
| Letter 8.5×11 (default) | Most cards: shared cut lines | **9** (3×3, portrait) |
| Letter 8.5×11 | Bleed + gutters (⅛″ bleed on every card) | 6 (landscape) |

4×6, 5×7, 8×10, A4 and 13×19 are also available.

- **Regular 320 gsm stock:** leave "holographic paper" off. The foil look is printed as color.
- **Holographic paper:** tick "Printing on holographic paper". The foil areas (border, ribbon, foil name) are left **unprinted**, so your paper's own holo shows there. Text on foil prints in dark ink, because inkjets can't print white.
- **Print dialog:** choose Letter, set **Scale 100% / Actual size**, and turn off headers and footers. The page sets the paper size itself (works best in Chrome or Edge).
- **Feeding:** put thick stock and holo sheets through the rear manual feed, and pick the closest heavy media type in the Canon driver.
- **Cutting:** cut on the crop marks, then round the corners with a ⅛″ (3 mm) corner punch.
- **Several players at once:** Print at home → "Print several players' cards on one sheet" takes approved card files and fills as many sheets as needed.
- **First run:** print one sheet on plain paper and measure. Each card should be exactly 2.5″×3.5″.

## Installing on GoDaddy Airo
GoDaddy's Airo support statement lists custom code as **not supported**, but your current `/card-creator` page is already custom code running on Airo. Try these in order:

1. **Airo's AI editor / code access (how the existing Card Creator was built):** replace `/card-creator/build`, or add `/card-studio`, using this file's `<head>` scripts, `<style>`, markup and both `<script>` blocks unchanged. As a page on your site, it keeps your normal gmafocus.com header menu and footer.
2. **An HTML / Embed section, if your editor offers one:** paste the entire file. The embed runs in an iframe, so make the section tall (about 2,400 px on phones). Your site menu stays around it.
3. **Fallback:** host the file on any static host (for example a `cards.gmafocus.com` subdomain) and point the Card Creator menu item at it. Hosted alone, it has no site menu.

The page loads three.js and holospot from the jsDelivr CDN at pinned versions (`three@0.187.0`, `holospot@v0.1.0`), so the site needs no extra files. Change the branding at the top of the main script: `BRAND = { site, mark, total }`.

## Licensing
- **holospot:** MIT License, Copyright (c) 2026 Dmitry Kurash. Commercial use is allowed as long as the license text stays with the code. The full text is in `THIRD_PARTY_LICENSE-holospot.txt`, and a credit line is in the page footer. Keep both.
- **three.js:** MIT.
- **Fonts:** Barlow Condensed and Inter (SIL Open Font License).
- The four frames and the lite CSS foil are original to this project.
