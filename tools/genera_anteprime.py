"""Genera le anteprime per i social (Open Graph) e i relativi tag <meta> in ogni pagina.

Uso, dalla radice del repository:  python3 tools/genera_anteprime.py   (serve Pillow: pip install pillow)

Per ogni pagina dell'elenco PAGINE:
- crea assets/social/<nome>.jpg a 1200x630, la misura usata da Facebook, WhatsApp, LinkedIn e X.
  Se la pagina ha una sua foto, la foto fa da sfondo, con il credito dell'autore; altrimenti lo
  sfondo è il gradiente dell'intestazione del sito. Non si usa mai la foto di un altro luogo;
- scrive nella <head> il blocco tra <!-- anteprima social --> e <!-- /anteprima social -->
  (og:*, twitter:*, link canonical). Titolo e descrizione vengono da <title> e
  <meta name="description"> della pagina, così restano sempre allineati.

Dopo aver cambiato titolo, descrizione o foto di una pagina, rilanciare lo script.
Facebook conserva in cache le anteprime: per aggiornarle subito si usa
https://developers.facebook.com/tools/debug/ ("Recupera di nuovo").
"""
import html
import os
import re

from PIL import Image, ImageDraw, ImageFont

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITO = "https://fabriziomartini.github.io/civitella-in-pillole/"
LARGO, ALTO = 1200, 630
MARGINE = 72

FONT_TITOLO = os.path.join(RADICE, "tools", "fonts", "plus-jakarta-sans-latin-800-normal.woff")
FONT_TESTO = os.path.join(RADICE, "tools", "fonts", "plus-jakarta-sans-latin-500-normal.woff")

INK = (54, 42, 30)
TERRACOTTA = (193, 96, 47)
TERRACOTTA_SCURO = (150, 71, 31)
ORO = (210, 149, 47)

FRAZIONE = "Frazione di Civitella in Val di Chiana"
COMUNE = "Civitella in Val di Chiana"

# pagina, nome immagine, titolo sulla card, sottotitolo, foto (o None), credito della foto
PAGINE = [
    ("index.html", "home", "Civitella in Pillole", "Storia, frazioni e memoria di Civitella in Val di Chiana",
     "civitella-rocca.jpg", "Foto: Argentieri.Andrea, CC BY-SA 4.0"),
    ("storia.html", "storia", "Storia", COMUNE,
     "eccidio-monumento.jpg", "Foto: Anna.Massini, CC BY 4.0"),
    ("geografia.html", "geografia", "Geografia e territorio", COMUNE,
     "valdichiana-panorama.jpg", "Foto: Paolo Menchetti (PMM), CC BY-SA 4.0"),
    ("frazioni.html", "frazioni", "Le frazioni", COMUNE, None, None),
    ("patrimonio.html", "patrimonio", "Il patrimonio del territorio", COMUNE, None, None),
    ("lavoro-e-sapori.html", "lavoro-e-sapori", "Lavoro e sapori", COMUNE, None, None),
    ("feste-e-associazioni.html", "feste-e-associazioni", "Feste e associazioni", COMUNE, None, None),
    ("amministrazione.html", "amministrazione", "Amministrazione", COMUNE, None, None),
    ("fonti.html", "fonti", "Le fonti del sito", COMUNE, None, None),
    ("quiz.html", "quiz", "Quanto conosci Civitella?", "Il quiz: 15 domande su storia, frazioni e territorio", None, None),
    ("frazioni/civitella.html", "civitella", "Civitella", "Il capoluogo storico del comune",
     "civitella-rocca.jpg", "Foto: Argentieri.Andrea, CC BY-SA 4.0"),
    ("frazioni/albergo.html", "albergo", "Albergo", FRAZIONE, None, None),
    ("frazioni/badia-al-pino.html", "badia-al-pino", "Badia al Pino", FRAZIONE,
     "badia-al-pino-san-bartolomeo.jpg", "Foto: LigaDue, CC BY-SA 4.0"),
    ("frazioni/ciggiano.html", "ciggiano", "Ciggiano", FRAZIONE,
     "ciggiano-san-biagio.jpg", "Foto: LigaDue, CC BY-SA 4.0"),
    ("frazioni/cornia.html", "cornia", "Cornia", FRAZIONE,
     "cornia-san-michele-arcangelo.jpg", "Foto: LigaDue, CC BY-SA 4.0"),
    ("frazioni/gebbia.html", "gebbia", "Gebbia", FRAZIONE, None, None),
    ("frazioni/oliveto.html", "oliveto", "Oliveto", FRAZIONE,
     "oliveto-villa-mazzi.jpg", "Foto: LigaDue, CC BY-SA 4.0"),
    ("frazioni/pieve-a-maiano.html", "pieve-a-maiano", "Pieve a Maiano", FRAZIONE,
     "pieve-a-maiano-chiesa.jpg", "Foto: LigaDue, CC BY-SA 4.0"),
    ("frazioni/pieve-al-toppo.html", "pieve-al-toppo", "Pieve al Toppo", FRAZIONE, None, None),
    ("frazioni/ponticino.html", "ponticino", "Ponticino", FRAZIONE, None, None),
    ("frazioni/spoiano.html", "spoiano", "Spoiano", FRAZIONE, None, None),
    ("frazioni/tegoleto.html", "tegoleto", "Tegoleto", FRAZIONE, None, None),
    ("frazioni/tuori.html", "tuori", "Tuori", FRAZIONE,
     "tuori-santi-giorgio-e-luca.jpg", "Foto: LigaDue, CC BY-SA 4.0"),
    ("frazioni/viciomaggio.html", "viciomaggio", "Viciomaggio", FRAZIONE,
     "viciomaggio-veduta.jpg", "Foto: Undini Alessio, pubblico dominio"),
    ("frazioni/borghi-minori.html", "borghi-minori", "Borghi e località minori", COMUNE, None, None),
]


def gradiente():
    """Lo stesso gradiente a 155° dell'intestazione del sito (ink → terracotta scuro → terracotta)."""
    img = Image.new("RGB", (LARGO, ALTO))
    px = img.load()
    for y in range(ALTO):
        for x in range(LARGO):
            t = min(1.0, (x * 0.42 + y * 0.9) / (LARGO * 0.42 + ALTO * 0.9) * 1.2)
            a, b, k = (INK, TERRACOTTA_SCURO, t / 0.68) if t < 0.68 else (TERRACOTTA_SCURO, TERRACOTTA, (t - 0.68) / 0.52)
            px[x, y] = tuple(round(a[i] + (b[i] - a[i]) * k) for i in range(3))
    return img


def sfondo_foto(nome):
    """Foto ritagliata a 1200x630 al centro, scurita a sinistra e in basso perché il testo si legga."""
    foto = Image.open(os.path.join(RADICE, "assets", "images", nome)).convert("RGB")
    scala = max(LARGO / foto.width, ALTO / foto.height)
    foto = foto.resize((round(foto.width * scala), round(foto.height * scala)), Image.LANCZOS)
    x, y = (foto.width - LARGO) // 2, (foto.height - ALTO) // 2
    foto = foto.crop((x, y, x + LARGO, y + ALTO))
    velo = Image.new("L", (LARGO, ALTO))
    pv = velo.load()
    for yy in range(ALTO):
        for xx in range(LARGO):
            sinistra = max(0.0, 1 - xx / (LARGO * 0.85))
            basso = max(0.0, (yy - ALTO * 0.35) / (ALTO * 0.65))
            pv[xx, yy] = round(255 * min(0.88, 0.28 + 0.5 * sinistra + 0.45 * basso))
    return Image.composite(Image.new("RGB", (LARGO, ALTO), INK), foto, velo)


def a_capo(testo, font, larghezza, disegno):
    righe, riga = [], ""
    for parola in testo.split():
        prova = (riga + " " + parola).strip()
        if disegno.textlength(prova, font=font) <= larghezza or not riga:
            riga = prova
        else:
            righe.append(riga)
            riga = parola
    return righe + [riga]


def card(titolo, sottotitolo, foto, credito, destinazione):
    img = sfondo_foto(foto) if foto else gradiente()
    d = ImageDraw.Draw(img)
    larghezza = LARGO - 2 * MARGINE

    marchio = ImageFont.truetype(FONT_TITOLO, 26)
    d.rectangle((MARGINE, MARGINE + 4, MARGINE + 40, MARGINE + 9), fill=ORO)
    d.text((MARGINE + 56, MARGINE - 6), "CIVITELLA IN PILLOLE", font=marchio, fill=ORO)

    # Titolo: il più grande possibile entro due righe.
    for corpo in range(88, 47, -4):
        ft = ImageFont.truetype(FONT_TITOLO, corpo)
        righe = a_capo(titolo, ft, larghezza, d)
        if len(righe) <= 2:
            break
    fs = ImageFont.truetype(FONT_TESTO, 32)
    righe_sotto = a_capo(sottotitolo, fs, larghezza, d)[:2]
    interlinea = round(corpo * 1.08)
    y = ALTO - MARGINE - len(righe_sotto) * 42 - 26 - len(righe) * interlinea
    for r in righe:
        d.text((MARGINE, y), r, font=ft, fill=(255, 255, 255))
        y += interlinea
    y += 26
    for r in righe_sotto:
        d.text((MARGINE, y), r, font=fs, fill=(242, 226, 210))
        y += 42

    if credito:
        fc = ImageFont.truetype(FONT_TESTO, 18)
        w = d.textlength(credito, font=fc)
        d.text((LARGO - MARGINE - w, MARGINE - 2), credito, font=fc, fill=(235, 220, 205))
    img.save(destinazione, "JPEG", quality=84, optimize=True, progressive=True)


def leggi(contenuto, schema):
    m = re.search(schema, contenuto, re.S)
    return html.unescape(re.sub(r"\s+", " ", m.group(1)).strip()) if m else ""


def tag(pagina, nome, contenuto):
    url = SITO + ("" if pagina == "index.html" else pagina)
    titolo = leggi(contenuto, r"<title>(.*?)</title>")
    descrizione = leggi(contenuto, r'<meta name="description" content="(.*?)"')
    immagine = SITO + "assets/social/%s.jpg" % nome
    alt = "%s — Civitella in Pillole" % leggi(contenuto, r"<h1[^>]*>(.*?)</h1>").replace("<br>", " ") if pagina != "index.html" else "Civitella in Pillole"
    alt = re.sub(r"<[^>]+>", "", alt)
    e = lambda s: html.escape(s, quote=True)  # noqa: E731
    righe = [
        '<link rel="canonical" href="%s" />' % url,
        '<meta property="og:type" content="%s" />' % ("website" if pagina == "index.html" else "article"),
        '<meta property="og:site_name" content="Civitella in Pillole" />',
        '<meta property="og:locale" content="it_IT" />',
        '<meta property="og:url" content="%s" />' % url,
        '<meta property="og:title" content="%s" />' % e(titolo),
        '<meta property="og:description" content="%s" />' % e(descrizione),
        '<meta property="og:image" content="%s" />' % immagine,
        '<meta property="og:image:width" content="%d" />' % LARGO,
        '<meta property="og:image:height" content="%d" />' % ALTO,
        '<meta property="og:image:alt" content="%s" />' % e(alt),
        '<meta name="twitter:card" content="summary_large_image" />',
    ]
    return "    <!-- anteprima social: generata da tools/genera_anteprime.py -->\n" + "".join(
        "    %s\n" % r for r in righe) + "    <!-- /anteprima social -->\n"


def main():
    os.makedirs(os.path.join(RADICE, "assets", "social"), exist_ok=True)
    for pagina, nome, titolo, sottotitolo, foto, credito in PAGINE:
        percorso = os.path.join(RADICE, pagina)
        contenuto = open(percorso, encoding="utf-8").read()
        card(titolo, sottotitolo, foto, credito, os.path.join(RADICE, "assets", "social", nome + ".jpg"))
        contenuto = re.sub(r"    <!-- anteprima social.*?<!-- /anteprima social -->\n", "", contenuto, flags=re.S)
        m = re.search(r'    <meta name="description"[^\n]*\n', contenuto)
        if not m:
            raise SystemExit("manca <meta name=\"description\"> in " + pagina)
        contenuto = contenuto[:m.end()] + tag(pagina, nome, contenuto) + contenuto[m.end():]
        open(percorso, "w", encoding="utf-8").write(contenuto)
    print("%d anteprime generate in assets/social/." % len(PAGINE))


if __name__ == "__main__":
    main()
