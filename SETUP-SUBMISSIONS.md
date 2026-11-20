# Player cards on gmafocus.com: setup

This sets up the whole loop: a player makes a card, you approve it, and it appears on the site and on their profile. Everything runs from one Google Sheet. It's free, and it needs no changes to how Airo stores data.

```
Player: Card Studio ──Submit──▶ Google Sheet "Submissions" (status: pending) + card saved in Drive
                                     │  you change Status to "approved"
                                     ▼
gmafocus.com: Cards gallery / player profile ◀── reads approved cards ── "View in 3D foil" opens the Card Studio viewer
```

Allow about 20 minutes, once.

## 1. Create the Sheet and its script
1. Create a Google Sheet named **GMA Focus Cards**.
2. In the Sheet, open **Extensions → Apps Script**. Delete what's there and paste in all of `google-sheet/Code.gs`. Click **Save**.
3. Choose **setup** in the function menu at the top and click **Run**, then allow access.
   - Google will warn "Google hasn't verified this app". That's expected for your own script: click **Advanced → Go to … (unsafe)**.
   - This creates the **Submissions** tab with a Status dropdown, and a **GMA Focus Cards** folder in your Drive.
4. Click **Deploy → New deployment → Select type: Web app**, with these settings:
   - Execute as: **Me**
   - Who has access: **Anyone**
5. Click **Deploy** and copy the **Web app URL** (it ends in `/exec`).

## 2. Connect the two pages
Open each file in Notepad, paste your URL, and save.
- `card-studio.html`: find `const SUBMIT_URL = "";` and put the URL between the quotes.
- `cards-gallery.html`: find `apiUrl: "",` and put the same URL between the quotes. Also set `studioUrl` to wherever the Card Studio page lives on your site (for example `https://gmafocus.com/card-studio`).

Until a URL is set, "Submit" still works: it saves a card file and tells the player to email it to info@gmafocus.com.

## 3. Optional: auto-fill player stats from a roster
1. Add a tab named **Roster** to the same Sheet, and paste in `roster-template.csv` to get the columns. One row per player.
2. Open **File → Share → Publish to web**, pick the **Roster** tab and **Comma-separated values (.csv)**, click **Publish**, and copy the link.
3. In `card-studio.html`, put that link in `const ROSTER_URL = "";`.

Players then see **Find yourself on the roster**. Picking their name fills in the school, logo, colors, sport, number, position, stats, abilities and the two card-game ratings (`off`/`def`). Edit the Sheet whenever stats change; the site updates by itself.

For abilities, type a preset name (for example `Floor General`) or your own text in the form `Keyword: what it does`.

## 4. Put the pages on your Airo site
Paste these prompts into Airo, one at a time. If Airo offers an **HTML / Embed** section, these are exactly what it's for.

**Card Studio**
> Create a new page at /card-studio. Add one full-width HTML/custom code section and paste this code exactly as-is, without changing it: [paste all of card-studio.html]. Make the section at least 2400 px tall on mobile. Change the "Card Creator" link in the footer to go to /card-studio.

**Cards gallery**
> Create a new page at /cards with one full-width HTML/custom code section containing exactly this code: [paste all of cards-gallery.html]. Add "Cards" to the main menu.

**Player profiles**
> On each athlete profile page, add a section titled "Cards" with an HTML/custom code section containing this code exactly: [paste cards-gallery.html], but change the line `player: "",` to the athlete's full name in quotes, for example `player: "David Unrein",`.

The name has to match the name on the card exactly; capitals don't matter.

If Airo refuses custom code, host the two HTML files on any static host (for example a `cards.gmafocus.com` subdomain) and ask Airo to link to them instead.

## 5. Approving cards
- New cards arrive as **pending**, and you get an email.
- To review one, open the **Card image** link in its row.
- Set **Status** to **approved** to publish it, or to **rejected** to keep it off the site. You can change your mind at any time.
- Only approved cards are ever listed. The full card file, which contains the player's original photo, stays private in your Drive. The site only gets the finished card image.

## 6. Printing approved cards on the PRO-1100
1. Download the **Card file** (`.gmacard.json`) of each card you want to print from the GMA Focus Cards Drive folder.
2. In the Card Studio, open **Print at home → Print several players' cards on one sheet → Add card files**.
3. Choose Letter, and holographic paper or cardstock, then click **Print sheet**. Nine different cards fit per sheet, and more cards go onto extra sheets automatically.
4. To fix a card first (typo, crop), use **For GMA Focus staff → Open card file**, edit it, and print from there.

## Good to know
- **Changing the script later:** if you edit `Code.gs`, use **Deploy → Manage deployments → Edit → Version: New version** so the URL stays the same.
- **Spam or junk submissions:** they only ever land as *pending*. Delete the row and the Drive files.
- **Not tested end to end:** this was tested with a stand-in server that behaves the same way, not with a live Google account or on Airo. Do a test submission yourself after setup.
