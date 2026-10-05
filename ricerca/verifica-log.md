# Registro della verifica con NotebookLM

Notebook "Civitella – verifica fonti", con i blocchi A–D di `fonti-notebooklm.md` e 42 fonti caricate.

## Prompt 0: inventario delle fonti
- Da eliminare: n. 4 "Chiese parrocchiali – Diocesi" (vuota), n. 32 "Giostre del Toppo" (duplicato),
  n. 36 "Storia Militare Medievale" (fuori tema).
- Peso basso: n. 5 Discover Arezzo, n. 34 ToscanaNovecento e le voci Wikipedia servono solo come conferma.
- Fonti non importate da reintegrare con "Testo copiato" in un secondo momento: Treccani "Pieve al Toppo",
  le schede CEI (San Biagio a Ciggiano, Santa Maria Assunta a Civitella), il Catalogo Beni Culturali
  (Parchi della Rimembranza di Tuori e Ciggiano), SIUSA (Comunità di Viciomaggio e di Badia al Pino).
- Fonti nuove emerse: 1° e 3° itinerario (nuclei di collina e di piano, con il 3° che comprende
  Albergo), le schede del Comune su Cornia, Oliveto, Badia al Pino, Castello di Gaenne, Montarfoni e
  Percorso Rosa, la scheda SIUSA della Podesteria di Civitella (1385–1838).
- Da notare: la scheda SIUSA data la Podesteria di Civitella al **1385**, il sito dice **1348**
  (storia.html, pieve-al-toppo.html). Da verificare nel prompt 4.

## Prompt 2: errori sospetti
- **Chiese Santa Maria (1635) e San Pietro (1836):** sono di **Ciggiano** secondo Discover Arezzo. La rimozione da Albergo è confermata.
  - Su Ciggiano ho tolto "(o della Costarella)", "presso Villa Cardinali", la data alternativa 1863 e l'altare Mazzeschi: nessuno di questi è nelle fonti.
- **Ciggiano, popolazione:** la scheda del Comune riporta 359 m, 634 abitanti (1833), 508 (2001), 610 (2011). Aggiunto.
- **Vittime del 1944:** ToscanaNovecento dà 244 (115+58+71); l'Atlante dà 146 (Civitella+Cornia+Gebbia) + 58 (San Pancrazio) = 204.
  - storia.html e civitella.html ora riportano entrambe le cifre.
  - Da chiarire: il numero 58 compare per Cornia in una fonte e per San Pancrazio nell'altra; Gebbia ha 16 vittime secondo "altre fonti"?
- **Montoto:** sta lungo Via della Centrale, vicino a Pieve a Maiano. "VII-VIII secolo" e la chiesa di San Giovanni Battista e San Martino non sono nelle fonti: tolto il punto "Antico guado di Montoto" da Ponticino.
- **Popolazione delle altre frazioni:** il dato ufficiale c'è solo per Ciggiano. Il Comune dice che il 70% vive a Badia al Pino, Pieve al Toppo, Tegoleto e Viciomaggio.
  - Corretti geografia.html (prima citava Ciggiano, che è in collina) e albergo.html (Albergo non è tra quei centri).
  - I numeri di Pieve al Toppo (1.531), Viciomaggio (905), Spoiano (31), Matroia (~30) e Tuori (120-130) **restano da verificare** con l'ISTAT, per località al censimento 2011.

## Prompt 3: Ciggiano, Cornia, Gebbia
- **Ciggiano:**
  - Confermati: borgo fortificato nell'XI secolo, antiche fortificazioni, pieve nel 1465, Maddalena attribuita al Sansovino. Confermato anche l'**altare Mazzeschi** (1° itinerario), che ho rimesso.
  - Tolti perché non presenti nelle fonti: la leggenda di Noè, il cippo romano di località La Villa, la Festa dell'uva del 1952 con il carro a razzo. Si possono reintegrare se si trova una fonte.
  - Aggiunti: la fucilazione dei partigiani Marmo e Marapitti (16 aprile 1944) e il monumento ai caduti (ToscanaNovecento).
- **Cornia:** la lapide con 58 nomi comprende anche le frazioni vicine e San Pancrazio, fra il 29 giugno e il 16 luglio; l'Atlante elenca 32 vittime per "Cornia e dintorni". Hazbi Ismail è un partigiano di 28 anni; "albanese" non è nelle fonti ed è stato tolto.
- **Gebbia:**
  - L'Atlante elenca 16 nomi, l'Archivio parla di 8 uomini fucilati. La nota "4 vittime" era sbagliata.
  - Corretti "Arrigucci Odorlindo" in Orlindo e tolto "Arrigucci Dante (49)", che non risulta tra le vittime di Gebbia.
  - Corretto il racconto: le case non furono bruciate, gli animali furono uccisi.
- Da verificare più avanti: la divisione "Hermann Göring", il capitano Heinz Barz, la biografia dei Cau, il cippo di Cornia del 1969, le scope di saggina, il sentiero CAI 113, Vallebuona.

## Prompt 4: affermazioni puntuali
- **Civitella/Storia:**
  - Tolti "Civitella del Vescovo", la ricostruzione del 1272 e la podesteria del 1348: non sono nelle fonti.
  - Corretto con la **podesteria del 1385** (scheda SIUSA, fino al 1838) e aggiunto il castello del 1048 (Wikipedia).
- **Badia al Pino:**
  - Tolti il feudo di Giovanni Acuto (1384) e "Corso Italia".
  - Restano 1441/1446 e la dedica a Martino e Lorenzo. Il notebook li segna come "contraddetti", ma la voce Wikipedia sulla chiesa di San Bartolomeo li conferma: quel titolo si è aggiunto nel Cinquecento.
- **Oliveto:**
  - Tolti il 1318 con Guido Tarlati, le mura rinforzate dopo il 1384 e l'autonomia fino al 1774. Rimangono le mura del XIV secolo.
  - Muriel Spark a Oliveto resta: la fonte dice "cimitero comunale" e non lo contraddice.
- **Pieve al Toppo:**
  - La pieve e l'ospedale risultano documentati dal 938 e distrutti "intorno al 1500" (non nel 1502).
  - Oratorio della Madonna del Conforto: confermato solo il 1906.
  - Mugliano ridotto a "fattoria" senza l'origine romana. Tolti 1311/1348 e l'unione con Sant'Andrea di Oliveto.
- **Viciomaggio:** tolta Villa Milioni; il resto è confermato.
- **Tuori:** la chiesa diventa **Santi Giorgio e Lucia** (itinerario del Comune, e anche il file su Commons). Il Cassero e il presidio aretino non sono nelle fonti del notebook, ma vengono da ruderimedievali.altervista.org, che è in Fonti: per ora restano.
- **Tegoleto:** tolti la "corte dell'anno 1000" e la Fattoria seicentesca. La chiesa di San Biagio del X secolo è dubbia: il notebook l'ha confusa con Ciggiano. Da verificare con l'annuario della Diocesi.
- **"Frazione più popolosa":** la rivendicavano Tegoleto, Badia al Pino e Pieve al Toppo insieme. Tolto da tutte e tre, insieme al numero 1.531.

## Prompt 5: parrocchie (annuario della Diocesi)
_in attesa_
