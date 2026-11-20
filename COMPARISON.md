# Current Card Creator vs. rebuild

Reviewed live on 2026-11-20: gmafocus.com/card-creator and /card-creator/build, desktop and phone.

| | Current (gmafocus.com/card-creator/build) | Rebuild (card-studio.html) |
|---|---|---|
| Focus | Defaults to an **MTG proxy** frame ("Legendary Creature", mana cost, Hybrid/Phyrexian/Twobrid symbols, set symbols, background art like Dragon/Angel) | Built for **high school athletes**: name, school, position, jersey #, class year, sport, 3 stats |
| Frames | GMA Sports, MTG Proxy, Pokémon, GMA TCG, Naruto TCG, Holo 3D | Varsity, Spotlight, Legend, Prism. All original designs. |
| Third-party IP | MTG, Pokémon and Naruto names and look-alike frames, plus MTG mana symbols, on a paid business site | None |
| Holo / foil | A single "Foil" toggle | Real 3D foil from holospot (7 materials, every setting adjustable, holo.spot looks can be pasted in). Foil sits only where the frame has foil. CSS fallback for older phones. |
| Download | Locked (padlock icon) | Unlocked after a permission checkbox, 1500×2100 PNG (600 dpi), plus a 3D snapshot |
| Print | Print button | True-size Letter sheets (9-up, or 6-up with bleed) at 600 dpi, with crop marks and a holo-paper mode that leaves foil areas unprinted |
| Photo | Upload, or "My Photos" after login | Upload or drag-and-drop, zoom, drag-to-position. No login. |
| Mobile | Good: bottom-sheet controls | Good: stacked layout, no sideways scroll |
| Empty state | Fields show "Card Name", "Add ability text…" | Filled-in sample player, so the card always looks finished |

## Worth fixing whatever you decide
1. **IP exposure.** Pokémon, Magic: The Gathering and Naruto are trademarks of other companies. Offering their frames, plus an MTG proxy print sheet (the Scryfall deck builder on /card-creator), on a site that sells services is a risk worth running past someone qualified. The rebuild avoids it completely.
2. **Off-brand default.** A parent arriving from a game gallery lands on a Magic card with mana symbols. The rebuild opens on a sports card.
3. **Locked download.** If that's meant to drive logins or sales, say so on the page. Otherwise it reads as broken.
4. **Things I saw elsewhere on the site:** "Book" CTAs point to /booking, /services and ShootProof inconsistently. "Mythic Specials" is never explained. The header's "Full" and "Media" buttons have no context.

## Not carried over (by design)
- "My Photos" (logged-in GMA gallery). This needs your Airo login backend. It could be added later by passing a photo URL into `GMACardStudio.loadFile`.
- Card Gallery and Share-to-gallery, which need server storage.
- The MTG Proxy Deck Builder. That is a separate tool, and the IP issue above applies to it.
