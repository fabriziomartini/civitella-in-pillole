# Statistiche del quiz su Google Fogli

A fine partita il quiz invia in forma anonima il punteggio e l'esito di ogni domanda a un foglio Google tuo. Non vengono raccolti né salvati nomi, email o indirizzi IP.

**Cosa trovi nel foglio:**
- **Partite:** una riga per partita, con data, punti, quota di risposte giuste e id delle domande sbagliate.
- **Risposte:** una riga per ogni domanda giocata (id, categoria, testo, giusta 1 o sbagliata 0).
- **Statistiche:** si aggiorna da solo con:
  - partite giocate, punteggio medio, quota media di risposte giuste, partite perfette;
  - le categorie dalla più difficile alla più facile;
  - le domande dalla più sbagliata alla più facile.

  Una domanda sbagliata molto spesso può voler dire due cose: un argomento poco conosciuto, oppure una domanda formulata male da rivedere.

## Come attivarlo (circa 10 minuti, una volta sola)

1. **Crea il foglio.**
   - Vai su https://sheets.google.com e crea un foglio vuoto, per esempio «Quiz Civitella – statistiche».
2. **Apri l'editor degli script.**
   - Dal menu del foglio: **Estensioni → Apps Script**.
   - Cancella il codice di esempio (`function myFunction…`).
   - Incolla **tutto** il contenuto del file `tools/quiz-statistiche.gs` di questo repository.
   - Salva con l'icona del dischetto.
3. **Prepara i fogli.**
   - In alto, nel menu a tendina accanto a «Esegui», scegli la funzione **`prepara`** e premi **Esegui**.
   - Google chiede l'autorizzazione: scegli il tuo account.
   - Se compare «Google non ha verificato questa app», clicca **Avanzate → Vai a … (non sicuro)**. È normale: lo script è tuo e gira solo sul tuo foglio.
   - Torna al foglio: devono esserci le schede **Partite**, **Risposte** e **Statistiche**.
4. **Pubblica lo script come app web.**
   - Nell'editor: **Esegui il deployment → Nuovo deployment**.
   - Clicca l'ingranaggio accanto a «Seleziona tipo» e scegli **App web**, poi compila:
     - Descrizione: `Quiz Civitella`;
     - Esegui come: **Me**;
     - Chi ha accesso: **Chiunque** (serve perché il quiz possa inviare i dati: nessuno può leggere il foglio).
   - Premi **Esegui il deployment** e copia l'**URL dell'app web**. Finisce con `/exec`.
5. **Incollami l'URL** nella chat. Lo inserisco io nel quiz (`STATISTICHE_URL` in `js/quiz.js`) e pubblico.
   - Da quel momento la pagina del quiz mostra anche la nota sulla raccolta anonima dei dati.

## Da sapere

- **Il foglio resta privato:** lo vedi solo tu. Chiunque può inviare dati all'app web, ma nessuno può leggerli.
- **Controllo dei dati in arrivo:** lo script scarta tutto ciò che non ha la forma esatta di una partita del quiz. Per esempio, il punteggio deve corrispondere alle risposte giuste e le categorie devono essere quelle del quiz.
- **Se modifichi lo script:**
  - usa **Esegui il deployment → Gestisci deployment → Modifica**, poi **Nuova versione**: così l'URL resta lo stesso;
  - con «Nuovo deployment» l'URL cambia e va aggiornato nel quiz.
- **Per sospendere la raccolta:**
  - disattiva il deployment da «Gestisci deployment»;
  - oppure chiedi a Claude di svuotare `STATISTICHE_URL`.
- **Se una domanda viene riformulata,** cambia il suo id e le sue statistiche ripartono da zero (vedi `tools/genera_quiz.py`).

## Correggere la difficoltà con i dati

Il livello di ogni domanda (facile, media, difficile) nasce da una regola scritta in `tools/quiz_difficolta.py`. Quando le partite sono abbastanza, lo correggono le risposte vere:

1. Nel foglio apri la scheda **Risposte** e scegli **File → Scarica → Valori separati da virgola (.csv)**.
2. Passa il file a Claude, oppure lancia `python3 tools/calibra_difficolta.py Risposte.csv` e poi `python3 tools/genera_quiz.py`.

Le domande con almeno 20 risposte prendono il livello dai dati: oltre il 75% di risposte giuste diventano facili, sotto il 40% difficili. Le altre restano con il livello della regola.
