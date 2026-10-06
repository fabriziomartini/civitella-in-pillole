/**
 * Statistiche anonime del quiz di Civitella in Pillole.
 *
 * Da incollare in un foglio Google: Estensioni → Apps Script.
 * Istruzioni complete in ricerca/quiz-statistiche.md.
 *
 * Riceve dal quiz (js/quiz.js) un JSON come questo:
 *   { v: 1, punti: 9, totale: 15,
 *     risposte: [ { id: "5a86694d", c: "geo", q: "Quanti residenti…", ok: 1 }, … ] }
 * e scrive una riga nel foglio «Partite» e una riga per domanda nel foglio «Risposte».
 * Non riceve e non salva dati personali: niente nomi, email o indirizzi IP.
 */

var CATEGORIE = {
  geo: 'Geografia', storia: 'Storia', '1944': 'Il 1944', frazioni: 'Frazioni',
  borghi: 'Borghi minori', economia: 'Lavoro e sapori', feste: 'Feste e sport'
};

function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    var dati = JSON.parse(e.postData.contents);
    if (!valido(dati)) return risposta('rifiutato');

    lock.waitLock(10000);
    var foglio = SpreadsheetApp.getActiveSpreadsheet();
    var partite = foglio.getSheetByName('Partite');
    var risposte = foglio.getSheetByName('Risposte');
    if (!partite || !risposte) return risposta('lancia prima la funzione prepara');

    var adesso = new Date();
    var numero = partite.getLastRow(); // la riga 1 è l'intestazione
    var sbagliate = dati.risposte.filter(function (r) { return !r.ok; }).map(function (r) { return r.id; });
    partite.appendRow([adesso, numero, dati.punti, dati.totale, dati.punti / dati.totale, sbagliate.join(' ')]);

    var righe = dati.risposte.map(function (r) {
      return [adesso, numero, r.id, CATEGORIE[r.c], String(r.q).slice(0, 300), r.ok ? 1 : 0];
    });
    risposte.getRange(risposte.getLastRow() + 1, 1, righe.length, righe[0].length).setValues(righe);
    return risposta('ok');
  } catch (err) {
    return risposta('errore');
  } finally {
    try { lock.releaseLock(); } catch (e2) { /* nessun lock da rilasciare */ }
  }
}

// Scarta tutto ciò che non ha la forma esatta di una partita del quiz.
function valido(d) {
  if (!d || d.v !== 1 || !Array.isArray(d.risposte)) return false;
  if (typeof d.totale !== 'number' || d.totale < 5 || d.totale > 30) return false;
  if (d.risposte.length !== d.totale) return false;
  var giuste = 0;
  for (var i = 0; i < d.risposte.length; i++) {
    var r = d.risposte[i];
    if (!r || !/^[0-9a-f]{8}$/.test(r.id) || !CATEGORIE[r.c] || (r.ok !== 0 && r.ok !== 1)) return false;
    giuste += r.ok;
  }
  return d.punti === giuste;
}

function risposta(testo) {
  return ContentService.createTextOutput(testo).setMimeType(ContentService.MimeType.TEXT);
}

/**
 * Le formule sono in sintassi inglese (virgole): Apps Script le converte nella lingua del foglio.
 *
 * Da lanciare UNA volta dall'editor (menu a tendina delle funzioni → prepara → Esegui):
 * crea i fogli Partite, Risposte e Statistiche con intestazioni e formule.
 */
function prepara() {
  var foglio = SpreadsheetApp.getActiveSpreadsheet();

  function crea(nome, intestazione) {
    var f = foglio.getSheetByName(nome) || foglio.insertSheet(nome);
    if (f.getLastRow() === 0) {
      f.appendRow(intestazione);
      f.getRange(1, 1, 1, intestazione.length).setFontWeight('bold');
      f.setFrozenRows(1);
    }
    return f;
  }

  var partite = crea('Partite', ['Data', 'Partita', 'Punti', 'Domande', 'Quota giuste', 'Id sbagliate']);
  partite.getRange('E:E').setNumberFormat('0%');
  crea('Risposte', ['Data', 'Partita', 'Id', 'Categoria', 'Domanda', 'Giusta (1/0)']);

  var stat = foglio.getSheetByName('Statistiche') || foglio.insertSheet('Statistiche');
  stat.clear();
  stat.getRange('A1:B4').setValues([
    ['Partite giocate', '=COUNTA(Partite!A2:A)'],
    ['Punteggio medio', '=IFERROR(AVERAGE(Partite!C2:C),"")'],
    ['Quota media di risposte giuste', '=IFERROR(AVERAGE(Partite!E2:E),"")'],
    ['Partite perfette', '=COUNTIF(Partite!E2:E,1)']
  ]);
  stat.getRange('B2').setNumberFormat('0.0');
  stat.getRange('B3').setNumberFormat('0%');
  stat.getRange('A1:A4').setFontWeight('bold');

  stat.getRange('A7').setValue('Per categoria (dalla più difficile)').setFontWeight('bold');
  stat.getRange('A8').setFormula(`=IFERROR(QUERY(Risposte!D2:F,"select D, count(F), avg(F) where D is not null group by D order by avg(F) label D 'Categoria', count(F) 'Risposte', avg(F) 'Quota giuste'",0),"Ancora nessuna partita")`);

  stat.getRange('A18').setValue('Per domanda (dalla più sbagliata)').setFontWeight('bold');
  stat.getRange('A19').setFormula(`=IFERROR(QUERY(Risposte!C2:F,"select C, E, D, count(F), avg(F) where C is not null group by C, E, D order by avg(F) label C 'Id', E 'Domanda', D 'Categoria', count(F) 'Risposte', avg(F) 'Quota giuste'",0),"Ancora nessuna partita")`);

  stat.setColumnWidth(1, 260);
  stat.setColumnWidth(2, 420);
}

// Fine dello script: se copiando non vedi questa riga, il codice è stato tagliato.
