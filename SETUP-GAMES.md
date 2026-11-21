# Game Photos page: setup

`games.html` is one page that lists every ShootProof game gallery, newest first, with the **Buy 4, get 1 free** offer at the top and your three packages at the bottom.

**Use this page's link everywhere:** every social post, the QR code at the gym, texts to parents. People find their game in one tap instead of digging through ShootProof.

Each game shows:
- **New** for galleries 7 days old or less.
- **Last chance: N days** when the deal is about to end.
- **▶ Highlights** when you add a video link.
- **Share**, which copies a link straight to that game (or opens the phone's share sheet).

Visitors can filter by sport and school. You can also link to a filtered view, for example `…/games?sport=Basketball`.

## 1. Add a "Games" tab to your Google Sheet (5 minutes, once)
Use the same **GMA Focus Cards** Sheet as the Card Studio.
1. Add a tab named **Games** and paste in the columns from `games-template.csv`.
2. Open **File → Share → Publish to web**, pick the **Games** tab and **Comma-separated values (.csv)**, click **Publish**, and copy the link.
3. In `games.html`, put that link in `gamesCsvUrl: "",`.

Until a link is set, the page shows 4 sample games and a notice that says so.

| Column | What to put |
|---|---|
| `date` | Game date, `2026-11-20` or `11/20/2026` |
| `sport`, `school`, `opponent` | For example `Basketball`, `Davenport High`, `Smithson Valley` |
| `home_away` | `Home` or `Away`. Away games show "at" instead of "vs". |
| `level` | `Varsity`, `JV`, `Freshman`… (optional) |
| `gallery_url` | **Required.** The ShootProof gallery link. Rows without one are hidden. |
| `cover_url` | Optional photo for the tile. Leave blank to show the matchup in big letters. |
| `highlight_url` | Optional YouTube or Hudl highlight link |
| `deal_ends` | Optional. If blank, the deal runs 7 days after the game. |
| `notes` | Optional. Searchable, for example "Senior Night". |

## 2. After every game (2 minutes)
1. Upload the game to ShootProof as **one gallery per game**, named like `Davenport vs Smithson Valley · Nov 20`.
2. Add one row to the **Games** tab with the gallery link. The page updates by itself within a few minutes.
3. Post 3–5 teaser photos on social with the line: *"Find your athlete → [Game Photos link]. Buy 4, get 1 free this week."*
4. Two days before `deal_ends`, post the **Last chance** reminder.

## 3. Settings at the top of the script
- `links.gameDay`, `links.season`, `links.scout`: where the package buttons go. The defaults are your ShootProof booking page, /services and /contact. Point **Reserve the season** at a real checkout or booking form when you have one.
- `scoutPrice`: set it to something like `"From $___"` to show a starting price for College Scout.
- `newDays`, `lastChanceDays`, `defaultDealDays`: badge and deal timing.

## 4. Put it on gmafocus.com
Use the same route as the Card Studio (see `README.md` → *Installing on GoDaddy Airo*). The Airo prompt:

> Create a new page at /games with one full-width HTML/custom code section containing exactly this code: [paste all of games.html]. Add "Game Photos" to the main menu, right after Home.

Or link to the hosted copy at `https://cards.gmafocus.com/games.html`.

**Check before you advertise it:** make sure ShootProof itself applies the buy 4 get 1 free deal at checkout. This page only describes the offer.
