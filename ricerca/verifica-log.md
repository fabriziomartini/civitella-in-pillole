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
Parrocchie ufficiali (annuario 2022):
| Località | Titolo |
|---|---|
| Badia al Pino | San Bartolomeo |
| Ciggiano | San Biagio |
| Civitella | Santa Maria Assunta |
| Oliveto | Sant'Andrea Apostolo |
| Pieve a Maiano | Santa Maria Assunta |
| Pieve al Toppo | San Giovanni Battista |
| Spoiano | San Giovanni Battista |
| Tegoleto | San Biagio |
| Tuori | Santi Giorgio e Luca |
| Viciomaggio | San Martino |

Albergo, Cornia (San Michele Arcangelo è chiesa, non parrocchia autonoma), Matroia e Gebbia non hanno una parrocchia propria. La parrocchia di Ponticino (Santi Iacopo e Cristoforo) è nel comune di Laterina Pergine Valdarno.

- **Tuori:** torno a **Santi Giorgio e Luca**, il titolo ufficiale della Diocesi. "Lucia" (itinerario del Comune) resta come variante nella nota.
- **Tegoleto:** San Biagio confermato (3° itinerario): già esistente nel X secolo, ristrutturata nel XII, oggi restano i resti dell'abside. Anche Ciggiano ha una sua San Biagio, ma è un'altra chiesa.
- **Albergo:** il 3° itinerario dice "antico borgo, probabilmente di origine romana. Nel nucleo sorgeva un ospedale per viandanti e malati". Aggiunto, e precisato che non c'è una parrocchia.
- **Cornia:** tolte le scope di saggina; Vallebuona diventa "complesso religioso", perché il titolo di Santa Maria Maddalena non ha riscontro.
- **Ponticino:** precisato dove ha sede la parrocchia.
- **Criterio adottato:** le descrizioni architettoniche non trovate (torre colombaria di Villa Pecchioli, Cassero e torrione di Oliveto, ponte romanico di Ponticino) restano **in sospeso**. Potrebbero venire dalle schede edifici del Piano Strutturale, non caricate: da verificare con il secondo notebook.

## Prompt 6: dettagli rimanenti
- **Altitudine del capoluogo:** Wikipedia e ToscanaNovecento dicono **500 m** ("Colline delle Lepri"), non 525. Corretti index (anche il riquadro dei numeri), geografia e civitella.
- **Pianura:** la fonte indica una fascia di 250–350 m, non 250–270. Corretto.
- **Vino:** è **Chianti Colli Aretini**. Tolto anche "tra le colline del Chianti" dalla home: Civitella non è nel Chianti.
- **Cornia:** le **scope di saggina sono confermate** (1° itinerario), quindi le ho rimesse: al giro 5 le avevo tolte per errore. Confermati 560 m e cippo del 1969. Il "CAI 113" non è nelle fonti (le fonti citano il 105, vicino a Poggio Castellare): tolto il numero.
- **Spoiano:** confermati origine romana ed edifici accorpati nel Settecento; il Comune la mette tra i nuclei di piano. Tolta la cisterna, che nelle fonti è nella piazza del capoluogo, non a Spoiano.
- **Viciomaggio:** confermati Malpertuso, Le Fosse (abbandonati nel tardo Medioevo) e Tribbio (dal trivio romano). Arricchito il testo.
- **Pieve al Toppo:** confermata l'origine longobarda di "Toppo"; tolto l'altorilievo di don Fortunato Bardelli.
- **Civitella:** confermati i bombardamenti alleati sulla rocca e il Palazzo Pretorio trecentesco con gli stemmi dei podestà (aggiunti).
- **Gebbia:** confermati la divisione "Hermann Göring", Heinz Barz e l'uccisione dei Cau. La biografia dei Cau si appoggia a Liber Liber, già in Fonti: resta.
- **In sospeso:** Matroia (nessuna fonte nel notebook, serve il Piano Strutturale); Ponticino (Tabula Peutingeriana, stazione 1866, divisione tra tre comuni, referendum 2017); Marcia per la pace.

## Prompt 7: vita locale e Novecento recente
- **Confermati:**
  - Villa Oliveto: Barbolani di Montauto, aspetto ottocentesco, parco con cedri e lecci, Centro di documentazione.
  - Tegoleto: Giro d'Italia del 12 maggio 2004, vinto da Petacchi davanti a Del Tongo.
  - La Marcia per la pace va da Civitella a San Pancrazio, con il comune di Bucine (corretto storia.html).
  - Muriel Spark: sepolta nel cimitero comunale.
- **Tolti:**
  - Tuori, "11% di origine albanese": il dato ISTAT esiste solo per l'intero comune, quindi era attribuito alla frazione sbagliata.
  - Oliveto, l'opera di Enzo Scatragli.
- **In sospeso, servono fonti di cronaca o Pro Loco (notebook 3):**
  - le sagre (Crostino, Bistecca, Cinghiale, Baccelli), la Fiera del Miele e il mercato del venerdì;
  - la Festa Sportiva Tegoleto, il TMT, il Presepe Vivente di Oliveto;
  - il libro di Renzetti su Spoiano;
  - per Muriel Spark: Penelope Jardine, la cittadinanza onoraria 2005, il circolo di lettura 2023, la mostra 2024.
- **In sospeso, serve il Piano Strutturale (notebook 2):**
  - Pieve a Maiano: fornace di Vallimboi, ceramiche romane, Casa al Cincio;
  - Oliveto: Cappella della Compagnia, San Rocco ottocentesco, Cassero e torrione;
  - Spoiano: torre colombaria di Villa Pecchioli;
  - Ponticino: ponte romanico;
  - tutta la pagina di Matroia;
  - Cornia: Parco faunistico e ANPIL.
- **In sospeso, serve l'ISTAT:** la popolazione delle frazioni.

---

# Notebook 2: Piano Strutturale (Norme Tecniche e Repertorio dei beni storici)

- **Matroia:**
  - Confermato l'allevamento di cavalli (NTA art. 49). L'ambito è "fondovalle, pianura e lungo la Via Vecchia Senese": quindi **non** è un nucleo collinare, e il "272 m" non ha fonte.
  - Il Repertorio vi censisce i resti di un convento con chiesetta di San Michele Arcangelo e una sorgente medicamentosa. La pagina diceva invece "nessuna struttura religiosa".
  - Tolti terrazzamenti, Chianti, esodo, "trenta abitanti" e impianto medievale: la pagina è stata riscritta.
- **Pieve a Maiano:** confermate la fornace di Vallimboi e le ceramiche del I–II secolo; tolta Casa al Cincio. Aggiunti gli altri ritrovamenti: scultura marmorea, fornace agli Ortali, moneta d'oro di Claudio.
- **Oliveto:**
  - Confermati il cassero (oggi abitazione), la porta e le mura, la Cappella della Compagnia (1637) e San Rocco (tabernacolo diventato cappella nel XIX secolo). Il "torrione presso la Porta Nord" non è nelle fonti.
  - Aggiunta la Casa del Podestà.
- **Spoiano:**
  - Confermata Villa Pecchioli, settecentesca, con torre piccionaia.
  - Il **portale ad arco policentrico appartiene al Saracino di Tuori**: era attribuito al luogo sbagliato, tolto.
  - Aggiunto il tesoretto monetale romano. Tolta la "chiesetta ad aula unica" (doppione della chiesa di Spoiano).
- **Ponticino:** il ponte romanico non è nelle fonti; l'unico bene censito è il Mulino di Ponticino. Sostituito.
- **Cornia:** il Parco faunistico e l'ANPIL sono confermati (NTA artt. 23 e 53).
- **Recuperati grazie al Repertorio** (erano stati tolti perché il notebook 1 non li trovava):
  - la Fattoria di Tegoleto;
  - **Villa Milloni** a Viciomaggio (con due "l"), con la sua cappella. Senza i dettagli non verificati del Fondaccio e dell'orologio.
- **Aggiunti:** il Cippo delle Giostre del Toppo (Pieve al Toppo) e la fonte-cisterna di Albergo.
- **Confermati anche:** il TMT di Tegoleto, il Cassero di Tuori, il Saracino (casa colonica del XVI secolo), i resti del castello di Badia al Pino.
- Esiste un **Oratorio della Madonna della Costarella nel capoluogo**: conferma che la "Santa Maria della Costarella" di Ciggiano era un'attribuzione sbagliata.

---

# Verifica diretta su fonti di cronaca (ricerca web, senza notebook)

- **Ponticino, errore grave:**
  - Fino al 2017 era diviso tra **Civitella, Laterina e Pergine Valdarno**, non tra Civitella, Laterina e **Bucine**. Dal 2018 è diviso tra due comuni: Civitella e Laterina Pergine Valdarno.
  - "Da quattro a tre comuni" era sbagliato, e la spiegazione storica con la Valdambra e Bucine era inventata. Riscritta la sezione: referendum del 29–30 ottobre 2017, 53,73% di sì, decisivo il voto di Ponticino.
  - Confermata la stazione del 1866 (Wikipedia). Tolti la Tabula Peutingeriana, lo scalo merci e lo "strada-paese".
- **Sagre:**
  - Confermate Crostino (Albergo, luglio), Bistecca (Badia al Pino, fine agosto–inizio settembre), Cinghiale (Pieve a Maiano, fine agosto).
  - Baccelli: non "l'ultima domenica di maggio", ma due fine settimana di maggio; nata nel 1975.
- **Tegoleto:** si chiama "Festa al Tegoleto" ed è organizzata dall'USD Tegoleto. Tolta la "52ª edizione nel 2026", non confermata (un articolo cita la 47ª). Tolti anche il badge "corte dell'anno 1000" e i "265 m".
- **Pieve al Toppo:** Fiera del Miele confermata (prima domenica di ottobre, con Slow Food Valdichiana). Il **mercato del venerdì** non ha riscontro ed è stato tolto.
- **Oliveto:** Presepe Vivente confermato (dal 2014, oltre 80 figuranti, Natività a San Rocco).
- **Spoiano:** il libro di Renzetti è confermato; "fine 2025" è sostituito da "uscito di recente".
- **Muriel Spark:** confermati Penelope Jardine, la morte a Oliveto nel 2006, la sepoltura nel cimitero di Sant'Andrea Apostolo, la cittadinanza onoraria (settembre 2005), il circolo di lettura e la mostra.
- **Ancora in sospeso:** la popolazione delle frazioni (ISTAT).

## Popolazione delle frazioni
- Gli aggregatori danno cifre in conflitto con il sito: Spoiano 112 (il sito diceva 31), Pieve al Toppo 1.635 (il sito diceva 1.531), Matroia 25. Nessuna di queste viene da una fonte primaria.
- Tolti i numeri di Spoiano (31, anche nel sottotitolo) e di Viciomaggio (905). Resta Tuori (120-130), coerente con il dato di 129 abitanti nel 2021 (Wikipedia EN).
- Resta solo il dato ufficiale di Ciggiano (scheda del Comune). Per reintegrare gli altri serve la tabella ISTAT "Popolazione per località abitata" (censimento 2011 o 2021).

---

# Notebook 2: estrazione per arricchire le pagine

## Gruppo 1: Oliveto, Ciggiano, Tuori
- **Oliveto:**
  - Castello attestato nel XII secolo, con origini tardo-imperiali e longobarde; feudo degli Ubertini e dei Saracini; Casa del Podestà riedificata nel Seicento.
  - Aggiunti: casa trecentesca (vincolo nazionale), ex scuola del 1896, Castellare di San Giovanni d'Oliveto con il progetto di parco archeologico, mulino dell'Infernaccio, descrizione del Centro di Documentazione.
  - Da chiarire: il repertorio collega la "cappella ad aula del 1637" a San Giovanni / San Salvatore; sul sito resta "Cappella della Compagnia".
- **Ciggiano:**
  - Storia riscritta dal repertorio: vicus romano, castello con pieve nell'XI secolo, date 1250, 1307, 1381, 1385, 1431, 1554 e 1774, la dogana e la "calla" dei pastori.
  - Aggiunti: le mura e le torri, i siti archeologici (ceramica romana nelle mura, La Cascinella), la Compagnia di Santa Croce, gli oratori di Caggiolo e San Francesco, il frantoio e il mulino.
- **Tuori:**
  - Corretta l'origine: è attestato dal **1021**, non "XIV secolo". Centro storico con vincolo nazionale.
  - Aggiunti il portale ad arco policentrico del Saracino (il suo posto giusto) e la ciclabile dei borghi pedecollinari.

---

# Popolazione: censimento ISTAT 2021 per località (file della Regione Toscana)
| Località | Tipo | Residenti |
|---|---|---|
| Pieve al Toppo | centro | 1.545 |
| Tegoleto | centro | 1.412 |
| Badia al Pino | centro | 1.059 |
| Viciomaggio | centro | 950 |
| Ciggiano | centro | 530 |
| Albergo | centro | 279 |
| Pieve a Maiano | centro | 242 |
| Civitella (borgo) | centro | 148 |
| Tuori | centro | 129 |
| Spoiano | nucleo | 120 |
| Matroia | nucleo | 23 |
| Oliveto | centro | 15 |
| Casali, Le Poggiole, Malpertuso, Poggio Basso, area produttiva | — | 106 |
| Case sparse | — | 2.256 |
| **Totale comune** | | **8.814** |

- Cornia e Gebbia non sono località censite. Ponticino ("Ponticino-Cavi Casalone", 1.997 residenti) è attribuito a Laterina Pergine Valdarno.
- Pieve al Toppo **è** il centro più popoloso: l'affermazione torna, ora con la fonte.
- Il "70% nei centri di pianura" non trova conferma: i quattro centri maggiori fanno il 56%. Sostituito con il dato ISTAT.
- I vecchi numeri sul sito erano sbagliati: Spoiano 120 (non 31), Pieve al Toppo 1.545 (non 1.531), Viciomaggio 950 (non 905). Home: 8.814 abitanti al posto di "circa 9.000".

## Gruppo 2: Civitella, Badia al Pino, Tegoleto
- **Storia:**
  - Tolto il legame "distruzione del XIII secolo – Dante": non ha fonte, perché Dante cita Pieve al Toppo, non Civitella.
  - Sostituito con la storia della rocca dal repertorio: palazzo-torre nel 1182, dimora del vescovo Guglielmino degli Ubertini nel 1248, assedio aretino 1284–85.
- **Civitella:**
  - Aggiunti la descrizione della Rocca (Palatium-torre e cisterna), Palazzo Becattini (ospedale dal 1877, del Comune dal 1978), gli oratori (Santissima Trinità, Mercatale, Costarella), la cisterna, la Pinacoteca.
  - Aggiunti i luoghi della memoria: Stanza della Memoria (2004) e Cappella dei Martiri; e i progetti del Piano (Rocca museo, Percorso della Memoria).
- **Badia al Pino:** aggiunti Palazzo Santini-Paccinelli (il notebook lo attribuiva anche a Civitella, ma la scheda lo colloca in Via Roma/Via Europa a Badia), Villa del Bosco, il monumento ai caduti del 1951, le case coloniche storiche.
- **Tegoleto:** la torre fu ricostruita dai fiorentini a fine Trecento; la Fattoria è dell'Ordine di Santo Stefano dal 1783 (non "seicentesca", come diceva il sito prima); aggiunta la storia del TMT.

## Gruppo 3: Pieve a Maiano, Pieve al Toppo, Viciomaggio
- **Pieve a Maiano:**
  - "Maiano" è un toponimo prediale romano (da *Marius*).
  - Aggiunti: il sito paleolitico di Podere Casella, l'insediamento romano al campo sportivo, la fornace di Vallimboi descritta, l'aureo di Claudio, la Fattoria di Maiano, il tabernacolo dell'antica pieve, la "porta" della Riserva di Ponte a Buriano e Penna.
- **Pieve al Toppo:** la parrocchiale è moderna (progetto 1967, porticato 1977); aggiunte le fornaci di terra sigillata aretina de I Ponti e i progetti del Piano (piazza, cintura verde).
- **Viciomaggio:**
  - Villa Milloni descritta per intero: XVIII secolo, restauro 1868, limonaia 1836, cappella secentesca **con orologio e campanile a vela**. Quindi l'"orologio sul fianco sud" che avevo tolto era corretto: era sulla cappella. Il "Fondaccio" resta non verificato e non è stato rimesso.
  - Aggiunti la Villa di Viciomaggio, l'urna etrusca iscritta (1872), i vasi del I secolo a.C., il monile al Museo Mecenate e il rifugio della Seconda guerra mondiale lungo il Fosso del Riolo.
- **Ancora non verificato:** la leggenda di Annibale a Viciomaggio, presentata sul sito come leggenda.
