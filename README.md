# Civitella in Pillole

Sito informativo personale dedicato al Comune di Civitella in Val di Chiana (provincia di Arezzo, Toscana): storia, geografia e una pagina per ciascuna delle tredici frazioni e per il capoluogo storico, una pagina dedicata ai borghi minori, una al patrimonio storico del territorio, una all'economia e ai prodotti locali (Lavoro e sapori) e una al calendario delle feste, alle associazioni e allo sport (Feste e associazioni).

Nota sulle frazioni: l'infobox di Wikipedia elenca ufficialmente 13 frazioni includendo **Gebbia** (non Ponticino, che è frazione del comune di Laterina Pergine Valdarno). Il sito include comunque anche **Ponticino**, perché una porzione del suo abitato ricade nel territorio di Civitella in Val di Chiana &mdash; ha quindi una pagina propria che ne spiega la particolarità di frazione condivisa tra tre comuni. Le frazioni trattate sul sito sono perciò 14 in totale (le 13 ufficiali + Ponticino).

Non è un sito istituzionale del Comune, ma un progetto personale di raccolta e divulgazione di contenuti sul territorio.

## Struttura

```
index.html          Home
storia.html          Storia del comune
geografia.html       Geografia e territorio
frazioni.html        Indice di tutte le frazioni
frazioni/*.html       Una pagina per ciascuna frazione (+ capoluogo)
patrimonio.html       Patrimonio: castelli, ville, mulini, archeologia
lavoro-e-sapori.html  Economia, agricoltura, Slow Food
feste-e-associazioni.html  Calendario delle feste, associazioni, sport
fonti.html            Fonti e bibliografia usate
css/styles.css        Bootstrap 5.3.8 (compilato)
css/civitella.css     Palette e font custom
js/partials.js        Navbar e footer condivisi, iniettati via JS in ogni pagina
```

Sito statico in puro HTML/CSS/JS, senza build tool: pensato per essere pubblicato su GitHub Pages.

## Sviluppo locale

Per vedere navbar/footer correttamente (iniettati via JS) è consigliato servire i file con un piccolo server locale invece di aprirli direttamente da filesystem:

```
python3 -m http.server
```

e poi visitare `http://localhost:8000/`.

## Stato dei contenuti

Storia, Geografia e tutte le pagine delle frazioni (capoluogo storico incluso) hanno un contenuto completo, basato su ricerca multi-fonte (Wikipedia, siti diocesani, Pro Loco, stampa locale aretina, portali istituzionali) e verificato tramite NotebookLM.

La pagina Fonti va aggiornata con l'elenco puntuale delle fonti usate per le frazioni popolate in questa iterazione (vedi TODO più sotto).

## Da fare

- Aggiungere a `fonti.html` le fonti specifiche usate per le 12 frazioni popolate nell'ultima iterazione (oggi citate genericamente in fondo a ciascuna pagina).
- Verificare su fonte primaria i dati di dettaglio sulla giunta comunale e sullo storico elettorale (vedi `output/notebook6_output.md`), che al momento provengono in parte da un solo aggregatore non istituzionale.
