# College Scout profiles: setup

`athlete.html` does two jobs:

- **`athlete.html`** on its own lists every College Scout athlete, with filters for sport and class ("Recruit Davenport").
- **`athlete.html?name=First Last`** shows one athlete. Coaches see the highlight video first, then the key numbers, then contacts they can reach in one tap.

That one link is what families and you send to college coaches, put in X/Instagram bios and recruiting emails, and print on QR codes.

Each profile has:
- the highlight video, playing right on the page (YouTube or Vimeo), plus a Hudl link
- class, position, number, height, weight and GPA
- season stats
- measurables
- honors
- a short scouting note
- game photos
- **Email coach** and **Email family** buttons, with the subject line already filled in
- **Share profile**, which copies the link
- **Print one-sheet**, a clean one-page PDF for camps and showcases, with the email addresses and profile link printed on it
- **Get your athlete a profile like this**, which brings in the next College Scout family

## 1. Add a "Profiles" tab to your Google Sheet (5 minutes, once)
Use the same **GMA Focus Cards** Sheet.
1. Add a tab named **Profiles** and paste in the columns from `profiles-template.csv`.
2. Open **File → Share → Publish to web**, pick the **Profiles** tab and **Comma-separated values (.csv)**, click **Publish**, and copy the link.
3. In `athlete.html`, put that link in `profilesCsvUrl: "",`.

Until a link is set, the page shows two sample athletes and a notice that says so.

| Column | What to put |
|---|---|
| `name` | Full name. This is also the profile link: `?name=Caden Scott`. |
| `grad_year`, `sport`, `position`, `school`, `number` | For example `2027`, `Basketball`, `Point Guard`, `Davenport High`, `11` |
| `height`, `weight`, `gpa` | For example `6'1"`, `175`, `3.8` (all optional) |
| `photo_url` | A portrait (4:5 crop works best). Use a direct image link. |
| `highlight_url` | A YouTube or Vimeo link. It plays right on the page. Unlisted YouTube works. |
| `hudl_url` | Optional Hudl profile link |
| `stats` | `Label:Value` pairs separated by `|`, for example `PPG:18.4|REB:6.1|AST:7.2` |
| `measurables` | Same format, for example `Vertical:32 in|40 yd:4.6s` |
| `achievements` | Separated by `|`, for example `All-District 1st Team|Team captain` |
| `bio` | One or two sentences, written the way a scout would describe the athlete |
| `parent_name`, `parent_email`, `coach_name`, `coach_email` | Contacts. See privacy below. |
| `x_handle`, `instagram` | Optional, without the @ |
| `photos` | Optional game photo links separated by `|` (your best 4–8) |
| `committed` | The college the athlete committed to, for example `UT Dallas`. Shows a green **Committed** badge on the profile and on their tile in the list. |
| `status` | `live` to show the athlete. `draft` or `hidden` keeps them off the page while you build the profile. |

## 2. Privacy (these are minors)
- Get a signed **Media Release** (you already have /media-release) and the parent's OK for everything on the profile before setting `status` to `live`.
- Use **parent and coach email only.** There's no phone column on purpose, and the athlete's own email and home address shouldn't go on a public page.
- Photo links should be images you've chosen to publish, not private ShootProof gallery links.

## 3. Keeping profiles fresh (the College Scout promise)
| When | What |
|---|---|
| Weekly in season | Update `stats` and swap in the newest game photos |
| After each reel | Update `highlight_url` |
| Monthly | Send each family their link with a short note ("Here's the updated profile to send coaches") |
| End of season | Update `achievements`, and post the one-sheet on social |

## 4. Put it on gmafocus.com
Use the same route as the Card Studio (see `README.md` → *Installing on GoDaddy Airo*). The Airo prompt:

> Create a new page at /recruit with one full-width HTML/custom code section containing exactly this code: [paste all of athlete.html]. Add "Recruit" to the main menu. On the College Scout package, add a button "See College Scout profiles" that links to /recruit.

Or link to the hosted copy at `https://cards.gmafocus.com/athlete.html`. A single athlete is then at `https://cards.gmafocus.com/athlete.html?name=Caden%20Scott`.

If you paste the page into Airo, change `gamesUrl` and `cardsUrl` at the top of the script to full `https://` addresses so those buttons still work.
