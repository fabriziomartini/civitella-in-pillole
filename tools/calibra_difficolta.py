"""Aggiorna i livelli di difficoltà del quiz con le risposte reali dei giocatori.

Uso, dalla radice del repository:
  1. nel foglio Google delle statistiche apri la scheda «Risposte» e scegli
     File → Scarica → Valori separati da virgola (.csv);
  2. python3 tools/calibra_difficolta.py percorso/del/file.csv
  3. python3 tools/genera_quiz.py

Per ogni domanda con almeno MINIMO risposte:
  - più del 75% di risposte giuste → facile;
  - meno del 40% → difficile;
  - altrimenti → media.
Il risultato va nel dizionario DATI di tools/quiz_difficolta.py e prevale sul codice della regola.
Le domande con meno risposte restano con il livello calcolato dal codice.
"""
import collections
import csv
import os
import re
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE = os.path.join(RADICE, "tools", "quiz_difficolta.py")
MINIMO = 20


def main():
    if len(sys.argv) != 2:
        sys.exit("Uso: python3 tools/calibra_difficolta.py Risposte.csv")
    risposte = collections.defaultdict(list)
    with open(sys.argv[1], encoding="utf-8") as f:
        for riga in csv.DictReader(f):
            esito = (riga.get("Giusta (1/0)") or "").strip()
            if re.fullmatch(r"[0-9a-f]{8}", (riga.get("Id") or "").strip()) and esito in ("0", "1"):
                risposte[riga["Id"].strip()].append(int(esito))

    dati = {}
    for i, esiti in sorted(risposte.items()):
        if len(esiti) >= MINIMO:
            quota = sum(esiti) / len(esiti)
            dati[i] = 1 if quota > 0.75 else 3 if quota < 0.40 else 2

    sys.path.insert(0, os.path.join(RADICE, "tools"))
    from quiz_difficolta import CODICI, livello  # noqa: E402
    dati = {i: v for i, v in dati.items() if i in CODICI}  # domande tolte o riformulate: si ignorano
    cambiate = sum(1 for i, v in dati.items() if v != livello(CODICI[i]))

    testo = open(FILE, encoding="utf-8").read()
    blocco = "DATI = {\n" + "".join('    "%s": %d,\n' % (i, v) for i, v in sorted(dati.items())) + "}\n"
    testo = re.sub(r"DATI = \{.*?\}\n", lambda m: blocco, testo, count=1, flags=re.S)
    open(FILE, "w", encoding="utf-8").write(testo)
    print("%d domande con almeno %d risposte; %d cambiano livello rispetto alla regola." % (len(dati), MINIMO, cambiate))


if __name__ == "__main__":
    main()
