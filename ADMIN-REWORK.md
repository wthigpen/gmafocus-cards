# gmafocus.com admin rework

## The vision in one sentence
**Every athlete gets a home page on gmafocus.com.** ShootProof fills it with their best photos automatically. Families reach it through the client portal and app. The card generator, sharing and College Scout live on it.

- **ShootProof:** stores every photo and **sells** them.
- **gmafocus.com:** shows each athlete's **best** photos and sends people to ShootProof to buy.
- **Admin:** only shows you what needs a decision.

## What the admin becomes: 5 sections

| Section | What's in it | Replaces |
|---|---|---|
| **Today** | One queue of things to act on: new ShootProof photos to pick from, unassigned events, card submissions, unsigned media releases, inbox messages | Dashboard, Inbox, Site Stats (stats become a small panel) |
| **Athletes** | One page per athlete with tabs for **Profile**, **Photos**, **Highlights**, **College Scout**, **Cards**, **Release**, **Account** | Players, Media Day, Media Releases, Cards & Packs, Gallery, Manage Albums |
| **ShootProof** | The connection, event list, assign-to-athlete, auto-sync, and a **Show on Game Photos** switch for each game | SP Migration, Import Unimported, Sync Event Names, Purge, Game Albums, Bulk Upload |
| **Clients** | Accounts, client portal and app access, and who bought what (Game Day / Season / College Scout) | Client Management |
| **Site** | Updates, Instagram feeds, social, homepage, settings, inbox settings | Updates, Social Media, Settings, Inbox Settings |

**Removed:** Game Albums. A "game" is just a ShootProof event, so it doesn't need its own album system.
**Hidden but kept (data stays):** Media Day, the Cards & Packs admin, Bulk Upload. They're used rarely, so they move inside an athlete's page or behind a "More" link.

## The automatic photo flow
```
Game night ─▶ Freefield sorts photos per athlete ─▶ upload to ShootProof
                                                   (Davenport › season › sport › game)
                                                              │ auto-sync (already built)
                                                              ▼
            Today queue: "12 new photos of Ricky Groff from vs Steele"
                        tap ★ on the best 3–5   (or "Auto-pick" picks for you)
                                                              ▼
            Athlete home page: new photos on top ─▶ card generator ─▶ share ─▶ "Buy on ShootProof"
```
**The key rule:** the site never copies whole games. It only keeps the ★ picks for each athlete. That's what drives your storage, Purge and Gallery sections today, and it's why those sections can go.

## Airo prompts, in order
Paste one prompt into Airo's AI editor, check the result, then do the next. Each one asks Airo not to delete data.

### Step 0: Safety first
> Before any changes: export a backup of all players, ShootProof event assignments, gallery photos, cards, clients and media releases. Tell me where the backup is saved. Don't change anything else yet.

### Step 1: Remove Game Albums
> In the admin, remove the "Game Albums" section from the sidebar and any routes or menus that point to it. Don't delete any photos or ShootProof event assignments. If any player profile shows photos that only exist in Game Albums, list those players for me first instead of removing them.

### Step 2: Regroup the sidebar into 5 sections
> Reorganize the admin sidebar into exactly five sections: Today, Athletes, ShootProof, Clients, Site.
> - Today: dashboard plus inbox.
> - Athletes: the Players list. Move Media Releases, Cards & Packs and each player's gallery photos inside the individual player page as tabs.
> - ShootProof: move the connection status, auto-sync, import, sync event names, purge and the events list here, on one page.
> - Clients: client management.
> - Site: updates, social media / Instagram feeds, settings, inbox settings, site stats.
> Hide Media Day, Bulk Upload, Gallery and Manage Albums from the sidebar, but keep their pages reachable from a "More tools" link at the bottom. Don't delete any data or features. Only move navigation.

### Step 3: The Today queue
> Make the admin home page a "Today" queue, newest first. Show one card per item: (1) ShootProof events with new photos assigned to an athlete: "N new photos of [athlete] from [event]", with a button to pick photos; (2) ShootProof events not assigned to any athlete, with an Assign button; (3) pending card submissions; (4) athletes with no signed media release; (5) unread inbox messages. Each card disappears once it's handled. Put a small site-stats summary at the top.

### Step 4: Pick the best photos (the automation)
> When I open "pick photos" for an athlete and event, show that event's photos in a grid. I tap a star on the best ones and they're added to that athlete's profile photos, newest first. Add an "Auto-pick 5" button that stars the 5 photos ShootProof marks as favorites or highlights (or, if there are none, the first 5). Only starred photos are copied to the site. Never copy an entire event. Each profile photo keeps a "Buy this photo" link to its ShootProof page.

### Step 5: The athlete's home page (public)
> Redesign the public player profile as the athlete's home page, in this order: hero photo with name, class, position, number and team; College Scout badge and "Committed: [college]" badge when set; highlight reel; their starred photos, each with Share and "Buy on ShootProof" buttons; "Make my card" (opens the card generator with this athlete's details and photo already filled in); stats; Instagram feed; and contact for coaches (College Scout only). Add a Share button that copies the profile link. Keep the existing client portal and app login working.

### Step 6: College Scout fields
> On the admin player page, add a College Scout tab with: College Scout on/off, committed college, GPA, height, weight, measurables, honors, scouting note, coach name and email, parent name and email (shown only with a signed media release), and a "Print one-sheet" button that makes a one-page PDF for coaches. On /athletes, add a "College Scout" filter and show the committed badge on athlete tiles.

### Step 7: Public Game Photos page
> Create a public /games page listing ShootProof events where "Show on Game Photos" is on, newest first, with season and sport filters. Each game shows the date, matchup, cover photo and a "See photos" button linking to its ShootProof album. At the top, show a banner: "Every game photo is $10 — 5 for $39.99." Add "Game Photos" to the main menu.

## Stop doing
- Copying whole games onto the site
- Keeping a second album system next to ShootProof
- Adding a new admin section for a new idea. **New features go inside one of the 5 sections, or they wait.**

## Design reference
`games.html` and `athlete.html` in this repo show the intended look and behavior for steps 5–7. Airo can be told "match the layout of this page".
