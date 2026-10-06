# Revisione frase per frase del sito

Ogni prompt contiene **tutte** le frasi di una pagina del sito, numerate ed estratte automaticamente dall'HTML. Le pagine lunghe sono divise in più parti, di 35 frasi al massimo.

## Cosa c'è in ciascun notebook

Ricostruito dai registri di questa ricerca. Prima di iniziare conviene confermarlo con il prompt di inventario qui sotto.

| Notebook | Contenuto | Serve per |
|---|---|---|
| **N1** "Civitella – verifica fonti" (42 fonti, blocchi A–D di `fonti-notebooklm.md`) | Schede «Luoghi» e itinerari del Comune; vecchio portale Halleyweb; annuario delle parrocchie della Diocesi; SIUSA; Archivio della Memoria; Atlante delle stragi; ToscanaNovecento; Villa Oliveto (Regione, Storia e Memorie); Discover Arezzo; Wikipedia (Civitella, Badia al Pino, Villa Oliveto) | Frazioni, Borghi, Storia, Patrimonio, Home |
| **N2** Piano Strutturale | Solo **Norme Tecniche di Attuazione** e **Repertorio dei beni storici** | Non serve più: gli stessi due PDF sono anche in N3 |
| **N3** economia e feste | Cittaslow; CEIA, Chimet, Del Tongo e Kico; Slow Food, Città dell'Olio, Strada del Vino; sagre e feste (Sagre Toscane, Arezzo Notizie, La Nazione, Arezzo24); RioFest; sport; elenco RUNTS e lettera della Consulta dello Sport; PDF del Piano (**NTA**, **Repertorio**, **C1.1 Relazione generale**, tav. C4.4, B8.6.6, B8.1.4b, relazione del Piano Operativo); Wikipedia (Civitella, squadra Del Tongo) | Geografia, Lavoro e sapori, Feste e associazioni; seconda passata per tutte le altre pagine |

**Prompt di inventario** (lancialo in N1 e in N3 e incollami le due risposte):
```
Elenca tutte le fonti di questo notebook, una per riga, con il titolo esatto e il tipo (sito web, PDF, testo copiato). Indica anche il numero totale.
```

## Come procedere
1. **Pagine di frazioni, Borghi, Storia, Patrimonio, Home, Amministrazione:** lancia il prompt prima in **N1**. Poi incollami la risposta: per le frasi NON PRESENTE o PARZIALE ti preparo un secondo prompt, breve e mirato, da lanciare in **N3**, che ha il Piano Strutturale e la Relazione generale.
2. **Pagine di Geografia, Lavoro e sapori, Feste e associazioni:** lancia il prompt direttamente in **N3**.
3. **Regola finale:** una frase resta sul sito solo se almeno una fonte la conferma alla lettera. Le altre vengono riscritte o tolte, e ogni decisione viene annotata nel registro.

**Casi particolari:**
- **Le righe "Residenti" sono escluse:** vengono dal CSV del censimento ISTAT 2021, già verificato a parte.
- **Amministrazione:** le schede del sindaco e degli assessori sul sito del Comune probabilmente non sono in nessun notebook. Se N1 risponde NON PRESENTE quasi ovunque, conviene aggiungerle a N1 come "Sito web" prima di ripetere il prompt.
- **Feste nelle pagine delle frazioni:** le frasi su sagre e feste sono già state verificate nel notebook 3. Se N1 le dà NON PRESENTE è normale, e la seconda passata in N3 le copre.

**Ordine consigliato:** le frazioni una alla volta, poi Borghi, Storia, Patrimonio, Geografia, Lavoro e sapori, Feste, Home, Amministrazione.

---

## Civitella (capoluogo) (`frazioni/civitella.html`): prima N1, poi seconda passata in N3 · 27 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Civitella (capoluogo)». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Il borgo collinare che dà il nome al comune, a circa 500 metri di altezza.
2. Altitudine: circa 500 m
3. Parrocchia: Santa Maria Assunta
4. Castello: 1048
5. Civitella è il borgo storico che dà il nome al comune, arroccato su un colle tra Valdambra e Valdichiana.
6. Sorge su un insediamento etrusco-romano; in epoca longobarda la sua altura era già un forte a controllo del territorio.
7. Il castello fu eretto nel 1048 e dall'XI secolo fu un presidio dei vescovi-conti di Arezzo: nel 1182 aveva l'aspetto di un palazzo-torre, e nel 1248 il vescovo Guglielmino degli Ubertini lo scelse come dimora, potenziandone le mura.
8. Nel 1385 Firenze, acquisiti Arezzo e il suo contado, fece di Civitella il capoluogo di una propria podesteria, che durò fino al 1838.
9. Pur dando il nome al comune, oggi Civitella non ne è la sede: gli uffici si trovano dal 1917 a Badia al Pino, nella pianura sottostante.
10. La Rocca: sulla più alta delle due sommità del colle si conserva il Palatium-torre, formato dalla torre vera e propria e dal recinto d'accesso con la cisterna per l'acqua.
11. Fu distrutta da un bombardamento alleato nel 1944.
12. Il Piano Strutturale ne prevede il restauro come museo dei castelli e dei borghi del territorio.
13. Chiesa di Santa Maria Assunta: eretta come priorato benedettino nell'XI secolo e completata in stile romanico nel 1252.
14. In facciata si apre la porta in bronzo dello scultore fiorentino Bino Bini.
15. Palazzo Pretorio: trecentesco, con un portico a cinque archi e gli stemmi dei podestà fiorentini in facciata.
16. Palazzo Becattini: nato dalla fusione di edifici medievali e trasformato nell'Ottocento; il notaio Becattini, morto nel 1877, lo lasciò alla Confraternita di Carità perché diventasse un ospedale per i poveri.
17. Dal 1978 è del Comune.
18. Oratori della Santissima Trinità, della Madonna di Mercatale e della Madonna della Costarella; la cisterna medievale di Piazza Lazzeri e la Pinacoteca d'arte contemporanea.
19. Il 29 giugno 1944, giorno di San Pietro e Paolo, reparti tedeschi uccisero 115 civili nel solo paese di Civitella, nell'ambito di una rappresaglia che colpì anche Cornia, Gebbia e San Pancrazio di Bucine.
20. Il totale delle vittime varia secondo le fonti: 244 nel bilancio più citato, 204 secondo le schede dell'Atlante delle stragi naziste e fasciste.
21. La Stanza della Memoria, inaugurata nel 2004 per il sessantesimo anniversario, raccoglie reperti rinvenuti sulle vittime, fotografie del paese prima e dopo la distruzione, documenti, testimonianze e atti giudiziari.
22. Ci sono poi la Cappella dei Martiri e la lapide sul luogo dell'eccidio.
23. In occasione della ricorrenza si tiene la Marcia per la pace da Civitella a San Pancrazio, organizzata insieme al comune di Bucine.
24. Il borgo è il cuore delle iniziative del Comune e di Slow Food Valdichiana, che ha sede proprio a Civitella.
25. A maggio piazza Lazzeri ospita il Mercato del Cacio, arrivato nel 2025 alla 22ª edizione, con gli ospiti del comune gemellato di Kämpfelbach, in Germania.
26. Ad agosto, tra le vie del borgo, Calici sotto la Torre propone i vini della Strada del Vino Terre di Arezzo.
27. Nel paese ha sede anche la Pro Loco.
```

---

## Albergo (`frazioni/albergo.html`): prima N1, poi seconda passata in N3 · 14 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Albergo». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Un centro della pianura, servito dalla ferrovia Arezzo–Sinalunga.
2. Origine: Probabilmente romana
3. Parrocchia: Nessuna propria
4. Ferrovia: Linea Arezzo–Sinalunga
5. Albergo è un antico borgo della pianura, probabilmente di origine romana, sviluppato lungo le vie storiche del territorio.
6. Secondo l'itinerario dei nuclei di piano del Comune, nel nucleo sorgeva un ospedale per viandanti e malati.
7. Le fonti non spiegano però esplicitamente l'origine del toponimo.
8. Va chiarito un equivoco ricorrente: il podere Spedaluccio, ciò che resta di un antico ospizio per viandanti documentato dal 1198, è un luogo distinto.
9. Non si trova ad Albergo ma lungo la statale 69, circa un chilometro oltre Pieve a Maiano.
10. Centro storico: il nucleo antico del paese, censito tra i centri storici del Piano Strutturale, che ne prevede la valorizzazione insieme ai suoi complessi religiosi.
11. Fonte-cisterna di Albergo: l'antica riserva d'acqua del borgo.
12. Stazione ferroviaria: Albergo ha una propria fermata sulla linea Arezzo–Sinalunga.
13. Nelle settimane centrali di luglio la Polisportiva Albergo Oliveto, che si occupa anche di ciclismo giovanile, organizza al campo sportivo la Sagra del Crostino, arrivata nel 2026 alla 51ª edizione: tra i piatti tipici, i crostini neri di fegatini preparati con il vinsanto.
14. Accanto al campo sportivo c'è ora anche un campo polivalente a uso libero.
```

---

## Badia al Pino (`frazioni/badia-al-pino.html`): prima N1, poi seconda passata in N3 · 21 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Badia al Pino». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. La sede comunale, nata attorno a un'antica abbazia benedettina.
2. Attestata: 1039 (abbazia del Pino)
3. Parrocchia: San Bartolomeo
4. Ruolo: Sede comunale (dal 1917)
5. Badia al Pino nasce attorno all'antica abbazia benedettina del Pino, ricordata per la prima volta nel 1039 e dedicata ai santi Martino e Lorenzo.
6. Attorno al monastero sorse un borgo fortificato, di cui restano una torre e i resti di una porta.
7. Soppressa nel 1441 (secondo altre fonti nel 1446) e unita al monastero fiorentino del Paradiso a Ripoli, l'abbazia perse il suo ruolo e il paese divenne un centro soprattutto rurale.
8. La svolta arriva nel 1917: a causa dello spopolamento delle zone collinari, la sede comunale viene trasferita qui dal borgo storico di Civitella.
9. Da allora Badia al Pino è il capoluogo amministrativo del comune.
10. Chiesa di San Bartolomeo: la parrocchiale, annessa all'antica abbazia, con origini che risalgono al X secolo.
11. Nel Cinquecento al titolo originario dei santi Martino e Lorenzo si aggiunse quello di San Bartolomeo, rimasto fino a oggi.
12. Torre e porta del castello: quanto resta del borgo fortificato sorto attorno all'abbazia; la torre è tutelata da vincolo nazionale.
13. Palazzetto settecentesco: fu sede comunale dal 1917 fino ai primi anni Settanta; oggi ospita la Biblioteca comunale, dove si riunisce anche il circolo di lettura dedicato a Muriel Spark.
14. Palazzo Santini-Paccinelli: villa settecentesca a pianta rettangolare, simmetrica rispetto alla scala centrale, ai margini del nucleo medievale.
15. Villa del Bosco: con il suo parco storico e un filare di pini.
16. Monumento ai caduti: nel piazzale della chiesa, inaugurato il 26 agosto 1951.
17. Nella campagna intorno al paese si trovano alcune case coloniche di pregio, come Bellavista, il Casetto (o Casa del Moro) e l'ex chiesa di San Lorentino di Loreto, trasformata in abitazione.
18. La stazione di Civitella-Badia al Pino è sulla linea Arezzo–Sinalunga.
19. Tra la fine di agosto e l'inizio di settembre il Circolo Ricreativo Olinto Paccinelli organizza la Sagra della Bistecca, dedicata alla carne chianina cotta alla grande griglia, arrivata nel 2026 alla 46ª edizione.
20. Badia al Pino è anche uno dei poli produttivi del comune: qui nel 1976 Chimet aprì il suo primo stabilimento (vedi Lavoro e sapori).
21. Lo stadio comunale con la pista, il palazzetto dello sport e l'area sportiva della scuola media ospitano il calcio della S.S. Badiese 1948, la pallavolo e il ciclismo giovanile.
```

---

## Ciggiano (`frazioni/ciggiano.html`): prima N1, poi seconda passata in N3 · 27 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Ciggiano». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Un borgo fortificato sulle colline, con la pieve di San Biagio.
2. Altitudine: circa 360 m
3. Attestata: XI secolo (castello con pieve)
4. Parrocchia: San Biagio
5. Ciggiano sorge su un colle che separa le valli del Gargaiolo e dell'Esse.
6. Nacque come vicus romano, con un nome di origine incerta (forse dalla gens Ceia o Cedia, oppure da Cocceia), e nell'XI secolo era già un «castello con pieve».
7. La posizione, sotto i valichi di Palazzuolo e San Pancrazio, ne fece un nodo strategico.
8. Gli statuti di dogana della Repubblica fiorentina lo indicavano come tappa obbligata per i mercanti tra Siena e Firenze, e qui i pastori diretti dall'Appennino alla Maremma facevano la calla, la conta degli animali, pagando la gabella.
9. Nel 1250 Ciggiano compare alleato del vescovo Guglielmino; nel 1307 è di parte guelfa, nel 1381 appartiene agli Ubertini e nel 1385 passa a Firenze.
10. Fu assediato e saccheggiato dalle truppe di Niccolò Piccinino nel 1431 e di nuovo nel 1554.
11. Nel 1774 venne aggregato alla Comunità di Civitella.
12. Del castello resta ben leggibile l'impianto.
13. Sopravvivono il possente bastione sud-ovest, un tratto di mura trecentesche con la torre oggi inglobata nella casa canonica, una torretta cinquecentesca con feritoia per archibugi e una grande torre sul lato nord.
14. Il cuore del paese è Piazza Alta, con il pozzo comunitario.
15. Chiesa di San Biagio: la parrocchiale, elevata a pieve nel 1465; custodisce l'altare Mazzeschi della metà del Seicento e una scultura di Santa Maria Maddalena del primo Cinquecento attribuita ad Andrea Sansovino.
16. Chiesa della Compagnia di Santa Croce: costruita sulle mura occidentali del castello per custodire una reliquia della Croce, esposta il 3 maggio e il 14 settembre.
17. Documentata dal 1558, fu soppressa da Pietro Leopoldo nel 1783 e ripristinata nel 1794.
18. Chiesa di Santa Maria: realizzata nel 1635 fuori dall'abitato, lungo il percorso della transumanza, con un portico dove i pastori potevano ripararsi.
19. Chiesa di San Pietro: di origine medievale; il suo aspetto eclettico è frutto di un intervento del 1836.
20. Oratori di San Francesco e di Caggiolo: quest'ultimo, dedicato a Santa Maria e San Filippo Neri, sorge presso Villa Centeni Romani, tutelata da vincolo nazionale.
21. Poco distante si trovano il frantoio di Caggiolo e il mulino di Ciggiano.
22. Ricognizioni condotte nel 2004 hanno individuato ceramica romana di età imperiale nelle mura del paese e, in località La Cascinella davanti al cimitero, i resti di un vasto insediamento affiorati con i lavori agricoli: frammenti di macine etrusche, tegole e vasellame romani, fino a materiali del tardo Medioevo.
23. Il 16 aprile 1944 un gruppo di SS fermò due giovani partigiani, Giovanni Marmo e Mario Marapitti, mentre requisivano un camion di legna e carbone, e li fucilò sul posto.
24. In un giardino del centro il monumento ai caduti riunisce tre lapidi: per i 30 caduti e 2 dispersi delle due guerre mondiali, per Enrico Scapecchi, medaglia d'argento al valor militare, e per Marmo e Marapitti.
25. Secondo la scheda del Comune, Ciggiano contava 634 abitanti nel 1833, 508 nel 2001 e 610 nel 2011.
26. A settembre la Pro Loco di Ciggiano organizza la Festa dell'uva, del vino e dell'olio, arrivata nel 2026 alla 49ª edizione, e nel 2027 sarà la cinquantesima.
27. Il paese ha anche la sua banda, la Società Filarmonica Ciggiano.
```

---

## Cornia (`frazioni/cornia.html`): prima N1, poi seconda passata in N3 · 18 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Cornia». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Un piccolo nucleo collinare segnato per sempre dal 29 giugno 1944.
2. Altitudine: circa 560 m
3. Attestata: 1274 (decime)
4. Chiesa: San Michele Arcangelo (detta Sant'Angelo)
5. Cornia è un piccolo nucleo collinare, immerso in un'area di alto valore naturalistico.
6. La sua chiesa di Sant'Angelo compare già nelle decime del 1274, nel piviere di Santa Maria al Toppo, e nel 1833 il paese contava 292 anime.
7. In tempi più recenti vi esisteva un centro per la lavorazione delle scope di saggina.
8. Nei boschi vicini si trova il Castellare di Sant'Angelo: muri di pietra spessi fino a un metro e mezzo, forse resti di un vicus romano rioccupato in età longobarda, dove sono stati raccolti frammenti di tegole e vasi tardo-romani e parte di una piccola macina.
9. Era uno dei «castellari» del sistema fortificato della Val di Chiana settentrionale.
10. Chiesa di San Michele Arcangelo (Sant'Angelo di Cornia): la chiesa del paese, medievale.
11. Castellare di Sant'Angelo: il sito fortificato nel bosco, dove il Piano Strutturale prevede un campo scuola di scavo.
12. Complesso religioso di Vallebuona, tra quelli da recuperare, e la fonte della Cornia.
13. Parco faunistico e ANPIL: il Piano Strutturale individua l'area per un Parco Faunistico Naturalistico e un'Area Naturale Protetta di Interesse Locale, con sentieri, punti di avvistamento della fauna e un centro servizi ricavato negli edifici inutilizzati del borgo.
14. Il 29 giugno 1944 reparti della divisione corazzata tedesca «Hermann Göring» compirono a Cornia una strage di civili, contemporaneamente a quelle di Civitella e San Pancrazio.
15. A differenza che altrove, qui la violenza fu indiscriminata e colpì anche donne e bambini.
16. Lastra dei martiri di Cornia: presso la chiesa, riporta i nomi di 58 caduti di Cornia, Burrone, Morcaggiolo, Solaia, Cellere, San Pancrazio e Caselle, uccisi nelle rappresaglie fra il 29 giugno e il 16 luglio 1944.
17. L'Atlante delle stragi elenca 32 vittime per «Cornia e dintorni», tra cui il partigiano Hazbi Ismail (o Ismaili), 28 anni.
18. Cippo dell'eccidio: eretto nel 1969, nel venticinquesimo anniversario, presso il cimitero.
```

---

## Gebbia (`frazioni/gebbia.html`): prima N1, poi seconda passata in N3 · 13 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Gebbia». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Una piccola frazione collinare, anch'essa segnata dal 29 giugno 1944.
2. Distanza: circa 3,5 km (dal capoluogo)
3. Data: 29 giugno 1944
4. Gebbia è una piccola località collinare della campagna di Civitella.
5. Le fonti disponibili non documentano origini medievali né edifici storici: l'unico episodio storico ampiamente documentato riguarda la Seconda guerra mondiale.
6. Oggi la zona ospita un casale agrituristico, una struttura ricettiva moderna.
7. Il 29 giugno 1944 reparti della divisione corazzata «Hermann Göring», con la Feldgendarmerie del capitano Heinz Barz, applicarono a Gebbia lo stesso metodo usato a Civitella e a Cornia: rastrellamento degli uomini ed esecuzioni sommarie.
8. Secondo l'Archivio della Memoria, donne e bambini non furono toccati né le case bruciate, ma i tedeschi uccisero tutti gli animali.
9. Otto uomini furono fatti prigionieri e portati attraverso i boschi di Valibona fino al Podere Valle, vicino a San Pancrazio: lì furono fucilati e gettati in una capanna poi data alle fiamme.
10. L'Atlante delle stragi naziste e fasciste elenca 16 vittime per «Gebbia e dintorni», tra cui Arrigucci Orlindo (69 anni), Biagiotti Giulio (62) e Pratesi Silvestro (58); nell'elenco figurano anche alcune donne e due bambini di uno e tre anni.
11. A Gebbia furono catturati anche Giovanni Cau, scrittore e divulgatore scientifico nato a Cagliari nel 1892, e la moglie Helga Elmqvist, pittrice e traduttrice svedese: si erano trasferiti da Firenze per sfuggire ai pericoli della guerra.
12. Furono uccisi il 2 luglio 1944 a Monte San Savino.
13. Le fonti non coincidono sul numero delle vittime: l'Archivio della Memoria parla di 8 uomini fucilati, l'Atlante elenca 16 nomi per Gebbia e i suoi dintorni.
```

---

## Oliveto (`frazioni/oliveto.html`): prima N1, poi seconda passata in N3 · 21 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Oliveto». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Un borgo murato in posizione dominante sulla Val di Chiana, con una storia sorprendentemente internazionale.
2. Attestata: XII secolo (castello)
3. Parrocchia: Sant'Andrea Apostolo
4. Novecento: Villa Oliveto (campo di internamento 1940)
5. Oliveto è un borgo in posizione dominante sulla Val di Chiana.
6. Il suo castello è ricordato già nel XII secolo, ma la fortificazione aveva origini più antiche, tardo-imperiali e poi longobarde: della massiccia cinta muraria restano oggi alcuni tratti.
7. Il borgo fu feudo delle famiglie Ubertini e Saracini, che nella prima metà del Seicento, tornate proprietarie, riedificarono l'edificio del Podestà affacciato sulla piazza d'armi.
8. All'inizio dell'Ottocento il palazzo divenne casa colonica e granaio, e la piazza fu trasformata in vigneto e oliveto.
9. Chiesa di Sant'Andrea: parrocchiale di origine trecentesca, rifatta nel 1933 in stile neomedievale; custodisce una Madonna del Rosario del pittore cinquecentesco Orazio Porta.
10. Cassero, mura e Casa del Podestà: del castello restano il cassero, oggi abitazione, la porta d'accesso, tratti di mura e la torre sull'ex piazza d'armi.
11. Inglobata nelle mura c'è anche una casa trecentesca su tre piani, tutelata da vincolo nazionale.
12. Villa Oliveto (già Villa Mazzi): dimora dei conti Barbolani di Montauto, rimaneggiata nell'Ottocento, con un parco di ispirazione romantica ricco di cedri e lecci.
13. Cappella della Compagnia, rifatta attorno al 1637 come indica l'iscrizione sul portale, e Oratorio di San Rocco, nato come tabernacolo e trasformato in cappella nell'Ottocento.
14. Castellare e chiesa di San Giovanni d'Oliveto: un sito fortificato di età romana e medievale, con una chiesa altomedievale ricordata nelle decime del 1274 e ricostruita nel 1343.
15. Il Piano Strutturale vi prevede un parco archeologico con un campo scuola di scavo.
16. Nel giugno 1940 a Villa Oliveto fu istituito un campo di internamento che ospitò soprattutto famiglie ebree di nazionalità britannica provenienti dalla Libia; nel 1944 furono deportate a Bergen-Belsen.
17. Ceduta al Comune nel 1980, la villa ospita oggi il Centro di Documentazione «Villa Oliveto», dedicato alle politiche di esclusione e reclusione nel Novecento, con un archivio sui circa 50 campi italiani, una mostra e percorsi didattici per le scuole.
18. Oliveto è legata anche al nome della scrittrice scozzese Muriel Spark, autrice de Gli anni fulgenti di Miss Brodie.
19. Visse qui dagli anni Settanta con l'artista Penelope Jardine, ricevette nel 2005 la cittadinanza onoraria di Civitella e, morta nel 2006, è sepolta nel cimitero di Sant'Andrea Apostolo a Oliveto.
20. In sua memoria si riunisce un circolo di lettura alla Biblioteca comunale di Badia al Pino.
21. Dal 2014, nel periodo natalizio, la parrocchia organizza il Presepe Vivente di Oliveto: oltre 80 figuranti animano le antiche botteghe lungo le vie del paese, e un percorso illuminato da torce, tra gli olivi fuori dalle mura, conduce alla Natività allestita nella chiesetta di San Rocco.
```

---

## Pieve a Maiano (`frazioni/pieve-a-maiano.html`): prima N1, poi seconda passata in N3 · 21 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Pieve a Maiano». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Un toponimo che ricorda una pieve scomparsa, ai confini con Arezzo.
2. Origine: Romana (toponimo da Marius)
3. Parrocchia: Santa Maria Assunta
4. Natura: Porta della Riserva (di Ponte a Buriano e Penna)
5. Pieve a Maiano è un'antica località ai confini con il comune di Arezzo.
6. Il nome unisce il ricordo di una pieve, oggi scomparsa, a «Maiano», un toponimo romano derivato dal nome di un antico proprietario terriero, probabilmente un Marius.
7. Il territorio è abitato da tempi remotissimi: al Podere Casella sono stati trovati strumenti in pietra del Paleolitico, le testimonianze più antiche dell'intero comune.
8. Lungo la via della Centrale si trovano i Poderi Montoto I e II, case coloniche sorte su quanto resta di un fortilizio longobardo.
9. Il castello di Montoto passò da Arezzo a Firenze nel 1385; il Piano Strutturale lo indica come sito di notevole interesse storico-archeologico.
10. Chiesa di Santa Maria Assunta: edificio ottocentesco che conserva una campana del 1358 proveniente da Montoto.
11. Un tabernacolo ricorda il luogo dell'antica pieve.
12. Podere Spedaluccio: circa un chilometro dopo il paese, lungo la statale 69, una discesa sterrata porta alla casa colonica che è tutto ciò che resta di un antico ospizio per viandanti, documentato dal 1198.
13. Non ha legami con la frazione di Albergo, a cui a volte viene erroneamente associato.
14. Fattoria di Maiano: tutelata da vincolo nazionale.
15. Campo sportivo: un consistente insediamento romano, documentato da frammenti di vasi e tegole del I–II secolo d.C.
16. Vallimboi: una piccola fornace romana circolare, scavata nell'argilla nel bosco, che conserva ancora tracce di nerofumo.
17. Nei vecchi catasti il borro vicino si chiamava «Fossato della Fonte agli Urci».
18. Moneta d'oro dell'imperatore Claudio (41–54 d.C.): un aureus di circa 18 grammi.
19. Nella zona sono censite anche una scultura in marmo e i resti di un'altra fornace agli Ortali.
20. Il Piano Strutturale assegna a Pieve a Maiano il ruolo di «porta d'accesso» meridionale alla Riserva naturale di Ponte a Buriano e Penna, con la riqualificazione del paese, della via della Diga, dell'area dell'ex mulino e della vecchia stazione.
21. A fine agosto, su due lunghi fine settimana, il Circolo ricreativo U.S. Pieve a Maiano organizza la Sagra del Cinghiale, arrivata nel 2026 alla 42ª edizione.
```

---

## Pieve al Toppo (`frazioni/pieve-al-toppo.html`): prima N1, poi seconda passata in N3 · 19 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Pieve al Toppo». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Il centro abitato più popoloso del comune, teatro di una battaglia che Dante non ha dimenticato.
2. Attestata: 938 (la pieve)
3. Parrocchia: San Giovanni Battista
4. Battaglia: 26 giugno 1288
5. Il nome della frazione viene dalla sua pieve, una chiesa parrocchiale di campagna costruita in posizione elevata;
6. «Toppo» è quasi sicuramente un toponimo di origine longobarda.
7. L'antichissima pieve, con annesso un ospedale per i pellegrini, è documentata già nel 938 e fu distrutta intorno al 1500 da eventi bellici.
8. Il luogo è celebre per la battaglia di Pieve al Toppo, combattuta il 26 giugno 1288.
9. Gli aretini ghibellini, guidati da Buonconte da Montefeltro e Guglielmino de' Pazzi, tesero un'imboscata ai senesi guelfi che rientravano verso casa e, pur in inferiorità numerica, ne fecero strage.
10. Dante la ricorda nel XIII canto dell'Inferno con le «giostre del Toppo», dove fra gli scialacquatori compare Lano da Siena, caduto in quella battaglia.
11. Oratorio della Madonna del Conforto: sorge sul sito dell'antica pieve ed è dedicato alla Madonna del Conforto dal 1906.
12. Cippo delle Giostre del Toppo: ricorda la battaglia del 1288.
13. Chiesa di San Giovanni Battista: la parrocchiale, una chiesa moderna progettata nel 1967 dallo studio Martini-Matteini-La Rocca; il porticato fu aggiunto nel 1977.
14. Fattoria di Mugliano: complesso rurale censito tra gli edifici storici del Piano Strutturale.
15. In località I Ponti, su segnalazione del Gruppo Archeologico del Dopolavoro Ferroviario di Arezzo, sono venuti alla luce a circa 1,60 metri di profondità i muri di strutture romane interpretate come fornaci per la terra sigillata aretina, la celebre ceramica rossa da mensa della prima età imperiale, insieme a scarti di lavorazione e probabili scorie di fusione.
16. La prima domenica di ottobre, nel piazzale del Circolo ricreativo, si svolge la Fiera del Miele, organizzata dal Comune con Slow Food Valdichiana e arrivata nel 2026 alla 22ª edizione.
17. A fine estate il Circolo ARCI organizza la Sagra della Pesca, dedicata al frutto.
18. Lo stadio di via del Sembolino è la casa della Polisportiva Pieve al Toppo 06, e da poco il paese ha anche un campo polivalente a uso libero.
19. Il Piano Strutturale prevede di trasformare il grande incrocio al centro del paese in una piazza e di circondare l'abitato con una «cintura verde» di percorsi.
```

---

## Ponticino (`frazioni/ponticino.html`): prima N1, poi seconda passata in N3 · 14 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Ponticino». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Un solo abitato, diviso tra più comuni.
2. Comuni: Civitella e Laterina Pergine Valdarno
3. Stazione: 1866 (linea Firenze–Roma)
4. Parrocchia: Santi Iacopo e Cristoforo (con sede a Laterina Pergine V.)
5. Ponticino si è sviluppato nel fondovalle, lungo le direttrici verso il Valdarno, servito dal 1866 dalla stazione sulla ferrovia Firenze–Roma: quell'anno fu inaugurato il tratto Montevarchi–Arezzo–Tuoro e completato il primo collegamento ferroviario tra le due città.
6. L'abitato si trova a cavallo del confine comunale: percorrendo l'itinerario Valdarno–Civitella del Comune si esce brevemente dal territorio di Civitella proprio presso Ponticino, per rientrarvi subito dopo.
7. Ponticino è un caso singolare di geografia amministrativa.
8. Fino al 2017 era diviso tra tre comuni: Civitella in Val di Chiana, che ne comprende la maggior parte del territorio, Laterina e Pergine Valdarno.
9. Nel referendum del 29 e 30 ottobre 2017 la fusione tra Laterina e Pergine passò con il 53,73% dei voti: i due capoluoghi votarono in maggioranza contro, e furono le frazioni, Ponticino su tutte, a decidere.
10. Dal 1° gennaio 2018 esiste il comune di Laterina Pergine Valdarno, e Ponticino è oggi divisa tra due comuni.
11. Mulino di Ponticino: l'unico bene storico censito a Ponticino dal Repertorio del Piano Strutturale.
12. Stazione ferroviaria: attiva dal 1866, oggi servita da treni regionali.
13. Chiesa dei Santi Iacopo e Cristoforo: la parrocchiale, che ha sede nella parte del paese compresa nel comune di Laterina Pergine Valdarno.
14. Al censimento ISTAT 2021 il centro abitato di Ponticino («Ponticino-Cavi Casalone») è attribuito al comune di Laterina Pergine Valdarno; nel territorio di Civitella non risulta censita una località abitata di Ponticino.
```

---

## Spoiano (`frazioni/spoiano.html`): prima N1, poi seconda passata in N3 · 13 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Spoiano». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Un borgo di origine romana, tra la villa dei Pecchioli e la sagra dei baccelli.
2. Origine: Romana
3. Parrocchia: San Giovanni Battista
4. Edificio simbolo: Villa Pecchioli (XVIII secolo)
5. Spoiano è una località di origine romana, come confermano il ritrovamento di un tesoretto di monete e le fonti turistiche del territorio.
6. Il Comune la include tra i nuclei di piano, in posizione panoramica e circondata dal paesaggio collinare.
7. Il borgo è formato da una piazza centrale e da edifici accorpati nel Settecento attorno alla villa padronale e alla chiesa.
8. Villa Pecchioli: edificio settecentesco della famiglia Pecchioli, formato da un lungo corpo di fabbrica sormontato da una torre-piccionaia, con un piccolo campanile a vela al centro della facciata.
9. Nel 1928 divenne asilo infantile ed è stata restaurata nel 1981.
10. Conserva il parco storico, una cisterna e un pozzo; il Piano Strutturale ne prevede il recupero.
11. Chiesa di San Giovanni Battista: la parrocchiale della frazione, parte del complesso del borgo.
12. A maggio, su due fine settimana, la Polisportiva Spoiano organizza al circolo del paese la Sagra dei Baccelli, arrivata nel 2025 alla 48ª edizione: le fave fresche si servono crude con olio extravergine, pecorino o finocchiona.
13. Spoiano è al centro del libro Un uomo dabbene per davvero dell'avvocato aretino Giuseppe Renzetti, un racconto della vita contadina e della saggezza popolare della Valdichiana attraverso la figura del padre dell'autore, Francesco detto «Didi».
```

---

## Tegoleto (`frazioni/tegoleto.html`): prima N1, poi seconda passata in N3 · 21 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Tegoleto». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Uno dei centri della pianura dove vive la maggior parte della popolazione del comune.
2. Attestata: X secolo (chiesa di San Biagio)
3. Parrocchia: San Biagio
4. Cultura: Teatro Moderno Tegoleto (dal 1960)
5. Tegoleto è un borgo di origine medievale nella pianura del comune, storicamente dedito all'agricoltura.
6. La sua chiesa di San Biagio esisteva già nel X secolo; del sistema difensivo dell'abitato medievale resta la torre, ricostruita dai fiorentini alla fine del Trecento.
7. Nel 1783 la fattoria del paese passò all'Ordine dei Cavalieri di Santo Stefano.
8. Oggi Tegoleto è, dopo Pieve al Toppo, il centro più popoloso del comune.
9. Chiesa di San Biagio: la chiesa romanica, già esistente nel X secolo e ristrutturata nel XII, sopravvive nei resti della parte absidale, ancora visibili nell'abitato.
10. Torre medievale: ricostruita dai fiorentini alla fine del Trecento e più volte restaurata; persa la funzione militare, divenne edificio colonico.
11. È tutelata da vincolo nazionale.
12. Fattoria di Tegoleto: acquistata nel 1783 dall'Ordine dei Cavalieri di Santo Stefano dal patrimonio Marzocchi.
13. La casa d'agenzia, con torre colombaria e due edifici simmetrici attorno al cortile con il pozzo, risultava di recente costruzione nel 1814.
14. TMT – Teatro Moderno Tegoleto: nato nel 1960 come cinema per iniziativa di alcuni parrocchiani, dal 1997 è una sala polifunzionale gestita dal Gruppo Teatro La Torre, con una stagione da ottobre a marzo.
15. Tegoleto ha uno dei calendari più ricchi del comune.
16. Tra l'ultima settimana di giugno e la prima di luglio l'U.S.D. Tegoleto, con l'associazione Comunità & Tegoleto, organizza la Festa al Tegoleto, con luna park, ballo, stand gastronomici e fuochi d'artificio, arrivata nel 2025 alla 52ª edizione.
17. Comunità & Tegoleto promuove anche Cinema sotto le Stelle, proiezioni gratuite il mercoledì sera di luglio in piazza della Chiesa, nate nel 2018, e dal 2025 il RioFest, un festival di musica, incontri e spettacoli a ingresso gratuito che si tiene a settembre.
18. Ad aprile, sempre in piazza della Chiesa, il Comune e Slow Food Valdichiana organizzano il Mercato dei Sapori e della Terra.
19. Allo stadio di via del Chiassobuio gioca l'U.S.D. Tegoleto 1970, dalla scuola calcio alla prima squadra; nella palestra della scuola primaria Arcobaleno si praticano pallavolo e taekwondo.
20. Per oltre sessant'anni il paese è stato la sede delle cucine Del Tongo, fallite nel 2018 (vedi Lavoro e sapori).
21. Il 12 maggio 2004 a Tegoleto si concluse la quarta tappa del Giro d'Italia, vinta da Alessandro Petacchi davanti allo stabilimento del mobilificio Del Tongo.
```

---

## Tuori (`frazioni/tuori.html`): prima N1, poi seconda passata in N3 · 13 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Tuori». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Un antico avamposto militare aretino, a guardia della Val di Chiana e della Valdambra.
2. Attestata: 1021
3. Parrocchia: Santi Giorgio e Luca
4. Patrono: San Giorgio (23 aprile)
5. Tuori è ricordato già nel 1021 come abitato del piviere di Santa Maria al Toppo.
6. In seguito divenne un castello, sede di guarnigioni a presidio della città di Arezzo.
7. La sua posizione dominante permetteva di vigilare sia sulla Val di Chiana sia sulla Valdambra, e lo inseriva nel cosiddetto «terzo anello» difensivo dello Stato aretino.
8. Delle fortificazioni restano poche tracce e il cassero; il centro storico è tutelato da vincolo nazionale.
9. Chiesa dei Santi Giorgio e Luca: edificio del XIII secolo, appartenuto al piviere di Santa Maria al Toppo.
10. «Santi Giorgio e Luca» è il titolo ufficiale secondo la Diocesi; l'itinerario del Comune e altre fonti riportano «Giorgio e Lucia».
11. Il Cassero: castello del XIV secolo costruito dagli aretini, usato come presidio e come punto di comunicazione visiva con la Val di Chiana senese; oggi è incorporato in un edificio rurale, in parte in abbandono.
12. Il Saracino: in località Sasso Saracino, una casa colonica cinquecentesca costruita dalla Fraternita dei Laici di Arezzo, con un portale in mattoni ad arco policentrico.
13. Il Piano Strutturale inserisce Tuori tra le tappe della «ciclabile dei borghi pedecollinari», con il recupero dei tracciati storici, dei basolati e dei muri in pietra.
```

---

## Viciomaggio (`frazioni/viciomaggio.html`): prima N1, poi seconda passata in N3 · 21 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Viciomaggio». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Un toponimo romano, una leggenda su Annibale e una pagina dolorosa del 1944.
2. Attestata: 1024 (atto notarile)
3. Parrocchia: San Martino
4. Toponimo: Vicus maior
5. Il nome di Viciomaggio viene dal latino vicus maior, il «villaggio maggiore».
6. Il territorio era abitato già in età etrusca e romana, e il borgo medievale è ricordato in un atto notarile del 1024.
7. Storicamente ha avuto funzioni agricole e commerciali, grazie alla sua posizione lungo il percorso tra Arezzo e Civitella.
8. Nei dintorni sorgevano i borghi medievali di Malpertuso e Le Fosse e il fortilizio di Poggio Castellare, prima bizantino e poi longobardo, già abbandonati nel tardo Medioevo.
9. Poco lontano c'è l'antico insediamento di Tribbio, il cui nome viene dal trivio romano attorno a cui sorse, e sulle colline si trovano le rovine del castello di Gaenne, distrutto per ordine di Firenze dopo il 1385.
10. Chiesa di San Martino: la parrocchiale, all'ingresso del paese.
11. La chiesa altomedievale originaria è scomparsa e il titolo è passato al nuovo edificio.
12. Villa Milloni (Fattoria di Viciomaggio): villa padronale settecentesca nata dall'accorpamento di edifici più antichi, con decorazioni pittoriche del 1868 e, oltre la strada, un giardino con una limonaia del 1836.
13. La grande cappella secentesca annessa ha un quadrante d'orologio e un piccolo campanile a vela sul fianco sud.
14. Villa di Viciomaggio: un'altra villa storica con la sua cappella.
15. Nel 1872 vi fu ritrovata un'urna cineraria etrusca in arenaria, di età ellenistica, con l'iscrizione l. prastn[a] nerinal, insieme a un vaso a vernice nera anch'esso iscritto: provenivano probabilmente da una tomba a camera.
16. Sono stati trovati anche vasi del I secolo a.C. e un monile romano, oggi al Museo Archeologico Nazionale «Gaio Cilnio Mecenate» di Arezzo.
17. Il 29 marzo 1944 la frazione fu teatro di una strage fascista in cui fu ucciso Mario Mannelli, pochi mesi prima dell'eccidio del 29 giugno (vedi la pagina Storia).
18. Durante la guerra la popolazione si rifugiava dai bombardamenti in un cunicolo con una stanza scavata sottoterra lungo il Fosso del Riolo, verso Malpertuso, oggi censito tra i luoghi della memoria.
19. Una leggenda locale, priva di riscontro storico, attribuisce il nome del paese al passaggio di Annibale.
20. Tra la fine di aprile e l'inizio di maggio l'A.S.D. Viciomaggio organizza la Festa della Rosa, con ristorante, tornei, musica e i pranzi del 25 aprile e del 1° maggio.
21. Nella zona industriale del paese hanno sede due delle aziende più note del comune: CEIA, che dal 1968 costruisce metal detector e sistemi di ispezione venduti in tutto il mondo, e uno stabilimento di Chimet, aperto negli anni Ottanta (vedi Lavoro e sapori).
```

---

## Borghi e località minori (`frazioni/borghi-minori.html`): prima N1, poi seconda passata in N3 · 58 frasi

**Parte 1 di 2**

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Borghi e località minori», parte 1 di 2. Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Piccoli nuclei, castellari e ville-fattoria che non sono frazioni, ma raccontano il territorio.
2. Oltre al capoluogo e alle frazioni, il territorio di Civitella è punteggiato di piccoli luoghi con una storia propria: nuclei rurali, fortilizi d'altura abbandonati da secoli, ville-fattoria e insediamenti antichi.
3. Qui li raccogliamo in schede brevi, ciascuna con un rimando alla frazione più vicina.
4. Una chiesetta dedicata a San Michele Arcangelo, un rocchio di colonna in arenaria accanto alla porta e una vasca oggi interrata sono quanto resta di un insediamento religioso più vasto, sede di un convento.
5. Il luogo era noto per una sorgente dalle acque ritenute medicamentose, usate soprattutto per guarire i lattanti; vi era venerata una Madonna del Latte, ed è probabile che il culto delle acque risalisse all'antichità.
6. Oggi a Matroia c'è un allevamento di cavalli, che il Piano Strutturale prevede di trasformare in Centro di Equitazione.
7. Al censimento ISTAT 2021 il nucleo contava 23 residenti.
8. Fondovalle, lungo la Via Vecchia Senese
9. Nucleo rurale
10. Lungo la via della Centrale, i Poderi Montoto I e II sono case coloniche sorte su quanto resta di un fortilizio longobardo.
11. Il castello passò da Arezzo a Firenze nel 1385; da qui proviene la campana del 1358 oggi nella chiesa di Pieve a Maiano.
12. Il Piano Strutturale lo indica come sito di notevole interesse storico-archeologico, con un campo scuola di scavo e un punto panoramico collegato ai sentieri della Riserva di Ponte a Buriano e Penna.
13. Vicino a Pieve a Maiano
14. Fortilizio longobardo
15. Sulla cima del poggio, a 483 metri e a sud di Gaenne, restano i ruderi di una cinta muraria ellittica a secco, spessa 1,60 metri e lunga circa 300, con all'interno le fondamenta di altri muri.
16. La datazione è discussa: gli studiosi l'hanno attribuita all'età etrusca o romana, al Medioevo, o a un arco che va dalla protostoria alla fine dell'età antica; il Comune la descrive come fortilizio prima bizantino e poi longobardo, già abbandonato nel tardo Medioevo.
17. Insieme a Gaenne è destinato a diventare un parco archeologico con campo scuola di scavo.
18. Poco prima del poggio passa il sentiero CAI 105.
19. Vicino a Viciomaggio
20. Castellare
21. Due piccoli borghi medievali già abbandonati nel tardo Medioevo.
22. Malpertuso oggi è di nuovo abitato: al censimento ISTAT 2021 il nucleo contava 17 residenti.
23. A Le Fosse il Repertorio dei beni storici registra il ritrovamento di un cippo romano in travertino.
24. Durante la Seconda guerra mondiale gli abitanti di Viciomaggio si rifugiavano dai bombardamenti in un cunicolo con una stanza scavata sottoterra lungo il Fosso del Riolo, verso Malpertuso.
25. Vicino a Viciomaggio
26. Borghi medievali
27. Un antico insediamento raggiungibile da una strada sterrata.
28. Il nome viene dal trivium, l'incrocio di tre strade attorno a cui sorse in età romana; ancora oggi è un crocevia rurale, con un vecchio pozzo censito tra i beni storici.
29. Vicino a Viciomaggio
30. Insediamento antico
31. Il nome ricorda un antico proprietario germanico: «Monte di Arfo».
32. Del castello medievale, aggregato al Comune di Civitella nel 1774, restano la porta d'accesso e tratti della cinta muraria, in parte inglobati nella villa padronale.
33. Oggi Montarfoni è un borgo-fattoria organizzato come un piccolo paese, con la piazzetta, la chiesa di Sant'Andrea, la cantina e il frantoio-mulino, e un antico tratto di strada romana.
34. In fondo, dominante sulla valle, c'è la villa seicentesca con la limonaia e il parco terrazzato.
35. Lungo l'itinerario Valdarno–Civitella, dopo Ponticino
```

**Parte 2 di 2**

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Borghi e località minori», parte 2 di 2. Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
36. Castello e borgo-fattoria
37. Fu un insediamento fortificato longobardo di primaria importanza, tenuto tra l'VIII e il X secolo dai patroni della Pieve al Toppo.
38. Un documento del 1181 parla del castrum Durna e della sua corte; la torre, ricordata dal 1198, è la parte più antica rimasta integra.
39. Nel 1182 è documentata anche una chiesa dei Santi Vito e Nicola, poi diventata oratorio e infine inglobata in una casa colonica.
40. Al centro dell'abitato sorge la villa-fattoria settecentesca: nel XVIII secolo era dei Riccardi e nel 1814 fu acquistata dalle suore Montalve della Quiete di Firenze.
41. Lungo l'itinerario dei nuclei di collina
42. Castello longobardo e villa-fattoria
43. Piccolo nucleo d'altura a circa 540 metri.
44. La sua prima chiesa, San Martino di Loreto, sorgeva nella vicina località Pian del Pozzo: è ricordata nel 1194 tra i possessi dell'abbazia di Agnano e scompare dai documenti dal XV secolo; oggi ne resta un'edicola.
45. L'attuale chiesa dei Santi Maria e Carlo fu costruita nel 1690 grazie al patrimonio donato dal nobile fiorentino Carlo Casini, ampliata nel 1726 e divenuta parrocchia nel 1814; nel 1845 la parrocchia contava 317 abitanti.
46. Il nucleo conserva anche un pozzo, il monumento ai caduti della Prima guerra mondiale, la villa e i filari di cipressi.
47. Oltre il paese, il sentiero CAI 107 porta all'Oratorio della Madonna di Mercatale.
48. Lungo l'itinerario Valdarno–Civitella, dopo Montarfoni
49. Nucleo storico
50. Su un pianoro ellittico dai fianchi scoscesi restano i ruderi di un castello medievale sorto a controllo della strada tra Valdichiana e Valdarno.
51. Il nome è forse di origine etrusca, e il castello sorse forse su un fortilizio bizantino.
52. Nel 1069 apparteneva ai longobardi di Dorna, poi passò ai Tarlati di Arezzo; nel 1385 finì sotto Firenze, che lo descrisse come «un forte castello di sito e di muro» e ne ordinò la distruzione.
53. Del cassero restano spessi tratti di muratura nel punto più alto; tra i ruderi sono state trovate maiolica arcaica e tubi in terracotta, forse di una cisterna.
54. Nella Seconda guerra mondiale, con il passaggio del fronte, il luogo fu bombardato.
55. Ci si arriva da Viciomaggio per una strada sterrata e poi a piedi, anche lungo il sentiero CAI 105.
56. Il Piano Strutturale prevede qui, con Poggio Castellare, un parco archeologico.
57. Vicino a Viciomaggio
58. Castello in rovina
```

---

## Storia (`storia.html`): prima N1, poi seconda passata in N3 · 23 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Storia». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Dalle origini etrusco-romane alla ricostruzione del dopoguerra.
2. Il territorio di Civitella è abitato da tempi remotissimi: a Pieve a Maiano sono stati trovati strumenti in pietra del Paleolitico, e in tutta la zona affiorano tracce etrusche e romane, dall'urna iscritta di Viciomaggio alle fornaci di terra sigillata aretina di Pieve al Toppo.
3. Molti nomi di paese sono di origine latina, come vicus maior (Viciomaggio) o Maiano, dal nome di un proprietario romano.
4. In epoca longobarda il colle di Civitella era già un forte a controllo del territorio, e una rete di piccoli siti fortificati, i castellari, sorvegliava la Val di Chiana settentrionale.
5. Il castello di Civitella fu eretto nel 1048, e dall'XI secolo la rocca fu un presidio dei vescovi-conti di Arezzo.
6. Nel 1182 la rocca aveva già l'aspetto di un palazzo-torre, e nel 1248 il vescovo Guglielmino degli Ubertini la scelse come propria dimora e ne potenziò la cinta muraria.
7. Il territorio fu coinvolto nelle guerre del tempo: il 26 giugno 1288, a Pieve al Toppo, gli aretini sconfissero i senesi nella battaglia che Dante ricorda come le «giostre del Toppo», e tra il 1284 e il 1285 la rocca di Civitella fu assediata dagli stessi aretini.
8. Nel 1385, dopo aver acquisito Arezzo e il suo contado, la Repubblica fiorentina riorganizzò l'intero territorio aretino: Civitella fu staccata dalla podesteria di Valdambra e divenne capoluogo di una propria podesteria, che durò fino al 1838.
9. Nel 1774 le antiche comunità di Ciggiano, Viciomaggio e Badia al Pino, insieme al castello di Montarfoni, furono aggregate alla Comunità di Civitella.
10. Con lo spopolamento delle zone collinari, nel 1917 la sede comunale fu trasferita da Civitella a Badia al Pino, nella pianura, dove si trova ancora oggi.
11. È in pianura che vive oggi la maggior parte degli abitanti: al censimento del 2021 il centro più popoloso era Pieve al Toppo.
12. Nel giugno 1940 a Villa Oliveto fu istituito un campo di internamento che ospitò soprattutto famiglie ebree di nazionalità britannica provenienti dalla Libia, deportate nel 1944 a Bergen-Belsen.
13. Il 29 giugno 1944, nella ricorrenza dei santi Pietro e Paolo, reparti tedeschi compirono una rappresaglia efferata a Civitella, Cornia, Gebbia e San Pancrazio di Bucine, uccidendo centinaia di civili.
14. È uno degli episodi più gravi delle stragi naziste in Toscana, ancora oggi al centro della memoria collettiva del territorio.
15. Negli stessi mesi un bombardamento alleato distrusse buona parte della rocca.
16. In occasione della ricorrenza si tiene la Marcia per la pace da Civitella a San Pancrazio, organizzata insieme al comune di Bucine.
17. Le fonti non concordano sulle cifre.
18. La ricostruzione di ToscanaNovecento riporta 244 morti: 115 a Civitella, 58 a Cornia e 71 a San Pancrazio.
19. L'Atlante delle stragi naziste e fasciste in Italia conta invece 146 vittime per l'episodio di Civitella, Cornia e Gebbia (di cui 32 a Cornia e dintorni e 16 a Gebbia e dintorni) e 58 per quello di San Pancrazio, per un totale di 204.
20. La lapide di Cornia con 58 nomi comprende anche caduti di San Pancrazio e di altre località vicine.
21. Per il dettaglio vedi le pagine di Cornia e Gebbia.
22. Questa pagina riassume in poche righe secoli di storia.
23. Ogni frazione ha una pagina con la propria storia e le proprie fonti; l'elenco completo è nella pagina Fonti.
```

---

## Patrimonio (`patrimonio.html`): prima N1, poi seconda passata in N3 · 95 frasi

**Parte 1 di 3**

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Patrimonio», parte 1 di 3. Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Castellari, ville-fattoria, mulini e duemila anni di archeologia, frazione per frazione.
2. Le pagine delle frazioni raccontano i luoghi uno per uno.
3. Questa pagina li legge invece per temi, collegando ciò che il territorio ha in comune: le fortificazioni, le grandi fattorie, i mulini e le tracce archeologiche.
4. Ogni voce rimanda alla pagina della frazione dove approfondirla.
5. Fin dall'età longobarda una rete di piccoli siti fortificati d'altura, i castellari, sorvegliava la Val di Chiana settentrionale.
6. Nel Medioevo i borghi si chiusero dentro mura e casseri, e molti ne conservano ancora le tracce.
7. Il Piano Strutturale prevede di collegare i castellari in un unico itinerario di visita.
8. Rocca di Civitella: forte già in età longobarda, castello dal 1048, dimora del vescovo Guglielmino degli Ubertini dal 1248; ne resta il Palatium-torre.
9. Civitella
10. Castellare di Sant'Angelo: forse un vicus romano rioccupato in età longobarda, nei boschi di Cornia.
11. Cornia
12. Castellare di San Giovanni d'Oliveto e il cassero del borgo murato di Oliveto, ricordato dal XII secolo.
13. Oliveto
14. Poggio Castellare: una cinta muraria ellittica a secco lunga circa 300 metri, di datazione discussa (dalla protostoria al Medioevo).
15. Con Gaenne è destinato a diventare un parco archeologico.
16. Borghi minori
17. Montoto: fortilizio longobardo, passato a Firenze nel 1385.
18. Borghi minori
19. Castello di Gaenne: a guardia della strada tra Valdichiana e Valdarno, forse sorto su un fortilizio bizantino, dei longobardi di Dorna nel 1069 e poi dei Tarlati, distrutto per ordine di Firenze dopo il 1385; oggi ne restano le rovine nel bosco.
20. Borghi minori
21. Castello di Montarfoni, di cui restano la porta e tratti di mura, e il castello longobardo di Dorna, documentato nel 1181, con la torre ricordata dal 1198.
22. Borghi minori
23. Cassero di Tuori: presidio aretino d'altura, nel borgo attestato dal 1021.
24. Tuori
25. Mura e torri di Ciggiano: bastione, torre trecentesca e torretta cinquecentesca per archibugi.
26. Ciggiano
27. Torri di pianura: la torre di Tegoleto, ricostruita dai fiorentini a fine Trecento, e quella del castello sorto attorno all'abbazia di Badia al Pino.
28. Tegoleto, Badia al Pino
29. Tra Sei e Ottocento le grandi famiglie e gli ordini religiosi organizzarono la campagna in fattorie, con la villa padronale, la casa d'agenzia, la cappella e il giardino.
30. Molte sono ancora riconoscibili, e diverse sono tutelate da vincolo.
31. Villa Oliveto (già Villa Mazzi): dimora dei conti Barbolani di Montauto, campo di internamento dal 1940, oggi Centro di Documentazione.
32. Oliveto
33. Villa Milloni: villa settecentesca con limonaia del 1836 e cappella secentesca con orologio e campanile a vela; accanto, la Villa di Viciomaggio.
34. Viciomaggio
35. Fattoria di Tegoleto: dell'Ordine dei Cavalieri di Santo Stefano dal 1783, con la casa d'agenzia e la torre colombaria.
```

**Parte 2 di 3**

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Patrimonio», parte 2 di 3. Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
36. Tegoleto
37. Villa Pecchioli: settecentesca, con torre-piccionaia; asilo dal 1928, restaurata nel 1981.
38. Spoiano
39. Palazzo Santini-Paccinelli e Villa del Bosco, con il parco e il filare di pini.
40. Badia al Pino
41. Fattoria di Maiano, tutelata da vincolo nazionale.
42. Pieve a Maiano
43. Villa Centeni Romani con l'oratorio di Caggiolo.
44. Ciggiano
45. Villa seicentesca di Montarfoni, con limonaia, parco terrazzato e borgo-fattoria; villa-fattoria di Dorna, dei Riccardi e poi, dal 1814, delle suore Montalve;
46. Villa di San Martino in Poggio.
47. Borghi minori
48. Lungo i torrenti che scendono dalle colline sorgevano mulini e frantoi, al servizio delle fattorie e dei borghi.
49. Il Repertorio dei beni storici del Piano Strutturale ne censisce diversi.
50. L'Infernaccio, il mulino di Oliveto.
51. Oliveto
52. Mulino di Ciggiano e frantoio di Caggiolo.
53. Ciggiano
54. Mulino di Ponticino, l'unico bene storico censito nella frazione.
55. Ponticino
56. Mulino di Montarfoni.
57. Borghi minori
58. Ex mulino di Pieve a Maiano, la cui area il Piano Strutturale prevede di riqualificare.
59. Pieve a Maiano
60. Il territorio di Civitella conserva tracce di quasi tutte le epoche.
61. Ecco i ritrovamenti censiti dal Repertorio dei beni storici, in ordine di tempo.
62. Strumenti in pietra del Paleolitico medio e superiore al Podere Casella, le testimonianze più antiche del comune.
63. Pieve a Maiano
64. Paleolitico
65. Un'urna cineraria ellenistica in arenaria con l'iscrizione l. prastn[a] nerinal e un vaso iscritto, ritrovati nel 1872.
66. Viciomaggio
67. Frammenti di macine da grano nel vasto insediamento della Cascinella.
68. Ciggiano
69. La cinta ellittica di Poggio Castellare, datata da alcuni studiosi già alla protostoria o all'età etrusca, e il nome di Gaenne, forse di origine etrusca.
70. Borghi minori
```

**Parte 3 di 3**

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Patrimonio», parte 3 di 3. Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
71. Forse già allora frequentata la sorgente salutare di Matroia.
72. Borghi minori
73. Età etrusca
74. Vasi del I secolo a.C. e un monile oggi al Museo archeologico di Arezzo.
75. Viciomaggio
76. Le fornaci de I Ponti, dove si produceva la terra sigillata aretina della prima età imperiale.
77. Pieve al Toppo
78. Un insediamento del I–II secolo d.C., la fornace di Vallimboi e un aureus dell'imperatore Claudio (41–54 d.C.).
79. Pieve a Maiano
80. Un cippo romano in travertino a Le Fosse.
81. Borghi minori
82. Un tesoretto di monete romane.
83. Spoiano
84. Il vicus romano all'origine del paese e la ceramica imperiale nelle sue mura.
85. Ciggiano
86. Il trivio da cui prende nome Tribbio.
87. Borghi minori
88. Età romana
89. Il Castellare di Sant'Angelo, forse un vicus romano rioccupato in età longobarda.
90. Cornia
91. Il fortilizio di Poggio Castellare, che il Comune descrive come bizantino e poi longobardo, il castello longobardo di Dorna, tenuto tra l'VIII e il X secolo dai patroni della Pieve al Toppo, e il fortilizio di Montoto.
92. Borghi minori
93. Le origini tardo-imperiali e longobarde delle fortificazioni di Oliveto e il forte longobardo sul colle di Civitella.
94. Oliveto, Civitella
95. Tarda antichità e Longobardi
```

---

## Geografia (`geografia.html`): N3 · 33 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Geografia». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Tra le prime colline dell'Appennino e la pianura della Val di Chiana.
2. Superficie: 100,33 km²
3. Altitudine: circa 500 m (il capoluogo)
4. Zona climatica: E (2.269 gradi giorno)
5. Il comune di Civitella in Val di Chiana si trova in provincia di Arezzo, circa 15 km a sud-ovest del capoluogo di provincia, nella Val di Chiana aretina.
6. Il capoluogo storico sorge a circa 500 metri sul livello del mare, sul colle che separa la Valdambra dalla Valdichiana; i centri abitati del comune si trovano tra circa 300 e 600 metri di quota.
7. Il comune confina con Arezzo, Bucine, Laterina Pergine Valdarno e Monte San Savino.
8. Il territorio comunale si divide in due anime ben distinte: una zona collinare e di bassa montagna, coperta da boschi e caratterizzata da piccoli borghi fortificati, e una zona di pianura che forma la parte settentrionale della Val di Chiana, coltivata in modo intensivo.
9. È in quest'ultima zona che si concentra la popolazione: al censimento ISTAT 2021 i quattro centri maggiori, Pieve al Toppo, Tegoleto, Badia al Pino e Viciomaggio, contavano insieme quasi 5.000 residenti, più della metà degli 8.814 abitanti del comune.
10. Circa un quarto della popolazione vive invece in case sparse.
11. Residenti per località abitata al censimento ISTAT 2021:
12. Pieve al Toppo: 1.545
13. Tegoleto: 1.412
14. Badia al Pino: 1.059
15. Viciomaggio: 950
16. Ciggiano: 530
17. Albergo: 279
18. Pieve a Maiano: 242
19. Civitella (borgo storico): 148
20. Tuori: 129
21. Spoiano: 120
22. Matroia: 23
23. Oliveto: 15
24. Altri piccoli nuclei e località (Casali, Le Poggiole, Malpertuso, Poggio Basso e altre): 106
25. Case sparse: 2.256
26. Cornia e Gebbia non sono censite come località abitate a sé: i loro residenti rientrano tra le case sparse.
27. Il centro abitato di Ponticino è attribuito dall'ISTAT al comune di Laterina Pergine Valdarno.
28. Sui pendii collinari prevalgono gli oliveti, spesso su piccoli terrazzamenti sostenuti da muri in pietra o su ciglionamenti, alternati a vigneti, dove si produce il Chianti Colli Aretini, e ad ampie aree boscate.
29. In pianura l'agricoltura è intensiva: seminativi, frutteti e vigneti arrivano fino alla base delle colline, ma il paesaggio conserva ancora i segni della bonifica, a cominciare dal reticolo dei fossi minori.
30. A nord una parte del territorio comunale rientra nella Riserva naturale di Ponte a Buriano e Penna, che protegge il tratto dell'Arno tra Ponte a Buriano e la diga della Penna e le zone intorno, nei comuni di Arezzo, Civitella e Laterina.
31. Pieve a Maiano ne è la porta d'accesso meridionale (vedi Pieve a Maiano).
32. Dalle colline scendono i torrenti Esse, Leprone, Trove e Lota, insieme a una fitta rete di borri e fossi.
33. Nella piana i corsi d'acqua fanno parte della grande opera di bonifica della Val di Chiana, e nei secoli sono stati più volte regimati.
```

---

## Lavoro e sapori (`lavoro-e-sapori.html`): N3 · 62 frasi

**Parte 1 di 2**

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Lavoro e sapori», parte 1 di 2. Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Le industrie della piana, una grande fabbrica che non c'è più, e l'olio e il vino delle colline.
2. Il territorio di Civitella ha due anime economiche.
3. In pianura si sono sviluppate le aree produttive di Badia al Pino, Tegoleto, Pieve al Toppo e Viciomaggio.
4. Sulle colline restano gli olivi, le vigne e le aziende agricole a conduzione familiare, attorno a cui il Comune e Slow Food Valdichiana costruiscono buona parte del calendario delle feste.
5. Cittaslow: dal 2002
6. Città dell'Olio: dal 2025
7. CEIA: dal 1968 (Viciomaggio)
8. Chimet: dal 1974 (Badia al Pino e Viciomaggio)
9. Accanto a poche grandi aziende, il tessuto produttivo è fatto di piccole e medie imprese artigiane, in particolare nei settori dell'oreficeria, del legno e delle calzature.
10. Il Piano Strutturale individua le aree produttive di Badia al Pino, Pieve al Toppo e Tegoleto, l'area industriale di Viciomaggio e tre zone industriali isolate: quelle della Del Tongo e della Chimet e una terza in località Le Caserosse, nella pianura tra Viciomaggio e Pieve al Toppo.
11. Il Piano Operativo del 2023 non prevede nuove aree industriali, perché considera il territorio ormai saturo: restano soltanto le superfici produttive già previste in passato e non ancora realizzate.
12. Progetta e costruisce metal detector e sistemi di ispezione elettromagnetica, per la sicurezza e per l'industria, venduti in tutto il mondo.
13. Ha sede nella zona industriale di Viciomaggio.
14. Brevetto e prime produzioni di metal detector per l'industria tessile.
15. 1962
16. Costituzione della società.
17. 1968
18. I primi metal detector per gli aeroporti.
19. 1975
20. Recupera e affina i metalli preziosi contenuti negli scarti industriali: elettronici, fotografici, galvanici, farmaceutici, chimici e orafi.
21. Fondazione.
22. 1974
23. Primo stabilimento a Badia al Pino.
24. 1976
25. Secondo stabilimento a Viciomaggio.
26. Anni Ottanta
27. Legata al distretto orafo aretino è anche Zone Creative, a Badia al Pino, che costruisce macchinari per l'oreficeria.
28. Per oltre sessant'anni il nome di Tegoleto è stato legato a quello delle cucine Del Tongo.
29. L'azienda oggi non esiste più, ma ha segnato l'economia della piana e anche la storia del ciclismo.
30. I fratelli Stefano e Pasquale Del Tongo fondano a Tegoleto l'azienda di cucine componibili, che arriverà a venderle in tutto il mondo.
31. 1954
32. Sponsorizza una squadra ciclistica professionistica che vince due Giri d'Italia (Giuseppe Saronni nel 1983 e Franco Chioccioli nel 1991), 29 tappe del Giro, la Milano-Sanremo 1983 e due Giri di Lombardia (1982 e 1986).
33. Con questa maglia esordisce tra i professionisti Mario Cipollini.
34. 1982–1991
35. La quarta tappa del Giro d'Italia arriva a Tegoleto, davanti allo stabilimento; la vince Alessandro Petacchi.
```

**Parte 2 di 2**

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Lavoro e sapori», parte 2 di 2. Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
36. 2004
37. Fallimento dell'azienda.
38. 2018
39. Il marchio viene aggiudicato all'asta all'azienda teramana Kico.
40. 2022
41. Sulle colline prevalgono l'olivo e la vite; in pianura, prati e seminativi.
42. Le aziende agricole e gli allevamenti sono per lo più a conduzione familiare, e nel fondovalle e lungo la via Vecchia Senese si allevano cavalli; il Piano Strutturale censisce diversi centri di equitazione, tra cui quelli delle località Fogliarina e La Casina.
43. Secondo il Piano Operativo l'agriturismo è un settore ancora in crescita.
44. Vino.
45. Il vitigno principale è il Sangiovese.
46. Il territorio rientra nelle denominazioni Chianti DOCG, Chianti Colli Aretini DOCG, Colli dell'Etruria Centrale DOC e Vin Santo del Chianti, e nella zona del Bianco Vergine della Valdichiana, oggi Valdichiana Toscana DOC.
47. Il Bianco Vergine è DOC dai primi anni Settanta: Cittaslow indica il 1972, altre fonti il 1970.
48. Il Comune fa parte della Strada del Vino Terre di Arezzo.
49. Olio.
50. Le varietà tradizionali sono frantoio, leccino, moraiolo e pendolino, e l'olio rientra nella denominazione Toscano IGP.
51. Dal 2025 Civitella fa parte dell'associazione nazionale Città dell'Olio.
52. Ogni autunno l'olio nuovo è protagonista della rassegna L'Olio Novo.
53. Miele, formaggi e prodotti della terra hanno ciascuno il loro mercato o la loro fiera, dal Mercato del Cacio alla Fiera del Miele: date e luoghi sono nel calendario delle feste.
54. Dal luglio 2002 Civitella fa parte di Cittaslow, la rete internazionale dei comuni che si impegnano a tutelare l'ambiente, i prodotti tipici e le tradizioni contadine.
55. Ha sede a Civitella anche la condotta Slow Food Valdichiana, che con il Comune organizza ogni anno una serie di appuntamenti dedicati ai prodotti del territorio:
56. Mercato dei Sapori e della Terra, ad aprile a Tegoleto.
57. Mercato del Cacio, a maggio nel borgo di Civitella.
58. Calici sotto la Torre, ad agosto nel borgo di Civitella, con i vini della Strada del Vino.
59. Fiera del Miele, la prima domenica di ottobre a Pieve al Toppo.
60. L'Olio Novo, tra novembre e dicembre in varie frazioni.
61. Nelle scuole dell'Istituto comprensivo Martiri di Civitella, Slow Food porta il progetto Orto in Condotta, dedicato all'educazione alimentare e ambientale.
62. Nel febbraio 2026 la Pinacoteca di Civitella ha ospitato l'assemblea regionale di Slow Food Toscana.
```

---

## Feste e associazioni (`feste-e-associazioni.html`): N3 · 71 frasi

**Parte 1 di 3**

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Feste e associazioni», parte 1 di 3. Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Un anno di sagre, mercati e rassegne, e le associazioni che li tengono in vita, frazione per frazione.
2. Quasi ogni frazione ha la sua festa, e dietro quasi ogni festa c'è un circolo, una Pro Loco o una società sportiva.
3. Questa pagina raccoglie il calendario dell'anno, le associazioni del comune e le società sportive.
4. Le date cambiano di anno in anno: prima di mettervi in viaggio, controllate il programma con gli organizzatori.
5. Festa della RosaViciomaggio · A.S.D. ViciomaggioDa fine aprile all'inizio di maggio, con i pranzi del 25 aprile e del 1° maggio.
6. Mercato dei Sapori e della TerraTegoleto · Comune e Slow Food Valdichiana, con Comunità & TegoletoIn piazza della Chiesa; 5ª edizione nel 2024.
7. Sagra dei BaccelliSpoiano · Polisportiva SpoianoDue fine settimana, al circolo del paese; 48ª edizione nel 2025.
8. Mercato del CacioCivitella · Comune e Slow Food ValdichianaIn piazza Lazzeri, con gli ospiti del comune gemellato di Kämpfelbach; 22ª edizione nel 2025.
9. Festa al TegoletoTegoleto · U.S.D. Tegoleto, con Comunità & TegoletoTra fine giugno e inizio luglio; 52ª edizione nel 2025.
10. Marcia per la paceCivitella  San Pancrazio · Comune, con il comune di BucineIl 29 giugno, anniversario dell'eccidio del 1944.
11. Sagra del CrostinoAlbergo · Polisportiva Albergo OlivetoAl campo sportivo, a metà luglio; 51ª edizione nel 2026.
12. Cinema sotto le StelleTegoleto · Comunità & TegoletoProiezioni gratuite il mercoledì sera in piazza della Chiesa; dal 2018.
13. Calici sotto la TorreCivitella · Comune e Slow Food ValdichianaInizio agosto: degustazioni dei vini della Strada del Vino Terre di Arezzo con i sommelier AIS.
14. Sagra del CinghialePieve a Maiano · Circolo ricreativo U.S. Pieve a MaianoDue fine settimana a fine agosto; 42ª edizione nel 2026.
15. Sagra della BisteccaBadia al Pino · Circolo Ricreativo Olinto PaccinelliTra fine agosto e inizio settembre; 46ª edizione nel 2026.
16. Festa dell'uva, del vino e dell'olioCiggiano · Pro Loco di Ciggiano49ª edizione nel 2026: nel 2027 sarà la cinquantesima.
17. Sagra della PescaPieve al Toppo · Circolo ARCI Pieve al ToppoDedicata al frutto, a fine estate.
18. RioFestTegoleto · Comunità & TegoletoFestival di musica, incontri e spettacoli a ingresso gratuito, nato nel 2025.
19. Fiera del MielePieve al Toppo · Comune e Slow Food ValdichianaLa prima domenica di ottobre, nel piazzale del Circolo ricreativo; 22ª edizione nel 2026.
20. L'Olio NovoVarie frazioni · Comune e Slow Food ValdichianaDa metà novembre all'inizio di dicembre, dedicata all'olio extravergine appena franto; 28ª edizione nel 2025.
21. Presepe ViventeOliveto · Parrocchia di OlivetoNel periodo natalizio, tra le vie del borgo; dal 2014.
22. Il calendario comprende solo le feste confermate da almeno una fonte recente.
23. Qualche manifestazione citata in vecchie schede turistiche non ha trovato riscontro, e per questo non compare.
24. L'elenco si basa sul Registro unico nazionale del Terzo settore (RUNTS) e sull'elenco delle società della Consulta comunale dello Sport.
25. Le etichette indicano il tipo di associazione.
26. Pro LocoPro Loco Civitella in Val di Chiana
27. CiboSlow Food Val di Chiana: la condotta locale, con sede a Civitella; con il Comune organizza mercati e fiere in tutto il territorio.
28. SportPolisportiva Albergo Oliveto: ciclismo giovanile; organizza la Sagra del Crostino.
29. SportRamananda Scuola di Yoga Integrale, a Oliveto.
30. CircoloCircolo Ricreativo Olinto Paccinelli: organizza la Sagra della Bistecca.
31. SportS.S. Badiese 1948: calcio, allo stadio comunale.
32. Pro LocoPro Loco di Ciggiano: organizza la Festa dell'uva, del vino e dell'olio.
33. MusicaSocietà Filarmonica Ciggiano: la banda del paese.
34. CircoloUnione Sportiva Pieve a Maiano: circolo ricreativo e sportivo; organizza la Sagra del Cinghiale.
35. CircoloARCI Pieve al Toppo: organizza la Sagra della Pesca.
```

**Parte 2 di 3**

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Feste e associazioni», parte 2 di 3. Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
36. SportPolisportiva Dilettantistica Pieve al Toppo 06: scuola calcio, allo stadio di via del Sembolino.
37. SportLet Me Dance: danza classica, moderna, contemporanea e aerea, e ginnastica.
38. CircoloCircolo MCL Spoiano
39. SportPolisportiva Spoiano: organizza la Sagra dei Baccelli.
40. CulturaComunità & Tegoleto: organizza il RioFest e Cinema sotto le Stelle, e collabora alla Festa al Tegoleto.
41. CulturaGruppo Teatro La Torre: gestisce il Teatro Moderno, con la stagione da ottobre a marzo e gli spettacoli amatoriali del gruppo.
42. CircoloCircolo Sportivo Tegoleto (ACLI)
43. SportU.S.D.
44. Tegoleto 1970: calcio, dalla scuola calcio alla prima squadra, allo stadio di via del Chiassobuio; organizza la Festa al Tegoleto.
45. SportTegoleto Volley: pallavolo per bambini e ragazzi.
46. SportTaekyon Club: taekwondo per bambini e ragazzi.
47. CircoloCircolo Sportivo Viciomaggio
48. SportA.S.D.
49. Viciomaggio: organizza la Festa della Rosa.
50. SportAssociazione Dilettantistica Equestre Fogliarina, in località Fogliarina.
51. SportLa Casina: centro di equitazione in località La Casina.
52. VolontariatoGruppo Fratres MonteCivi: donatori di sangue.
53. VolontariatoAnimali Senza Casa Arezzo: volontariato per gli animali.
54. AmbienteComitato dei cittadini per la salute e l'ambiente
55. Nel RUNTS sono iscritte con sede nel comune anche il Centro di aggregazione sociale La Torre, Sentieri in Comune, Archetypus, Amici di Moba e Consulta per il futuro, ma il registro non indica né la frazione né le attività.
56. Il Centro La Torre è un ente distinto dal Gruppo Teatro La Torre di Tegoleto.
57. Il Comune tiene anche un albo delle associazioni, che però non è pubblicato online.
58. Nel 2022 il Comune ha istituito la Consulta comunale dello Sport, che riunisce le società del territorio.
59. Ecco gli impianti, frazione per frazione.
60. Badia al Pino: lo stadio comunale con la pista, usata anche per il ciclismo giovanile, il palazzetto dello sport e l'area sportiva della scuola media, da poco riqualificata.
61. Badia al Pino
62. Tegoleto: lo stadio di via del Chiassobuio e la palestra della scuola primaria Arcobaleno.
63. Tegoleto
64. Pieve al Toppo: lo stadio di via del Sembolino e un nuovo campo polivalente a uso libero.
65. Pieve al Toppo
66. Albergo: il campo sportivo e un nuovo campo polivalente a uso libero.
67. Albergo
68. Spoiano, Pieve a Maiano e Viciomaggio: i campi dei circoli e delle società locali.
69. La storia sportiva del comune passa per il ciclismo.
70. Tra il 1982 e il 1991 la squadra professionistica sponsorizzata dalle cucine Del Tongo di Tegoleto vinse due Giri d'Italia, con Giuseppe Saronni e Franco Chioccioli, e nel 2004 una tappa del Giro arrivò proprio a Tegoleto.
```

**Parte 3 di 3**

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Feste e associazioni», parte 3 di 3. Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
71. La storia completa è nella pagina Lavoro e sapori.
```

---

## Home (`index.html`): prima N1, poi seconda passata in N3 · 9 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Home». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Un piccolo archivio dedicato a Civitella in Val di Chiana: un comune composto da un borgo storico e tredici frazioni, tra le colline aretine e la pianura della Val di Chiana.
2. Civitella in Val di Chiana è un comune di circa 8.800 abitanti situato a una quindicina di chilometri a sud-ovest di Arezzo.
3. Il capoluogo storico, un borgo collinare a circa 500 metri di altezza con la sua Rocca medievale, convive con tredici frazioni sparse tra le colline e la pianura della Val di Chiana — dove oggi vive la maggior parte della popolazione.
4. 8.814 abitanti (ISTAT 2021)
5. 13 frazioni oltre al capoluogo
6. 500 m la Rocca sul colle
7. Dalle origini etrusco-romane ai vescovi di Arezzo, dalla podesteria fiorentina all'eccidio nazifascista del 1944 e alla Marcia per la pace che lo ricorda: un percorso attraverso i secoli che hanno segnato il territorio.
8. Un territorio a cavallo tra le prime propaggini dell'Appennino e la pianura della Val di Chiana, con vigneti di Chianti Colli Aretini e oliveti che ne disegnano il paesaggio.
9. Civitella (capoluogo storico), Albergo, Badia al Pino, Ciggiano, Cornia, Gebbia, Oliveto, Pieve a Maiano, Pieve al Toppo, Ponticino, Spoiano, Tegoleto, Tuori e Viciomaggio, più i borghi minori come Matroia e Montoto: quattordici volti dello stesso comune.
```

---

## Le frazioni (indice) (`frazioni.html`): prima N1, poi seconda passata in N3 · 2 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Le frazioni (indice)». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Il capoluogo storico, le tredici frazioni del comune e i borghi minori.
2. Ogni pagina racconta storia, monumenti e vita locale della frazione, con i dati del censimento 2021 e le fonti usate — il lavoro procede per iterazioni successive.
```

---

## Amministrazione (`amministrazione.html`): prima N1, poi seconda passata in N3 · 21 frasi

```
Sei un verificatore rigoroso. Qui sotto ci sono frasi pubblicate sul sito «Civitella in Pillole», pagina «Amministrazione». Controlla OGNI frase usando SOLO le fonti di questo notebook.
Per ciascuna frase rispondi su una riga:
N. | ESITO | passaggio esatto tra virgolette | documento
ESITO deve essere uno di questi:
- CONFERMATA: ogni dettaglio (nomi, date, numeri, luoghi, secoli, e parole come «più antico», «unico», «principale», «tutelato», «oggi») è scritto esplicitamente nelle fonti;
- PARZIALE: solo una parte è scritta nelle fonti; indica con precisione quale parte NON lo è;
- SMENTITA: le fonti dicono una cosa diversa; cita cosa dicono;
- NON PRESENTE: le fonti non ne parlano.
Non dedurre, non fare calcoli, non usare conoscenze generali. Se un dettaglio non è scritto esplicitamente, la frase è PARZIALE.
Alla fine elenca SOLO le frasi PARZIALE o SMENTITA, ciascuna con una riformulazione che usi soltanto ciò che è scritto nelle fonti.

FRASI:
1. Sindaco, giunta e consiglio comunale in carica dal 2021.
2. Questa pagina riguarda persone reali attualmente in carica: i dati su sindaco e giunta sono verificati sulle rispettive pagine ufficiali del sito del Comune; consiglio comunale e storico elettorale si basano anche su un aggregatore non istituzionale (tuttitalia.it) e andrebbero riconfermati periodicamente.
3. Il sindaco in carica è Andrea Tavarnesi, della lista civica "Solidarietà e Progresso", eletto il 3-4 ottobre 2021 e insediatosi il 23 ottobre 2021.
4. Le sue deleghe dirette comprendono pianificazione del territorio, urbanistica ed edilizia, sanità e sociale, personale, bilancio, ambiente, politiche energetiche e innovazione tecnologica.
5. Gian Luca Lucchetti — vicesindaco: attività produttive e commercio, promozione del territorio e turismo, polizia municipale e protezione civile.
6. Ivano Capacci — assessore: lavori pubblici, patrimonio, manutenzioni, decoro urbano, viabilità, politiche agricole.
7. Serena Nardi — assessore: politiche scolastiche, pari opportunità, politiche per l'accoglienza e l'integrazione.
8. Claudia Del Tongo — assessore: politiche sportive, rapporti con le associazioni e il volontariato, politiche giovanili e cultura.
9. La giunta si è insediata tra il 4 e il 23 ottobre 2021;
10. Tavarnesi era già stato assessore nella precedente giunta guidata da Ginetta Menchetti.
11. Il consiglio eletto nell'ottobre 2021 è composto da 8 consiglieri di maggioranza (lista "Solidarietà e Progresso") e 4 di opposizione (lista "Il Governo dei Cittadini", guidata dalla candidata sindaca Rosaria Migliore).
12. Maggioranza: Silvia Donati, Serena Fabbriciani, Cristina Lanini, Ginetta Menchetti (ex sindaca), Daniele Ortaggi, Paolo Randellini, Luca Terrazzi.
13. Opposizione: Rosaria Migliore, Fabio Badii, Dante Moretti, Luca Veneri, Luca Zeffiri.
14. Alle amministrative del 3-4 ottobre 2021, Andrea Tavarnesi ("Solidarietà e Progresso") ha ottenuto il 65,47% dei voti (2.853 voti) contro il 34,53% di Rosaria Migliore ("Il Governo dei Cittadini", 1.505 voti).
15. L'affluenza è stata del 62,47% (4.546 votanti su 7.277 aventi diritto).
16. Gilberto Dindalini (PCI poi PDS, poi lista civica): sindaco dal 1988 al 2001, con una breve gestione commissariale (dott.ssa Rosalba Guarino) tra dicembre 1992 e giugno 1993.
17. Massimiliano Dindalini (lista civica, poi centrosinistra): sindaco dal 2001 al 2011.
18. Ginetta Menchetti (lista civica "Solidarietà e Progresso"): sindaca dal 2011 al 2021, per due mandati.
19. Andrea Tavarnesi (lista civica "Solidarietà e Progresso"): sindaco dal 2021, in carica.
20. Per i sindaci precedenti al 1988 non è stata reperita una fonte affidabile: andrebbero cercati nell'archivio storico comunale.
21. Le fonti usate per il sito sono elencate nella pagina Fonti.
```
