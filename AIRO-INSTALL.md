# Installing the new pages on gmafocus.com (GoDaddy Airo)

The `airo/` folder holds **paste-ready code** for Airo. Each file is one block you paste into one custom code / HTML section. It has no `<html>`, `<head>` or `<body>`, and its styles only affect its own section, so your site's header, menu, fonts and footer stay as they are.

| Paste this file | On this Airo page | What it is |
|---|---|---|
| `airo/game-photos.html` | **/games** (menu: "Game Photos") | Every ShootProof game gallery, plus the Buy 4 get 1 free offer and your packages |
| `airo/recruit.html` | **/recruit** (menu: "Recruit") | The College Scout athlete list for coaches |
| `airo/recruit-ricky-groff.html` | **/recruit/ricky-groff** | Ricky Groff's College Scout profile |

## How to paste (each page)
1. Open the file on GitHub, click **Raw**, then select all (Ctrl+A) and copy (Ctrl+C).
2. In Airo, create the page, add a **custom code / HTML** section, paste, and save.
3. Make the section **full width**. If Airo asks for a height, use about **2400 px on phones** and **1600 px on desktop**.
4. Publish, then open the page on your phone and tap a few buttons.

If you use Airo's AI editor instead, these prompts work:

> Create a new page at /games with one full-width custom code section. Paste this code exactly as-is, without changing or reformatting it: [paste airo/game-photos.html]. Add "Game Photos" to the main menu right after Home.

> Create a new page at /recruit with one full-width custom code section containing exactly this code: [paste airo/recruit.html]. Add "Recruit" to the main menu. On the homepage College Scout section, add a button "See College Scout profiles" linking to /recruit.

> Create a new page at /recruit/ricky-groff with one full-width custom code section containing exactly this code: [paste airo/recruit-ricky-groff.html]. Don't add it to the menu.

**If Airo won't take nested paths** like `/recruit/ricky-groff`, use `/recruit-ricky-groff`. Then change `"profileUrl"` in `airo/recruit.html` and `airo/recruit-ricky-groff.html` to `"https://gmafocus.com/recruit-{slug}"`.

**If buttons do nothing on the live page**, Airo is probably running the code in a locked-down frame. Change `"linkTarget": "_top"` to `"linkTarget": "_blank"` in that page's `GMA_CONFIG` and paste it again.

## Changing settings
Each file starts with `window.GMA_CONFIG = { … }`. That's the only part you ever edit:
- **game-photos:** `gamesCsvUrl` (your published Games tab), `links` (where the package buttons go), and `scoutPrice`.
- **recruit / recruit-ricky-groff:** `profilesCsvUrl` (your published Profiles tab), or `profilesData` (the athlete rows typed right into the page).

**Recommended:** connect the Google Sheet tabs (`SETUP-GAMES.md`, `SETUP-PROFILES.md`) and set the `…CsvUrl` once on each page. After that you never touch Airo again: add a game or update a stat in the Sheet, and every page updates by itself.

## Ricky Groff's profile: what to fill in
His page currently has only what's confirmed: name, Basketball, Davenport High, and his spotlight photo from your homepage. Add the rest to his row in the **Profiles** tab, or to `profilesData` in both recruit files:

- position and jersey number (class of 2027 is already in)
- height, weight and GPA
- **highlight reel link** (YouTube or Vimeo): this matters most to coaches
- last season's stats, for example `PPG:…|REB:…|AST:…`
- honors and a one-line scouting note
- parent and coach emails, **with the family's OK**
- where he signed or committed, if he did. A commitment is the best proof that College Scout works, so put it in `achievements` and on the homepage.

## A second athlete page
Copy `airo/recruit-ricky-groff.html`, change `"athlete": "Ricky Groff"` to the new name, and paste it on `/recruit/first-last`. The name must match the `name` in the Profiles data.

## For whoever maintains this repo
`games.html` and `athlete.html` are the full pages. The `airo/` files are built from them by:

```
python3 tools/build-airo.py
```

Re-run it after changing either page. Settings for the built files are in the `SNIPPETS` list in that script.
