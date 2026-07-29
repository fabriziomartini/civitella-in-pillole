# Civitella in Pillole

Sito informativo personale dedicato al Comune di Civitella in Val di Chiana (provincia di Arezzo, Toscana): storia, geografia e una pagina per ciascuna delle tredici frazioni oltre al capoluogo storico.

Non è un sito istituzionale del Comune, ma un progetto personale di raccolta e divulgazione di contenuti sul territorio.

## Struttura

```
index.html          Home
storia.html          Storia del comune
geografia.html       Geografia e territorio
frazioni.html        Indice di tutte le frazioni
frazioni/*.html       Una pagina per ciascuna frazione (+ capoluogo)
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

Storia, Geografia, Fonti, il capoluogo storico (Civitella) e la frazione di Tegoleto hanno già un contenuto completo. Le altre dodici frazioni sono presenti come pagine scaffold ("contenuto in arrivo") e verranno popolate nelle prossime iterazioni.
