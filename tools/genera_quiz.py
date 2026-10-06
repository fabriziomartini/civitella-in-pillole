"""Genera js/quiz-data.js e ricerca/quiz-domande.md da tools/quiz_domande.py.

Uso, dalla radice del repository:  python3 tools/genera_quiz.py

Ogni domanda riceve un id stabile (le prime 8 cifre dell'MD5 del testo della domanda):
le statistiche del foglio Google restano legate alla domanda anche se cambia l'ordine del pool.
Se si riformula una domanda cambia anche il suo id, e le sue statistiche ripartono da zero.
"""
import collections
import hashlib
import json
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "tools"))
from quiz_domande import Q  # noqa: E402

NOMI = {
    "geo": "Geografia", "storia": "Storia", "1944": "Il 1944", "frazioni": "Frazioni",
    "borghi": "Borghi minori", "economia": "Lavoro e sapori", "feste": "Feste e sport",
}


def ident(domanda):
    return hashlib.md5(domanda.encode("utf-8")).hexdigest()[:8]


def controlla():
    errori, visti = [], set()
    for c, d, ok, no, sp, ln in Q:
        if c not in NOMI:
            errori.append("categoria sconosciuta: " + c)
        if d in visti:
            errori.append("domanda doppia: " + d)
        visti.add(d)
        if len(no) != 3 or len({ok, *no}) != 4:
            errori.append("servono 4 risposte diverse: " + d)
        pagina, _, ancora = ln.partition("#")
        percorso = os.path.join(RADICE, pagina)
        if not os.path.exists(percorso):
            errori.append("pagina inesistente: " + ln)
        elif ancora and 'id="%s"' % ancora not in open(percorso, encoding="utf-8").read():
            errori.append("ancora inesistente: " + ln)
    ids = [ident(d) for _, d, *_ in Q]
    if len(set(ids)) != len(ids):
        errori.append("collisione tra id")
    return errori


def main():
    errori = controlla()
    if errori:
        sys.exit("\n".join(errori))

    dati = [{"id": ident(d), "c": c, "q": d, "a": ok, "x": no, "s": sp, "l": ln} for c, d, ok, no, sp, ln in Q]
    with open(os.path.join(RADICE, "js", "quiz-data.js"), "w", encoding="utf-8") as f:
        f.write("// Domande del quiz: file GENERATO da tools/genera_quiz.py, non modificarlo a mano.\n")
        f.write("// Fonte: tools/quiz_domande.py (solo fatti di livello R, N, W in ricerca/fatti-verificati.md).\n")
        f.write("// Campi: id stabile, c categoria, q domanda, a risposta corretta, x sbagliate, s spiegazione, l pagina.\n")
        f.write("window.QUIZ_DOMANDE = " + json.dumps(dati, ensure_ascii=False, indent=0) + ";\n")

    righe = [
        "# Domande del quiz\n\n",
        "Elenco leggibile del pool usato da `quiz.html`. **Non modificarlo a mano:** le domande si cambiano in "
        "`tools/quiz_domande.py`, poi si lancia `python3 tools/genera_quiz.py`, che rigenera questo file e `js/quiz-data.js`.\n\n",
        "**Regola:** ogni domanda nasce da un fatto di livello R, N o W in `fatti-verificati.md`, mai da un fatto su cui le fonti divergono.\n\n",
        "L'**id** tra parentesi quadre è quello che compare nel foglio delle statistiche.\n\n",
        "Totale: %d domande.\n" % len(Q),
    ]
    per_cat = collections.OrderedDict((k, []) for k in NOMI)
    for voce in Q:
        per_cat[voce[0]].append(voce)
    for k, voci in per_cat.items():
        righe.append("\n## %s (%d)\n\n" % (NOMI[k], len(voci)))
        for i, (c, d, ok, no, sp, ln) in enumerate(voci, 1):
            righe.append("%d. [%s] **%s**  \n   ✔ %s · ✘ %s  \n   _%s_ → `%s`\n" % (i, ident(d), d, ok, " · ".join(no), sp, ln))
    with open(os.path.join(RADICE, "ricerca", "quiz-domande.md"), "w", encoding="utf-8") as f:
        f.write("".join(righe))
    print("%d domande generate." % len(Q))


if __name__ == "__main__":
    main()
