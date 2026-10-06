// Quiz su Civitella in Val di Chiana.
// Pesca N domande da window.QUIZ_DOMANDE mescolando livelli e categorie, mescola le risposte,
// mostra la correzione dopo ogni risposta e un riepilogo finale.
(function () {
  var CATEGORIE = {
    geo: { nome: "Geografia", accento: "campi" },
    storia: { nome: "Storia", accento: "castelli" },
    "1944": { nome: "Il 1944", accento: "memoria" },
    frazioni: { nome: "Frazioni", accento: "mulini" },
    borghi: { nome: "Borghi minori", accento: "ville" },
    economia: { nome: "Lavoro e sapori", accento: "industria" },
    feste: { nome: "Feste e sport", accento: "cultura" }
  };
  var LETTERE = ["A", "B", "C", "D"];
  var LUNGHEZZA = 15;
  var CHIAVE_RECORD = "civitella-quiz-record";
  // Indirizzo dell'app web di Google Apps Script che raccoglie le statistiche anonime
  // (vedi tools/quiz-statistiche.gs). Vuoto = invio disattivato.
  var STATISTICHE_URL = "https://script.google.com/macros/s/AKfycbyKP2GX48pHJ_YVPeOI7TBHcVkCgxMsS4FOYz-xZPQpddd4CrJZeXI5FrvVkPbS1Z9U/exec";

  var stato = { lunghezza: LUNGHEZZA, domande: [], indice: 0, risposte: [] };
  var el = {};

  function mescola(lista) {
    var a = lista.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  // Peso di ogni categoria nella pesca: storia, geografia e frazioni escono più spesso.
  // La probabilità di una categoria cresce con la radice del numero di domande,
  // così le categorie piccole non si ripetono a ogni partita e quelle grandi non dominano.
  var PESO = { storia: 1.4, geo: 1.3, frazioni: 1.2, "1944": 1.1, borghi: 1, economia: 0.7, feste: 0.7 };
  var LIVELLI = { 1: "Facile", 2: "Media", 3: "Difficile" };
  var CHIAVE_VISTE = "civitella-quiz-viste";

  function intero(min, max) { return min + Math.floor(Math.random() * (max - min + 1)); }

  // Id delle domande già uscite, dalla più vecchia alla più recente.
  function leggiViste() {
    try { var v = JSON.parse(localStorage.getItem(CHIAVE_VISTE)); return Array.isArray(v) ? v : []; } catch (e) { return []; }
  }

  // Ricorda circa i due terzi dell'archivio: una domanda torna solo dopo che sono uscite quasi tutte le altre.
  function salvaViste(nuove) {
    try {
      var v = leggiViste().filter(function (id) { return nuove.indexOf(id) === -1; }).concat(nuove);
      var max = Math.floor(window.QUIZ_DOMANDE.length * 0.65);
      localStorage.setItem(CHIAVE_VISTE, JSON.stringify(v.slice(-max)));
    } catch (e) { /* storage non disponibile: il quiz funziona lo stesso */ }
  }

  function pescaPesata(lista, peso) {
    var pesi = lista.map(peso);
    var totale = pesi.reduce(function (a, b) { return a + b; }, 0);
    var r = Math.random() * totale;
    for (var i = 0; i < lista.length; i++) { r -= pesi[i]; if (r <= 0) return lista[i]; }
    return lista[lista.length - 1];
  }

  // Ogni partita mescola i livelli (circa un terzo facili, un terzo medie, un quarto difficili, con variazioni casuali),
  // evita le domande uscite di recente e distribuisce le categorie senza farne prevalere una.
  function pescaDomande(n) {
    var tutte = window.QUIZ_DOMANDE;
    var dimensione = {};
    tutte.forEach(function (d) { dimensione[d.c] = (dimensione[d.c] || 0) + 1; });
    var viste = leggiViste();
    var eta = {};
    viste.forEach(function (id, i) { eta[id] = viste.length - i; }); // 1 = uscita nell'ultima partita

    var facili = intero(4, 6), difficili = intero(3, 5);
    var livelli = [];
    for (var k = 0; k < n; k++) livelli.push(k < facili ? 1 : k < facili + difficili ? 3 : 2);

    var prese = {}, usate = {}, scelte = [];
    mescola(livelli).forEach(function (livello) {
      var libere = tutte.filter(function (d) { return !prese[d.id]; });
      var candidate = libere.filter(function (d) { return d.d === livello; });
      if (!candidate.length) candidate = libere;
      var mai = candidate.filter(function (d) { return !eta[d.id]; });
      if (mai.length) candidate = mai;
      else {
        // Tutte già viste: si pesca nella metà uscita meno di recente.
        candidate.sort(function (a, b) { return eta[b.id] - eta[a.id]; });
        candidate = candidate.slice(0, Math.max(1, Math.ceil(candidate.length / 2)));
      }
      var d = pescaPesata(candidate, function (x) {
        return (PESO[x.c] || 1) / Math.sqrt(dimensione[x.c]) / Math.pow(1 + (usate[x.c] || 0), 2);
      });
      prese[d.id] = true;
      usate[d.c] = (usate[d.c] || 0) + 1;
      scelte.push(d);
    });
    salvaViste(scelte.map(function (d) { return d.id; }));
    return mescola(scelte).map(function (d) {
      return { dati: d, opzioni: mescola([d.a].concat(d.x)) };
    });
  }

  function crea(tag, classe, testo) {
    var nodo = document.createElement(tag);
    if (classe) nodo.className = classe;
    if (testo !== undefined) nodo.textContent = testo;
    return nodo;
  }

  function leggiRecord() {
    try { return JSON.parse(localStorage.getItem(CHIAVE_RECORD)) || {}; } catch (e) { return {}; }
  }

  function salvaRecord(n, punti) {
    try {
      var r = leggiRecord();
      var precedente = r[n];
      if (precedente === undefined || punti > precedente) {
        r[n] = punti;
        localStorage.setItem(CHIAVE_RECORD, JSON.stringify(r));
        return precedente !== undefined; // il primo punteggio non è un "nuovo record"
      }
    } catch (e) { /* storage non disponibile: il quiz funziona lo stesso */ }
    return false;
  }

  function mostra(sezione) {
    ["start", "play", "result"].forEach(function (s) { el[s].hidden = s !== sezione; });
  }

  function aggiornaStart() {
    var r = leggiRecord()[LUNGHEZZA];
    el.record.textContent = r !== undefined ? "Il tuo record: " + r + "/" + LUNGHEZZA : "";
    el.totale.textContent = window.QUIZ_DOMANDE.length;
  }

  function inizia(n) {
    stato.lunghezza = n;
    stato.domande = pescaDomande(n);
    stato.indice = 0;
    stato.risposte = [];
    mostra("play");
    disegnaDomanda();
  }

  function disegnaDomanda() {
    var corrente = stato.domande[stato.indice];
    var d = corrente.dati;
    var cat = CATEGORIE[d.c];
    el.card.className = "wm-quiz-card wm-accent--" + cat.accento;
    el.categoria.textContent = cat.nome;
    el.livello.className = "wm-quiz-level wm-quiz-level--" + d.d;
    el.livello.textContent = LIVELLI[d.d];
    el.contatore.textContent = "Domanda " + (stato.indice + 1) + " di " + stato.lunghezza;
    el.barra.style.width = (stato.indice / stato.lunghezza) * 100 + "%";
    el.barraWrap.setAttribute("aria-valuenow", String(stato.indice));
    el.barraWrap.setAttribute("aria-valuemax", String(stato.lunghezza));
    el.domanda.textContent = d.q;
    el.opzioni.innerHTML = "";
    corrente.opzioni.forEach(function (testo, i) {
      var b = crea("button", "wm-quiz-option");
      b.type = "button";
      b.appendChild(crea("span", "wm-quiz-option__letter", LETTERE[i]));
      b.appendChild(crea("span", "wm-quiz-option__text", testo));
      b.addEventListener("click", function () { rispondi(i); });
      el.opzioni.appendChild(b);
    });
    el.feedback.hidden = true;
    el.avanti.hidden = true;
    // Niente scorrimento automatico: si torna su solo se la nuova domanda è fuori schermo.
    el.domanda.focus({ preventScroll: true });
    if (el.card.getBoundingClientRect().top < 0) el.play.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function rispondi(i) {
    if (stato.risposte.length > stato.indice) return;
    var corrente = stato.domande[stato.indice];
    var scelta = corrente.opzioni[i];
    var giusta = scelta === corrente.dati.a;
    stato.risposte.push({ scelta: scelta, giusta: giusta });

    Array.prototype.forEach.call(el.opzioni.children, function (b, k) {
      b.disabled = true;
      var testo = corrente.opzioni[k];
      if (testo === corrente.dati.a) b.classList.add("is-correct");
      else if (k === i) b.classList.add("is-wrong");
    });

    el.esito.textContent = giusta ? "Esatto!" : "Non è questa. La risposta giusta è: " + corrente.dati.a;
    el.esito.className = "wm-quiz-feedback__esito " + (giusta ? "is-correct" : "is-wrong");
    el.spiegazione.textContent = corrente.dati.s;
    el.feedback.hidden = false;
    el.avanti.textContent = stato.indice + 1 < stato.lunghezza ? "Avanti" : "Vedi il risultato";
    el.avanti.hidden = false;
    el.avanti.focus({ preventScroll: true });
  }

  function avanti() {
    stato.indice++;
    if (stato.indice < stato.lunghezza) disegnaDomanda();
    else risultato();
  }

  function giudizio(perc) {
    if (perc === 100) return "Perfetto: conosci Civitella come le tue tasche.";
    if (perc >= 80) return "Ottimo: sei un vero esperto del territorio.";
    if (perc >= 60) return "Bene: conosci il comune più di molti altri.";
    if (perc >= 40) return "Non male: qualche pagina del sito ti farà diventare un esperto.";
    return "C'è ancora molto da scoprire: il sito è qui apposta.";
  }

  // Invia in forma anonima il punteggio e, per ogni domanda, id, categoria, testo e giusto/sbagliato.
  // text/plain evita la richiesta preliminare CORS, che Apps Script non gestisce.
  function inviaStatistiche(punti) {
    if (!STATISTICHE_URL || !window.fetch) return;
    var dati = {
      v: 1,
      punti: punti,
      totale: stato.lunghezza,
      risposte: stato.domande.map(function (corrente, k) {
        return { id: corrente.dati.id, c: corrente.dati.c, q: corrente.dati.q, ok: stato.risposte[k].giusta ? 1 : 0 };
      })
    };
    try {
      fetch(STATISTICHE_URL, {
        method: "POST",
        mode: "no-cors",
        keepalive: true,
        headers: { "Content-Type": "text/plain;charset=utf-8" },
        body: JSON.stringify(dati)
      }).catch(function () { /* le statistiche non devono mai bloccare il quiz */ });
    } catch (e) { /* idem */ }
  }

  function risultato() {
    var punti = stato.risposte.filter(function (r) { return r.giusta; }).length;
    var n = stato.lunghezza;
    var record = salvaRecord(n, punti);
    inviaStatistiche(punti);
    el.barra.style.width = "100%";
    el.punteggio.textContent = punti + "/" + n;
    el.giudizio.textContent = giudizio(Math.round((punti / n) * 100)) + (record ? " Nuovo record personale!" : "");
    el.riepilogo.innerHTML = "";
    stato.domande.forEach(function (corrente, k) {
      var r = stato.risposte[k];
      var d = corrente.dati;
      var li = crea("li", "wm-quiz-review " + (r.giusta ? "is-correct" : "is-wrong") + " wm-accent--" + CATEGORIE[d.c].accento);
      var testa = crea("div", "wm-quiz-review__head");
      var icona = crea("span", "wm-quiz-review__icon");
      icona.setAttribute("aria-label", r.giusta ? "Risposta esatta" : "Risposta sbagliata");
      icona.appendChild(crea("i", "bi " + (r.giusta ? "bi-check-lg" : "bi-x-lg")));
      testa.appendChild(icona);
      testa.appendChild(crea("span", "wm-quiz-review__cat", CATEGORIE[d.c].nome));
      testa.appendChild(crea("span", "wm-quiz-level wm-quiz-level--" + d.d, LIVELLI[d.d]));
      li.appendChild(testa);
      li.appendChild(crea("p", "wm-quiz-review__q", (k + 1) + ". " + d.q));
      if (!r.giusta) li.appendChild(crea("p", "wm-quiz-review__tua", "La tua risposta: " + r.scelta));
      li.appendChild(crea("p", "wm-quiz-review__ok", "Risposta esatta: " + d.a));
      var sp = crea("p", "wm-quiz-review__s", d.s + " ");
      // Nuova scheda: chi approfondisce non perde il riepilogo della partita.
      var a = crea("a", "", "Approfondisci");
      a.href = d.l;
      a.target = "_blank";
      a.rel = "noopener";
      sp.appendChild(a);
      li.appendChild(sp);
      el.riepilogo.appendChild(li);
    });
    mostra("result");
    el.punteggio.focus({ preventScroll: true });
    el.result.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  document.addEventListener("DOMContentLoaded", function () {
    ["start", "play", "result", "record", "totale", "card", "categoria", "livello", "contatore", "barra", "barraWrap",
      "domanda", "opzioni", "feedback", "esito", "spiegazione", "avanti", "punteggio", "giudizio", "riepilogo"]
      .forEach(function (id) { el[id] = document.getElementById("quiz-" + id); });
    if (!el.start || !window.QUIZ_DOMANDE) return;

    Array.prototype.forEach.call(document.querySelectorAll("[data-quiz-start]"), function (b) {
      b.addEventListener("click", function () { inizia(LUNGHEZZA); });
    });
    el.avanti.addEventListener("click", avanti);
    document.getElementById("quiz-rigioca").addEventListener("click", function () { inizia(stato.lunghezza); });

    // Tastiera: 1-4 o A-D per rispondere, Invio per andare avanti.
    document.addEventListener("keydown", function (e) {
      if (el.play.hidden || e.altKey || e.ctrlKey || e.metaKey) return;
      var tasto = e.key.toUpperCase();
      var i = ["1", "2", "3", "4"].indexOf(tasto);
      if (i === -1) i = LETTERE.indexOf(tasto);
      if (i !== -1 && stato.risposte.length === stato.indice) { e.preventDefault(); rispondi(i); }
    });

    if (STATISTICHE_URL) document.getElementById("quiz-privacy").hidden = false;
    aggiornaStart();
    mostra("start");
  });
})();
