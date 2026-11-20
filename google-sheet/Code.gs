/**
 * GMA Focus Card Studio: submissions + approved-card gallery.
 * Paste this into your Google Sheet: Extensions > Apps Script. Then run setup() once and deploy as a Web app
 * (Execute as: Me, Who has access: Anyone). Full steps: SETUP-SUBMISSIONS.md.
 *
 * You approve a card by changing its Status cell to "approved". Only approved cards are ever listed.
 */
const FOLDER_NAME = 'GMA Focus Cards';
const SHEET = 'Submissions';
const HEAD = ['Submitted', 'ID', 'Status', 'Player', 'School', 'Sport', 'Template', 'Card image', 'Card file', 'Notes'];
const COL = { submitted: 0, id: 1, status: 2, player: 3, school: 4, sport: 5, template: 6, image: 7, file: 8 };
const MAX_CHARS = 15e6;          // about 11 MB of card data
const NOTIFY = true;             // email you when a new card arrives

/** Run once from the Apps Script editor (select "setup", press Run, allow access). */
function setup() {
  const ss = SpreadsheetApp.getActive();
  const sh = ss.getSheetByName(SHEET) || ss.insertSheet(SHEET);
  sh.getRange(1, 1, 1, HEAD.length).setValues([HEAD]).setFontWeight('bold');
  sh.setFrozenRows(1);
  const rule = SpreadsheetApp.newDataValidation().requireValueInList(['pending', 'approved', 'rejected'], true).build();
  sh.getRange(2, COL.status + 1, sh.getMaxRows() - 1, 1).setDataValidation(rule);
  folder_();
}

function folder_() {
  const it = DriveApp.getFoldersByName(FOLDER_NAME);
  return it.hasNext() ? it.next() : DriveApp.createFolder(FOLDER_NAME);
}
function out_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
function rows_() {
  const v = SpreadsheetApp.getActive().getSheetByName(SHEET).getDataRange().getValues();
  v.shift();
  return v;
}
function fileId_(url) {
  const m = String(url).match(/[-\w]{25,}/);
  return m ? m[0] : '';
}
const low_ = s => String(s || '').trim().toLowerCase();

/** A player submits a card from the Card Studio. It is stored as "pending". */
function doPost(e) {
  try {
    const body = (e.postData && e.postData.contents) || '';
    if (body.length > MAX_CHARS) return out_({ ok: false, error: 'That card is too large to submit.' });
    const d = JSON.parse(body);
    if (d.action !== 'submit') return out_({ ok: false, error: 'Unknown request.' });
    const st = (d.card && d.card.state) || {};
    const player = String(st.name || '').trim().slice(0, 60);
    if (!player) return out_({ ok: false, error: 'Add the player name first.' });
    const m = /^data:image\/(jpeg|png);base64,(.+)$/.exec(d.image || '');
    if (!m) return out_({ ok: false, error: 'The card image is missing.' });

    const id = Utilities.getUuid().slice(0, 8);
    const safe = player.replace(/[^\w -]+/g, '').replace(/\s+/g, '-') || 'player';
    const folder = folder_();
    const img = folder.createFile(Utilities.newBlob(Utilities.base64Decode(m[2]), 'image/' + m[1], `${safe}-${id}.${m[1] === 'png' ? 'png' : 'jpg'}`));
    img.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);   // so the gallery can show it once approved
    const file = folder.createFile(Utilities.newBlob(JSON.stringify(d.card), 'application/json', `${safe}-${id}.gmacard.json`)); // private

    const lock = LockService.getScriptLock();
    lock.waitLock(20000);
    try {
      SpreadsheetApp.getActive().getSheetByName(SHEET).appendRow([
        new Date(), id, 'pending', player, String(st.school || ''), String(st.sport || ''), String(st.frame || ''), img.getUrl(), file.getUrl(), '']);
    } finally { lock.releaseLock(); }

    if (NOTIFY) {
      try {
        MailApp.sendEmail(Session.getEffectiveUser().getEmail(), `New card to approve: ${player}`,
          `${player} (${st.school || ''}, ${st.sport || ''}) submitted a card.\n\nCard: ${img.getUrl()}\n` +
          `Approve it by setting Status to "approved": ${SpreadsheetApp.getActive().getUrl()}`);
      } catch (err) { /* email is optional */ }
    }
    return out_({ ok: true, id: id });
  } catch (err) {
    return out_({ ok: false, error: 'Something went wrong saving the card.' });
  }
}

/**
 * The gallery and the 3D viewer read approved cards:
 *   ?player=Name  ?school=Davenport  ?sport=Basketball   list approved cards (all filters optional)
 *   ?action=card&id=ID                                  one approved card's full file (for 3D view and reprint)
 */
function doGet(e) {
  const p = (e && e.parameter) || {};
  const approved = rows_().filter(r => low_(r[COL.status]) === 'approved');
  if (p.action === 'card') {
    const r = approved.find(r => String(r[COL.id]) === String(p.id));
    if (!r) return out_({ ok: false, error: 'Card not found.' });
    const card = JSON.parse(DriveApp.getFileById(fileId_(r[COL.file])).getBlob().getDataAsString());
    return out_({ ok: true, card: card });
  }
  const cards = approved
    .filter(r => !p.player || low_(r[COL.player]) === low_(p.player))
    .filter(r => !p.school || low_(r[COL.school]).indexOf(low_(p.school)) >= 0)
    .filter(r => !p.sport || low_(r[COL.sport]) === low_(p.sport))
    .map(r => ({
      id: String(r[COL.id]), player: r[COL.player], school: r[COL.school], sport: r[COL.sport], template: r[COL.template],
      image: 'https://drive.google.com/thumbnail?id=' + fileId_(r[COL.image]) + '&sz=w1000',
      submitted: r[COL.submitted]
    }))
    .reverse();
  return out_({ ok: true, cards: cards });
}
