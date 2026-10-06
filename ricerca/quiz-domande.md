# Domande del quiz

Elenco leggibile del pool usato da `quiz.html`. **Non modificarlo a mano:** le domande si cambiano in `tools/quiz_domande.py`, poi si lancia `python3 tools/genera_quiz.py`, che rigenera questo file e `js/quiz-data.js`.

**Regola:** ogni domanda nasce da un fatto di livello R, N o W in `fatti-verificati.md`, mai da un fatto su cui le fonti divergono.

L'**id** tra parentesi quadre è quello che compare nel foglio delle statistiche; il livello (●○○ facile, ●●○ media, ●●● difficile) e il codice che lo determina sono spiegati in `tools/quiz_difficolta.py`.

Totale: 309 domande.

## Geografia (42)

1. [5a86694d] ●●● `Nv=` **Quanti residenti contava il comune al censimento ISTAT del 2021?**  
   ✔ 8.814 · ✘ 6.512 · 11.230 · 15.400  
   _Al censimento 2021 il comune contava 8.814 residenti._ → `geografia.html`
2. [ebc792a8] ●●○ `-v=` **Qual è il centro abitato più popoloso del comune?**  
   ✔ Pieve al Toppo · ✘ Badia al Pino · Civitella · Ciggiano  
   _Pieve al Toppo, con 1.545 residenti nel 2021, è il centro più popoloso._ → `geografia.html`
3. [eec92ec8] ●●○ `-v=` **Quale centro è il secondo per numero di abitanti, dopo Pieve al Toppo?**  
   ✔ Tegoleto · ✘ Ciggiano · Albergo · Spoiano  
   _Tegoleto contava 1.412 residenti nel 2021._ → `geografia.html`
4. [3224d171] ●●○ `Nn=` **Quanto è esteso, all'incirca, il territorio comunale?**  
   ✔ Circa 100 km² · ✘ Circa 20 km² · Circa 300 km² · Circa 600 km²  
   _La superficie del comune è di 100,33 km²._ → `geografia.html`
5. [e4b714c5] ●○○ `-n=` **Dove si trova Civitella in Val di Chiana rispetto ad Arezzo?**  
   ✔ A circa 15 km a sud-ovest · ✘ A circa 15 km a nord-est · A circa 60 km a nord · A circa 40 km a est  
   _Civitella sorge a circa 15 km a sud-ovest di Arezzo._ → `geografia.html`
6. [b23a93db] ●●○ `-v=` **Con quale di questi comuni confina Civitella in Val di Chiana?**  
   ✔ Monte San Savino · ✘ Cortona · Montevarchi · Siena  
   _Il comune confina con Arezzo, Bucine, Laterina Pergine Valdarno e Monte San Savino._ → `geografia.html`
7. [e3946457] ●●○ `-v=` **Quale di questi comuni NON confina con Civitella in Val di Chiana?**  
   ✔ Cortona · ✘ Arezzo · Bucine · Laterina Pergine Valdarno  
   _I comuni confinanti sono Arezzo, Bucine, Laterina Pergine Valdarno e Monte San Savino._ → `geografia.html`
8. [4746e93c] ●○○ `Pd=` **Su quali colline sorge il capoluogo storico, secondo Wikipedia e ToscanaNovecento?**  
   ✔ Le Colline delle Lepri · ✘ Le Colline Metallifere · Le colline del Chianti · Le Crete Senesi  
   _Civitella sorge sulle Colline delle Lepri, a circa 500 metri._ → `geografia.html`
9. [fea6dfb9] ●●○ `Nd=` **A quale altitudine sorge, all'incirca, il borgo di Civitella?**  
   ✔ Circa 500 metri · ✘ Circa 150 metri · Circa 900 metri · Circa 1.300 metri  
   _Il capoluogo storico sorge a circa 500 metri sul livello del mare._ → `geografia.html`
10. [f2064462] ●○○ `Pd-` **Tra quali valli si trova il colle di Civitella?**  
   ✔ Valdambra e Valdichiana · ✘ Casentino e Valtiberina · Val d'Orcia e Valdelsa · Mugello e Valdisieve  
   _Il Repertorio del Piano descrive il colle di Civitella «tra Valdambra e Valdichiana»._ → `geografia.html`
11. [75a8fc8f] ●○○ `Pd=` **Quale di questi torrenti scorre nel territorio comunale?**  
   ✔ L'Esse · ✘ L'Ombrone · Il Serchio · La Cecina  
   _Tra i torrenti del territorio ci sono l'Esse, il Leprone, il Trove e la Lota._ → `geografia.html`
12. [e2f25241] ●●○ `Pn=` **Una parte del territorio comunale rientra in quale riserva naturale?**  
   ✔ Ponte a Buriano e Penna · ✘ Lago di Montepulciano · Monte Rufeno · Bosco di Sant'Agnese  
   _La Riserva di Ponte a Buriano e Penna protegge un tratto dell'Arno e si estende nei comuni di Arezzo, Civitella e Laterina._ → `geografia.html`
13. [e65e12bd] ●○○ `-d-` **Quale fiume protegge la Riserva naturale di Ponte a Buriano e Penna?**  
   ✔ L'Arno · ✘ Il Tevere · L'Ombrone · Il Serchio  
   _La riserva protegge il tratto dell'Arno tra Ponte a Buriano e la diga della Penna._ → `geografia.html`
14. [96d34023] ●●○ `-v+` **Quale frazione il Piano Strutturale indica come «porta d'accesso» meridionale alla Riserva di Ponte a Buriano e Penna?**  
   ✔ Pieve a Maiano · ✘ Spoiano · Tegoleto · Oliveto  
   _Il Piano assegna a Pieve a Maiano il ruolo di porta d'accesso meridionale alla Riserva._ → `frazioni/pieve-a-maiano.html`
15. [1a05018c] ●○○ `Pd=` **Quale vino si produce sulle colline del comune?**  
   ✔ Il Chianti Colli Aretini · ✘ Il Brunello di Montalcino · Il Morellino di Scansano · La Vernaccia di San Gimignano  
   _Nella fascia collinare si producono vigneti di Chianti Colli Aretini._ → `geografia.html`
16. [607cb6d7] ●○○ `-d=` **Come sono sistemati, tradizionalmente, gli oliveti sui pendii collinari?**  
   ✔ Su terrazzamenti e ciglionamenti · ✘ In serre riscaldate · In risaie allagate · Su terreni sabbiosi di duna  
   _La Relazione del Piano descrive oliveti su terrazzamenti sostenuti da muri in pietra o ciglionamenti._ → `geografia.html`
17. [878f8be1] ●●● `Nn+` **Circa quanti abitanti del comune vivono in case sparse, fuori dai centri abitati?**  
   ✔ Circa un quarto · ✘ Quasi nessuno · Circa tre quarti · Più del 90%  
   _Al censimento 2021 le case sparse contavano 2.256 residenti su 8.814._ → `geografia.html`
18. [b051cf1f] ●●○ `-v=` **Quale frazione è divisa tra Civitella e il comune di Laterina Pergine Valdarno?**  
   ✔ Ponticino · ✘ Tuori · Cornia · Spoiano  
   _Ponticino è a cavallo del confine comunale; il centro abitato è attribuito dall'ISTAT a Laterina Pergine Valdarno._ → `frazioni/ponticino.html`
19. [7a620330] ●●○ `Pn+` **Con quale comune tedesco è gemellato Civitella in Val di Chiana?**  
   ✔ Kämpfelbach · ✘ Heidelberg · Rosenheim · Bamberga  
   _I rappresentanti di Kämpfelbach partecipano ogni anno al Mercato del Cacio._ → `frazioni/civitella.html`
20. [608e57f8] ●●○ `Nn=` **Da quando Civitella fa parte della rete Cittaslow?**  
   ✔ Dal 2002 · ✘ Dal 1985 · Dal 2015 · Dal 2023  
   _Il comune aderisce a Cittaslow dal luglio 2002._ → `lavoro-e-sapori.html`
21. [f5a0d8d3] ●●● `Nn+` **In quale anno Civitella è entrata nell'associazione Città dell'Olio?**  
   ✔ 2025 · ✘ 1998 · 2008 · 2016  
   _Civitella fa parte delle Città dell'Olio dal 2025._ → `lavoro-e-sapori.html`
22. [38fd6d61] ●○○ `-d+` **Che cosa è stato trovato nel 2004 in località La Cascinella, presso Ciggiano?**  
   ✔ Tracce di un insediamento etrusco e romano · ✘ Una nave medievale · Un tesoro di monete d'oro · Un mosaico bizantino  
   _Frammenti di macine etrusche, tegole e vasellame romani della prima età imperiale._ → `frazioni/ciggiano.html`
23. [c7eef4ea] ●○○ `-d+` **Secondo Visit Tuscany, che cosa è stato trovato nella chiesa di San Pietro a Ciggiano?**  
   ✔ Reperti con iscrizioni etrusche · ✘ Un affresco di Giotto · Una nave romana · Un codice miniato  
   _Secondo il portale turistico della Regione, i reperti etruschi di Viciomaggio e di San Pietro a Ciggiano attestano un abitato antico._ → `frazioni/ciggiano.html`
24. [eab967e7] ●●○ `Nd+` **Fino a che spessore arrivano i muri del Castellare di Sant'Angelo, presso Cornia?**  
   ✔ Circa un metro e mezzo · ✘ Circa dieci centimetri · Circa cinque metri · Circa dieci metri  
   _I muri di pietra, forse resti di un vicus romano rioccupato in età longobarda, sono spessi fino a un metro e mezzo._ → `frazioni/cornia.html`
25. [1526724b] ●●○ `Pn+` **Su segnalazione di chi furono scoperte le fornaci romane in località I Ponti, a Pieve al Toppo?**  
   ✔ Del Gruppo Archeologico del Dopolavoro Ferroviario di Arezzo · ✘ Di un parroco del paese · Della Soprintendenza di Firenze durante un restauro · Di una scuola elementare  
   _Le strutture, a circa 1,60 m di profondità, sono interpretate come fornaci per la terra sigillata aretina._ → `frazioni/pieve-al-toppo.html`
26. [5b8c6dd0] ●●○ `-n+` **Quale reperto da Viciomaggio è conservato al Museo Archeologico Nazionale di Arezzo?**  
   ✔ Un cammeo di diaspro · ✘ Un'anfora greca · Una statua di bronzo · Un elmo longobardo  
   _Al Museo «Gaio Cilnio Mecenate» è conservato il cammeo; i vasi del I secolo a.C. sono invece in luogo sconosciuto._ → `frazioni/viciomaggio.html`
27. [dc640362] ●○○ `-d=` **Che cosa prevede il Piano Strutturale per l'area di Cornia?**  
   ✔ Un parco faunistico e un'area naturale protetta · ✘ Una zona industriale · Un aeroporto · Una diga  
   _Il Piano prevede il Parco Faunistico Naturalistico, l'ANPIL di Cornia e un centro servizi negli edifici inutilizzati del borgo._ → `frazioni/cornia.html`
28. [20b4867a] ●○○ `-d=` **Tra quali località si estende il tratto dell'Arno protetto dalla Riserva naturale di Ponte a Buriano e Penna?**  
   ✔ Tra Ponte a Buriano e la diga della Penna · ✘ Tra Firenze e Pontassieve · Tra Stia e Poppi · Tra Empoli e Pisa  
   _La Riserva protegge il tratto dell'Arno tra Ponte a Buriano e la diga della Penna._ → `geografia.html`
29. [848435e4] ●●○ `Nd=` **Tra quali quote si trovano i centri abitati del comune, secondo Cittaslow?**  
   ✔ Tra circa 300 e 600 metri · ✘ Tra 0 e 100 metri · Tra 800 e 1.200 metri · Tra 1.200 e 1.500 metri  
   _I centri abitati del comune stanno tra circa 300 e 600 metri di quota._ → `geografia.html`
30. [4298beed] ●○○ `-v-` **La pianura del comune è la parte settentrionale di quale valle?**  
   ✔ La Val di Chiana · ✘ Il Valdarno · La Val d'Orcia · Il Casentino  
   _Il territorio ha una zona collinare e una di pianura, che è la parte settentrionale della Val di Chiana._ → `geografia.html`
31. [a852afc3] ●○○ `Pd=` **Quale di questi è uno dei torrenti principali del comune, insieme a Esse, Trove e Lota?**  
   ✔ Il Leprone · ✘ L'Arbia · La Merse · Il Bisenzio  
   _I torrenti principali sono Esse, Leprone, Trove e Lota._ → `geografia.html`
32. [4d63ebae] ●●● `Nn+` **Quanti residenti contava Pieve al Toppo, il centro più popoloso del comune, al censimento del 2021?**  
   ✔ 1.545 · ✘ 545 · 3.545 · 6.200  
   _Al censimento ISTAT 2021 Pieve al Toppo contava 1.545 residenti, davanti a Tegoleto (1.412)._ → `geografia.html`
33. [52faadf9] ●●○ `-v+` **Quale centro è il terzo per numero di abitanti, dopo Pieve al Toppo e Tegoleto?**  
   ✔ Badia al Pino · ✘ Viciomaggio · Ciggiano · Albergo  
   _Al censimento 2021 Badia al Pino contava 1.059 residenti, Viciomaggio 950._ → `geografia.html`
34. [729c801a] ●●● `Nv+` **Quanti residenti contava il borgo di Civitella, il capoluogo storico, al censimento del 2021?**  
   ✔ 148 · ✘ 1.480 · 2.300 · 15  
   _Il borgo storico contava 148 residenti; la maggior parte degli abitanti vive in pianura._ → `geografia.html`
35. [2a6d43b8] ●●○ `-v+` **Quale di queste località era la meno popolosa al censimento del 2021?**  
   ✔ Oliveto · ✘ Tuori · Spoiano · Albergo  
   _Oliveto contava 15 residenti, Spoiano 120, Tuori 129, Albergo 279._ → `geografia.html`
36. [dc924e7d] ●●○ `-v+` **Quale frazione contava circa 950 residenti al censimento del 2021?**  
   ✔ Viciomaggio · ✘ Ciggiano · Albergo · Tuori  
   _Viciomaggio contava 950 residenti, Ciggiano 530, Albergo 279, Tuori 129._ → `geografia.html`
37. [3589ff26] ●●○ `-v+` **Di quale epoca sono gli strumenti in pietra trovati al Podere Casella, presso Pieve a Maiano?**  
   ✔ Del Paleolitico medio e superiore · ✘ Dell'età del bronzo · Dell'età del ferro · Del Neolitico finale  
   _Il Repertorio del Piano segnala al Podere Casella strumenti del Paleolitico medio e superiore._ → `frazioni/pieve-a-maiano.html`
38. [414fd435] ●●○ `-v+` **Dove è stato individuato un insediamento romano del I-II secolo d.C. a Pieve a Maiano?**  
   ✔ Al campo sportivo · ✘ Sotto la chiesa · Nel cimitero · Lungo la ferrovia  
   _Il Repertorio segnala un insediamento romano al campo sportivo e una fornace a Vallimboi._ → `frazioni/pieve-a-maiano.html`
39. [e19b1b46] ●●● `Pv+` **In quale località di Pieve a Maiano c'era una fornace romana?**  
   ✔ Vallimboi · ✘ I Ponti · Le Fosse · Tribbio  
   _Vicino all'insediamento romano del campo sportivo c'era la fornace di Vallimboi; le fornaci de I Ponti sono a Pieve al Toppo._ → `frazioni/pieve-a-maiano.html`
40. [aae10fe5] ●●○ `-n+` **Quale ritrovamento attesta l'origine romana di Spoiano?**  
   ✔ Un tesoretto di monete romane · ✘ Un anfiteatro · Un mosaico pavimentale · Un tratto di acquedotto  
   _A Spoiano è stato trovato un tesoretto di monete romane._ → `frazioni/spoiano.html`
41. [3b033cf0] ●●● `Pv+` **A quale epoca risale l'urna etrusca con iscrizione trovata a Viciomaggio nel 1872?**  
   ✔ All'età ellenistica · ✘ All'età villanoviana · All'età del bronzo · All'età longobarda  
   _Nel 1872 a Viciomaggio fu trovata un'urna etrusca di età ellenistica con un'iscrizione._ → `frazioni/viciomaggio.html`
42. [1ab2c013] ●○○ `Pd=` **Di quale catena collinare è una propaggine la zona collinare del comune?**  
   ✔ I Preappennini toscani · ✘ Le Alpi Apuane · Il Monte Amiata · Le Colline Metallifere  
   _La parte collinare e di bassa montagna, coperta di boschi, è una propaggine dei Preappennini toscani._ → `index.html`

## Storia (48)

1. [fe9e42b2] ●●● `Nv=` **A quale anno risale la prima notizia del castello di Civitella?**  
   ✔ 1048 · ✘ 1288 · 1385 · 1527  
   _Il castello di Civitella è ricordato per la prima volta nel 1048._ → `storia.html`
2. [db28ef0d] ●○○ `-d-` **Che cosa era il colle di Civitella in epoca longobarda?**  
   ✔ Una roccaforte a controllo del territorio · ✘ Un porto fluviale · Un monastero femminile · Una zecca  
   _Già frequentata in epoca etrusca e romana, Civitella divenne una roccaforte longobarda._ → `storia.html`
3. [3dd6026e] ●●○ `Pv=` **Quale vescovo di Arezzo scelse nel 1248 la rocca di Civitella come propria dimora?**  
   ✔ Guglielmino degli Ubertini · ✘ Guido Tarlati · Immone · Lorenzo de' Medici  
   _Nel 1248 Guglielmino degli Ubertini scelse la rocca come dimora e ne potenziò le mura._ → `storia.html`
4. [d6478a7e] ●○○ `-d+` **Che aspetto aveva la rocca di Civitella nel 1182, secondo il Repertorio del Piano?**  
   ✔ Quello di un palazzo-torrione · ✘ Quello di una villa rinascimentale · Quello di una fortezza a stella · Quello di una chiesa romanica  
   _Nel 1182 la rocca aveva già l'aspetto di un palazzo-torrione._ → `frazioni/civitella.html`
5. [2fd2d624] ●●● `Nv=` **In quale anno Firenze fece di Civitella il capoluogo di una propria podesteria?**  
   ✔ 1385 · ✘ 1248 · 1527 · 1774  
   _Nel 1385, acquisiti Arezzo e il suo contado, Firenze staccò Civitella dalla podesteria di Valdambra._ → `storia.html`
6. [edd96569] ●●○ `Pv=` **Da quale podesteria fu staccata Civitella nel 1385?**  
   ✔ Valdambra · ✘ Casentino · Valtiberina · Valdarno  
   _Civitella fu scorporata dalla podesteria di Valdambra e divenne capoluogo di una propria circoscrizione._ → `storia.html`
7. [b9e45476] ●●● `Nv=` **Fino a quale anno durò la podesteria di Civitella?**  
   ✔ 1838 · ✘ 1385 · 1774 · 1917  
   _La podesteria di Civitella fu soppressa con la riforma del 1838._ → `storia.html`
8. [77748394] ●●● `Nv=` **In quale anno le comunità di Ciggiano, Viciomaggio e Badia al Pino e il castello di Montarfoni furono aggregati alla Comunità di Civitella?**  
   ✔ 1774 · ✘ 1385 · 1838 · 1917  
   _L'aggregazione avvenne nel 1774._ → `storia.html`
9. [b929883a] ●●○ `Nv-` **In quale anno la sede comunale fu trasferita da Civitella a Badia al Pino?**  
   ✔ 1917 · ✘ 1861 · 1946 · 1774  
   _Nel 1917 la sede comunale fu trasferita a Badia al Pino._ → `storia.html`
10. [4ffa7202] ●○○ `-d=` **Perché nel 1917 la sede comunale fu trasferita a Badia al Pino?**  
   ✔ Per lo spopolamento delle zone collinari · ✘ Per un terremoto · Per un'alluvione · Per ordine del Granduca  
   _Lo spopolamento della collina aveva reso le frazioni di pianura molto più popolose del borgo di Civitella._ → `storia.html`
11. [32504015] ●●○ `Nv-` **In quale anno fu combattuta la battaglia di Pieve al Toppo?**  
   ✔ 1288 · ✘ 1260 · 1385 · 1530  
   _La battaglia fu combattuta il 26 giugno 1288._ → `frazioni/pieve-al-toppo.html`
12. [1e4dc6a7] ●●○ `-v=` **Chi vinse la battaglia di Pieve al Toppo del 1288?**  
   ✔ Gli aretini · ✘ I senesi · I fiorentini · I pisani  
   _Gli aretini ghibellini tesero un'imboscata ai senesi guelfi e ne fecero strage._ → `frazioni/pieve-al-toppo.html`
13. [571968bf] ●○○ `Pn-` **Quale poeta ricorda la battaglia di Pieve al Toppo come le «giostre del Toppo»?**  
   ✔ Dante Alighieri · ✘ Francesco Petrarca · Giovanni Boccaccio · Niccolò Machiavelli  
   _Dante la ricorda nel XIII canto dell'Inferno._ → `frazioni/pieve-al-toppo.html`
14. [1230b87b] ●●● `Nv+` **In quale canto dell'Inferno Dante ricorda le «giostre del Toppo»?**  
   ✔ Il XIII · ✘ Il V · Il XXVI · Il XXXIII  
   _Le «giostre del Toppo» compaiono nel XIII canto, tra gli scialacquatori._ → `frazioni/pieve-al-toppo.html`
15. [a95227b3] ●●● `Pv+` **Quale personaggio, caduto nella battaglia di Pieve al Toppo, compare nell'Inferno di Dante?**  
   ✔ Lano da Siena · ✘ Farinata degli Uberti · Pier della Vigna · Brunetto Latini  
   _Lano da Siena compare tra gli scialacquatori nel XIII canto._ → `frazioni/pieve-al-toppo.html`
16. [a7c46ad1] ●○○ `-d-` **Che cosa distrusse la rocca di Civitella?**  
   ✔ Un bombardamento alleato · ✘ Un terremoto · Un incendio nel Settecento · Un assedio fiorentino  
   _La rocca longobarda fu distrutta da un bombardamento alleato._ → `frazioni/civitella.html`
17. [fb55e686] ●●● `Nv=` **In quale anno a Villa Oliveto fu istituito un campo di internamento?**  
   ✔ 1940 · ✘ 1915 · 1936 · 1944  
   _Il campo fu istituito nel giugno 1940._ → `frazioni/oliveto.html`
18. [b5f15efd] ●○○ `-n=` **Chi era internato soprattutto nel campo di Villa Oliveto?**  
   ✔ Famiglie ebree britanniche provenienti dalla Libia · ✘ Prigionieri di guerra americani · Soldati tedeschi · Profughi istriani  
   _Il campo ospitò soprattutto famiglie ebree di nazionalità britannica provenienti dalla Libia._ → `frazioni/oliveto.html`
19. [71ecaade] ●●○ `Pv=` **Dove furono deportate nel 1944 le famiglie internate a Villa Oliveto?**  
   ✔ A Bergen-Belsen · ✘ A Dachau · A Mauthausen · A Buchenwald  
   _Nel 1944 furono deportate a Bergen-Belsen._ → `frazioni/oliveto.html`
20. [bebf7d33] ●●○ `-v=` **Da quale espressione latina deriva il nome di Viciomaggio?**  
   ✔ Vicus maior · ✘ Via magna · Villa maior · Vicus Martis  
   _Vicus maior significa «villaggio maggiore»._ → `frazioni/viciomaggio.html`
21. [26c46d87] ●○○ `-n=` **Di quale origine è, quasi sicuramente, il toponimo «Toppo»?**  
   ✔ Longobarda · ✘ Etrusca · Araba · Francese  
   _Le fonti indicano «Toppo» come toponimo quasi sicuramente longobardo._ → `frazioni/pieve-al-toppo.html`
22. [d150c402] ●○○ `-n=` **Da che cosa deriva il nome «Maiano»?**  
   ✔ Dal nome di un proprietario romano, probabilmente un Marius · ✘ Dal mese di maggio · Da una famiglia medievale fiorentina · Da una divinità etrusca  
   _«Maiano» è un toponimo prediale romano, da Marius._ → `frazioni/pieve-a-maiano.html`
23. [bb0a87e4] ●○○ `-d=` **Da che cosa prende il nome Tribbio?**  
   ✔ Da un trivio, un incrocio di tre strade · ✘ Da una tribù etrusca · Da un tribunale medievale · Da un torrente  
   _Il nome viene dal trivium, l'incrocio di tre strade; il Repertorio lo cataloga come trivio, forse di età romana._ → `frazioni/borghi-minori.html#tribbio`
24. [410b1cb5] ●●○ `Nn=` **In quale anno il titolo di pieve e il fonte battesimale passarono dalla Pieve al Toppo a Badia al Pino?**  
   ✔ 1502 · ✘ 1288 · 1774 · 1917  
   _Nel 1502, distrutta la pieve del Toppo, il titolo di pieve passò alla chiesa di Badia al Pino._ → `frazioni/badia-al-pino.html`
25. [c87b3b73] ●●● `Nn+` **In quale anno fu soppressa la Badia del Pino?**  
   ✔ 1441 · ✘ 1288 · 1774 · 1917  
   _Dopo la soppressione della Badia, nel 1441, il paese divenne un insediamento essenzialmente rurale._ → `frazioni/badia-al-pino.html`
26. [7a384985] ●●○ `Nn=` **In quale anno furono distrutti la pieve e l'ospedale per i pellegrini di Pieve al Toppo?**  
   ✔ 1502 · ✘ 1288 · 1385 · 1944  
   _Chiesa e ospedale furono distrutti nel 1502; sul sito sorse poi l'Oratorio della Madonna del Conforto._ → `frazioni/pieve-al-toppo.html`
27. [cb2abf6f] ●○○ `Pd=` **Sotto quali valichi si trova Ciggiano, che ne fecero un nodo strategico?**  
   ✔ Palazzuolo e San Pancrazio · ✘ La Futa e la Raticosa · L'Abetone e la Cisa · I Mandrioli e la Scheggia  
   _La posizione sotto i valichi di Palazzuolo e San Pancrazio fece di Ciggiano una tappa obbligata della dogana fiorentina._ → `frazioni/ciggiano.html`
28. [96a6f855] ●○○ `-n=` **Che cos'era la «calla» che i pastori facevano a Ciggiano?**  
   ✔ La conta degli animali, con il pagamento della gabella · ✘ Una festa per la fine della transumanza · Un mercato della lana · Una gara di tosatura  
   _Gli statuti di dogana fiorentini indicavano Ciggiano come tappa obbligata: qui si faceva la calla e si pagava la gabella._ → `frazioni/ciggiano.html`
29. [523cea0b] ●●● `Pv+` **Le truppe di quale condottiero assediarono e saccheggiarono Ciggiano nel 1431?**  
   ✔ Niccolò Piccinino · ✘ Giovanni Acuto · Castruccio Castracani · Federico da Montefeltro  
   _Nel 1431 Ciggiano fu assediato e saccheggiato dalle truppe di Niccolò Piccinino; nel 1554 subì un altro assedio._ → `frazioni/ciggiano.html`
30. [01491e5c] ●●○ `Pv=` **Quale granduca soppresse nel 1783 la Compagnia di Santa Croce di Ciggiano?**  
   ✔ Pietro Leopoldo · ✘ Cosimo I de' Medici · Ferdinando III · Napoleone Bonaparte  
   _La Compagnia fu soppressa da Pietro Leopoldo nel 1783 e ripristinata nel 1794._ → `frazioni/ciggiano.html`
31. [f4c98a78] ●●● `Pv+` **Quali famiglie, tornate proprietarie del feudo, riedificarono nel Seicento la Casa del Podestà di Oliveto?**  
   ✔ Ubertini e Saracini · ✘ Medici e Pazzi · Guidi e Tarlati · Strozzi e Rucellai  
   _La Casa del Podestà fu riedificata nella prima metà del Seicento dalle famiglie aretine Ubertini e Saracini._ → `frazioni/oliveto.html`
32. [4fcbea87] ●○○ `-d+` **Che cosa diventò all'inizio dell'Ottocento la piazza d'armi del castello di Oliveto?**  
   ✔ Un vigneto e oliveto · ✘ Un mercato coperto · Un cimitero · Un giardino all'italiana  
   _Il palazzo del Podestà divenne casa colonica e granaio, e la piazza fu trasformata in vigneto e oliveto._ → `frazioni/oliveto.html`
33. [f8e908eb] ●○○ `-d=` **Che funzione aveva il castello di Tuori nel Medioevo?**  
   ✔ Era sede di guarnigioni a presidio di Arezzo · ✘ Era la residenza estiva dei Medici · Era un convento fortificato · Era una dogana senese  
   _Tuori divenne un castello sede di guarnigioni militari a presidio della città di Arezzo; ne resta il cassero._ → `frazioni/tuori.html`
34. [7a62a739] ●●● `Nv+` **In quale giorno fu combattuta la battaglia di Pieve al Toppo del 1288?**  
   ✔ Il 26 giugno · ✘ Il 29 giugno · Il 4 luglio · Il 15 agosto  
   _Il 26 giugno 1288 gli aretini ghibellini sconfissero i senesi guelfi._ → `storia.html`
35. [18947b6d] ●●○ `-v=` **Di quale parte erano i senesi sconfitti al Toppo nel 1288?**  
   ✔ Guelfa · ✘ Ghibellina · Imperiale · Dei Bianchi  
   _Gli aretini ghibellini sconfissero i senesi guelfi._ → `frazioni/pieve-al-toppo.html`
36. [4497e778] ●○○ `-d=` **In quali epoche fu frequentato il colle di Civitella, prima di diventare una roccaforte longobarda?**  
   ✔ In epoca etrusca e romana · ✘ Solo dall'età moderna · In epoca normanna · In epoca bizantina e araba  
   _Già frequentata in epoca etrusca e romana, Civitella divenne una roccaforte longobarda._ → `frazioni/civitella.html`
37. [4c4023b6] ●●○ `Pv=` **A presidio di chi sorgevano, dall'XI secolo, le strutture sul colle di Civitella?**  
   ✔ Dei vescovi-conti aretini · ✘ Dei Medici · Della Repubblica di Siena · Dei conti Guidi  
   _Dall'XI secolo sul colle sorgevano strutture a presidio dei vescovi-conti aretini._ → `storia.html`
38. [0a7ac152] ●○○ `-d=` **Che cosa fece alla rocca di Civitella il vescovo Guglielmino degli Ubertini, che nel 1248 la scelse come dimora?**  
   ✔ Ne potenziò le mura · ✘ La fece demolire · La vendette a Firenze · La trasformò in un convento  
   _Nel 1248 Guglielmino degli Ubertini scelse la rocca come dimora e ne potenziò le mura._ → `storia.html`
39. [6869ff95] ●●○ `Pv-` **Quale città acquisì Arezzo e il suo contado prima di fare di Civitella, nel 1385, il capoluogo di una propria podesteria?**  
   ✔ Firenze · ✘ Siena · Perugia · Pisa  
   _Nel 1385 Firenze, acquisiti Arezzo e il suo contado, fece di Civitella il capoluogo di una sua podesteria._ → `storia.html`
40. [cf547452] ●●● `Pv+` **Quale castello fu aggregato alla Comunità di Civitella nel 1774, insieme a Ciggiano, Viciomaggio e Badia al Pino?**  
   ✔ Montarfoni · ✘ Gaenne · Dorna · Montoto  
   _Nel 1774 Ciggiano, Viciomaggio, Badia al Pino e il castello di Montarfoni furono aggregati alla Comunità di Civitella._ → `storia.html`
41. [6a7032b1] ●●● `Nv+` **In quale anno Ciggiano subì un altro assedio, dopo il saccheggio di Niccolò Piccinino del 1431?**  
   ✔ 1554 · ✘ 1385 · 1502 · 1774  
   _Nel 1431 Ciggiano fu saccheggiato dalle truppe di Piccinino e nel 1554 subì un altro assedio._ → `frazioni/ciggiano.html`
42. [5ff357cf] ●●● `Pv+` **Quale altro titolo, oltre a quello di pieve, passò a Badia al Pino nel 1583?**  
   ✔ Quello di Santa Lucia a Campigliano · ✘ Quello di sede vescovile · Quello di abbazia di Vallombrosa · Quello di priorato di Camaldoli  
   _Nel 1502 arrivarono il fonte battesimale e il titolo di pieve, nel 1583 il titolo di Santa Lucia a Campigliano._ → `frazioni/badia-al-pino.html`
43. [d1c40d05] ●●● `Nv+` **In quale anno un documento chiama l'abbazia «Badia di S. Martino e S. Lorenzo al Pino»?**  
   ✔ 1046 · ✘ 1039 · 1441 · 1502  
   _Un documento del 1046 chiama l'abbazia «Badia di S. Martino e S. Lorenzo al Pino»; il 1039 si riferisce alla chiesa._ → `frazioni/badia-al-pino.html`
44. [572b6b97] ●○○ `-n=` **Che cosa c'era accanto all'antica pieve del Toppo?**  
   ✔ Un ospedale per i pellegrini · ✘ Un castello · Un mercato coperto · Un mulino  
   _La pieve, con un ospedale per i pellegrini, fu confermata nel 938 tra i possedimenti del Capitolo di Arezzo._ → `frazioni/pieve-al-toppo.html`
45. [12a183b1] ●●● `Pv+` **Tra i possedimenti di chi fu confermata nel 938 la pieve del Toppo?**  
   ✔ Del Capitolo di Arezzo · ✘ Dell'abbazia di Agnano · Del vescovo di Siena · Dei conti Guidi  
   _Nel 938 la pieve fu confermata tra i possedimenti del Capitolo di Arezzo._ → `frazioni/pieve-al-toppo.html`
46. [3fa9492f] ●●● `Nv+` **In quale mese del 1940 fu istituito il campo di internamento di Villa Oliveto?**  
   ✔ Giugno · ✘ Gennaio · Settembre · Dicembre  
   _Il campo fu istituito nel giugno 1940._ → `frazioni/oliveto.html`
47. [748416c9] ●●○ `-v=` **Da chi fu assediata la rocca di Civitella tra il 1284 e il 1285?**  
   ✔ Dagli aretini · ✘ Dai fiorentini · Dai senesi · Dai pisani  
   _Tra il 1284 e il 1285 la rocca fu assediata dagli stessi aretini che nel 1288 vinsero la battaglia del Toppo._ → `storia.html`
48. [4fe3b32c] ●●● `Nv+` **Quanti piccoli comuni furono aggregati alla Comunità di Civitella nel 1774, secondo il Repertorio del Piano Strutturale?**  
   ✔ Nove · ✘ Tre · Quindici · Venti  
   _Il Repertorio parla di nove piccoli comuni aggregati nel 1774; tra questi gli itinerari del Comune ricordano Ciggiano, Viciomaggio e Badia al Pino._ → `storia.html`

## Il 1944 (28)

1. [3e37b695] ●●○ `Nv-` **In quale data avvenne la strage nazista di Civitella?**  
   ✔ 29 giugno 1944 · ✘ 25 aprile 1945 · 8 settembre 1943 · 4 giugno 1944  
   _La strage avvenne il 29 giugno 1944._ → `storia.html`
2. [75f82986] ●●○ `Pv=` **Quale festa si celebrava a Civitella il giorno della strage del 1944?**  
   ✔ Quella dei santi Pietro e Paolo · ✘ Quella di San Giovanni · L'Assunta · Ognissanti  
   _Il paese era affollato per la festa dei patroni Pietro e Paolo._ → `storia.html`
3. [3440c37a] ●●○ `-v=` **Quale di queste località NON fu colpita dalla strage del 29 giugno 1944?**  
   ✔ Tegoleto · ✘ Cornia · Gebbia · San Pancrazio  
   _La strage colpì Civitella, Cornia, Gebbia e San Pancrazio di Bucine._ → `storia.html`
4. [f4da425c] ●●○ `Nd=` **Quante vittime ci furono nel solo paese di Civitella, secondo ToscanaNovecento?**  
   ✔ 115 · ✘ 15 · 400 · 1.000  
   _ToscanaNovecento conta 115 morti a Civitella._ → `frazioni/civitella.html`
5. [e98abd07] ●●○ `Pv=` **Quale reparto tedesco compì le stragi del 29 giugno 1944?**  
   ✔ La divisione corazzata «Hermann Göring» · ✘ La divisione «Das Reich» · La divisione «Totenkopf» · L'Afrikakorps  
   _Le fonti indicano reparti della divisione «Hermann Göring»._ → `frazioni/cornia.html`
6. [ae2d129c] ●●○ `-v=` **Di quale comune fa parte San Pancrazio, colpito dalla strage del 1944?**  
   ✔ Bucine · ✘ Civitella in Val di Chiana · Arezzo · Monte San Savino  
   _San Pancrazio è una frazione di Bucine._ → `storia.html`
7. [d650b33d] ●●○ `-v=` **Dove arriva la Marcia per la pace che parte da Civitella?**  
   ✔ A San Pancrazio · ✘ Ad Arezzo · A Cortona · A Monte San Savino  
   _La Marcia per la pace va da Civitella a San Pancrazio._ → `frazioni/civitella.html`
8. [76c00bc0] ●●○ `-v=` **Con quale comune è organizzata la Marcia per la pace?**  
   ✔ Bucine · ✘ Arezzo · Firenze · Siena  
   _La marcia è realizzata in collaborazione con il comune di Bucine._ → `frazioni/civitella.html`
9. [ab4e24ee] ●○○ `Pd=` **Quale associazione ha allestito la Sala della Memoria a Civitella?**  
   ✔ Civitella Ricorda · ✘ La Pro Loco di Civitella · Slow Food Valdichiana · Comunità & Tegoleto  
   _La Sala della Memoria è stata allestita dall'associazione «Civitella Ricorda» in via Martiri di Civitella._ → `frazioni/civitella.html`
10. [7461cfc3] ●○○ `Pd=` **Come si chiama il monumento sul muro accanto alla chiesa di Civitella?**  
   ✔ Pietà del giugno 1944 · ✘ Vittoria alata · Il Milite Ignoto · Madonna della Pace  
   _Il monumento «Pietà del giugno 1944» ricorda l'eccidio._ → `frazioni/civitella.html`
11. [471dce11] ●●● `Nv=` **In quale anno fu realizzato il portale in bronzo di Bino Bini per la chiesa di Civitella?**  
   ✔ 1994 · ✘ 1954 · 1974 · 2014  
   _Il portale, del 1994, ricorda l'eccidio nel cinquantesimo anniversario._ → `frazioni/civitella.html`
12. [b6c6fc75] ●●● `Nv+` **In quale data le SS fucilarono a Ciggiano i partigiani Marmo e Marapitti?**  
   ✔ 16 aprile 1944 · ✘ 29 giugno 1944 · 25 aprile 1945 · 8 settembre 1943  
   _Giovanni Marmo e Mario Marapitti furono fucilati il 16 aprile 1944._ → `frazioni/ciggiano.html`
13. [9b2fcfcf] ●●● `Nv+` **In quale anno fu eretto il cippo dell'eccidio di Cornia?**  
   ✔ 1969 · ✘ 1945 · 1994 · 2004  
   _Il cippo fu eretto nel 1969, nel venticinquesimo anniversario._ → `frazioni/cornia.html`
14. [9677ff56] ●●● `Nn+` **Quanti nomi riporta la lastra dei martiri di Cornia?**  
   ✔ 58 · ✘ 8 · 115 · 300  
   _La lastra riporta 58 caduti di Cornia e delle località vicine._ → `frazioni/cornia.html`
15. [24c8d8bd] ●●○ `-n+` **Chi era Giovanni Cau, catturato a Gebbia nel 1944?**  
   ✔ Un insegnante di scienze naturali e autore di testi scolastici · ✘ Il parroco del paese · Un comandante partigiano · Il podestà di Civitella  
   _Giovanni Cau e la moglie Helga Elmqvist furono catturati a Gebbia e uccisi il 2 luglio 1944._ → `frazioni/gebbia.html`
16. [dad49b73] ●○○ `-d=` **Che cosa raccoglie la Sala della Memoria allestita a Civitella dall'associazione «Civitella Ricorda»?**  
   ✔ Reperti delle vittime, fotografie e testimonianze sull'eccidio · ✘ Opere d'arte rinascimentali · Attrezzi della civiltà contadina · Reperti etruschi  
   _Ci sono i reperti rinvenuti sulle vittime, fotografie del paese prima e dopo la distruzione, testimonianze, libri e residuati bellici._ → `frazioni/civitella.html`
17. [4dc5acd4] ●●● `Pv+` **Quale reparto operò a Gebbia il 29 giugno 1944, insieme alla divisione «Hermann Göring»?**  
   ✔ La Feldgendarmerie del capitano Heinz Barz · ✘ La Guardia Nazionale Repubblicana · Un reparto di alpini · Le SS di stanza a Firenze  
   _Reparti della «Hermann Göring», con la Feldgendarmerie del capitano Heinz Barz, applicarono a Gebbia lo stesso metodo usato a Civitella e a Cornia._ → `frazioni/gebbia.html`
18. [5c286059] ●●○ `-n+` **Secondo l'Archivio della Memoria, che cosa uccisero i tedeschi a Gebbia, oltre agli uomini?**  
   ✔ Tutti gli animali · ✘ Nessun altro essere vivente · I cavalli della fattoria · Solo i cani da guardia  
   _Donne e bambini non furono toccati né le case bruciate, ma i tedeschi uccisero tutti gli animali._ → `frazioni/gebbia.html`
19. [7ec5aac3] ●●○ `-v+` **Dove furono fucilati gli uomini presi a Gebbia, secondo l'Archivio della Memoria?**  
   ✔ Presso il Podere Valle, vicino a San Pancrazio · ✘ Nella piazza di Civitella · Nel cimitero di Cornia · Alla stazione di Albergo  
   _Furono fucilati presso il Podere Valle, vicino a San Pancrazio._ → `frazioni/gebbia.html`
20. [15cc1db8] ●●● `Nv+` **In quale giorno furono uccisi Giovanni Cau e la moglie Helga Elmqvist, catturati a Gebbia?**  
   ✔ Il 2 luglio 1944 · ✘ Il 29 giugno 1944 · Il 16 aprile 1944 · L'8 settembre 1943  
   _Furono catturati a Gebbia e uccisi il 2 luglio 1944._ → `frazioni/gebbia.html`
21. [320d4828] ●●● `Nv+` **Fino a quale giorno arrivano le morti ricordate dalla lastra dei martiri di Cornia?**  
   ✔ Il 16 luglio 1944 · ✘ Il 29 giugno 1944 · Il 25 aprile 1945 · Il 2 luglio 1944  
   _La lastra riporta 58 nomi di caduti uccisi fra il 29 giugno e il 16 luglio 1944._ → `frazioni/cornia.html`
22. [e6acc20f] ●●● `Pv+` **Chi fucilò a Ciggiano, il 16 aprile 1944, i partigiani Giovanni Marmo e Mario Marapitti?**  
   ✔ Le SS · ✘ La divisione «Hermann Göring» · I carabinieri · La Feldgendarmerie di Heinz Barz  
   _Secondo ToscanaNovecento furono fucilati dalle SS._ → `frazioni/ciggiano.html`
23. [5b3d98f6] ●●○ `Pv=` **Quale luogo della memoria si trova a Civitella, oltre alla «Pietà del giugno 1944» e alla Sala della Memoria?**  
   ✔ La Cappella dei Martiri · ✘ Il Sacrario militare · Il Museo della Resistenza · La Torre della Memoria  
   _A Civitella ci sono la Cappella dei Martiri e il monumento «Pietà del giugno 1944»._ → `frazioni/civitella.html`
24. [d69a35d2] ●●○ `-v+` **Dove si rifugiavano durante la guerra gli abitanti di Viciomaggio?**  
   ✔ In un cunicolo con una stanza sotterranea lungo il Fosso del Riolo · ✘ Nelle cantine della villa · In una galleria ferroviaria · Nel campanile della chiesa  
   _Il rifugio era un cunicolo con una stanza sotterranea lungo il Fosso del Riolo, verso Malpertuso._ → `frazioni/viciomaggio.html`
25. [f6883e41] ●●○ `-n+` **Chi era Hazbi Ismail, tra le vittime elencate dall'Atlante per «Cornia e dintorni»?**  
   ✔ Un partigiano di 28 anni · ✘ Il parroco di Cornia · Un soldato tedesco · Il maestro del paese  
   _L'Atlante delle stragi elenca tra le vittime il partigiano Hazbi Ismail, di 28 anni._ → `frazioni/cornia.html`
26. [cdce2f79] ●○○ `-d=` **Che cosa ricorda il portale in bronzo di Bino Bini nella chiesa di Civitella?**  
   ✔ L'eccidio del 1944, nel cinquantesimo anniversario · ✘ La battaglia del Toppo · La fondazione del priorato · La visita di un papa  
   _Il portale del 1994 ricorda l'eccidio nel cinquantesimo anniversario._ → `frazioni/civitella.html`
27. [67e04d32] ●○○ `-n=` **Perché la rocca di Civitella fu bombardata dagli Alleati?**  
   ✔ Perché al suo interno si era installato il comando tedesco · ✘ Per errore, scambiandola per un ponte · Perché era un deposito di munizioni italiano · Per colpire la ferrovia vicina  
   _La rocca, da secoli simbolo del paese, fu distrutta da un bombardamento alleato perché vi si era installato il comando tedesco._ → `storia.html`
28. [d46d4a3e] ●●○ `-n+` **Come morì Mario Mannelli, ricordato da un monumento a Viciomaggio?**  
   ✔ Fu ucciso per rappresaglia fascista nel 1944 · ✘ Cadde nella battaglia del Toppo · Morì nel bombardamento della rocca · Fu ucciso nella Grande Guerra  
   _Mario Mannelli fu ucciso dai fascisti nel 1944; sulla data esatta le fonti non concordano._ → `frazioni/viciomaggio.html`

## Frazioni (94)

1. [a6b8c90b] ●○○ `-v-` **In quale frazione ha sede il Comune?**  
   ✔ Badia al Pino · ✘ Civitella · Tegoleto · Pieve al Toppo  
   _Dal 1917 la sede comunale è a Badia al Pino._ → `frazioni/badia-al-pino.html`
2. [3f92e789] ●●○ `Pv=` **A quali santi era dedicata l'antica abbazia del Pino?**  
   ✔ Martino e Lorenzo · ✘ Pietro e Paolo · Biagio e Rocco · Giorgio e Luca  
   _Un documento del 1046 la chiama «Badia di S. Martino e S. Lorenzo al Pino»._ → `frazioni/badia-al-pino.html`
3. [0542f44e] ●●○ `Pv=` **Qual è il titolo della parrocchia di Badia al Pino?**  
   ✔ San Bartolomeo · ✘ San Biagio · San Martino · Sant'Andrea  
   _La parrocchia di Badia al Pino è dedicata a San Bartolomeo._ → `frazioni/badia-al-pino.html`
4. [e6beb218] ●●● `Pv+` **Quale santo è titolare delle parrocchie sia di Ciggiano sia di Tegoleto?**  
   ✔ San Biagio · ✘ San Martino · Sant'Andrea · San Bartolomeo  
   _Ciggiano e Tegoleto hanno entrambe una chiesa parrocchiale di San Biagio._ → `frazioni/tegoleto.html`
5. [a36520a9] ●●● `Pv+` **Quale santo è titolare delle parrocchie sia di Spoiano sia di Pieve al Toppo?**  
   ✔ San Giovanni Battista · ✘ San Biagio · San Martino · Santa Maria Assunta  
   _Spoiano e Pieve al Toppo hanno entrambe la parrocchia di San Giovanni Battista._ → `frazioni/spoiano.html`
6. [120e1846] ●●○ `Pv=` **A quale santo è dedicata la parrocchia di Viciomaggio?**  
   ✔ San Martino · ✘ San Biagio · San Bartolomeo · Sant'Andrea  
   _La parrocchiale di Viciomaggio è San Martino._ → `frazioni/viciomaggio.html`
7. [f2907c6a] ●●○ `Pv=` **A quale santo è dedicata la parrocchia di Oliveto?**  
   ✔ Sant'Andrea Apostolo · ✘ San Rocco · San Martino · San Biagio  
   _La parrocchia di Oliveto è Sant'Andrea Apostolo._ → `frazioni/oliveto.html`
8. [1b1b61a6] ●●● `Nn+` **In quale anno Tuori compare per la prima volta nei documenti?**  
   ✔ 1021 · ✘ 1385 · 1774 · 1917  
   _Tuori è ricordato nel 1021 come abitato del piviere di Santa Maria al Toppo._ → `frazioni/tuori.html`
9. [b24d9f73] ●●● `Nn+` **Da quale anno è documentata l'antica pieve di Pieve al Toppo?**  
   ✔ 938 · ✘ 1288 · 1500 · 1906  
   _La pieve, con un ospedale, è documentata dal 938._ → `frazioni/pieve-al-toppo.html`
10. [c686859b] ●●● `Nn+` **In quale anno fu progettata la moderna chiesa parrocchiale di Pieve al Toppo?**  
   ✔ 1967 · ✘ 1288 · 1806 · 2005  
   _La chiesa di San Giovanni Battista fu progettata nel 1967; il porticato è del 1977._ → `frazioni/pieve-al-toppo.html`
11. [c2c65bab] ●●● `Nn+` **In quale anno la chiesa di San Biagio a Ciggiano fu elevata a pieve?**  
   ✔ 1465 · ✘ 1048 · 1774 · 1917  
   _San Biagio di Ciggiano fu elevata a pieve nel 1465._ → `frazioni/ciggiano.html`
12. [b555e58c] ●●○ `Pv=` **A quale scultore è attribuita la Santa Maria Maddalena della chiesa di San Biagio a Ciggiano?**  
   ✔ Andrea Sansovino · ✘ Michelangelo · Donatello · Giambologna  
   _La scultura del primo Cinquecento è attribuita ad Andrea Sansovino._ → `frazioni/ciggiano.html`
13. [c31940bf] ●●○ `-v=` **In quale frazione si trova la chiesa della Madonna della Costarella, costruita nel 1635 con le elemosine dei pastori della transumanza?**  
   ✔ Ciggiano · ✘ Albergo · Spoiano · Tuori  
   _Sorge fuori dal castello di Ciggiano, lungo la via vecchia senese percorsa dalle greggi._ → `frazioni/ciggiano.html`
14. [8d375aa0] ●●○ `-v+` **Quale borgo collinare si trova a circa 360 metri, su un colle tra le valli del Gargaiolo e dell'Esse?**  
   ✔ Ciggiano · ✘ Tegoleto · Albergo · Badia al Pino  
   _La scheda del Comune indica per Ciggiano un'altitudine di 359 metri._ → `frazioni/ciggiano.html`
15. [264f4207] ●○○ `-n=` **Quale attività artigianale esisteva un tempo a Cornia?**  
   ✔ La lavorazione delle scope di saggina · ✘ La produzione di cappelli di paglia · La soffiatura del vetro · La lavorazione del corallo  
   _A Cornia esisteva un centro per la lavorazione delle scope di saggina._ → `frazioni/cornia.html`
16. [7460edf6] ●●○ `Pn=` **A quale santo è dedicata la chiesa di Cornia, detta di Sant'Angelo?**  
   ✔ San Michele Arcangelo · ✘ San Rocco · San Giorgio · San Francesco  
   _La chiesa di Cornia è San Michele Arcangelo, detta Sant'Angelo._ → `frazioni/cornia.html`
17. [c1b2389e] ●●○ `-v+` **Quale frazione è la più alta tra queste, a circa 560 metri?**  
   ✔ Cornia · ✘ Tegoleto · Badia al Pino · Albergo  
   _Cornia si trova a circa 560 metri._ → `frazioni/cornia.html`
18. [d02d06cf] ●●○ `Pv=` **Di quale famiglia fu dimora Villa Oliveto, già Villa Mazzi?**  
   ✔ I conti Barbolani di Montauto · ✘ I Medici · I Guidi · I Ricasoli  
   _Villa Oliveto fu dimora dei conti Barbolani di Montauto._ → `frazioni/oliveto.html`
19. [782eea04] ●○○ `Pd-` **Quale scrittrice scozzese visse a Oliveto ed è sepolta nel suo cimitero?**  
   ✔ Muriel Spark · ✘ Agatha Christie · Virginia Woolf · Jane Austen  
   _Muriel Spark visse a Oliveto dagli anni Settanta e vi morì nel 2006._ → `frazioni/oliveto.html`
20. [f98ae568] ●○○ `Pd-` **Quale romanzo ha scritto Muriel Spark, che visse a Oliveto?**  
   ✔ Gli anni fulgenti di Miss Brodie · ✘ Gita al faro · Orgoglio e pregiudizio · Assassinio sull'Orient Express  
   _Muriel Spark è l'autrice de «Gli anni fulgenti di Miss Brodie»._ → `frazioni/oliveto.html`
21. [ae843126] ●●○ `Nn=` **In quale anno Muriel Spark ricevette la cittadinanza onoraria di Civitella?**  
   ✔ 2005 · ✘ 1975 · 1990 · 2015  
   _La cittadinanza onoraria le fu conferita nel settembre 2005._ → `frazioni/oliveto.html`
22. [4570545d] ●●● `Nn+` **Da quale anno si tiene il Presepe Vivente di Oliveto?**  
   ✔ 2014 · ✘ 1950 · 1985 · 2022  
   _Il Presepe Vivente di Oliveto si tiene dal 2014._ → `frazioni/oliveto.html`
23. [605f6a96] ●○○ `-d=` **Dove è allestita la Natività del Presepe Vivente di Oliveto?**  
   ✔ Nella chiesetta di San Rocco · ✘ Nella Rocca di Civitella · Nel Teatro Moderno · Nella stazione di Albergo  
   _Un percorso illuminato da torce conduce alla Natività nella chiesetta di San Rocco._ → `frazioni/oliveto.html`
24. [8c3a7f97] ●○○ `-d=` **Che cosa è stato trovato al Podere Casella, presso Pieve a Maiano?**  
   ✔ Strumenti in pietra del Paleolitico · ✘ Un tesoro di monete medievali · Una nave romana · Un mosaico bizantino  
   _Al Podere Casella sono stati trovati strumenti in pietra del Paleolitico._ → `frazioni/pieve-a-maiano.html`
25. [f229085c] ●●● `Pv+` **Di quale imperatore è la moneta d'oro trovata a Pieve a Maiano?**  
   ✔ Claudio · ✘ Nerone · Augusto · Traiano  
   _È un aureus dell'imperatore Claudio (41–54 d.C.)._ → `frazioni/pieve-a-maiano.html`
26. [9ed31f21] ●●○ `-v=` **Vicino a quale frazione si trova il podere Spedaluccio?**  
   ✔ Pieve a Maiano · ✘ Albergo · Tegoleto · Ciggiano  
   _Lo Spedaluccio è nei pressi di Pieve a Maiano; in passato era stato attribuito per errore ad Albergo._ → `frazioni/pieve-a-maiano.html`
27. [91b7689b] ●○○ `-d=` **Che cosa si produceva nelle fornaci romane di località I Ponti, a Pieve al Toppo?**  
   ✔ Terra sigillata aretina · ✘ Vetro soffiato · Porcellana · Mattoni rinascimentali  
   _Le fornaci producevano la terra sigillata aretina, la ceramica rossa da mensa della prima età imperiale._ → `frazioni/pieve-al-toppo.html`
28. [ac4c5d0d] ●●○ `Nn=` **Da quale anno Ponticino ha una stazione ferroviaria?**  
   ✔ 1866 · ✘ 1830 · 1910 · 1955  
   _La stazione di Ponticino è attiva dal 1866._ → `frazioni/ponticino.html`
29. [21a4f930] ●○○ `-n=` **Su quale linea ferroviaria si trova la stazione di Ponticino?**  
   ✔ Firenze–Roma · ✘ Arezzo–Sinalunga · Siena–Chiusi · Pisa–Firenze  
   _Ponticino è servito dalla ferrovia Firenze–Roma._ → `frazioni/ponticino.html`
30. [1938aa25] ●●● `Nn+` **In quale anno un referendum approvò la fusione tra Laterina e Pergine Valdarno, che riguarda anche Ponticino?**  
   ✔ 2017 · ✘ 1999 · 2009 · 2023  
   _Il referendum del 29–30 ottobre 2017 approvò la fusione con il 53,73% dei voti._ → `frazioni/ponticino.html`
31. [b126f10e] ●●○ `-v=` **Con quali comuni Civitella si divideva Ponticino prima del 2018?**  
   ✔ Laterina e Pergine Valdarno · ✘ Bucine e Arezzo · Monte San Savino e Arezzo · Bucine e Montevarchi  
   _Fino al 2017 Ponticino era diviso tra Civitella, Laterina e Pergine Valdarno._ → `frazioni/ponticino.html`
32. [86a6174e] ●●○ `Pv=` **Quale villa settecentesca si trova a Spoiano?**  
   ✔ Villa Pecchioli · ✘ Villa di Viciomaggio · Villa Oliveto · Villa del Bosco  
   _Villa Pecchioli è l'edificio simbolo di Spoiano._ → `frazioni/spoiano.html`
33. [d00da1ec] ●●○ `-n+` **Che cosa divenne Villa Pecchioli, a Spoiano, nel 1928?**  
   ✔ Un asilo infantile · ✘ Un ospedale · Una caserma · Una scuola di musica  
   _Nel 1928 Villa Pecchioli divenne asilo; fu restaurata nel 1981._ → `frazioni/spoiano.html`
34. [bd1eb40f] ●●○ `-v+` **Quale paese è al centro del libro «Un uomo dabbene per davvero» di Giuseppe Renzetti?**  
   ✔ Spoiano · ✘ Tuori · Gebbia · Oliveto  
   _Il libro racconta la vita contadina della Valdichiana attraverso la figura del padre dell'autore._ → `frazioni/spoiano.html`
35. [e7c2c418] ●●○ `-v=` **Chi ricostruì la torre di Tegoleto alla fine del Trecento?**  
   ✔ I fiorentini · ✘ I senesi · I longobardi · I francesi  
   _La torre fu ricostruita dai fiorentini alla fine del Trecento._ → `frazioni/tegoleto.html`
36. [1086aa45] ●●● `Pv+` **A quale ordine passò la fattoria di Tegoleto nel 1783?**  
   ✔ Ai Cavalieri di Santo Stefano · ✘ Ai Cavalieri di Malta · Ai Gesuiti · Ai Templari  
   _Nel 1783 la fattoria passò all'Ordine dei Cavalieri di Santo Stefano._ → `frazioni/tegoleto.html`
37. [3e486f3c] ●●○ `Nn=` **In quale anno nacque il Teatro Moderno di Tegoleto?**  
   ✔ 1960 · ✘ 1900 · 1925 · 2005  
   _Il TMT nacque nel 1960 come cinema, per iniziativa di alcuni parrocchiani._ → `frazioni/tegoleto.html`
38. [91b9c111] ●●○ `Pn=` **Chi gestisce il Teatro Moderno di Tegoleto?**  
   ✔ Il Gruppo Teatro La Torre · ✘ La Pro Loco di Civitella · Il Comune di Arezzo · Slow Food Valdichiana  
   _Il teatro è gestito dall'associazione culturale Gruppo Teatro La Torre._ → `frazioni/tegoleto.html`
39. [7c7d8c24] ●●○ `Nn=` **In quale anno a Tegoleto arrivò una tappa del Giro d'Italia?**  
   ✔ 2004 · ✘ 1983 · 1991 · 2018  
   _Il 12 maggio 2004 la quarta tappa del Giro d'Italia arrivò a Tegoleto._ → `frazioni/tegoleto.html`
40. [c1817196] ●●○ `Pv=` **Chi vinse la tappa del Giro d'Italia arrivata a Tegoleto nel 2004?**  
   ✔ Alessandro Petacchi · ✘ Mario Cipollini · Marco Pantani · Giuseppe Saronni  
   _Petacchi vinse davanti allo stabilimento del mobilificio Del Tongo._ → `frazioni/tegoleto.html`
41. [d7a4e134] ●●● `Nn+` **In quale anno fu trovata a Viciomaggio un'urna cineraria etrusca con iscrizione?**  
   ✔ 1872 · ✘ 1772 · 1922 · 1972  
   _L'urna ellenistica, con l'iscrizione l. prastn[a] nerinal, fu trovata nel 1872._ → `frazioni/viciomaggio.html`
42. [a06601d7] ●●○ `-v=` **In quale frazione si trova la villa-fattoria settecentesca con una limonaia del 1836 e una cappella con orologio e campanile a vela?**  
   ✔ Viciomaggio · ✘ Spoiano · Tuori · Ciggiano  
   _È la villa padronale di Viciomaggio, restaurata nel 1868._ → `frazioni/viciomaggio.html`
43. [1d45bdf1] ●●○ `Pv=` **Su quale linea ferroviaria si trova la stazione di Albergo?**  
   ✔ Arezzo–Sinalunga · ✘ Firenze–Roma · Faentina · Porrettana  
   _Le stazioni di Albergo e di Civitella-Badia al Pino sono sulla ferrovia Arezzo–Sinalunga._ → `frazioni/albergo.html`
44. [daf0e244] ●○○ `-d=` **Quale strada romana passava da Albergo, secondo l'itinerario del Comune?**  
   ✔ Una via municipalis unita a un ramo della Cassia · ✘ La via Appia · La via Aurelia · La via Emilia  
   _Da Albergo passava una via municipalis che si univa a un ramo della Cassia diretto in Valdarno._ → `frazioni/albergo.html`
45. [cc15f4f6] ●●○ `-v=` **A quale ordine religioso apparteneva il priorato da cui nacque la chiesa di Santa Maria Assunta a Civitella?**  
   ✔ Benedettino · ✘ Francescano · Gesuita · Domenicano  
   _La chiesa fu eretta come priorato benedettino nell'XI secolo._ → `frazioni/civitella.html`
46. [2a3e555c] ●●○ `Nn=` **In quale anno fu completata in stile romanico la chiesa di Santa Maria Assunta a Civitella?**  
   ✔ 1252 · ✘ 1048 · 1652 · 1944  
   _La chiesa fu ultimata in stile romanico nel 1252._ → `frazioni/civitella.html`
47. [bdcb792b] ●●● `Nn+` **Quanti archi ha il portico del Palazzo Pretorio di Civitella?**  
   ✔ Cinque · ✘ Due · Otto · Dodici  
   _Il trecentesco Palazzo Pretorio ha un portico a cinque archi._ → `frazioni/civitella.html`
48. [dedef337] ●○○ `-n=` **Per quale scopo il notaio Becattini lasciò il suo palazzo alla Confraternita di Carità?**  
   ✔ Per farne un ospedale per i poveri · ✘ Per farne una scuola · Per farne un teatro · Per farne una caserma  
   _Alla sua morte, nel 1877, lasciò ogni bene per un ospedale dei poveri del paese._ → `frazioni/civitella.html`
49. [8a7414cd] ●●● `Nn+` **Da quale anno Palazzo Becattini è di proprietà del Comune?**  
   ✔ 1978 · ✘ 1877 · 1917 · 2004  
   _Nel 1978 l'ospedale è passato in proprietà al Comune._ → `frazioni/civitella.html`
50. [4881de19] ●○○ `Pd=` **In quale piazza di Civitella si trova la cisterna medievale?**  
   ✔ Piazza Lazzeri · ✘ Piazza Grande · Piazza della Signoria · Piazza del Campo  
   _La cisterna medievale si trova in piazza Lazzeri, di fronte alla chiesa._ → `frazioni/civitella.html`
51. [bdf6b86c] ●●● `Pv+` **Chi costruì il Saracino, la casa colonica cinquecentesca presso Tuori?**  
   ✔ La Fraternita dei Laici di Arezzo · ✘ I Medici · Il vescovo di Arezzo · L'Ordine di Santo Stefano  
   _Il Saracino fu costruito dalla Fraternita dei Laici di Arezzo._ → `frazioni/tuori.html`
52. [8bc58b2b] ●●○ `-v+` **In quale frazione si trova Palazzo Santini-Paccinelli, villa settecentesca simmetrica rispetto alla scala centrale?**  
   ✔ Badia al Pino · ✘ Oliveto · Tuori · Spoiano  
   _Il palazzo sorge ai margini del nucleo medievale di Badia al Pino._ → `frazioni/badia-al-pino.html`
53. [19907f55] ●○○ `-n=` **Quale reliquia custodisce la chiesa della Compagnia di Santa Croce a Ciggiano?**  
   ✔ Una reliquia della Croce · ✘ Il velo della Madonna · Il mantello di San Martino · Un osso di San Biagio  
   _La reliquia veniva esposta nei giorni della festa, il 3 maggio e il 14 settembre._ → `frazioni/ciggiano.html`
54. [43d14c27] ●●● `Pv+` **Quale pittore dipinse la Madonna del Rosario conservata nella chiesa di Sant'Andrea a Oliveto?**  
   ✔ Orazio Porta · ✘ Piero della Francesca · Giorgio Vasari · Luca Signorelli  
   _La chiesa di Sant'Andrea, documentata dal 1300, conserva una Madonna del Rosario di Orazio Porta._ → `frazioni/oliveto.html`
55. [b4c51f53] ●●○ `Nn=` **In quale anno Villa Oliveto fu ceduta al Comune di Civitella?**  
   ✔ 1980 · ✘ 1940 · 1960 · 2005  
   _Ceduta al Comune nel 1980, la villa ospita il Centro di Documentazione sui campi di internamento._ → `frazioni/oliveto.html`
56. [4bfffd85] ●●○ `Pn+` **Chi fuse nel 1358 la campana oggi nel campanile della chiesa di Pieve a Maiano?**  
   ✔ Neri d'Arezzo · ✘ Giambologna · Benvenuto Cellini · Lorenzo Ghiberti  
   _La campana apparteneva alla distrutta chiesa di San Giovanni Battista a Montoto._ → `frazioni/pieve-a-maiano.html`
57. [1f3abaaa] ●○○ `-n=` **Che cos'era anticamente il podere Spedaluccio, vicino a Pieve a Maiano?**  
   ✔ Un ospizio per viandanti · ✘ Un mulino ad acqua · Un convento femminile · Una fornace romana  
   _La casa colonica dello Spedaluccio è tutto ciò che resta di un antico ospizio per viandanti._ → `frazioni/pieve-a-maiano.html`
58. [21e2abd1] ●●● `Nn+` **Da quale anno è documentato l'antico ospizio dello Spedaluccio?**  
   ✔ 1198 · ✘ 1048 · 1385 · 1774  
   _L'itinerario del Comune ricorda l'ospizio «documentato fino dal 1198»._ → `frazioni/pieve-a-maiano.html`
59. [388b792d] ●○○ `-n=` **Su che cosa sorge l'Oratorio della Madonna del Conforto a Pieve al Toppo?**  
   ✔ Sul sito dell'antica pieve · ✘ Sui resti di un tempio etrusco · Su un'antica fornace · Sulle mura del castello  
   _Fu edificato nel Cinquecento sui resti dell'antica pieve e dedicato alla Madonna del Conforto nel 1906._ → `frazioni/pieve-al-toppo.html`
60. [0ff18981] ●○○ `-d=` **Che cos'era all'inizio, nel 1960, il Teatro Moderno di Tegoleto?**  
   ✔ Un cinema · ✘ Una chiesa · Una fabbrica · Una scuola  
   _Nato per volontà di alcuni parrocchiani, fu cinema fino agli anni Ottanta e dal 1997 è sala polifunzionale._ → `frazioni/tegoleto.html`
61. [c5767706] ●●○ `-n+` **Che cosa c'è nel recinto d'accesso al Palatium-torre della Rocca di Civitella?**  
   ✔ La cisterna per la raccolta dell'acqua · ✘ Una cappella affrescata · Le prigioni · Un forno per il pane  
   _Il Palatium è formato dalla torre vera e propria e dal recinto d'accesso con la cisterna._ → `frazioni/civitella.html`
62. [99db94ce] ●●○ `Pn=` **Quale via medievale transitava da Albergo?**  
   ✔ La via senese-aretina · ✘ La via Francigena · La via Emilia · La via Flaminia  
   _Dall'antico borgo transitava in epoca medievale la via senese-aretina._ → `frazioni/albergo.html`
63. [a6b92165] ●○○ `-d=` **Quale bene è tutelato da vincolo nazionale a Badia al Pino?**  
   ✔ La torre dell'antico castello · ✘ La stazione ferroviaria · Il palazzetto dello sport · Il monumento ai caduti  
   _La torre fa parte di ciò che resta, con la porta, dell'antico castello sorto intorno all'abbazia._ → `frazioni/badia-al-pino.html`
64. [855aa29c] ●○○ `-d=` **Che cosa prevede il Piano Strutturale per la Rocca di Civitella?**  
   ✔ Il restauro e un «museo» dedicato ai castelli del territorio · ✘ La demolizione dei ruderi · Un albergo di lusso · Un parcheggio panoramico  
   _Il Piano prevede il restauro della Rocca e un «museo» come punto di riferimento per visitare castelli, rocche, torri e antichi tracciati._ → `frazioni/civitella.html`
65. [5290f03d] ●●○ `-v+` **Quali stemmi si vedono sul Palazzo Pretorio di Civitella?**  
   ✔ Quelli dei podestà fiorentini · ✘ Quelli dei vescovi di Arezzo · Quelli dei granduchi di Lorena · Quelli dei Savoia  
   _Il Palazzo Pretorio è trecentesco, con un portico a cinque archi e gli stemmi dei podestà fiorentini._ → `frazioni/civitella.html`
66. [77e1c3f5] ●●● `Nn+` **In quale anno morì il notaio Becattini, che lasciò il suo palazzo per un ospedale dei poveri?**  
   ✔ 1877 · ✘ 1777 · 1917 · 1944  
   _Il notaio morì il 19 luglio 1877; dal 1978 il palazzo è del Comune._ → `frazioni/civitella.html`
67. [fd831df6] ●●● `Pv+` **Quali oratori si trovano nel borgo di Civitella?**  
   ✔ Quello della Santissima Trinità e quello della Madonna di Mercatale · ✘ Quello della Madonna della Costarella e quello di San Rocco · Quello della Madonna del Conforto e quello di Santa Croce · Quello di San Rocco e quello della Madonna del Rosario  
   _A Civitella ci sono gli oratori della Santissima Trinità e della Madonna di Mercatale; la Costarella è a Ciggiano._ → `frazioni/civitella.html`
68. [608aba01] ●●○ `-n+` **Quale bene storico di Albergo è censito nel Repertorio del Piano Strutturale?**  
   ✔ La fonte-cisterna · ✘ Un acquedotto romano · Una torre di avvistamento · Un mulino ad acqua  
   _Il Repertorio censisce la fonte-cisterna di Albergo e ne valorizza il centro storico._ → `frazioni/albergo.html`
69. [e6917851] ●○○ `-n=` **Che cosa ospita oggi il palazzetto settecentesco di Badia al Pino, sede comunale fino ai primi anni Settanta?**  
   ✔ La Biblioteca comunale · ✘ Il municipio · Un museo archeologico · La scuola primaria  
   _Fu sede comunale dal 1917 ai primi anni Settanta; oggi è la Biblioteca comunale._ → `frazioni/badia-al-pino.html`
70. [c435203b] ●●● `Nv+` **In quale anno fu inaugurato il monumento ai caduti nel piazzale della chiesa di Badia al Pino?**  
   ✔ 1951 · ✘ 1921 · 1946 · 1971  
   _Il monumento ai caduti delle due guerre fu inaugurato il 26 agosto 1951._ → `frazioni/badia-al-pino.html`
71. [d3fdc7c5] ●●○ `-v+` **Che cosa caratterizza Villa del Bosco, a Badia al Pino?**  
   ✔ Un parco con un filare di pini · ✘ Una limonaia del 1836 · Una torre-piccionaia · Una cappella con orologio  
   _Villa del Bosco ha un parco e un filare di pini._ → `frazioni/badia-al-pino.html`
72. [7c31e8d6] ●●● `Pv+` **A quali santi è dedicata la chiesa di San Bartolomeo a Badia al Pino?**  
   ✔ Bartolomeo, Martino e Filippo · ✘ Bartolomeo, Pietro e Paolo · Bartolomeo, Biagio e Rocco · Bartolomeo, Giorgio e Luca  
   _La chiesa, annessa all'antica abbazia, è dedicata ai santi Bartolomeo, Martino e Filippo._ → `frazioni/badia-al-pino.html`
73. [f996bc77] ●●● `Pv+` **Quale altare custodisce la chiesa di San Biagio a Ciggiano?**  
   ✔ L'altare Mazzeschi · ✘ L'altare Pecchioli · L'altare Barbolani · L'altare Becattini  
   _San Biagio custodisce l'altare Mazzeschi e una Santa Maria Maddalena attribuita ad Andrea Sansovino._ → `frazioni/ciggiano.html`
74. [2c5801d3] ●●○ `-v+` **Di quale secolo è il loggiato della chiesa della Madonna della Costarella, a Ciggiano?**  
   ✔ Del Settecento · ✘ Del Trecento · Del Cinquecento · Del Novecento  
   _La chiesa fu terminata nel 1635; il loggiato è settecentesco._ → `frazioni/ciggiano.html`
75. [48e6e4b6] ●●● `Nv+` **In quale anno la chiesa di San Pietro a Ciggiano ebbe l'intervento che le diede l'aspetto eclettico?**  
   ✔ 1836 · ✘ 1636 · 1736 · 1936  
   _La chiesa è di origine medievale; il suo aspetto eclettico è frutto di un intervento del 1836._ → `frazioni/ciggiano.html`
76. [eccf0f3a] ●●○ `-v+` **In quali registri compare già nel 1274 la chiesa di Sant'Angelo a Cornia?**  
   ✔ Nelle decime · ✘ Nel catasto leopoldino · Negli statuti di Siena · Nei registri dell'ISTAT  
   _La chiesa di San Michele Arcangelo compare nelle decime del 1274._ → `frazioni/cornia.html`
77. [d4b4fda3] ●●● `Nv+` **In quale anno fu ricostruita la chiesa di San Giovanni d'Oliveto?**  
   ✔ 1343 · ✘ 1243 · 1443 · 1643  
   _San Giovanni d'Oliveto compare nelle decime del 1274 e fu ricostruita nel 1343._ → `frazioni/oliveto.html`
78. [2c46b6c8] ●○○ `-d+` **Che cos'era in origine l'Oratorio di San Rocco, a Oliveto?**  
   ✔ Un tabernacolo, diventato cappella nell'Ottocento · ✘ Una torre di guardia · Un mulino · Una scuola  
   _L'oratorio nacque come tabernacolo e divenne cappella nell'Ottocento._ → `frazioni/oliveto.html`
79. [1ee31880] ●●● `Nv+` **Attorno a quale anno fu rifatta la Cappella della Compagnia di Oliveto, secondo l'iscrizione sul portale?**  
   ✔ 1637 · ✘ 1337 · 1737 · 1937  
   _La Cappella della Compagnia fu rifatta attorno al 1637, come indica l'iscrizione sul portale._ → `frazioni/oliveto.html`
80. [49446c6c] ●○○ `-d=` **Di quali alberi è ricco il parco di Villa Oliveto?**  
   ✔ Cedri e lecci · ✘ Palme e agavi · Faggi e abeti · Pioppi e salici  
   _La villa ha un parco di ispirazione romantica ricco di cedri e lecci._ → `frazioni/oliveto.html`
81. [498b0966] ●●● `Nv=` **In quale anno morì Muriel Spark, che visse a Oliveto?**  
   ✔ 2006 · ✘ 1996 · 2001 · 2016  
   _Ricevette la cittadinanza onoraria nel 2005, morì nel 2006 ed è sepolta a Oliveto._ → `frazioni/oliveto.html`
82. [3bd4c74d] ●●● `Nv+` **In quale anno fu ampliata la chiesa di Santa Maria Assunta a Pieve a Maiano?**  
   ✔ 1865 · ✘ 1765 · 1824 · 1965  
   _La chiesa fu costruita dopo il 1824 e ampliata nel 1865._ → `frazioni/pieve-a-maiano.html`
83. [91087b87] ●●○ `Pv=` **Qual è il titolo della parrocchia di Pieve a Maiano?**  
   ✔ Santa Maria Assunta · ✘ San Biagio · San Martino · Sant'Andrea Apostolo  
   _La parrocchia di Pieve a Maiano è Santa Maria Assunta._ → `frazioni/pieve-a-maiano.html`
84. [253e4dff] ●●● `Nn+` **Da quale anno l'oratorio di Pieve al Toppo è dedicato alla Madonna del Conforto?**  
   ✔ 1906 · ✘ 1502 · 1806 · 1966  
   _L'oratorio sorge sul sito dell'antica pieve ed è dedicato alla Madonna del Conforto dal 1906._ → `frazioni/pieve-al-toppo.html`
85. [974228d6] ●●○ `-v+` **Qual è l'unico bene storico di Ponticino censito dal Repertorio del Piano?**  
   ✔ Il mulino · ✘ Il ponte romanico · La pieve · Il castello  
   _Il Repertorio censisce solo il Mulino di Ponticino; il «ponte romanico» non ha riscontri._ → `frazioni/ponticino.html`
86. [d9d80f19] ●●○ `-v+` **In quale comune ha sede la parrocchia dei Santi Iacopo e Cristoforo di Ponticino?**  
   ✔ Laterina Pergine Valdarno · ✘ Civitella in Val di Chiana · Arezzo · Bucine  
   _Secondo l'annuario della Diocesi la parrocchia ha sede nel comune di Laterina Pergine Valdarno._ → `frazioni/ponticino.html`
87. [3d4a15ba] ●●○ `-v+` **Quale elemento caratterizza Villa Pecchioli, a Spoiano?**  
   ✔ Una torre-piccionaia · ✘ Una limonaia del 1836 · Un filare di pini · Una cappella con orologio  
   _Villa Pecchioli è settecentesca, con una torre-piccionaia._ → `frazioni/spoiano.html`
88. [99f5bb0f] ●●○ `-n+` **In quale periodo dell'anno si tiene la stagione del Teatro Moderno di Tegoleto?**  
   ✔ Da ottobre a marzo · ✘ Da giugno ad agosto · Solo a dicembre · Da aprile a giugno  
   _Il TMT ha una stagione da ottobre a marzo._ → `frazioni/tegoleto.html`
89. [2f350987] ●●● `Nv+` **Quale tappa del Giro d'Italia 2004 arrivò a Tegoleto?**  
   ✔ La quarta · ✘ La prima · La decima · L'ultima  
   _Il 12 maggio 2004 vi arrivò la quarta tappa, vinta da Alessandro Petacchi._ → `frazioni/tegoleto.html`
90. [13de9716] ●●○ `Pv=` **Davanti a quale stabilimento si concluse la tappa del Giro d'Italia arrivata a Tegoleto nel 2004?**  
   ✔ Quello della Del Tongo · ✘ Quello della CEIA · Quello della Chimet · Quello della Kico  
   _La tappa fu vinta da Petacchi davanti allo stabilimento del mobilificio Del Tongo._ → `frazioni/tegoleto.html`
91. [ced4fecf] ●●○ `-v+` **Su quali beni di Tuori c'è un vincolo nazionale?**  
   ✔ Il cassero, la chiesa e il cimitero · ✘ Tutto il centro storico · Solo il Saracino · La villa e il suo parco  
   _Il vincolo riguarda cassero, chiesa e cimitero, non il centro storico._ → `frazioni/tuori.html`
92. [8288be8c] ●●○ `-v+` **Com'è fatto il portico del Saracino, presso Tuori?**  
   ✔ A tre archi a tutto sesto · ✘ A cinque archi a sesto acuto · A un solo grande arco · A colonne senza archi  
   _Il Saracino ha un portico a tre archi a tutto sesto e una loggia ad arco ribassato._ → `frazioni/tuori.html`
93. [b72de4ff] ●●● `Nv+` **In quale anno fu restaurata, con decorazioni pittoriche, la parte posteriore della Villa di Viciomaggio?**  
   ✔ 1868 · ✘ 1768 · 1836 · 1968  
   _La villa è settecentesca; la parte posteriore fu restaurata nel 1868, la limonaia è del 1836._ → `frazioni/viciomaggio.html`
94. [396551e5] ●●● `Pv+` **Di quale bottega è la Madonna con il Bambino del 1522 nel tabernacolo presso la Porta Senese di Civitella?**  
   ✔ Quella di Giovanni della Robbia · ✘ Quella di Donatello · Quella di Luca Signorelli · Quella del Sansovino  
   _È una terracotta invetriata del 1522 della bottega di Giovanni della Robbia._ → `frazioni/civitella.html`

## Borghi minori (35)

1. [cd56501b] ●○○ `-d=` **Per che cosa era noto il luogo di Matroia?**  
   ✔ Per una sorgente con acque ritenute medicamentose · ✘ Per una miniera d'argento · Per un castello dei Medici · Per una fornace di vetro  
   _Le acque, ritenute medicamentose, erano usate soprattutto per i lattanti._ → `frazioni/borghi-minori.html#matroia`
2. [e4363716] ●○○ `-d+` **Che cosa c'è oggi a Matroia, secondo il Piano Strutturale?**  
   ✔ Un allevamento di cavalli · ✘ Una cantina sociale · Un aeroporto · Una cava di marmo  
   _Il Piano prevede di trasformare l'allevamento in Centro di Equitazione._ → `frazioni/borghi-minori.html#matroia`
3. [dbcd5fc3] ●●○ `-v=` **Dove si trova oggi la campana del 1358 proveniente da Montoto?**  
   ✔ Nella chiesa di Pieve a Maiano · ✘ Nel Duomo di Arezzo · Nella Rocca di Civitella · Nel Museo del Bargello  
   _La campana di Montoto è conservata nella chiesa di Santa Maria Assunta a Pieve a Maiano._ → `frazioni/borghi-minori.html#montoto`
4. [ec3b56a5] ●●● `Nv=` **In quale anno il castello di Montoto passò da Arezzo a Firenze?**  
   ✔ 1385 · ✘ 1048 · 1774 · 1917  
   _Il castello di Montoto passò a Firenze nel 1385._ → `frazioni/borghi-minori.html#montoto`
5. [ba3dff5e] ●○○ `-d=` **Che cosa resta sulla cima di Poggio Castellare?**  
   ✔ Una cinta muraria ellittica a secco · ✘ Un anfiteatro romano · Una torre medicea · Un faro  
   _Restano i ruderi di una cinta ellittica a secco lunga circa 300 metri._ → `frazioni/borghi-minori.html#poggio-castellare`
6. [f06a2f2d] ●○○ `-n=` **Da che cosa deriva il nome di Montarfoni?**  
   ✔ Da «Monte di Arfo», un antico proprietario germanico · ✘ Da un torrente · Da una famiglia fiorentina · Da una battaglia  
   _Il nome ricorda un antico proprietario germanico._ → `frazioni/borghi-minori.html#montarfoni`
7. [d9e63c28] ●○○ `-d=` **Che cosa conserva oggi Montarfoni, oltre alla villa seicentesca?**  
   ✔ Un borgo-fattoria con chiesa, cantina e frantoio-mulino · ✘ Un aeroporto militare · Un anfiteatro romano · Una stazione termale  
   _Montarfoni è un borgo-fattoria organizzato come un piccolo paese._ → `frazioni/borghi-minori.html#montarfoni`
8. [d6eaf7ca] ●●● `Pv+` **Da chi fu acquistata nel 1814 la villa-fattoria di Dorna?**  
   ✔ Dalle suore Montalve della Quiete di Firenze · ✘ Dai Medici · Dai Gesuiti · Dal Comune di Arezzo  
   _Nel XVIII secolo era dei Riccardi; nel 1814 passò alle suore Montalve._ → `frazioni/borghi-minori.html#dorna`
9. [961f484f] ●○○ `-n=` **Che cosa è la torre di Dorna, ricordata dal 1198?**  
   ✔ La parte più antica rimasta integra del castello · ✘ Un campanile ottocentesco · Una torre dell'acquedotto · Un faro  
   _La torre è la parte più antica rimasta integra dell'insediamento longobardo._ → `frazioni/borghi-minori.html#dorna`
10. [7591d2bd] ●●● `Pv+` **A chi è dedicata la chiesa di San Martino in Poggio costruita nel 1690?**  
   ✔ Ai Santi Maria e Carlo · ✘ A San Martino e San Rocco · A San Biagio · A Sant'Andrea  
   _Il titolo ricorda il nobile fiorentino Carlo Casini, che la finanziò._ → `frazioni/borghi-minori.html#san-martino-in-poggio`
11. [ff97d330] ●●● `Pv+` **Grazie a chi fu costruita la chiesa di San Martino in Poggio nel 1690?**  
   ✔ Il nobile fiorentino Carlo Casini · ✘ Il vescovo Guglielmino degli Ubertini · La famiglia Pecchioli · Il notaio Becattini  
   _La chiesa fu costruita con il patrimonio donato da Carlo Casini._ → `frazioni/borghi-minori.html#san-martino-in-poggio`
12. [d3a07030] ●○○ `-n=` **Come descrissero i fiorentini il castello di Gaenne, passato sotto il loro dominio nel 1385?**  
   ✔ «Un forte castello di sito e di muro» · ✘ «La più bella rocca di Toscana» · «Un castello senza difese» · «Il nido dei ghibellini»  
   _Nel 1385 Gaenne passò a Firenze, che lo descrisse come «un forte castello di sito e di muro»._ → `frazioni/borghi-minori.html#gaenne`
13. [0aeb1238] ●●○ `Pv=` **A chi apparteneva il castello di Gaenne nel 1069?**  
   ✔ Ai longobardi di Dorna · ✘ Ai Medici · Ai vescovi di Siena · Ai conti Guidi  
   _Nel 1069 apparteneva ai longobardi di Dorna, poi passò ai Tarlati._ → `frazioni/borghi-minori.html#gaenne`
14. [b8b3b4f1] ●●○ `-v=` **Tra quali frazioni si trova la località Le Caserosse?**  
   ✔ Tra Viciomaggio e Pieve al Toppo · ✘ Tra Cornia e Tuori · Tra Oliveto e Ciggiano · Tra Spoiano e Gebbia  
   _Le Norme del Piano parlano di «località Caserosse (fra Viciomaggio e Pieve al Toppo)»._ → `lavoro-e-sapori.html#industria`
15. [e4fa556c] ●●● `Pv+` **In quale materiale è il cippo romano trovato a Le Fosse?**  
   ✔ Travertino · ✘ Marmo di Carrara · Bronzo · Granito  
   _A Le Fosse il Repertorio registra un cippo romano in travertino._ → `frazioni/borghi-minori.html#malpertuso-le-fosse`
16. [20485c5d] ●●○ `-n+` **Su che cosa sorsero i poderi di Montoto, lungo via della Centrale?**  
   ✔ Su un fortilizio longobardo · ✘ Su una villa romana · Su un convento francescano · Su una fornace etrusca  
   _I poderi di Montoto sorsero su un fortilizio longobardo, passato a Firenze nel 1385._ → `frazioni/borghi-minori.html#montoto`
17. [2bad47c2] ●●● `Pv+` **A quale santo è dedicata la chiesetta di Matroia?**  
   ✔ San Michele Arcangelo · ✘ San Rocco · San Biagio · Sant'Andrea  
   _La chiesetta di San Michele Arcangelo è quanto resta, con un rocchio di colonna e una vasca, di un antico insediamento religioso._ → `frazioni/borghi-minori.html#matroia`
18. [99c66c9f] ●●○ `-n+` **Che cosa si conserva a Tribbio, oltre al nome che ricorda un antico trivio?**  
   ✔ Un pozzo storico · ✘ Un arco romano · Una torre di guardia · Un ponte medievale  
   _Tribbio prende il nome da un trivio, un incrocio di tre strade, e conserva un vecchio pozzo censito tra i beni storici._ → `frazioni/borghi-minori.html#tribbio`
19. [7551f5ac] ●○○ `-n=` **Quando furono abbandonati i borghi medievali di Malpertuso e Le Fosse?**  
   ✔ Nel tardo Medioevo · ✘ Nell'Ottocento · Dopo il 1944 · In età romana  
   _Malpertuso e Le Fosse sono borghi medievali abbandonati nel tardo Medioevo._ → `frazioni/borghi-minori.html#malpertuso-le-fosse`
20. [d2a0a62f] ●●○ `-v=` **Di quale origine è il castello di Dorna?**  
   ✔ Longobarda · ✘ Etrusca · Normanna · Rinascimentale  
   _Dorna fu un castello longobardo (VIII–X secolo)._ → `frazioni/borghi-minori.html#dorna`
21. [a8e3eb8d] ●●● `Pv+` **Come è chiamata Dorna in un documento del 1181?**  
   ✔ Castrum Durna · ✘ Curtis Dornae · Villa Turna · Castellum Ornae  
   _Un documento del 1181 parla del castrum Durna; la torre è ricordata dal 1198._ → `frazioni/borghi-minori.html#dorna`
22. [e5f0dee8] ●●● `Pv+` **A quali santi era dedicata la chiesa documentata a Dorna nel 1182?**  
   ✔ Vito e Nicola · ✘ Pietro e Paolo · Cosma e Damiano · Giorgio e Luca  
   _Nel 1182 è documentata una chiesa dei Santi Vito e Nicola._ → `frazioni/borghi-minori.html#dorna`
23. [534d8c16] ●●● `Pv+` **A quale famiglia passò il castello di Gaenne dopo i longobardi di Dorna?**  
   ✔ I Tarlati · ✘ Gli Ubertini · I Medici · I conti Guidi  
   _Nel 1069 Gaenne apparteneva ai longobardi di Dorna, poi passò ai Tarlati._ → `frazioni/borghi-minori.html#gaenne`
24. [0574409f] ●●● `Nv+` **Da quale anno San Martino in Poggio è parrocchia?**  
   ✔ 1814 · ✘ 1690 · 1726 · 1917  
   _La chiesa del 1690 fu ampliata nel 1726 e divenne parrocchia nel 1814._ → `frazioni/borghi-minori.html#san-martino-in-poggio`
25. [a085dfa8] ●●○ `Nd+` **A che altitudine si trova, all'incirca, San Martino in Poggio?**  
   ✔ Circa 540 metri · ✘ Circa 140 metri · Circa 940 metri · Circa 1.240 metri  
   _San Martino in Poggio si trova a circa 540 metri._ → `frazioni/borghi-minori.html#san-martino-in-poggio`
26. [e834399c] ●●○ `Nd+` **Quanto è lunga, all'incirca, la cinta muraria a secco di Poggio Castellare?**  
   ✔ Circa 300 metri · ✘ Circa 30 metri · Circa 3 chilometri · Circa 10 metri  
   _Sulla cima resta una cinta ellittica a secco di circa 300 metri; la datazione è discussa._ → `frazioni/borghi-minori.html#poggio-castellare`
27. [1af9c0f0] ●●○ `Nd+` **Quanto è spessa, all'incirca, la cinta muraria a secco di Poggio Castellare?**  
   ✔ Circa 1,60 metri · ✘ Circa 16 centimetri · Circa 6 metri · Circa 16 metri  
   _La cinta ellittica a secco è spessa 1,60 metri e lunga circa 300._ → `frazioni/borghi-minori.html#poggio-castellare`
28. [6762121d] ●●○ `-v+` **Per curare quali malati si attingeva l'acqua della sorgente di Matroia?**  
   ✔ I neonati colpiti da malattie gastroenteriche · ✘ Gli anziani con dolori articolari · Chi soffriva di malattie della pelle · Chi aveva i calcoli renali  
   _Alla sorgente, presso la cappella di San Michele Arcangelo, erano attribuite virtù salutari soprattutto per i neonati._ → `frazioni/borghi-minori.html#matroia`
29. [191e897a] ●●○ `-n+` **Dove si trova oggi il mulino di Montoto?**  
   ✔ Sommerso dall'invaso della Penna · ✘ Trasformato in museo · Inglobato nella villa di Montarfoni · Ricostruito a Pieve a Maiano  
   _Il mulino di Montoto è oggi sommerso dall'invaso della Penna, lungo l'antica strada di Vallelunga._ → `frazioni/borghi-minori.html#montoto`
30. [de37df18] ●●○ `-n+` **Che cosa è stato trovato a Le Fosse, oltre a un cippo romano in travertino?**  
   ✔ Reperti sporadici di età preistorica e romana · ✘ Una necropoli etrusca · Un tesoro di monete medievali · Un mosaico pavimentale  
   _Il Repertorio registra a Le Fosse un cippo romano in travertino e reperti sporadici di età preistorica e romana._ → `frazioni/borghi-minori.html#malpertuso-le-fosse`
31. [ff1c509f] ●○○ `-d+` **Che cosa prevede il Piano Strutturale per il borgo-fattoria e la villa di Montarfoni?**  
   ✔ Un «polo di eccellenza territoriale» · ✘ Un centro commerciale · Una zona industriale · Un campeggio  
   _Il borgo-fattoria è organizzato come un piccolo paese, con piazzetta, chiesa, cantina e frantoio-mulino._ → `frazioni/borghi-minori.html#montarfoni`
32. [2e9fd6ab] ●●○ `-v+` **Di che cosa fu dotata la chiesa di San Martino in Poggio quando fu ampliata nel 1726?**  
   ✔ Di due nuovi altari · ✘ Di un campanile a vela · Di un organo · Di un portico a tre archi  
   _La chiesa dei Santi Maria e Carlo, costruita nel 1690, fu ampliata nel 1726 con due nuovi altari._ → `frazioni/borghi-minori.html#san-martino-in-poggio`
33. [585551af] ●●○ `-v=` **Quale altro luogo è destinato a diventare un parco archeologico insieme a Poggio Castellare?**  
   ✔ Il castello di Gaenne · ✘ Matroia · Tribbio · Dorna  
   _Il Piano Strutturale prevede un parco archeologico con campo scuola di scavo a Poggio Castellare e Gaenne._ → `frazioni/borghi-minori.html#poggio-castellare`
34. [dc8e4d56] ●●● `Pv+` **Quale Madonna era venerata a Matroia, legata al culto delle acque?**  
   ✔ La Madonna del Latte · ✘ La Madonna del Conforto · La Madonna della Costarella · La Madonna di Mercatale  
   _A Matroia era venerata una Madonna del Latte; l'acqua della sorgente si attingeva per i neonati._ → `frazioni/borghi-minori.html#matroia`
35. [1a6af485] ●●● `Pv+` **Sopra quale strada sorse il castello di Montarfoni?**  
   ✔ La strada Regia Aretina · ✘ La via Cassia · La via Francigena · La Via Vecchia Senese  
   _Il castello sorse sopra la strada Regia Aretina; ne restano la porta e tratti delle mura._ → `frazioni/borghi-minori.html#montarfoni`

## Lavoro e sapori (25)

1. [fbceb884] ●○○ `-d-` **Che cosa produce l'azienda CEIA di Viciomaggio?**  
   ✔ Metal detector e sistemi di ispezione · ✘ Cucine componibili · Gioielli · Macchine agricole  
   _CEIA progetta e costruisce metal detector e sistemi di ispezione elettromagnetica._ → `lavoro-e-sapori.html#industria`
2. [84695b7e] ●●● `Nv=` **In quale anno fu costituita la società CEIA?**  
   ✔ 1968 · ✘ 1954 · 1974 · 2002  
   _CEIA fu costituita nel 1968; il primo brevetto risale al 1962._ → `lavoro-e-sapori.html#industria`
3. [da81be25] ●●○ `-v=` **Per quale industria CEIA brevettò nel 1962 i suoi primi metal detector?**  
   ✔ L'industria tessile · ✘ L'industria automobilistica · L'industria aeronautica · L'industria mineraria  
   _Il primo brevetto del 1962 riguardava metal detector per l'industria tessile._ → `lavoro-e-sapori.html#industria`
4. [d00c385a] ●○○ `-d=` **Dal 1975 CEIA produce metal detector per quale settore?**  
   ✔ Gli aeroporti · ✘ Le miniere · Le cucine · I vigneti  
   _Dal 1975 CEIA realizza metal detector per gli aeroporti._ → `lavoro-e-sapori.html#industria`
5. [4fbe35df] ●○○ `-d=` **Di che cosa si occupa Chimet?**  
   ✔ Del recupero e dell'affinazione dei metalli preziosi · ✘ Della produzione di vino · Della costruzione di mobili · Della produzione di cucine  
   _Chimet recupera e affina i metalli preziosi contenuti negli scarti industriali._ → `lavoro-e-sapori.html#industria`
6. [ec632da2] ●●● `Nv=` **In quale anno fu fondata Chimet?**  
   ✔ 1974 · ✘ 1954 · 1968 · 1990  
   _Chimet fu fondata nel 1974._ → `lavoro-e-sapori.html#industria`
7. [15d7a73c] ●●○ `-v=` **Dove aprì Chimet il suo primo stabilimento, nel 1976?**  
   ✔ A Badia al Pino · ✘ A Tegoleto · A Ponticino · A Cornia  
   _Il primo stabilimento fu aperto a Badia al Pino; negli anni Ottanta seguì quello di Viciomaggio._ → `lavoro-e-sapori.html#industria`
8. [aaba5c69] ●○○ `-d-` **Che cosa produceva l'azienda Del Tongo di Tegoleto?**  
   ✔ Cucine componibili · ✘ Metal detector · Biciclette · Scarpe  
   _La Del Tongo produceva cucine componibili vendute in tutto il mondo._ → `lavoro-e-sapori.html#del-tongo`
9. [4825255e] ●●● `Nv=` **In quale anno fu fondata la Del Tongo?**  
   ✔ 1954 · ✘ 1968 · 1974 · 1982  
   _La Del Tongo fu fondata nel 1954 dai fratelli Stefano e Pasquale Del Tongo._ → `lavoro-e-sapori.html#del-tongo`
10. [51f555d3] ●●○ `Nn=` **In quale anno fallì la Del Tongo?**  
   ✔ 2018 · ✘ 1991 · 2004 · 2022  
   _L'azienda fallì nel 2018._ → `lavoro-e-sapori.html#del-tongo`
11. [005b6b8c] ●●● `Pv+` **Quale azienda acquisì nel 2022 il marchio Del Tongo?**  
   ✔ Kico · ✘ Scavolini · Lube · Veneta Cucine  
   _Il marchio fu aggiudicato all'asta all'azienda teramana Kico._ → `lavoro-e-sapori.html#del-tongo`
12. [6355b329] ●●● `Nv+` **In quali anni fu attiva la squadra ciclistica professionistica Del Tongo?**  
   ✔ Dal 1982 al 1991 · ✘ Dal 1954 al 1964 · Dal 1995 al 2005 · Dal 2004 al 2018  
   _La squadra corse tra i professionisti dal 1982 al 1991._ → `lavoro-e-sapori.html#del-tongo`
13. [92e0687d] ●●○ `Pv=` **Con quale corridore la squadra Del Tongo vinse il Giro d'Italia del 1983?**  
   ✔ Giuseppe Saronni · ✘ Francesco Moser · Fausto Coppi · Marco Pantani  
   _Saronni vinse il Giro 1983 e la Milano-Sanremo dello stesso anno._ → `lavoro-e-sapori.html#del-tongo`
14. [6c2a3e07] ●●● `Pv+` **Con quale corridore la squadra Del Tongo vinse il Giro d'Italia del 1991?**  
   ✔ Franco Chioccioli · ✘ Gianni Bugno · Claudio Chiappucci · Miguel Indurain  
   _Franco Chioccioli vinse il Giro d'Italia del 1991._ → `lavoro-e-sapori.html#del-tongo`
15. [fbd430a4] ●●○ `Pv=` **Quale celebre velocista esordì tra i professionisti con la maglia Del Tongo?**  
   ✔ Mario Cipollini · ✘ Alessandro Petacchi · Mark Cavendish · Erik Zabel  
   _Mario Cipollini esordì tra i professionisti con la Del Tongo._ → `lavoro-e-sapori.html#del-tongo`
16. [5ea5e45a] ●●○ `Pv=` **Quale di queste è una varietà tradizionale di olivo del territorio?**  
   ✔ Moraiolo · ✘ Nocellara · Taggiasca · Coratina  
   _Le varietà tradizionali sono frantoio, leccino, moraiolo e pendolino._ → `lavoro-e-sapori.html#campi`
17. [a04d9971] ●○○ `Pd=` **A quale Strada del Vino appartiene il Comune di Civitella?**  
   ✔ Strada del Vino Terre di Arezzo · ✘ Strada del Vino Nobile di Montepulciano · Strada del Chianti Classico · Strada del Vino della Costa degli Etruschi  
   _Il Comune è socio della Strada del Vino Terre di Arezzo._ → `lavoro-e-sapori.html#campi`
18. [92190992] ●●○ `-v=` **Dove ha sede la condotta Slow Food Valdichiana?**  
   ✔ A Civitella · ✘ A Montepulciano · A Cortona · A Siena  
   _Slow Food Valdichiana ha sede a Civitella in Val di Chiana._ → `lavoro-e-sapori.html#slow-food`
19. [fd5f1067] ●●○ `Pn=` **Come si chiama il progetto di educazione alimentare che Slow Food porta nelle scuole del comune?**  
   ✔ Orto in Condotta · ✘ Scuola in Fattoria · Mangia Sano · Cuochi in Classe  
   _Orto in Condotta si svolge nelle scuole dell'Istituto comprensivo Martiri di Civitella._ → `lavoro-e-sapori.html#slow-food`
20. [27480726] ●●○ `Pn=` **Chi fondò nel 1954 la Del Tongo?**  
   ✔ I fratelli Stefano e Pasquale Del Tongo · ✘ Il Comune di Civitella · Una cooperativa di falegnami · Un gruppo industriale milanese  
   _I fratelli Stefano e Pasquale Del Tongo fondarono a Tegoleto l'azienda di cucine componibili._ → `lavoro-e-sapori.html`
21. [ef327bd3] ●●● `Pv+` **Quale classica del ciclismo vinse la squadra Del Tongo nel 1983?**  
   ✔ La Milano-Sanremo · ✘ La Parigi-Roubaix · La Liegi-Bastogne-Liegi · Il Giro delle Fiandre  
   _Nel 1983 la Del Tongo vinse il Giro d'Italia con Saronni e la Milano-Sanremo._ → `lavoro-e-sapori.html`
22. [b2e17c50] ●●● `Nn+` **Quante tappe del Giro d'Italia vinse la squadra ciclistica Del Tongo?**  
   ✔ 29 · ✘ 9 · 59 · 99  
   _Tra il 1982 e il 1991 la squadra vinse 29 tappe del Giro d'Italia._ → `lavoro-e-sapori.html`
23. [8ee7c334] ●●○ `-v+` **Dove aprì Chimet il suo secondo stabilimento, negli anni Ottanta?**  
   ✔ A Viciomaggio · ✘ A Tegoleto · Ad Albergo · A Ponticino  
   _Chimet aprì il primo stabilimento a Badia al Pino nel 1976 e il secondo a Viciomaggio negli anni Ottanta._ → `lavoro-e-sapori.html`
24. [d8488735] ●○○ `Pd=` **Quali varietà di olivo sono tipiche del territorio, insieme al moraiolo?**  
   ✔ Frantoio, leccino e pendolino · ✘ Taggiasca, nocellara e coratina · Ogliarola, carolea e bosana · Itrana, peranzana e biancolilla  
   _Le varietà sono frantoio, leccino, moraiolo e pendolino; l'olio è Toscano IGP._ → `lavoro-e-sapori.html`
25. [8cac38d7] ●●○ `Pv=` **Quale indicazione geografica ha l'olio extravergine del territorio?**  
   ✔ Toscano IGP · ✘ Chianti Classico DOP · Riviera Ligure DOP · Terra di Bari DOP  
   _Le varietà locali sono frantoio, leccino, moraiolo e pendolino, e l'olio è Toscano IGP._ → `lavoro-e-sapori.html`

## Feste e sport (37)

1. [d16bdeb0] ●●○ `-v=` **In quale frazione si tiene la Sagra della Bistecca?**  
   ✔ Badia al Pino · ✘ Tegoleto · Spoiano · Ciggiano  
   _La Sagra della Bistecca si tiene a Badia al Pino tra fine agosto e inizio settembre._ → `feste-e-associazioni.html#agosto`
2. [3116bcad] ●●● `Pv+` **Chi organizza la Sagra della Bistecca?**  
   ✔ Il Circolo Ricreativo Olinto Paccinelli · ✘ La Pro Loco di Ciggiano · L'U.S.D. Tegoleto · Slow Food Valdichiana  
   _La organizza il Circolo Ricreativo Olinto Paccinelli di Badia al Pino._ → `feste-e-associazioni.html#agosto`
3. [f0be8eb1] ●●○ `-v=` **In quale frazione si tiene la Sagra del Crostino?**  
   ✔ Albergo · ✘ Oliveto · Tuori · Viciomaggio  
   _La Sagra del Crostino si tiene a luglio al campo sportivo di Albergo._ → `feste-e-associazioni.html#luglio`
4. [4422dd68] ●●● `Pv+` **Chi organizza la Sagra del Crostino di Albergo?**  
   ✔ La Polisportiva Albergo Oliveto · ✘ Il Circolo ARCI di Pieve al Toppo · La Pro Loco di Civitella · La parrocchia di Oliveto  
   _La Polisportiva Albergo Oliveto, che si occupa anche di ciclismo giovanile._ → `feste-e-associazioni.html#luglio`
5. [2d7782fe] ●●○ `-v=` **In quale frazione si tiene la Sagra dei Baccelli?**  
   ✔ Spoiano · ✘ Cornia · Albergo · Pieve a Maiano  
   _La Sagra dei Baccelli si tiene a Spoiano._ → `feste-e-associazioni.html#maggio`
6. [b7b8833c] ●○○ `-n=` **In quale mese si tiene la Sagra dei Baccelli?**  
   ✔ Maggio · ✘ Settembre · Dicembre · Febbraio  
   _La sagra si svolge su due fine settimana di maggio._ → `feste-e-associazioni.html#maggio`
7. [35bf8000] ●●○ `-v=` **In quale frazione si tiene la Sagra del Cinghiale?**  
   ✔ Pieve a Maiano · ✘ Badia al Pino · Tegoleto · Spoiano  
   _La organizza il Circolo ricreativo U.S. Pieve a Maiano a fine agosto._ → `feste-e-associazioni.html#agosto`
8. [18b90576] ●●○ `-v=` **In quale frazione si tiene la Festa dell'uva, del vino e dell'olio?**  
   ✔ Ciggiano · ✘ Pieve al Toppo · Albergo · Tegoleto  
   _La organizza la Pro Loco di Ciggiano a settembre._ → `feste-e-associazioni.html#settembre`
9. [e1d94892] ●●● `Nn+` **Quale edizione della Festa dell'uva di Ciggiano si è tenuta nel 2026?**  
   ✔ La 49ª · ✘ La 12ª · La 25ª · La 100ª  
   _Nel 2026 si è tenuta la 49ª edizione; nel 2027 sarà la cinquantesima._ → `feste-e-associazioni.html#settembre`
10. [3102235c] ●○○ `-d=` **A che cosa è dedicata la Sagra della Pesca di Pieve al Toppo?**  
   ✔ Al frutto, la pesca · ✘ Alla pesca sportiva · Al pesce di mare · Alla pesca di beneficenza  
   _È una sagra del frutto: l'ultimo giorno c'è persino il motoraduno «Peach and Bikers»._ → `feste-e-associazioni.html#settembre`
11. [642f3ac8] ●○○ `-n=` **Quando si tiene la Fiera del Miele di Pieve al Toppo?**  
   ✔ La prima domenica di ottobre · ✘ Il giorno di Pasqua · A Ferragosto · L'ultima domenica di gennaio  
   _La Fiera del Miele si tiene la prima domenica di ottobre, nel piazzale del Circolo ricreativo._ → `feste-e-associazioni.html#ottobre`
12. [3a131b5f] ●●○ `-v=` **In quale frazione si tiene la Fiera del Miele?**  
   ✔ Pieve al Toppo · ✘ Oliveto · Civitella · Spoiano  
   _La organizzano il Comune e Slow Food Valdichiana a Pieve al Toppo._ → `feste-e-associazioni.html#ottobre`
13. [f220d5ea] ●●○ `-v=` **Dove si tiene il Mercato del Cacio?**  
   ✔ Nel borgo di Civitella · ✘ A Tegoleto · A Pieve a Maiano · A Badia al Pino  
   _Il Mercato del Cacio si tiene a maggio in piazza Lazzeri, a Civitella._ → `feste-e-associazioni.html#maggio`
14. [beec873c] ●○○ `-d=` **Che cosa si degusta a Calici sotto la Torre?**  
   ✔ I vini della Strada del Vino Terre di Arezzo · ✘ Formaggi di fossa · Birre artigianali tedesche · Olio nuovo  
   _Ad agosto nel borgo di Civitella, con i sommelier AIS._ → `feste-e-associazioni.html#agosto`
15. [2e7141f4] ●●○ `-v=` **In quale frazione si tiene la Festa della Rosa?**  
   ✔ Viciomaggio · ✘ Oliveto · Cornia · Albergo  
   _La organizza l'A.S.D. Viciomaggio tra fine aprile e inizio maggio._ → `feste-e-associazioni.html#aprile`
16. [23617f63] ●●○ `-v=` **In quale frazione si tiene il RioFest?**  
   ✔ Tegoleto · ✘ Ciggiano · Tuori · Spoiano  
   _Il RioFest è un festival di musica e spettacoli nato a Tegoleto nel 2025._ → `feste-e-associazioni.html#settembre`
17. [8e949863] ●●● `Nv+` **In quale anno si è tenuta la prima edizione del RioFest?**  
   ✔ 2025 · ✘ 2010 · 2018 · 2026  
   _La prima edizione si è tenuta il 20 settembre 2025._ → `feste-e-associazioni.html#settembre`
18. [260bd43e] ●●○ `Pv=` **Quale associazione organizza il RioFest e Cinema sotto le Stelle?**  
   ✔ Comunità & Tegoleto · ✘ La Pro Loco di Ciggiano · Il Circolo Paccinelli · Slow Food Valdichiana  
   _Comunità & Tegoleto APS promuove entrambe le iniziative._ → `feste-e-associazioni.html#ass-tegoleto`
19. [253c5d99] ●○○ `-n=` **Dove si svolgono le proiezioni di Cinema sotto le Stelle?**  
   ✔ In piazza della Chiesa a Tegoleto · ✘ Nella Rocca di Civitella · Allo stadio di Badia al Pino · Al lago della Penna  
   _Le proiezioni gratuite si tengono il mercoledì sera di luglio, dal 2018._ → `feste-e-associazioni.html#luglio`
20. [4a402844] ●●○ `-v=` **In quale frazione si tiene il Mercato dei Sapori e della Terra?**  
   ✔ Tegoleto · ✘ Civitella · Pieve al Toppo · Oliveto  
   _Si tiene ad aprile in piazza della Chiesa a Tegoleto._ → `feste-e-associazioni.html#aprile`
21. [044286f0] ●○○ `-n=` **In quale periodo si tiene la rassegna L'Olio Novo?**  
   ✔ Tra novembre e dicembre · ✘ A febbraio · A giugno · A Ferragosto  
   _La rassegna dell'olio nuovo si tiene da metà novembre all'inizio di dicembre._ → `feste-e-associazioni.html#novembre`
22. [20356cbe] ●●○ `-v=` **In quale frazione si tiene il Presepe Vivente?**  
   ✔ Oliveto · ✘ Ciggiano · Tegoleto · Badia al Pino  
   _Il Presepe Vivente di Oliveto, organizzato dalla parrocchia, si tiene dal 2014._ → `feste-e-associazioni.html#dicembre`
23. [87a41003] ●●● `Pv+` **Chi organizza la Festa al Tegoleto?**  
   ✔ L'U.S.D. Tegoleto · ✘ La Pro Loco di Civitella · Il Circolo ARCI · La parrocchia di Tegoleto  
   _La organizza l'U.S.D. Tegoleto con l'associazione Comunità & Tegoleto._ → `feste-e-associazioni.html#giugno`
24. [2f520af4] ●●○ `-v=` **In quale frazione ha sede la Società Filarmonica, la banda del paese?**  
   ✔ Ciggiano · ✘ Tuori · Gebbia · Matroia  
   _La Società Filarmonica Ciggiano è iscritta al Registro del Terzo settore._ → `feste-e-associazioni.html#ass-ciggiano`
25. [909f8526] ●○○ `-d=` **Di quale sport si occupa la Polisportiva Albergo Oliveto con i più giovani?**  
   ✔ Ciclismo · ✘ Rugby · Nuoto · Scherma  
   _Organizza corsi di avviamento al ciclismo per bambini e ragazzi._ → `feste-e-associazioni.html#ass-albergo-oliveto`
26. [daf78ce6] ●●○ `Pv=` **Chi organizza la Sagra dei Baccelli di Spoiano?**  
   ✔ La Polisportiva Spoiano · ✘ La Pro Loco di Ciggiano · Il Circolo ARCI di Pieve al Toppo · La parrocchia di Spoiano  
   _La Sagra dei Baccelli è organizzata dalla Polisportiva Spoiano._ → `feste-e-associazioni.html`
27. [c3556ffe] ●●● `Nn+` **Quale edizione della Sagra dei Baccelli si è tenuta nel 2025?**  
   ✔ La 48ª · ✘ La 8ª · La 25ª · La 75ª  
   _Nel 2025 la Sagra dei Baccelli è arrivata alla 48ª edizione._ → `feste-e-associazioni.html`
28. [eb4598d2] ●●○ `Pv=` **Chi organizza la Sagra della Pesca di Pieve al Toppo?**  
   ✔ Il Circolo ARCI di Pieve al Toppo · ✘ L'U.S.D. Tegoleto · La Polisportiva Albergo Oliveto · La Pro Loco di Civitella  
   _La Sagra della Pesca, dedicata al frutto, è organizzata dal Circolo ARCI._ → `feste-e-associazioni.html`
29. [c9416e86] ●●○ `Pv=` **Chi organizza la Festa della Rosa di Viciomaggio?**  
   ✔ L'A.S.D. Viciomaggio · ✘ La parrocchia di San Martino · Il Circolo Paccinelli · Comunità & Tegoleto  
   _La Festa della Rosa, tra fine aprile e inizio maggio, è organizzata dall'A.S.D. Viciomaggio._ → `feste-e-associazioni.html`
30. [98eb66e1] ●●● `Pv+` **Chi organizza la Sagra del Cinghiale di Pieve a Maiano?**  
   ✔ L'U.S. Pieve a Maiano · ✘ La Pro Loco di Civitella · Il Circolo ARCI · Slow Food Valdichiana  
   _La Sagra del Cinghiale è organizzata dall'U.S. Pieve a Maiano._ → `feste-e-associazioni.html`
31. [da689784] ●●○ `Pv=` **Chi organizza la Festa dell'uva, del vino e dell'olio di Ciggiano?**  
   ✔ La Pro Loco di Ciggiano · ✘ La Società Filarmonica · La parrocchia di San Biagio · Il Comune con Slow Food  
   _La festa è organizzata dalla Pro Loco di Ciggiano._ → `feste-e-associazioni.html`
32. [9a5d061a] ●○○ `-n=` **In quale mese si tiene il Mercato del Cacio, nel borgo di Civitella?**  
   ✔ Maggio · ✘ Febbraio · Agosto · Novembre  
   _Il Mercato del Cacio si tiene a maggio ed è organizzato dal Comune con Slow Food._ → `feste-e-associazioni.html`
33. [11601917] ●○○ `-n=` **In quale mese si tiene la Sagra del Crostino di Albergo?**  
   ✔ Luglio · ✘ Marzo · Ottobre · Dicembre  
   _La Sagra del Crostino si tiene a luglio._ → `feste-e-associazioni.html`
34. [4c118d8f] ●●○ `-v=` **Chi organizza il Mercato del Cacio, Calici sotto la Torre e la Fiera del Miele?**  
   ✔ Il Comune con Slow Food Valdichiana · ✘ La Pro Loco di Ciggiano · Il Circolo ARCI · La Polisportiva Albergo Oliveto  
   _Queste manifestazioni sono organizzate dal Comune con Slow Food._ → `feste-e-associazioni.html`
35. [7f7108c7] ●●○ `-v+` **In quale giorno della settimana si tengono le proiezioni di Cinema sotto le Stelle a Tegoleto?**  
   ✔ Il mercoledì · ✘ Il lunedì · Il venerdì · La domenica  
   _Le proiezioni gratuite si tengono il mercoledì sera di luglio in piazza della Chiesa._ → `feste-e-associazioni.html`
36. [f146f2ed] ●●● `Nv+` **Da quale anno si tiene Cinema sotto le Stelle a Tegoleto?**  
   ✔ 2018 · ✘ 2008 · 2022 · 2025  
   _Le proiezioni sono nate nel 2018._ → `feste-e-associazioni.html`
37. [4be5e12f] ●●● `Nn+` **Quale edizione dell'Olio Novo si è tenuta nel 2025?**  
   ✔ La 28ª · ✘ La 5ª · La 50ª · La 100ª  
   _Nel 2025 L'Olio Novo è arrivato alla 28ª edizione._ → `feste-e-associazioni.html`
