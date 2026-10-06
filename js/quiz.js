// Quiz su Civitella in Val di Chiana.
// Pesca N domande da window.QUIZ_DOMANDE alternando le categorie, mescola le risposte,
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

  // Alterna le categorie in ordine casuale, così ogni partita tocca temi diversi.
  function pescaDomande(n) {
    var gruppi = {};
    window.QUIZ_DOMANDE.forEach(function (d) {
      (gruppi[d.c] = gruppi[d.c] || []).push(d);
    });
    Object.keys(gruppi).forEach(function (k) { gruppi[k] = mescola(gruppi[k]); });
    var scelte = [];
    while (scelte.length < n) {
      var chiavi = mescola(Object.keys(gruppi).filter(function (k) { return gruppi[k].length; }));
      if (!chiavi.length) break;
      for (var i = 0; i < chiavi.length && scelte.length < n; i++) scelte.push(gruppi[chiavi[i]].pop());
    }
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
    el.domanda.focus();
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
    el.avanti.focus();
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
    el.punteggio.focus();
  }

  document.addEventListener("DOMContentLoaded", function () {
    ["start", "play", "result", "record", "totale", "card", "categoria", "contatore", "barra", "barraWrap",
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
