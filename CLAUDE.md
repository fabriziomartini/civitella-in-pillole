# civitella-in-pillole

## Qualità dell'output web

- Non consegnare un layout che è di fatto un template scaricato con solo i colori cambiati. Prima di scrivere pagine HTML/CSS nuove, proponi una vera direzione di design (tipografia, palette, griglia) con riferimenti concreti — vedi la regola "Design prima del codice" nel CLAUDE.md globale.
- Tutti i tag `<img>` devono avere `width`/`height` espliciti (o un `aspect-ratio` in CSS) per evitare layout shift e immagini sovradimensionate. Le immagini in `frazioni/*.html` (es. `frazioni/civitella.html`) attualmente ne sono prive — è il tipo di regressione da non ripetere in nuove pagine, e da correggere se si torna a toccare quei file.
