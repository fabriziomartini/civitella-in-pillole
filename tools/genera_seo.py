"""Genera le parti del sito pensate per i motori di ricerca e per gli LLM.

Uso, dalla radice del repository:  python3 tools/genera_seo.py
(dopo tools/genera_anteprime.py, perché usa lo stesso elenco di pagine)

Per ogni pagina dell'elenco PAGINE di tools/genera_anteprime.py:
- scrive nella <head> il blocco tra <!-- dati strutturati --> e <!-- /dati strutturati -->:
  JSON-LD schema.org con il sito, l'autore, il luogo di cui parla la pagina e il percorso
  di navigazione (breadcrumb). Titolo e descrizione vengono da <title> e
  <meta name="description">;
- scrive il footer dentro <div id="footer-placeholder">, tra <!-- footer --> e <!-- /footer -->.
  Il footer è nell'HTML (non più iniettato via JS), così lo leggono anche i crawler che non
  eseguono JavaScript, compresi i link a tutte le frazioni.

Rigenera inoltre:
- sitemap.xml, con la data dell'ultimo commit di ogni pagina (<lastmod>);
- llms.txt, l'indice del sito in Markdown per gli LLM (proposta llmstxt.org).

Rilanciare dopo aver aggiunto una pagina o cambiato titoli e descrizioni.
"""
import html
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from genera_anteprime import PAGINE, SITO, RADICE  # noqa: E402

AUTORE = "Fabrizio Martini"
NOME_SITO = "Civitella in Pillole"
COMUNE = "Civitella in Val di Chiana"
WIKIPEDIA_COMUNE = "https://it.wikipedia.org/wiki/Civitella_in_Val_di_Chiana"

# Sezioni principali: (pagina, etichetta nel footer)
ESPLORA = [
    ("storia.html", "Storia"),
    ("geografia.html", "Geografia"),
    ("frazioni.html", "Le frazioni"),
    ("patrimonio.html", "Patrimonio"),
    ("lavoro-e-sapori.html", "Lavoro e sapori"),
    ("feste-e-associazioni.html", "Feste e associazioni"),
    ("amministrazione.html", "Amministrazione"),
    ("quiz.html", "Mettiti alla prova: il quiz"),
]

FRAZIONI = [
    ("civitella", "Civitella (capoluogo)"),
    ("albergo", "Albergo"),
    ("badia-al-pino", "Badia al Pino"),
    ("ciggiano", "Ciggiano"),
    ("cornia", "Cornia"),
    ("gebbia", "Gebbia"),
    ("oliveto", "Oliveto"),
    ("pieve-a-maiano", "Pieve a Maiano"),
    ("pieve-al-toppo", "Pieve al Toppo"),
    ("ponticino", "Ponticino"),
    ("spoiano", "Spoiano"),
    ("tegoleto", "Tegoleto"),
    ("tuori", "Tuori"),
    ("viciomaggio", "Viciomaggio"),
    ("borghi-minori", "Borghi e località minori"),
]


def leggi(contenuto, schema):
    m = re.search(schema, contenuto, re.S)
    return html.unescape(re.sub(r"\s+", " ", m.group(1)).strip()) if m else ""


def titolo_breve(titolo):
    return titolo.split(" — ")[0].strip()


def footer(base):
    esplora = "".join('<li><a href="%s%s">%s</a></li>' % (base, p, n) for p, n in ESPLORA)
    frazioni = "".join('<li><a href="%sfrazioni/%s.html">%s</a></li>' % (base, s, n) for s, n in FRAZIONI)
    righe = [
        '<footer class="site-footer py-5">',
        '<div class="container px-lg-5">',
        '<div class="row gy-4">',
        '<div class="col-lg-4">',
        '<h2 class="fw-bold mb-3">Civitella in Pillole</h2>',
        '<p class="mb-0 site-footer__testo">Un progetto personale di raccolta e divulgazione dedicato a Civitella in Val di Chiana, '
        'il suo capoluogo storico e le sue frazioni: storia, geografia, chiese, curiosità e tradizioni del territorio.</p>',
        '<p class="mt-3 mb-0 site-footer__autore">Ideato e curato da <strong>%s</strong></p>' % AUTORE,
        "</div>",
        '<div class="col-6 col-lg-2">',
        '<h3 class="fw-bold mb-3">Esplora</h3>',
        '<ul class="list-unstyled d-flex flex-column gap-2">%s</ul>' % esplora,
        "</div>",
        '<div class="col-6 col-lg-3">',
        '<h3 class="fw-bold mb-3">Le frazioni</h3>',
        '<ul class="list-unstyled d-flex flex-column gap-2">%s</ul>' % frazioni,
        "</div>",
        '<div class="col-lg-3">',
        '<h3 class="fw-bold mb-3">Trasparenza</h3>',
        '<p class="mb-2 site-footer__testo">Non è un sito istituzionale del Comune. Tutte le fonti usate sono elencate pubblicamente.</p>',
        '<a href="%sfonti.html">Vedi le fonti <i class="bi bi-arrow-right"></i></a>' % base,
        "</div>",
        "</div>",
        '<div class="footer-bottom mt-4 pt-4 text-center">Civitella in Pillole &mdash; ideato e curato da %s. '
        'Progetto personale, non affiliato al Comune di Civitella in Val di Chiana.</div>' % AUTORE,
        "</div>",
        "</footer>",
    ]
    return "<!-- footer: generato da tools/genera_seo.py -->" + "".join(righe) + "<!-- /footer -->"


def briciole(pagina, nome):
    voci = [("Home", SITO)]
    if pagina.startswith("frazioni/"):
        voci.append(("Le frazioni", SITO + "frazioni.html"))
    if pagina != "index.html":
        voci.append((nome, SITO + pagina))
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(voci)
        ],
    }


def dati_strutturati(pagina, contenuto):
    titolo = leggi(contenuto, r"<title>(.*?)</title>")
    descrizione = leggi(contenuto, r'<meta name="description" content="(.*?)"')
    nome = titolo_breve(titolo)
    url = SITO + pagina
    autore = {"@id": SITO + "#autore"}
    comune = {"@id": SITO + "#comune"}
    grafo = [
        {
            "@type": "WebSite",
            "@id": SITO + "#sito",
            "url": SITO,
            "name": NOME_SITO,
            "inLanguage": "it",
            "creator": autore,
            "publisher": autore,
            "about": comune,
        },
        {"@type": "Person", "@id": SITO + "#autore", "name": AUTORE},
        {
            "@type": "AdministrativeArea",
            "@id": SITO + "#comune",
            "name": COMUNE,
            "sameAs": WIKIPEDIA_COMUNE,
            "containedInPlace": {"@type": "AdministrativeArea", "name": "Provincia di Arezzo"},
        },
    ]
    if pagina.startswith("frazioni/") and not pagina.endswith("borghi-minori.html"):
        argomento = {"@type": "Place", "name": nome, "containedInPlace": comune}
    else:
        argomento = comune
    grafo.append({
        "@type": "WebPage",
        "@id": indirizzo(pagina),
        "url": indirizzo(pagina),
        "name": titolo,
        "description": descrizione,
        "inLanguage": "it",
        "isPartOf": {"@id": SITO + "#sito"},
        "author": autore,
        "about": argomento,
        "primaryImageOfPage": {"@type": "ImageObject", "url": SITO + "assets/social/%s.jpg" % immagine(pagina)},
        "breadcrumb": briciole(pagina, nome),
    })
    testo = json.dumps({"@context": "https://schema.org", "@graph": grafo}, ensure_ascii=False, indent=2)
    testo = testo.replace("</", "<\\/")
    righe = "\n".join("    " + r for r in testo.split("\n"))
    return ("    <!-- dati strutturati: generati da tools/genera_seo.py -->\n"
            '    <script type="application/ld+json">\n%s\n    </script>\n'
            "    <!-- /dati strutturati -->\n") % righe


def immagine(pagina):
    return next(n for p, n, *_ in PAGINE if p == pagina)


def indirizzo(pagina):
    """L'indirizzo canonico della pagina (la home è la cartella, non index.html)."""
    return SITO if pagina == "index.html" else SITO + pagina


def ultimo_commit(pagina):
    r = subprocess.run(["git", "log", "-1", "--format=%cs", "--", pagina], cwd=RADICE,
                       capture_output=True, text=True)
    return r.stdout.strip()


def main():
    indice = []
    for pagina, *_ in PAGINE:
        percorso = os.path.join(RADICE, pagina)
        contenuto = open(percorso, encoding="utf-8").read()
        base = "../" if pagina.startswith("frazioni/") else ""

        contenuto = re.sub(r"    <!-- dati strutturati.*?<!-- /dati strutturati -->\n", "", contenuto, flags=re.S)
        fine = contenuto.index("    <!-- /anteprima social -->\n") + len("    <!-- /anteprima social -->\n")
        contenuto = contenuto[:fine] + dati_strutturati(pagina, contenuto) + contenuto[fine:]

        nuovo, n = re.subn(r'<div id="footer-placeholder">.*?</div>(?=\s*<!-- Bootstrap|\s*<script)',
                           lambda m: '<div id="footer-placeholder">%s</div>' % footer(base), contenuto, count=1, flags=re.S)
        if n != 1:
            raise SystemExit("footer-placeholder non trovato in " + pagina)
        open(percorso, "w", encoding="utf-8").write(nuovo)

        indice.append((pagina, leggi(contenuto, r"<title>(.*?)</title>"),
                       leggi(contenuto, r'<meta name="description" content="(.*?)"')))

    mappa = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for pagina, _, _ in indice:
        data = ultimo_commit(pagina)
        mappa.append("  <url><loc>%s</loc>%s</url>" % (indirizzo(pagina), "<lastmod>%s</lastmod>" % data if data else ""))
    mappa.append("</urlset>")
    open(os.path.join(RADICE, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(mappa) + "\n")

    def voce(pagina, titolo, descrizione):
        return "- [%s](%s): %s" % (titolo_breve(titolo), indirizzo(pagina), descrizione)

    generali = [v for v in indice if not v[0].startswith("frazioni/")]
    frazioni = [v for v in indice if v[0].startswith("frazioni/")]
    llms = [
        "# Civitella in Pillole",
        "",
        "> Sito divulgativo su Civitella in Val di Chiana (provincia di Arezzo, Toscana): storia, geografia, "
        "frazioni, patrimonio, economia, feste e memoria dell'eccidio del 29 giugno 1944. "
        "Ideato e curato da %s. Progetto personale, non affiliato al Comune." % AUTORE,
        "",
        "Ogni fatto del sito viene da una fonte scritta, elencata nella pagina Fonti e in fondo a ogni pagina. "
        "Quando un fatto ha una sola fonte, il testo la nomina («secondo la Pro Loco», «secondo il Repetti»); "
        "quando le fonti non concordano, il sito riporta tutte le versioni. Dati demografici: ISTAT, censimento 2021.",
        "",
        "## Pagine principali",
        "",
    ] + [voce(*v) for v in generali] + [
        "",
        "## Frazioni e località",
        "",
    ] + [voce(*v) for v in frazioni] + [
        "",
        "## Optional",
        "",
        "- [Base dei fatti verificati](https://github.com/fabriziomartini/civitella-in-pillole/blob/main/ricerca/fatti-verificati.md): "
        "un fatto per riga, con fonte e livello di verifica, divergenze tra fonti ed esclusi",
        "",
    ]
    open(os.path.join(RADICE, "llms.txt"), "w", encoding="utf-8").write("\n".join(llms))
    print("%d pagine aggiornate; scritti sitemap.xml e llms.txt." % len(indice))


if __name__ == "__main__":
    main()
