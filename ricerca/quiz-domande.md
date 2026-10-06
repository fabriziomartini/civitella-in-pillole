# Domande del quiz

Elenco leggibile del pool usato da `quiz.html`. **Non modificarlo a mano:** le domande si cambiano in `tools/quiz_domande.py`, poi si lancia `python3 tools/genera_quiz.py`, che rigenera questo file e `js/quiz-data.js`.

**Regola:** ogni domanda nasce da un fatto di livello R, N o W in `fatti-verificati.md`, mai da un fatto su cui le fonti divergono.

L'**id** tra parentesi quadre è quello che compare nel foglio delle statistiche; il livello (●○○ facile, ●●○ media, ●●● difficile) e il codice che lo determina sono spiegati in `tools/quiz_difficolta.py`.

Totale: 350 domande.

## Geografia (47)

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
   _Secondo Wikipedia e ToscanaNovecento, Civitella sorge sulle Colline delle Lepri._ → `geografia.html`
9. [f2064462] ●○○ `Pd-` **Tra quali valli si trova il colle di Civitella?**  
   ✔ Valdambra e Valdichiana · ✘ Casentino e Valtiberina · Val d'Orcia e Valdelsa · Mugello e Valdisieve  
   _Il Repertorio del Piano descrive il colle di Civitella «tra Valdambra e Valdichiana»._ → `geografia.html`
10. [75a8fc8f] ●○○ `Pd=` **Quale di questi torrenti scorre nel territorio comunale?**  
   ✔ L'Esse · ✘ L'Ombrone · Il Serchio · La Cecina  
   _Tra i torrenti del territorio ci sono l'Esse, il Leprone, il Trove e la Lota._ → `geografia.html`
11. [e2f25241] ●●○ `Pn=` **Una parte del territorio comunale rientra in quale riserva naturale?**  
   ✔ Ponte a Buriano e Penna · ✘ Lago di Montepulciano · Monte Rufeno · Bosco di Sant'Agnese  
   _La Riserva di Ponte a Buriano e Penna protegge un tratto dell'Arno e si estende nei comuni di Arezzo, Civitella e Laterina._ → `geografia.html`
12. [e65e12bd] ●○○ `-d-` **Quale fiume protegge la Riserva naturale di Ponte a Buriano e Penna?**  
   ✔ L'Arno · ✘ Il Tevere · L'Ombrone · Il Serchio  
   _La riserva protegge il tratto dell'Arno tra Ponte a Buriano e la diga della Penna._ → `geografia.html`
13. [96d34023] ●●○ `-v+` **Quale frazione il Piano Strutturale indica come «porta d'accesso» meridionale alla Riserva di Ponte a Buriano e Penna?**  
   ✔ Pieve a Maiano · ✘ Spoiano · Tegoleto · Oliveto  
   _Il Piano assegna a Pieve a Maiano il ruolo di porta d'accesso meridionale alla Riserva._ → `frazioni/pieve-a-maiano.html`
14. [1a05018c] ●○○ `Pd=` **Quale vino si produce sulle colline del comune?**  
   ✔ Il Chianti Colli Aretini · ✘ Il Brunello di Montalcino · Il Morellino di Scansano · La Vernaccia di San Gimignano  
   _Nella fascia collinare si producono vigneti di Chianti Colli Aretini._ → `geografia.html`
15. [607cb6d7] ●○○ `-d=` **Come sono sistemati, tradizionalmente, gli oliveti sui pendii collinari?**  
   ✔ Su terrazzamenti e ciglionamenti · ✘ In serre riscaldate · In risaie allagate · Su terreni sabbiosi di duna  
   _La Relazione del Piano Strutturale descrive in collina oliveti su terrazzamenti e ciglionamenti._ → `geografia.html`
16. [878f8be1] ●●● `Nn+` **Circa quanti abitanti del comune vivono in case sparse, fuori dai centri abitati?**  
   ✔ Circa un quarto · ✘ Quasi nessuno · Circa tre quarti · Più del 90%  
   _Al censimento 2021 le case sparse contavano 2.256 residenti su 8.814._ → `geografia.html`
17. [b051cf1f] ●●○ `-v=` **Quale frazione è divisa tra Civitella e il comune di Laterina Pergine Valdarno?**  
   ✔ Ponticino · ✘ Tuori · Cornia · Spoiano  
   _Ponticino è a cavallo del confine comunale; il centro abitato è attribuito dall'ISTAT a Laterina Pergine Valdarno._ → `frazioni/ponticino.html`
18. [7a620330] ●●○ `Pn+` **Con quale comune tedesco è gemellato Civitella in Val di Chiana?**  
   ✔ Kämpfelbach · ✘ Heidelberg · Rosenheim · Bamberga  
   _Il comune è gemellato con Kämpfelbach, i cui rappresentanti partecipano al Mercato del Cacio._ → `frazioni/civitella.html`
19. [608e57f8] ●●○ `Nn=` **Da quando Civitella fa parte della rete Cittaslow?**  
   ✔ Dal 2002 · ✘ Dal 1985 · Dal 2015 · Dal 2023  
   _Il comune aderisce a Cittaslow dal luglio 2002._ → `lavoro-e-sapori.html`
20. [f5a0d8d3] ●●● `Nn+` **In quale anno Civitella è entrata nell'associazione Città dell'Olio?**  
   ✔ 2025 · ✘ 1998 · 2008 · 2016  
   _Civitella fa parte delle Città dell'Olio dal 2025._ → `lavoro-e-sapori.html`
21. [38fd6d61] ●○○ `-d+` **Che cosa è stato trovato nel 2004 in località La Cascinella, presso Ciggiano?**  
   ✔ Tracce di un insediamento etrusco e romano · ✘ Una nave medievale · Un tesoro di monete d'oro · Un mosaico bizantino  
   _Frammenti di macine etrusche, tegole e vasellame romani della prima età imperiale._ → `frazioni/ciggiano.html`
22. [c7eef4ea] ●○○ `-d+` **Secondo Visit Tuscany, che cosa è stato trovato nella chiesa di San Pietro a Ciggiano?**  
   ✔ Reperti con iscrizioni etrusche · ✘ Un affresco di Giotto · Una nave romana · Un codice miniato  
   _Secondo Visit Tuscany, nella chiesa di San Pietro a Ciggiano, di origine medievale, sono stati trovati reperti con iscrizioni etrusche._ → `frazioni/ciggiano.html`
23. [eab967e7] ●●○ `Nd+` **Fino a che spessore arrivano i muri del Castellare di Sant'Angelo, presso Cornia?**  
   ✔ Circa un metro e mezzo · ✘ Circa dieci centimetri · Circa cinque metri · Circa dieci metri  
   _Il Repertorio del Piano Strutturale descrive i muri del Castellare di Sant'Angelo, spessi fino a un metro e mezzo._ → `frazioni/cornia.html`
24. [1526724b] ●●○ `Pn+` **Su segnalazione di chi furono scoperte le fornaci romane in località I Ponti, a Pieve al Toppo?**  
   ✔ Del Gruppo Archeologico del Dopolavoro Ferroviario di Arezzo · ✘ Di un parroco del paese · Della Soprintendenza di Firenze durante un restauro · Di una scuola elementare  
   _Le strutture, a circa 1,60 m di profondità, sono interpretate come fornaci per la terra sigillata aretina._ → `frazioni/pieve-al-toppo.html`
25. [5b8c6dd0] ●●○ `-n+` **Quale reperto da Viciomaggio è conservato al Museo Archeologico Nazionale di Arezzo?**  
   ✔ Un cammeo di diaspro · ✘ Un'anfora greca · Una statua di bronzo · Un elmo longobardo  
   _Al Museo «Gaio Cilnio Mecenate» è conservato il cammeo; i vasi del I secolo a.C. sono invece in luogo sconosciuto._ → `frazioni/viciomaggio.html`
26. [dc640362] ●○○ `-d=` **Che cosa prevede il Piano Strutturale per l'area di Cornia?**  
   ✔ Un parco faunistico e un'area naturale protetta · ✘ Una zona industriale · Un aeroporto · Una diga  
   _Il Piano prevede a Cornia un Parco faunistico e un'ANPIL, con un centro servizi negli edifici inutilizzati del borgo._ → `frazioni/cornia.html`
27. [20b4867a] ●○○ `-d=` **Tra quali località si estende il tratto dell'Arno protetto dalla Riserva naturale di Ponte a Buriano e Penna?**  
   ✔ Tra Ponte a Buriano e la diga della Penna · ✘ Tra Firenze e Pontassieve · Tra Stia e Poppi · Tra Empoli e Pisa  
   _La Riserva protegge il tratto dell'Arno tra Ponte a Buriano e la diga della Penna._ → `geografia.html`
28. [848435e4] ●●○ `Nd=` **Tra quali quote si trovano i centri abitati del comune, secondo Cittaslow?**  
   ✔ Tra circa 300 e 600 metri · ✘ Tra 0 e 100 metri · Tra 800 e 1.200 metri · Tra 1.200 e 1.500 metri  
   _I centri abitati del comune stanno tra circa 300 e 600 metri di quota._ → `geografia.html`
29. [4298beed] ●○○ `-v-` **La pianura del comune è la parte settentrionale di quale valle?**  
   ✔ La Val di Chiana · ✘ Il Valdarno · La Val d'Orcia · Il Casentino  
   _Il territorio ha una zona collinare e una di pianura, che è la parte settentrionale della Val di Chiana._ → `geografia.html`
30. [a852afc3] ●○○ `Pd=` **Quale di questi è uno dei torrenti principali del comune, insieme a Esse, Trove e Lota?**  
   ✔ Il Leprone · ✘ L'Arbia · La Merse · Il Bisenzio  
   _I torrenti principali sono Esse, Leprone, Trove e Lota._ → `geografia.html`
31. [4d63ebae] ●●● `Nn+` **Quanti residenti contava Pieve al Toppo, il centro più popoloso del comune, al censimento del 2021?**  
   ✔ 1.545 · ✘ 545 · 3.545 · 6.200  
   _Al censimento ISTAT 2021 Pieve al Toppo contava 1.545 residenti, davanti a Tegoleto (1.412)._ → `geografia.html`
32. [52faadf9] ●●○ `-v+` **Quale centro è il terzo per numero di abitanti, dopo Pieve al Toppo e Tegoleto?**  
   ✔ Badia al Pino · ✘ Viciomaggio · Ciggiano · Albergo  
   _Al censimento 2021 Badia al Pino contava 1.059 residenti, Viciomaggio 950._ → `geografia.html`
33. [729c801a] ●●● `Nv+` **Quanti residenti contava il borgo di Civitella, il capoluogo storico, al censimento del 2021?**  
   ✔ 148 · ✘ 1.480 · 2.300 · 15  
   _Il borgo storico contava 148 residenti; il centro più popoloso, Pieve al Toppo, ne contava 1.545._ → `geografia.html`
34. [2a6d43b8] ●●○ `-v+` **Quale di queste località era la meno popolosa al censimento del 2021?**  
   ✔ Oliveto · ✘ Tuori · Spoiano · Albergo  
   _Oliveto contava 15 residenti, Spoiano 120, Tuori 129, Albergo 279._ → `geografia.html`
35. [dc924e7d] ●●○ `-v+` **Quale frazione contava circa 950 residenti al censimento del 2021?**  
   ✔ Viciomaggio · ✘ Ciggiano · Albergo · Tuori  
   _Viciomaggio contava 950 residenti, Ciggiano 530, Albergo 279, Tuori 129._ → `geografia.html`
36. [3589ff26] ●●○ `-v+` **Di quale epoca sono gli strumenti in pietra trovati al Podere Casella, presso Pieve a Maiano?**  
   ✔ Del Paleolitico medio e superiore · ✘ Dell'età del bronzo · Dell'età del ferro · Del Neolitico finale  
   _Il Repertorio del Piano segnala al Podere Casella strumenti del Paleolitico medio e superiore._ → `frazioni/pieve-a-maiano.html`
37. [414fd435] ●●○ `-v+` **Dove è stato individuato un insediamento romano del I-II secolo d.C. a Pieve a Maiano?**  
   ✔ Al campo sportivo · ✘ Sotto la chiesa · Nel cimitero · Lungo la ferrovia  
   _Il Repertorio segnala un insediamento romano al campo sportivo e una fornace a Vallimboi._ → `frazioni/pieve-a-maiano.html`
38. [e19b1b46] ●●● `Pv+` **In quale località di Pieve a Maiano c'era una fornace romana?**  
   ✔ Vallimboi · ✘ I Ponti · Le Fosse · Tribbio  
   _Vicino all'insediamento romano del campo sportivo c'era la fornace di Vallimboi; le fornaci de I Ponti sono a Pieve al Toppo._ → `frazioni/pieve-a-maiano.html`
39. [aae10fe5] ●●○ `-n+` **Quale ritrovamento attesta l'origine romana di Spoiano?**  
   ✔ Un tesoretto di monete romane · ✘ Un anfiteatro · Un mosaico pavimentale · Un tratto di acquedotto  
   _A Spoiano è stato trovato un tesoretto di monete romane._ → `frazioni/spoiano.html`
40. [3b033cf0] ●●● `Pv+` **A quale epoca risale l'urna etrusca con iscrizione trovata a Viciomaggio nel 1872?**  
   ✔ All'età ellenistica · ✘ All'età villanoviana · All'età del bronzo · All'età longobarda  
   _Nel 1872 a Viciomaggio fu trovata un'urna etrusca di età ellenistica con un'iscrizione._ → `frazioni/viciomaggio.html`
41. [1ab2c013] ●○○ `Pd=` **Di quale catena collinare è una propaggine la zona collinare del comune?**  
   ✔ I Preappennini toscani · ✘ Le Alpi Apuane · Il Monte Amiata · Le Colline Metallifere  
   _La parte collinare e di bassa montagna, coperta di boschi, è una propaggine dei Preappennini toscani._ → `index.html`
42. [2dab9df8] ●●○ `-v=` **Secondo il piano paesaggistico regionale, il monte di Civitella segna la separazione della Val di Chiana da quale valle?**  
   ✔ Il Valdarno · ✘ Il Casentino · La Val d'Orcia · La Valtiberina  
   _Il piano scrive che «il monte di Civitella Val di Chiana segna il punto di separazione col territorio del Valdarno»._ → `geografia.html`
43. [cb9f19ff] ●○○ `-d=` **Da che cosa deriva la pianura della Val di Chiana?**  
   ✔ Dal prosciugamento di un antico lago · ✘ Dal ritiro di un ghiacciaio · Da un'antica colata di lava · Dal ritiro del mare in età romana  
   _La pianura, a circa 250 metri di quota, deriva dal prosciugamento di un lago pleistocenico._ → `geografia.html`
44. [97b3e142] ●○○ `-d+` **Che cosa accadeva alle acque della Chiana presso il Toppo nell'XI secolo, secondo il Repetti?**  
   ✔ Si dividevano tra il Valdarno e il Tevere · ✘ Formavano una grande cascata · Scorrevano tutte verso il mare di Livorno · Erano già state bonificate dai Medici  
   _Secondo il Repetti, nell'XI secolo le acque della Chiana presso il Toppo «bilicavano» tra il Valdarno e il Tevere._ → `frazioni/pieve-al-toppo.html`
45. [cc3c0e44] ●●● `Nv=` **In quale anno di censimento il comune ha contato più abitanti?**  
   ✔ 2011, con 9.111 · ✘ 1951, con 8.147 · 2021, con 8.814 · 1936, con 8.126  
   _Al censimento del 2011 il comune contava 9.111 abitanti, il valore più alto della serie ISTAT dal 1861._ → `geografia.html`
46. [2a62011f] ●●○ `Nd=` **Quanti abitanti contava il comune al primo censimento dell'Italia unita, nel 1861?**  
   ✔ 5.777 · ✘ 2.777 · 8.814 · 12.500  
   _Nel 1861 il comune contava 5.777 abitanti; nel 2021 erano 8.814._ → `geografia.html`
47. [60dff0f2] ●○○ `-n=` **Come cambiò la popolazione del comune tra il censimento del 1951 e quello del 1961?**  
   ✔ Calò di quasi 1.500 abitanti · ✘ Crebbe di quasi 1.500 abitanti · Rimase quasi identica · Si dimezzò  
   _Si passò da 8.147 abitanti nel 1951 a 6.673 nel 1961._ → `geografia.html`

## Storia (62)

1. [db28ef0d] ●○○ `-d-` **Che cosa era il colle di Civitella in epoca longobarda?**  
   ✔ Una roccaforte a controllo del territorio · ✘ Un porto fluviale · Un monastero femminile · Una zecca  
   _Già frequentata in epoca etrusca e romana, Civitella divenne una roccaforte longobarda._ → `storia.html`
2. [3dd6026e] ●●○ `Pv=` **Quale vescovo di Arezzo scelse nel 1248 la rocca di Civitella come propria dimora?**  
   ✔ Guglielmino degli Ubertini · ✘ Guido Tarlati · Immone · Lorenzo de' Medici  
   _Nel 1248 Guglielmino degli Ubertini scelse la rocca come dimora e ne potenziò le mura._ → `storia.html`
3. [d6478a7e] ●○○ `-d+` **Che aspetto aveva la rocca di Civitella nel 1182, secondo il Repertorio del Piano?**  
   ✔ Quello di un palazzo-torrione · ✘ Quello di una villa rinascimentale · Quello di una fortezza a stella · Quello di una chiesa romanica  
   _Nel 1182 la rocca aveva già l'aspetto di un palazzo-torrione._ → `frazioni/civitella.html`
4. [2fd2d624] ●●● `Nv=` **In quale anno Firenze fece di Civitella il capoluogo di una propria podesteria?**  
   ✔ 1385 · ✘ 1248 · 1527 · 1774  
   _Nel 1385, acquisiti Arezzo e il suo contado, Firenze staccò Civitella dalla podesteria di Valdambra._ → `storia.html`
5. [edd96569] ●●○ `Pv=` **Da quale podesteria fu staccata Civitella nel 1385?**  
   ✔ Valdambra · ✘ Casentino · Valtiberina · Valdarno  
   _Civitella fu scorporata dalla podesteria di Valdambra e divenne capoluogo di una propria circoscrizione._ → `storia.html`
6. [b9e45476] ●●● `Nv=` **Fino a quale anno durò la podesteria di Civitella?**  
   ✔ 1838 · ✘ 1385 · 1774 · 1917  
   _La podesteria di Civitella, istituita da Firenze nel 1385, durò fino al 1838._ → `storia.html`
7. [77748394] ●●● `Nv=` **In quale anno le comunità di Ciggiano, Viciomaggio e Badia al Pino e il castello di Montarfoni furono aggregati alla Comunità di Civitella?**  
   ✔ 1774 · ✘ 1385 · 1838 · 1917  
   _L'aggregazione avvenne nel 1774._ → `storia.html`
8. [b929883a] ●●○ `Nv-` **In quale anno la sede comunale fu trasferita da Civitella a Badia al Pino?**  
   ✔ 1917 · ✘ 1861 · 1946 · 1774  
   _Nel 1917 la sede comunale fu trasferita a Badia al Pino._ → `storia.html`
9. [4ffa7202] ●○○ `-d=` **Perché nel 1917 la sede comunale fu trasferita a Badia al Pino?**  
   ✔ Per lo spopolamento delle zone collinari · ✘ Per un terremoto · Per un'alluvione · Per ordine del Granduca  
   _Con lo spopolamento delle zone collinari la sede passò a Badia al Pino; il comune mantenne il nome dell'antico borgo._ → `storia.html`
10. [32504015] ●●○ `Nv-` **In quale anno fu combattuta la battaglia di Pieve al Toppo?**  
   ✔ 1288 · ✘ 1260 · 1385 · 1530  
   _La battaglia fu combattuta il 26 giugno 1288._ → `frazioni/pieve-al-toppo.html`
11. [1e4dc6a7] ●●○ `-v=` **Chi vinse la battaglia di Pieve al Toppo del 1288?**  
   ✔ Gli aretini · ✘ I senesi · I fiorentini · I pisani  
   _Il 26 giugno 1288 gli aretini ghibellini sconfissero i senesi guelfi._ → `frazioni/pieve-al-toppo.html`
12. [571968bf] ●○○ `Pn-` **Quale poeta ricorda la battaglia di Pieve al Toppo come le «giostre del Toppo»?**  
   ✔ Dante Alighieri · ✘ Francesco Petrarca · Giovanni Boccaccio · Niccolò Machiavelli  
   _Dante la ricorda nel XIII canto dell'Inferno._ → `frazioni/pieve-al-toppo.html`
13. [1230b87b] ●●● `Nv+` **In quale canto dell'Inferno Dante ricorda le «giostre del Toppo»?**  
   ✔ Il XIII · ✘ Il V · Il XXVI · Il XXXIII  
   _Le «giostre del Toppo» compaiono nel XIII canto, tra gli scialacquatori._ → `frazioni/pieve-al-toppo.html`
14. [a95227b3] ●●● `Pv+` **Quale personaggio, caduto nella battaglia di Pieve al Toppo, compare nell'Inferno di Dante?**  
   ✔ Lano da Siena · ✘ Farinata degli Uberti · Pier della Vigna · Brunetto Latini  
   _Lano da Siena compare tra gli scialacquatori nel XIII canto._ → `frazioni/pieve-al-toppo.html`
15. [224669b9] ●○○ `-d-` **Che cosa distrusse la rocca di Civitella durante la seconda guerra mondiale?**  
   ✔ Un bombardamento alleato · ✘ Un terremoto · Un incendio appiccato dai partigiani · Un assalto dei carri armati tedeschi  
   _La rocca di Civitella fu distrutta da un bombardamento alleato durante la guerra._ → `frazioni/civitella.html`
16. [fb55e686] ●●● `Nv=` **In quale anno a Villa Oliveto fu istituito un campo di internamento?**  
   ✔ 1940 · ✘ 1915 · 1936 · 1944  
   _Il campo fu istituito nel giugno 1940._ → `frazioni/oliveto.html`
17. [b5f15efd] ●○○ `-n=` **Chi era internato soprattutto nel campo di Villa Oliveto?**  
   ✔ Famiglie ebree britanniche provenienti dalla Libia · ✘ Prigionieri di guerra americani · Soldati tedeschi · Profughi istriani  
   _Il campo ospitò soprattutto famiglie ebree di nazionalità britannica provenienti dalla Libia._ → `frazioni/oliveto.html`
18. [71ecaade] ●●○ `Pv=` **Dove furono deportate nel 1944 le famiglie internate a Villa Oliveto?**  
   ✔ A Bergen-Belsen · ✘ A Dachau · A Mauthausen · A Buchenwald  
   _Nel 1944 furono deportate a Bergen-Belsen._ → `frazioni/oliveto.html`
19. [bebf7d33] ●●○ `-v=` **Da quale espressione latina deriva il nome di Viciomaggio?**  
   ✔ Vicus maior · ✘ Via magna · Villa maior · Vicus Martis  
   _Vicus maior significa «villaggio maggiore»._ → `frazioni/viciomaggio.html`
20. [26c46d87] ●○○ `-n=` **Di quale origine è, quasi sicuramente, il toponimo «Toppo»?**  
   ✔ Longobarda · ✘ Etrusca · Araba · Francese  
   _Le fonti indicano «Toppo» come toponimo quasi sicuramente longobardo._ → `frazioni/pieve-al-toppo.html`
21. [d150c402] ●○○ `-n=` **Da che cosa deriva il nome «Maiano»?**  
   ✔ Dal nome di un proprietario romano, probabilmente un Marius · ✘ Dal mese di maggio · Da una famiglia medievale fiorentina · Da una divinità etrusca  
   _«Maiano» è un toponimo prediale romano, da Marius._ → `frazioni/pieve-a-maiano.html`
22. [bb0a87e4] ●○○ `-d=` **Da che cosa prende il nome Tribbio?**  
   ✔ Da un trivio, un incrocio di tre strade · ✘ Da una tribù etrusca · Da un tribunale medievale · Da un torrente  
   _Il nome viene dal trivium, l'incrocio di tre strade; il Repertorio lo cataloga come trivio, forse di età romana._ → `frazioni/borghi-minori.html#tribbio`
23. [410b1cb5] ●●○ `Nn=` **In quale anno il titolo di pieve e il fonte battesimale passarono dalla Pieve al Toppo a Badia al Pino?**  
   ✔ 1502 · ✘ 1288 · 1774 · 1917  
   _Nel 1502, distrutta la pieve del Toppo, il titolo di pieve passò alla chiesa di Badia al Pino._ → `frazioni/badia-al-pino.html`
24. [c87b3b73] ●●● `Nn+` **In quale anno fu soppressa la Badia del Pino?**  
   ✔ 1441 · ✘ 1288 · 1774 · 1917  
   _Dopo la soppressione della Badia, nel 1441, il paese divenne un insediamento essenzialmente rurale._ → `frazioni/badia-al-pino.html`
25. [7a384985] ●●○ `Nn=` **In quale anno furono distrutti la pieve e l'ospedale per i pellegrini di Pieve al Toppo?**  
   ✔ 1502 · ✘ 1288 · 1385 · 1944  
   _Chiesa e ospedale furono distrutti nel 1502; sul sito dell'antica pieve sorge oggi l'Oratorio della Madonna del Conforto._ → `frazioni/pieve-al-toppo.html`
26. [cb2abf6f] ●○○ `Pd=` **Sotto quali valichi si trova Ciggiano, che ne fecero un nodo strategico?**  
   ✔ Palazzuolo e San Pancrazio · ✘ La Futa e la Raticosa · L'Abetone e la Cisa · I Mandrioli e la Scheggia  
   _La posizione sotto i valichi di Palazzuolo e San Pancrazio fece di Ciggiano una tappa obbligata della dogana fiorentina._ → `frazioni/ciggiano.html`
27. [96a6f855] ●○○ `-n=` **Che cos'era la «calla» che i pastori facevano a Ciggiano?**  
   ✔ La conta degli animali, con il pagamento della gabella · ✘ Una festa per la fine della transumanza · Un mercato della lana · Una gara di tosatura  
   _Ciggiano era tappa obbligata della dogana fiorentina: qui i pastori facevano la «calla», la conta degli animali, pagando la gabella._ → `frazioni/ciggiano.html`
28. [523cea0b] ●●● `Pv+` **Le truppe di quale condottiero assediarono e saccheggiarono Ciggiano nel 1431?**  
   ✔ Niccolò Piccinino · ✘ Giovanni Acuto · Castruccio Castracani · Federico da Montefeltro  
   _Nel 1431 Ciggiano fu assediato e saccheggiato dalle truppe di Niccolò Piccinino; nel 1554 subì un altro assedio._ → `frazioni/ciggiano.html`
29. [01491e5c] ●●○ `Pv=` **Quale granduca soppresse nel 1783 la Compagnia di Santa Croce di Ciggiano?**  
   ✔ Pietro Leopoldo · ✘ Cosimo I de' Medici · Ferdinando III · Napoleone Bonaparte  
   _La Compagnia fu soppressa da Pietro Leopoldo nel 1783 e ripristinata nel 1794._ → `frazioni/ciggiano.html`
30. [f4c98a78] ●●● `Pv+` **Quali famiglie, tornate proprietarie del feudo, riedificarono nel Seicento la Casa del Podestà di Oliveto?**  
   ✔ Ubertini e Saracini · ✘ Medici e Pazzi · Guidi e Tarlati · Strozzi e Rucellai  
   _La Casa del Podestà fu riedificata nella prima metà del Seicento dalle famiglie aretine Ubertini e Saracini._ → `frazioni/oliveto.html`
31. [4fcbea87] ●○○ `-d+` **Che cosa diventò all'inizio dell'Ottocento la piazza d'armi del castello di Oliveto?**  
   ✔ Un vigneto e oliveto · ✘ Un mercato coperto · Un cimitero · Un giardino all'italiana  
   _Il palazzo del Podestà divenne casa colonica e granaio, e la piazza fu trasformata in vigneto e oliveto._ → `frazioni/oliveto.html`
32. [7a62a739] ●●● `Nv+` **In quale giorno fu combattuta la battaglia di Pieve al Toppo del 1288?**  
   ✔ Il 26 giugno · ✘ Il 29 giugno · Il 4 luglio · Il 15 agosto  
   _Il 26 giugno 1288 gli aretini ghibellini sconfissero i senesi guelfi._ → `storia.html`
33. [18947b6d] ●●○ `-v=` **Di quale parte erano i senesi sconfitti al Toppo nel 1288?**  
   ✔ Guelfa · ✘ Ghibellina · Imperiale · Dei Bianchi  
   _Gli aretini ghibellini sconfissero i senesi guelfi._ → `frazioni/pieve-al-toppo.html`
34. [4497e778] ●○○ `-d=` **In quali epoche fu frequentato il colle di Civitella, prima di diventare una roccaforte longobarda?**  
   ✔ In epoca etrusca e romana · ✘ Solo dall'età moderna · In epoca normanna · In epoca bizantina e araba  
   _Già frequentata in epoca etrusca e romana, Civitella divenne una roccaforte longobarda._ → `frazioni/civitella.html`
35. [4c4023b6] ●●○ `Pv=` **A presidio di chi sorgevano, dall'XI secolo, le strutture sul colle di Civitella?**  
   ✔ Dei vescovi-conti aretini · ✘ Dei Medici · Della Repubblica di Siena · Dei conti Guidi  
   _Dall'XI secolo sul colle sorgevano strutture a presidio dei vescovi-conti aretini._ → `storia.html`
36. [6869ff95] ●●○ `Pv-` **Quale città acquisì Arezzo e il suo contado prima di fare di Civitella, nel 1385, il capoluogo di una propria podesteria?**  
   ✔ Firenze · ✘ Siena · Perugia · Pisa  
   _Nel 1385 Firenze, acquisiti Arezzo e il suo contado, fece di Civitella il capoluogo di una sua podesteria._ → `storia.html`
37. [cf547452] ●●● `Pv+` **Quale castello fu aggregato alla Comunità di Civitella nel 1774, insieme a Ciggiano, Viciomaggio e Badia al Pino?**  
   ✔ Montarfoni · ✘ Gaenne · Dorna · Poggio Castellare  
   _Nel 1774 Ciggiano, Viciomaggio, Badia al Pino e il castello di Montarfoni furono aggregati alla Comunità di Civitella._ → `storia.html`
38. [6a7032b1] ●●● `Nv+` **In quale anno Ciggiano subì un altro assedio, dopo il saccheggio di Niccolò Piccinino del 1431?**  
   ✔ 1554 · ✘ 1385 · 1502 · 1774  
   _Nel 1431 Ciggiano fu saccheggiato dalle truppe di Piccinino e nel 1554 subì un altro assedio._ → `frazioni/ciggiano.html`
39. [5ff357cf] ●●● `Pv+` **Quale altro titolo, oltre a quello di pieve, passò a Badia al Pino nel 1583?**  
   ✔ Quello di Santa Lucia a Campigliano · ✘ Quello di sede vescovile · Quello di abbazia di Vallombrosa · Quello di priorato di Camaldoli  
   _Nel 1502 arrivarono il fonte battesimale e il titolo di pieve, nel 1583 il titolo di Santa Lucia a Campigliano._ → `frazioni/badia-al-pino.html`
40. [d1c40d05] ●●● `Nv+` **In quale anno un documento chiama l'abbazia «Badia di S. Martino e S. Lorenzo al Pino»?**  
   ✔ 1046 · ✘ 1039 · 1441 · 1502  
   _Un documento del 1046 chiama l'abbazia «Badia di S. Martino e S. Lorenzo al Pino»; il 1039 si riferisce alla chiesa._ → `frazioni/badia-al-pino.html`
41. [572b6b97] ●○○ `-n=` **Che cosa c'era accanto all'antica pieve del Toppo?**  
   ✔ Un ospedale per i pellegrini · ✘ Un castello · Un mercato coperto · Un mulino  
   _La pieve aveva accanto un ospedale per i pellegrini; chiesa e ospedale furono distrutti nel 1502._ → `frazioni/pieve-al-toppo.html`
42. [7d7a33f9] ●●● `Pv+` **A chi apparteneva anticamente la pieve del Toppo, con il suo ospedale per i pellegrini?**  
   ✔ Al Capitolo di Arezzo · ✘ All'abbazia di Agnano · Al vescovo di Siena · Ai conti Guidi  
   _Il Repertorio la ricorda tra i possedimenti del Capitolo di Arezzo._ → `frazioni/pieve-al-toppo.html`
43. [3fa9492f] ●●● `Nv+` **In quale mese del 1940 fu istituito il campo di internamento di Villa Oliveto?**  
   ✔ Giugno · ✘ Gennaio · Settembre · Dicembre  
   _Il campo fu istituito nel giugno 1940._ → `frazioni/oliveto.html`
44. [748416c9] ●●○ `-v=` **Da chi fu assediata la rocca di Civitella tra il 1284 e il 1285?**  
   ✔ Dagli aretini · ✘ Dai fiorentini · Dai senesi · Dai pisani  
   _Tra il 1284 e il 1285 la rocca fu assediata dagli stessi aretini che nel 1288 vinsero la battaglia del Toppo._ → `storia.html`
45. [4fe3b32c] ●●● `Nv+` **Quanti piccoli comuni furono aggregati alla Comunità di Civitella nel 1774, secondo il Repertorio del Piano Strutturale?**  
   ✔ Nove · ✘ Tre · Quindici · Venti  
   _Il Repertorio parla di nove piccoli comuni aggregati nel 1774; tra questi gli itinerari del Comune ricordano Ciggiano, Viciomaggio e Badia al Pino._ → `storia.html`
46. [3ff855bb] ●●● `Pv+` **Da quale vicariato dipendeva Civitella sotto i granduchi di Toscana?**  
   ✔ Da quello di Monte San Savino · ✘ Da quello di Arezzo · Da quello di Cortona · Da quello di Montevarchi  
   _Monte San Savino fu capoluogo di vicariato sotto i granduchi, con autorità su Civitella, Lucignano e Foiano della Chiana._ → `storia.html`
47. [37978868] ●●● `Pv+` **Quale podestà di Arezzo assediò e rase al suolo Civitella nel 1252, secondo la Pro Loco?**  
   ✔ Ildebrando Cacciaconti · ✘ Guido Tarlati · Buonconte da Montefeltro · Niccolò Piccinino  
   _Nel 1252 Civitella capitolò e fu rasa al suolo; il vescovo Guglielmino la fece poi ricostruire con una doppia cerchia di mura._ → `storia.html`
48. [fd4ef637] ●○○ `-d=` **Quale di questi comuni fu soppresso e unito a Civitella nel 1774?**  
   ✔ Ciggiano · ✘ Monte San Savino · Lucignano · Bucine  
   _Il 14 novembre 1774 alla Comunità di Civitella furono assegnati nove comuni: Civitella, Oliveto, Viciomaggio con Tuori, Tegoleto, Badia al Pino, Ciggiano, Cornia, Montarfoni e Montoto (Repetti)._ → `storia.html`
49. [274cd667] ●○○ `-d=` **Con quale nome fu ribattezzata Civitella quando, nell'XI secolo, passò al vescovo di Arezzo?**  
   ✔ «Civitella del Vescovo» · ✘ «Civitella dei Medici» · «Civitella del Papa» · «Civitella dei Conti»  
   _Passata al vescovo di Arezzo, fu detta «Civitella del Vescovo»; la Pro Loco ricorda anche il nome «Civitella di Valdambra»._ → `storia.html`
50. [8885f433] ●●● `Nn+` **In quale anno fu firmata a Civitella la «Pace di Civitella», secondo la Pro Loco?**  
   ✔ 1311 · ✘ 1252 · 1385 · 1554  
   _La Pro Loco data al 26 marzo 1311 la pace tra il vescovo Ildebrandino Guidi di Romena e l'imperatore Enrico VII (Arrigo VII)._ → `storia.html`
51. [ccfe4a64] ●●● `Nv+` **In quale giorno del 1774 fu emanato il provvedimento che assegnò nove comuni alla Comunità di Civitella?**  
   ✔ Il 14 novembre · ✘ Il 29 giugno · Il 1° gennaio · Il 25 marzo  
   _Con un provvedimento del 14 novembre 1774 alla Comunità di Civitella furono assegnati nove comuni preesistenti (Repetti)._ → `storia.html`
52. [42c23bec] ●●● `Pv+` **Secondo il Repetti, quale comune con il riordino del 1774 passò alla Comunità di Monte San Savino?**  
   ✔ Montagnano · ✘ Montarfoni · Montoto · Ciggiano  
   _Secondo il Repetti, con il provvedimento del 1774 il comune di Montagnano passò alla Comunità di Monte San Savino._ → `storia.html`
53. [41b02c31] ●●○ `Pv=` **Chi difese Civitella nel 1554 dall'assalto delle truppe senesi di Piero Strozzi?**  
   ✔ Paolo da Castello · ✘ Giovanni dalle Bande Nere · Niccolò Piccinino · Buonconte da Montefeltro  
   _Paolo da Castello, capitano al servizio di Cosimo I de' Medici, difese Civitella e la fortificò con nuove mura._ → `storia.html`
54. [7f8563ab] ●●● `Nv+` **Quanti abitanti contava la Comunità di Civitella nel 1833, secondo il Repetti?**  
   ✔ 4.883 · ✘ 1.883 · 8.814 · 14.883  
   _Nel 1833 la Comunità contava 4.883 abitanti; al censimento del 2021 il comune ne contava 8.814._ → `storia.html`
55. [84b5459a] ●●○ `-v+` **A chi consegnò Azzone degli Ubertini il castello di Oliveto nel settembre 1385?**  
   ✔ Alla Repubblica di Firenze · ✘ Alla Repubblica di Siena · Al vescovo di Arezzo · Ai Visconti di Milano  
   _Ricevuto in accomandigia da Firenze nel giugno 1385, l'8 settembre Azzone consegnò il castello, che i fiorentini fortificarono di torri._ → `frazioni/oliveto.html`
56. [094fa249] ●●○ `-n+` **Che cosa ordinò Firenze nel 1433 per i castelli di Oliveto e Ciggiano, presi nel 1431 da Niccolò Piccinino?**  
   ✔ Di smantellarli · ✘ Di ricostruirli più grandi · Di venderli ai senesi · Di affidarli al vescovo di Arezzo  
   _Secondo il Repetti, nel 1431 Piccinino prese Ciggiano e Oliveto; nel 1433 Firenze ordinò di smantellare quei castelli._ → `frazioni/oliveto.html`
57. [a4286437] ●●● `Nv+` **In quale data il popolo di Tegoleto si sottomise alla Repubblica fiorentina?**  
   ✔ Il 29 marzo 1385 · ✘ Il 26 giugno 1288 · Il 14 novembre 1774 · Il 2 agosto 1554  
   _Secondo il Repetti il popolo di Tegoleto si sottomise a Firenze il 29 marzo 1385._ → `frazioni/tegoleto.html`
58. [418b0da7] ●●○ `-v+` **Chi si accampò a Ciggiano nel 1307, secondo il Repetti?**  
   ✔ Un esercito della lega guelfa toscana · ✘ Le truppe di Niccolò Piccinino · L'esercito imperiale di Arrigo VII · I ghibellini di Arezzo  
   _Secondo il Repetti, nel 1307 a Ciggiano si accampò un esercito della lega guelfa toscana._ → `frazioni/ciggiano.html`
59. [a4e2efc3] ●●○ `-v+` **Che cosa fu firmato il 20 aprile 1261 nella chiesa della Badia al Pino?**  
   ✔ La concordia tra il vescovo Guglielmino e i cortonesi fuorusciti · ✘ La pace tra Arezzo e Siena · Lo statuto del comune di Civitella · La resa di Civitella ai fiorentini  
   _Secondo il Repetti, nella chiesa della Badia furono firmati i capitoli di concordia tra Guglielmino degli Ubertini e i cortonesi fuorusciti._ → `frazioni/badia-al-pino.html`
60. [ede3b0e0] ●●○ `Nn=` **In quale anno fu inaugurata la ferrovia Arezzo–Sinalunga, che ha una stazione a Badia al Pino?**  
   ✔ 1930 · ✘ 1866 · 1911 · 1948  
   _La linea fu inaugurata il 3 settembre 1930; nel comune si ferma alle stazioni di Civitella-Badia al Pino e di Albergo._ → `storia.html`
61. [4b7efa1f] ●○○ `-d+` **Con quale trazione funzionarono i treni della Arezzo–Sinalunga fin dall'apertura?**  
   ✔ Elettrica · ✘ A vapore · Diesel · A cavalli  
   _Il progetto prevedeva il vapore, ma su iniziativa dell'ingegnere Giacomo Sutter la linea fu elettrificata prima dell'apertura del 1930._ → `storia.html`
62. [bfaeeba1] ●●○ `-n+` **Che funzione aveva nel Medioevo il castello di Tuori, secondo il Repertorio del Piano Strutturale?**  
   ✔ Era sede di guarnigioni a presidio di Arezzo · ✘ Era la residenza estiva dei Medici · Era un convento fortificato · Era una dogana senese  
   _Secondo il Repertorio, Tuori, ricordato dal 1021, divenne un castello sede di guarnigioni militari a presidio della città di Arezzo; ne resta il cassero._ → `frazioni/tuori.html`

## Il 1944 (34)

1. [3e37b695] ●●○ `Nv-` **In quale data avvenne la strage nazista di Civitella?**  
   ✔ 29 giugno 1944 · ✘ 25 aprile 1945 · 8 settembre 1943 · 4 giugno 1944  
   _La strage avvenne il 29 giugno 1944._ → `storia.html`
2. [75f82986] ●●○ `Pv=` **Quale festa si celebrava a Civitella il giorno della strage del 1944?**  
   ✔ Quella dei santi Pietro e Paolo · ✘ Quella di San Giovanni · L'Assunta · Ognissanti  
   _Il paese era affollato per la festa dei patroni Pietro e Paolo._ → `storia.html`
3. [3440c37a] ●●○ `-v=` **Quale di queste località NON fu colpita dalla strage del 29 giugno 1944?**  
   ✔ Tegoleto · ✘ Cornia · Gebbia · San Pancrazio  
   _La strage colpì Civitella, Cornia, Gebbia e San Pancrazio di Bucine._ → `storia.html`
4. [e98abd07] ●●○ `Pv=` **Quale reparto tedesco compì le stragi del 29 giugno 1944?**  
   ✔ La divisione corazzata «Hermann Göring» · ✘ La divisione «Das Reich» · La divisione «Totenkopf» · L'Afrikakorps  
   _Le fonti indicano reparti della divisione «Hermann Göring»._ → `frazioni/cornia.html`
5. [ae2d129c] ●●○ `-v=` **Di quale comune fa parte San Pancrazio, colpito dalla strage del 1944?**  
   ✔ Bucine · ✘ Civitella in Val di Chiana · Arezzo · Monte San Savino  
   _San Pancrazio è una frazione di Bucine._ → `storia.html`
6. [d650b33d] ●●○ `-v=` **Dove arriva la Marcia per la pace che parte da Civitella?**  
   ✔ A San Pancrazio · ✘ Ad Arezzo · A Cortona · A Monte San Savino  
   _La Marcia per la pace va da Civitella a San Pancrazio._ → `frazioni/civitella.html`
7. [76c00bc0] ●●○ `-v=` **Con quale comune è organizzata la Marcia per la pace?**  
   ✔ Bucine · ✘ Arezzo · Firenze · Siena  
   _La marcia è realizzata in collaborazione con il comune di Bucine._ → `frazioni/civitella.html`
8. [ab4e24ee] ●○○ `Pd=` **Quale associazione ha allestito la Sala della Memoria a Civitella?**  
   ✔ Civitella Ricorda · ✘ La Pro Loco di Civitella · Slow Food Valdichiana · Comunità & Tegoleto  
   _La Sala della Memoria è stata allestita dall'associazione «Civitella Ricorda» in via Martiri di Civitella._ → `frazioni/civitella.html`
9. [7461cfc3] ●○○ `Pd=` **Come si chiama il monumento sul muro accanto alla chiesa di Civitella?**  
   ✔ Pietà del giugno 1944 · ✘ Vittoria alata · Il Milite Ignoto · Madonna della Pace  
   _Il monumento «Pietà del giugno 1944» ricorda l'eccidio._ → `frazioni/civitella.html`
10. [471dce11] ●●● `Nv=` **In quale anno fu realizzato il portale in bronzo di Bino Bini per la chiesa di Civitella?**  
   ✔ 1994 · ✘ 1954 · 1974 · 2014  
   _Il portale, del 1994, ricorda l'eccidio nel cinquantesimo anniversario._ → `frazioni/civitella.html`
11. [b6c6fc75] ●●● `Nv+` **In quale data le SS fucilarono a Ciggiano i partigiani Marmo e Marapitti?**  
   ✔ 16 aprile 1944 · ✘ 29 giugno 1944 · 25 aprile 1945 · 8 settembre 1943  
   _Giovanni Marmo e Mario Marapitti furono fucilati il 16 aprile 1944._ → `frazioni/ciggiano.html`
12. [9b2fcfcf] ●●● `Nv+` **In quale anno fu eretto il cippo dell'eccidio di Cornia?**  
   ✔ 1969 · ✘ 1945 · 1994 · 2004  
   _Il cippo fu eretto nel 1969, nel venticinquesimo anniversario._ → `frazioni/cornia.html`
13. [9677ff56] ●●● `Nn+` **Quanti nomi riporta la lastra dei martiri di Cornia?**  
   ✔ 58 · ✘ 8 · 115 · 300  
   _La lastra riporta 58 caduti di Cornia e delle località vicine._ → `frazioni/cornia.html`
14. [24c8d8bd] ●●○ `-n+` **Chi era Giovanni Cau, catturato a Gebbia nel 1944?**  
   ✔ Un insegnante di scienze naturali e autore di testi scolastici · ✘ Il parroco del paese · Un comandante partigiano · Il podestà di Civitella  
   _Nato a Cagliari, insegnava scienze naturali a Firenze e scriveva testi scolastici; fu ucciso con la moglie Helga Elmqvist il 2 luglio 1944._ → `frazioni/gebbia.html`
15. [dad49b73] ●○○ `-d=` **Che cosa raccoglie la Sala della Memoria allestita a Civitella dall'associazione «Civitella Ricorda»?**  
   ✔ Reperti delle vittime, fotografie e testimonianze sull'eccidio · ✘ Opere d'arte rinascimentali · Attrezzi della civiltà contadina · Reperti etruschi  
   _Ci sono i reperti rinvenuti sulle vittime, fotografie del paese prima e dopo la distruzione, testimonianze, libri e residuati bellici._ → `frazioni/civitella.html`
16. [4dc5acd4] ●●● `Pv+` **Quale reparto operò a Gebbia il 29 giugno 1944, insieme alla divisione «Hermann Göring»?**  
   ✔ La Feldgendarmerie del capitano Heinz Barz · ✘ La Guardia Nazionale Repubblicana · Un reparto di alpini · Le SS di stanza a Firenze  
   _Reparti della «Hermann Göring», con la Feldgendarmerie del capitano Heinz Barz, applicarono a Gebbia lo stesso metodo usato a Civitella e a Cornia._ → `frazioni/gebbia.html`
17. [5c286059] ●●○ `-n+` **Secondo l'Archivio della Memoria, che cosa uccisero i tedeschi a Gebbia, oltre agli uomini?**  
   ✔ Tutti gli animali · ✘ Nessun altro essere vivente · I cavalli della fattoria · Solo i cani da guardia  
   _Donne e bambini non furono toccati né le case bruciate, ma i tedeschi uccisero tutti gli animali._ → `frazioni/gebbia.html`
18. [7ec5aac3] ●●○ `-v+` **Dove furono fucilati gli uomini presi a Gebbia, secondo l'Archivio della Memoria?**  
   ✔ Presso il Podere Valle, vicino a San Pancrazio · ✘ Nella piazza di Civitella · Nel cimitero di Cornia · Alla stazione di Albergo  
   _Furono fucilati presso il Podere Valle, vicino a San Pancrazio._ → `frazioni/gebbia.html`
19. [15cc1db8] ●●● `Nv+` **In quale giorno furono uccisi Giovanni Cau e la moglie Helga Elmqvist, catturati a Gebbia?**  
   ✔ Il 2 luglio 1944 · ✘ Il 29 giugno 1944 · Il 16 aprile 1944 · L'8 settembre 1943  
   _Furono catturati a Gebbia e uccisi il 2 luglio 1944._ → `frazioni/gebbia.html`
20. [320d4828] ●●● `Nv+` **Fino a quale giorno arrivano le morti ricordate dalla lastra dei martiri di Cornia?**  
   ✔ Il 16 luglio 1944 · ✘ Il 29 giugno 1944 · Il 25 aprile 1945 · Il 2 luglio 1944  
   _La lastra riporta 58 nomi di caduti uccisi fra il 29 giugno e il 16 luglio 1944._ → `frazioni/cornia.html`
21. [e6acc20f] ●●● `Pv+` **Chi fucilò a Ciggiano, il 16 aprile 1944, i partigiani Giovanni Marmo e Mario Marapitti?**  
   ✔ Le SS · ✘ La divisione «Hermann Göring» · I carabinieri · La Feldgendarmerie di Heinz Barz  
   _Secondo ToscanaNovecento furono fucilati dalle SS._ → `frazioni/ciggiano.html`
22. [5b3d98f6] ●●○ `Pv=` **Quale luogo della memoria si trova a Civitella, oltre alla «Pietà del giugno 1944» e alla Sala della Memoria?**  
   ✔ La Cappella dei Martiri · ✘ Il Sacrario militare · Il Museo della Resistenza · La Torre della Memoria  
   _A Civitella ci sono la Cappella dei Martiri e il monumento «Pietà del giugno 1944»._ → `frazioni/civitella.html`
23. [d69a35d2] ●●○ `-v+` **Dove si rifugiavano durante la guerra gli abitanti di Viciomaggio?**  
   ✔ In un cunicolo con una stanza sotterranea lungo il Fosso del Riolo · ✘ Nelle cantine della villa · In una galleria ferroviaria · Nel campanile della chiesa  
   _Il rifugio era un cunicolo con una stanza sotterranea lungo il Fosso del Riolo, verso Malpertuso._ → `frazioni/viciomaggio.html`
24. [be3e83c9] ●●○ `-n+` **Chi era Ismail Harbi, tra le vittime elencate dall'Atlante per «Cornia e dintorni»?**  
   ✔ Un partigiano di 28 anni · ✘ Il parroco di Cornia · Un soldato tedesco · Il maestro del paese  
   _L'Atlante delle stragi elenca tra le vittime il partigiano Ismail Harbi, di 28 anni; sulla lapide dei decorati è scritto «Hasbi Ismaili»._ → `frazioni/cornia.html`
25. [cdce2f79] ●○○ `-d=` **Che cosa ricorda il portale in bronzo di Bino Bini nella chiesa di Civitella?**  
   ✔ L'eccidio del 1944, nel cinquantesimo anniversario · ✘ La battaglia del Toppo · La fondazione del priorato · La visita di un papa  
   _Il portale del 1994 ricorda l'eccidio nel cinquantesimo anniversario._ → `frazioni/civitella.html`
26. [67e04d32] ●○○ `-n=` **Perché la rocca di Civitella fu bombardata dagli Alleati?**  
   ✔ Perché al suo interno si era installato il comando tedesco · ✘ Per errore, scambiandola per un ponte · Perché era un deposito di munizioni italiano · Per colpire la ferrovia vicina  
   _La rocca fu distrutta da un bombardamento alleato perché vi si era installato il comando tedesco._ → `storia.html`
27. [d46d4a3e] ●●○ `-n+` **Come morì Mario Mannelli, ricordato da un monumento a Viciomaggio?**  
   ✔ Fu ucciso dai fascisti nel 1944 · ✘ Cadde nella battaglia del Toppo · Morì nel bombardamento della rocca · Fu ucciso nella Grande Guerra  
   _Mario Mannelli fu ucciso dai fascisti nel 1944; sulla data esatta le fonti non concordano._ → `frazioni/viciomaggio.html`
28. [34e88f74] ●○○ `-n=` **Chi era don Alcide Lazzeri, ucciso il 29 giugno 1944?**  
   ✔ Il parroco di Civitella · ✘ Il podestà di Civitella · Il maestro elementare · Il medico condotto  
   _Tra le vittime c'erano il parroco, don Alcide Lazzeri, e il podestà, Guido Mammoli._ → `storia.html`
29. [68125a92] ●●○ `-v+` **Quale incarico aveva Guido Mammoli, ucciso nell'eccidio del 29 giugno 1944?**  
   ✔ Podestà di Civitella · ✘ Parroco di Civitella · Maresciallo dei carabinieri · Capo della formazione partigiana  
   _Tra le vittime c'erano il parroco, don Alcide Lazzeri, e il podestà, Guido Mammoli._ → `storia.html`
30. [0b47361b] ●●○ `-v=` **Quale onorificenza ricevette nel 1963 la comunità di Civitella?**  
   ✔ La Medaglia d'Oro al Valor Civile · ✘ La Medaglia d'Oro al Valor Militare · La Croce di guerra · Il titolo di Città della Pace  
   _Nel 1963 la comunità ricevette la Medaglia d'Oro al Valor Civile, conferita anche alla memoria di don Alcide Lazzeri._ → `storia.html`
31. [f1973bd5] ●○○ `-d=` **A chi è intitolata la piazza centrale di Civitella?**  
   ✔ A don Alcide Lazzeri, il parroco ucciso nel 1944 · ✘ A Dante Alighieri · Al notaio Becattini · Ai santi Pietro e Paolo  
   _La piazza centrale è intitolata al parroco don Alcide Lazzeri; lì si trova anche la «Porta della Pace»._ → `frazioni/civitella.html`
32. [53ade602] ●●● `Pv+` **Come si chiamava la formazione partigiana che il 18 giugno 1944 tese un agguato ai soldati tedeschi nel dopolavoro di Civitella?**  
   ✔ «Renzino» · ✘ «Stella Rossa» · «Lupo» · «Monte Rosa»  
   _La formazione «Renzino» era guidata da Edoardo Succhielli; secondo l'Atlante, questa e altre azioni diedero ai tedeschi il pretesto per la rappresaglia._ → `storia.html`
33. [6060fc7e] ●●● `Pv+` **Verso quale località furono spinte le donne e i bambini di Civitella il 29 giugno 1944?**  
   ✔ Verso Poggiali · ✘ Verso Cornia · Verso Badia al Pino · Verso Arezzo  
   _Le donne e i bambini furono spinti fuori dal paese, verso Poggiali; gli uomini furono uccisi a gruppi di cinque._ → `storia.html`
34. [c840099b] ●●● `Pv+` **Quale tribunale condannò all'ergastolo, nel 2006, il sergente tedesco Max Josef Milde per l'eccidio di Civitella?**  
   ✔ Il Tribunale militare di La Spezia · ✘ Il tribunale di Norimberga · La Corte d'Assise di Arezzo · Il Tribunale di Firenze  
   _Nel 2006 il Tribunale militare di La Spezia condannò Milde e riconobbe responsabile anche la Repubblica Federale di Germania._ → `storia.html`

## Frazioni (104)

1. [a6b8c90b] ●○○ `-v-` **In quale frazione ha sede il Comune?**  
   ✔ Badia al Pino · ✘ Civitella · Tegoleto · Pieve al Toppo  
   _Dal 1917 la sede comunale è a Badia al Pino._ → `frazioni/badia-al-pino.html`
2. [3f92e789] ●●○ `Pv=` **A quali santi era dedicata l'antica abbazia del Pino?**  
   ✔ Martino e Lorenzo · ✘ Pietro e Paolo · Biagio e Rocco · Giorgio e Luca  
   _Un documento del 1046 la chiama «Badia di S. Martino e S. Lorenzo al Pino»._ → `frazioni/badia-al-pino.html`
3. [0542f44e] ●●○ `Pv=` **Qual è il titolo della parrocchia di Badia al Pino?**  
   ✔ San Bartolomeo · ✘ San Biagio · San Michele Arcangelo · Sant'Andrea  
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
8. [080e4e41] ●●● `Nn+` **In quale anno è già attestato Tuori, secondo il Repertorio?**  
   ✔ 1021 · ✘ 1385 · 1774 · 1917  
   _Il Repertorio attesta Tuori già nel 1021._ → `frazioni/tuori.html`
9. [c686859b] ●●● `Nn+` **In quale anno fu progettata la moderna chiesa parrocchiale di Pieve al Toppo?**  
   ✔ 1967 · ✘ 1288 · 1806 · 2005  
   _La chiesa di San Giovanni Battista fu progettata nel 1967; il porticato è del 1977._ → `frazioni/pieve-al-toppo.html`
10. [c2c65bab] ●●● `Nn+` **In quale anno la chiesa di San Biagio a Ciggiano fu elevata a pieve?**  
   ✔ 1465 · ✘ 1048 · 1774 · 1917  
   _San Biagio di Ciggiano fu elevata a pieve nel 1465._ → `frazioni/ciggiano.html`
11. [b555e58c] ●●○ `Pv=` **A quale scultore è attribuita la Santa Maria Maddalena della chiesa di San Biagio a Ciggiano?**  
   ✔ Andrea Sansovino · ✘ Michelangelo · Donatello · Giambologna  
   _Nella chiesa di San Biagio a Ciggiano c'è una Santa Maria Maddalena attribuita ad Andrea Sansovino._ → `frazioni/ciggiano.html`
12. [d971761e] ●●○ `-v=` **In quale frazione si trova la chiesa della Madonna della Costarella, terminata nel 1635 con le elemosine dei pastori della via vecchia senese?**  
   ✔ Ciggiano · ✘ Albergo · Spoiano · Tuori  
   _Sorge fuori dal castello di Ciggiano e fu terminata nel 1635; il loggiato è settecentesco._ → `frazioni/ciggiano.html`
13. [8d375aa0] ●●○ `-v+` **Quale borgo collinare si trova a circa 360 metri, su un colle tra le valli del Gargaiolo e dell'Esse?**  
   ✔ Ciggiano · ✘ Tegoleto · Albergo · Badia al Pino  
   _Il Repertorio colloca Ciggiano su un colle di circa 360 m tra il Gargaiolo e l'Esse; la scheda del Comune indica 359 m._ → `frazioni/ciggiano.html`
14. [264f4207] ●○○ `-n=` **Quale attività artigianale esisteva un tempo a Cornia?**  
   ✔ La lavorazione delle scope di saggina · ✘ La produzione di cappelli di paglia · La soffiatura del vetro · La lavorazione del corallo  
   _A Cornia esisteva un centro per la lavorazione delle scope di saggina._ → `frazioni/cornia.html`
15. [7460edf6] ●●○ `Pn=` **A quale santo è dedicata la chiesa di Cornia, detta di Sant'Angelo?**  
   ✔ San Michele Arcangelo · ✘ San Rocco · San Giorgio · San Francesco  
   _La chiesa di Cornia è San Michele Arcangelo, detta Sant'Angelo._ → `frazioni/cornia.html`
16. [c1b2389e] ●●○ `-v+` **Quale frazione è la più alta tra queste, a circa 560 metri?**  
   ✔ Cornia · ✘ Tegoleto · Badia al Pino · Albergo  
   _Cornia si trova a circa 560 metri._ → `frazioni/cornia.html`
17. [d02d06cf] ●●○ `Pv=` **Di quale famiglia fu dimora Villa Oliveto, già Villa Mazzi?**  
   ✔ I conti Barbolani di Montauto · ✘ I Medici · I Guidi · I Ricasoli  
   _Villa Oliveto fu dimora dei conti Barbolani di Montauto._ → `frazioni/oliveto.html`
18. [782eea04] ●○○ `Pd-` **Quale scrittrice scozzese visse a Oliveto ed è sepolta nel suo cimitero?**  
   ✔ Muriel Spark · ✘ Agatha Christie · Virginia Woolf · Jane Austen  
   _Muriel Spark visse a Oliveto con Penelope Jardine; morta nel 2006, è sepolta nel cimitero di Sant'Andrea Apostolo._ → `frazioni/oliveto.html`
19. [f98ae568] ●○○ `Pd-` **Quale romanzo ha scritto Muriel Spark, che visse a Oliveto?**  
   ✔ Gli anni fulgenti di Miss Brodie · ✘ Gita al faro · Orgoglio e pregiudizio · Assassinio sull'Orient Express  
   _Muriel Spark è l'autrice de «Gli anni fulgenti di Miss Brodie»._ → `frazioni/oliveto.html`
20. [ae843126] ●●○ `Nn=` **In quale anno Muriel Spark ricevette la cittadinanza onoraria di Civitella?**  
   ✔ 2005 · ✘ 1975 · 1990 · 2015  
   _La cittadinanza onoraria le fu conferita nel settembre 2005._ → `frazioni/oliveto.html`
21. [4570545d] ●●● `Nn+` **Da quale anno si tiene il Presepe Vivente di Oliveto?**  
   ✔ 2014 · ✘ 1950 · 1985 · 2022  
   _Il Presepe Vivente di Oliveto si tiene dal 2014._ → `frazioni/oliveto.html`
22. [605f6a96] ●○○ `-d=` **Dove è allestita la Natività del Presepe Vivente di Oliveto?**  
   ✔ Nella chiesetta di San Rocco · ✘ Nella Rocca di Civitella · Nel Teatro Moderno · Nella stazione di Albergo  
   _Il Presepe Vivente, con oltre 80 figuranti, si conclude con la Natività nella chiesetta di San Rocco._ → `frazioni/oliveto.html`
23. [8c3a7f97] ●○○ `-d=` **Che cosa è stato trovato al Podere Casella, presso Pieve a Maiano?**  
   ✔ Strumenti in pietra del Paleolitico · ✘ Un tesoro di monete medievali · Una nave romana · Un mosaico bizantino  
   _Al Podere Casella sono stati trovati strumenti in pietra del Paleolitico._ → `frazioni/pieve-a-maiano.html`
24. [f229085c] ●●● `Pv+` **Di quale imperatore è la moneta d'oro trovata a Pieve a Maiano?**  
   ✔ Claudio · ✘ Nerone · Augusto · Traiano  
   _È un aureus dell'imperatore Claudio (41–54 d.C.)._ → `frazioni/pieve-a-maiano.html`
25. [9ed31f21] ●●○ `-v=` **Vicino a quale frazione si trova il podere Spedaluccio?**  
   ✔ Pieve a Maiano · ✘ Albergo · Tegoleto · Ciggiano  
   _Lo Spedaluccio è nei pressi di Pieve a Maiano; in passato era stato attribuito per errore ad Albergo._ → `frazioni/pieve-a-maiano.html`
26. [91b7689b] ●○○ `-d=` **Che cosa si produceva nelle fornaci romane di località I Ponti, a Pieve al Toppo?**  
   ✔ Terra sigillata aretina · ✘ Vetro soffiato · Porcellana · Mattoni rinascimentali  
   _Le fornaci producevano la terra sigillata aretina, la ceramica rossa da mensa della prima età imperiale._ → `frazioni/pieve-al-toppo.html`
27. [ac4c5d0d] ●●○ `Nn=` **Da quale anno Ponticino ha una stazione ferroviaria?**  
   ✔ 1866 · ✘ 1830 · 1910 · 1955  
   _La stazione di Ponticino è attiva dal 1866._ → `frazioni/ponticino.html`
28. [21a4f930] ●○○ `-n=` **Su quale linea ferroviaria si trova la stazione di Ponticino?**  
   ✔ Firenze–Roma · ✘ Arezzo–Sinalunga · Siena–Chiusi · Pisa–Firenze  
   _Ponticino è servito dalla ferrovia Firenze–Roma._ → `frazioni/ponticino.html`
29. [1938aa25] ●●● `Nn+` **In quale anno un referendum approvò la fusione tra Laterina e Pergine Valdarno, che riguarda anche Ponticino?**  
   ✔ 2017 · ✘ 1999 · 2009 · 2023  
   _Il referendum del 29–30 ottobre 2017 approvò la fusione con il 53,73% dei voti._ → `frazioni/ponticino.html`
30. [b126f10e] ●●○ `-v=` **Con quali comuni Civitella si divideva Ponticino prima del 2018?**  
   ✔ Laterina e Pergine Valdarno · ✘ Bucine e Arezzo · Monte San Savino e Arezzo · Bucine e Montevarchi  
   _Fino al 2017 Ponticino era diviso tra Civitella, Laterina e Pergine Valdarno._ → `frazioni/ponticino.html`
31. [86a6174e] ●●○ `Pv=` **Quale villa settecentesca si trova a Spoiano?**  
   ✔ Villa Pecchioli · ✘ Villa di Viciomaggio · Villa Oliveto · Villa del Bosco  
   _Villa Pecchioli, a Spoiano, divenne asilo infantile nel 1928 e fu restaurata nel 1981._ → `frazioni/spoiano.html`
32. [d00da1ec] ●●○ `-n+` **Che cosa divenne Villa Pecchioli, a Spoiano, nel 1928?**  
   ✔ Un asilo infantile · ✘ Un ospedale · Una caserma · Una scuola di musica  
   _Nel 1928 Villa Pecchioli divenne asilo; fu restaurata nel 1981._ → `frazioni/spoiano.html`
33. [bd1eb40f] ●●○ `-v+` **Quale paese è al centro del libro «Un uomo dabbene per davvero» di Giuseppe Renzetti?**  
   ✔ Spoiano · ✘ Tuori · Gebbia · Oliveto  
   _Spoiano è al centro del libro di Giuseppe Renzetti._ → `frazioni/spoiano.html`
34. [e7c2c418] ●●○ `-v=` **Chi ricostruì la torre di Tegoleto alla fine del Trecento?**  
   ✔ I fiorentini · ✘ I senesi · I longobardi · I francesi  
   _La torre fu ricostruita dai fiorentini alla fine del Trecento._ → `frazioni/tegoleto.html`
35. [1086aa45] ●●● `Pv+` **A quale ordine passò la fattoria di Tegoleto nel 1783?**  
   ✔ Ai Cavalieri di Santo Stefano · ✘ Ai Cavalieri di Malta · Ai Gesuiti · Ai Templari  
   _Nel 1783 la fattoria passò all'Ordine dei Cavalieri di Santo Stefano._ → `frazioni/tegoleto.html`
36. [3e486f3c] ●●○ `Nn=` **In quale anno nacque il Teatro Moderno di Tegoleto?**  
   ✔ 1960 · ✘ 1900 · 1925 · 2005  
   _Il TMT nacque nel 1960 come cinema, per iniziativa di alcuni parrocchiani._ → `frazioni/tegoleto.html`
37. [91b9c111] ●●○ `Pn=` **Chi gestisce il Teatro Moderno di Tegoleto?**  
   ✔ Il Gruppo Teatro La Torre · ✘ La Pro Loco di Civitella · Il Comune di Arezzo · Slow Food Valdichiana  
   _Il teatro è gestito dall'associazione culturale Gruppo Teatro La Torre._ → `frazioni/tegoleto.html`
38. [7c7d8c24] ●●○ `Nn=` **In quale anno a Tegoleto arrivò una tappa del Giro d'Italia?**  
   ✔ 2004 · ✘ 1983 · 1991 · 2018  
   _Il 12 maggio 2004 la quarta tappa del Giro d'Italia arrivò a Tegoleto._ → `frazioni/tegoleto.html`
39. [c1817196] ●●○ `Pv=` **Chi vinse la tappa del Giro d'Italia arrivata a Tegoleto nel 2004?**  
   ✔ Alessandro Petacchi · ✘ Mario Cipollini · Marco Pantani · Giuseppe Saronni  
   _Petacchi vinse davanti allo stabilimento del mobilificio Del Tongo._ → `frazioni/tegoleto.html`
40. [d7a4e134] ●●● `Nn+` **In quale anno fu trovata a Viciomaggio un'urna cineraria etrusca con iscrizione?**  
   ✔ 1872 · ✘ 1772 · 1922 · 1972  
   _L'urna ellenistica, con l'iscrizione l. prastn[a] nerinal, fu trovata nel 1872._ → `frazioni/viciomaggio.html`
41. [8b92c31b] ●●○ `-v=` **In quale frazione si trova la villa padronale settecentesca con una limonaia del 1836 e una cappella con orologio e campanile a vela?**  
   ✔ Viciomaggio · ✘ Spoiano · Tuori · Ciggiano  
   _È la villa padronale di Viciomaggio, restaurata nella parte posteriore nel 1868._ → `frazioni/viciomaggio.html`
42. [1d45bdf1] ●●○ `Pv=` **Su quale linea ferroviaria si trova la stazione di Albergo?**  
   ✔ Arezzo–Sinalunga · ✘ Firenze–Roma · Faentina · Porrettana  
   _Le stazioni di Albergo e di Civitella-Badia al Pino sono sulla ferrovia Arezzo–Sinalunga._ → `frazioni/albergo.html`
43. [daf0e244] ●○○ `-d=` **Quale strada romana passava da Albergo, secondo l'itinerario del Comune?**  
   ✔ Una via municipalis unita a un ramo della Cassia · ✘ La via Appia · La via Aurelia · La via Emilia  
   _Da Albergo passava una via municipalis che si univa a un ramo della Cassia diretto in Valdarno._ → `frazioni/albergo.html`
44. [cc15f4f6] ●●○ `-v=` **A quale ordine religioso apparteneva il priorato da cui nacque la chiesa di Santa Maria Assunta a Civitella?**  
   ✔ Benedettino · ✘ Francescano · Gesuita · Domenicano  
   _La chiesa fu eretta come priorato benedettino nell'XI secolo._ → `frazioni/civitella.html`
45. [2a3e555c] ●●○ `Nn=` **In quale anno fu completata in stile romanico la chiesa di Santa Maria Assunta a Civitella?**  
   ✔ 1252 · ✘ 1048 · 1652 · 1944  
   _La chiesa fu ultimata in stile romanico nel 1252._ → `frazioni/civitella.html`
46. [bdcb792b] ●●● `Nn+` **Quanti archi ha il portico del Palazzo Pretorio di Civitella?**  
   ✔ Cinque · ✘ Due · Otto · Dodici  
   _Il trecentesco Palazzo Pretorio ha un portico a cinque archi._ → `frazioni/civitella.html`
47. [dedef337] ●○○ `-n=` **Per quale scopo il notaio Becattini lasciò il suo palazzo alla Confraternita di Carità?**  
   ✔ Per farne un ospedale per i poveri · ✘ Per farne una scuola · Per farne un teatro · Per farne una caserma  
   _Alla sua morte, nel 1877, lasciò ogni bene per un ospedale dei poveri del paese._ → `frazioni/civitella.html`
48. [8a7414cd] ●●● `Nn+` **Da quale anno Palazzo Becattini è di proprietà del Comune?**  
   ✔ 1978 · ✘ 1877 · 1917 · 2004  
   _Nel 1978 l'ospedale è passato in proprietà al Comune._ → `frazioni/civitella.html`
49. [4881de19] ●○○ `Pd=` **In quale piazza di Civitella si trova la cisterna medievale?**  
   ✔ Piazza Lazzeri · ✘ Piazza Grande · Piazza della Signoria · Piazza del Campo  
   _La cisterna medievale si trova in piazza Lazzeri, intitolata al parroco don Alcide Lazzeri._ → `frazioni/civitella.html`
50. [584e621e] ●●● `Pv+` **A quale ente apparteneva il Saracino, la casa colonica cinquecentesca presso Tuori?**  
   ✔ Alla Fraternita dei Laici · ✘ Ai Medici · Al vescovo di Arezzo · All'Ordine di Santo Stefano  
   _Il Repertorio la descrive come casa colonica del XVI secolo della Fraternita dei Laici._ → `frazioni/tuori.html`
51. [8bc58b2b] ●●○ `-v+` **In quale frazione si trova Palazzo Santini-Paccinelli, villa settecentesca simmetrica rispetto alla scala centrale?**  
   ✔ Badia al Pino · ✘ Oliveto · Tuori · Spoiano  
   _Il Repertorio lo descrive come villa settecentesca a pianta rettangolare, simmetrica rispetto al vano scala centrale._ → `frazioni/badia-al-pino.html`
52. [19907f55] ●○○ `-n=` **Quale reliquia custodisce la chiesa della Compagnia di Santa Croce a Ciggiano?**  
   ✔ Una reliquia della Croce · ✘ Il velo della Madonna · Il mantello di San Martino · Un osso di San Biagio  
   _La reliquia della Croce veniva esposta il 3 maggio e il 14 settembre._ → `frazioni/ciggiano.html`
53. [43d14c27] ●●● `Pv+` **Quale pittore dipinse la Madonna del Rosario conservata nella chiesa di Sant'Andrea a Oliveto?**  
   ✔ Orazio Porta · ✘ Piero della Francesca · Giorgio Vasari · Luca Signorelli  
   _La chiesa di Sant'Andrea, documentata dal 1300, conserva una Madonna del Rosario di Orazio Porta._ → `frazioni/oliveto.html`
54. [b4c51f53] ●●○ `Nn=` **In quale anno Villa Oliveto fu ceduta al Comune di Civitella?**  
   ✔ 1980 · ✘ 1940 · 1960 · 2005  
   _Ceduta al Comune nel 1980, la villa ospita il Centro di Documentazione sui campi di internamento._ → `frazioni/oliveto.html`
55. [4bfffd85] ●●○ `Pn+` **Chi fuse nel 1358 la campana oggi nel campanile della chiesa di Pieve a Maiano?**  
   ✔ Neri d'Arezzo · ✘ Giambologna · Benvenuto Cellini · Lorenzo Ghiberti  
   _La campana apparteneva alla distrutta chiesa di San Giovanni Battista a Montoto._ → `frazioni/pieve-a-maiano.html`
56. [1f3abaaa] ●○○ `-n=` **Che cos'era anticamente il podere Spedaluccio, vicino a Pieve a Maiano?**  
   ✔ Un ospizio per viandanti · ✘ Un mulino ad acqua · Un convento femminile · Una fornace romana  
   _La casa colonica dello Spedaluccio è tutto ciò che resta di un antico ospizio per viandanti._ → `frazioni/pieve-a-maiano.html`
57. [21e2abd1] ●●● `Nn+` **Da quale anno è documentato l'antico ospizio dello Spedaluccio?**  
   ✔ 1198 · ✘ 1048 · 1385 · 1774  
   _L'itinerario del Comune ricorda l'antico ospizio per viandanti, documentato dal 1198._ → `frazioni/pieve-a-maiano.html`
58. [388b792d] ●○○ `-n=` **Su che cosa sorge l'Oratorio della Madonna del Conforto a Pieve al Toppo?**  
   ✔ Sul sito dell'antica pieve · ✘ Sui resti di un tempio etrusco · Su un'antica fornace · Sulle mura del castello  
   _L'oratorio sorge sul sito dell'antica pieve ed è dedicato alla Madonna del Conforto dal 1906._ → `frazioni/pieve-al-toppo.html`
59. [0ff18981] ●○○ `-d=` **Che cos'era all'inizio, nel 1960, il Teatro Moderno di Tegoleto?**  
   ✔ Un cinema · ✘ Una chiesa · Una fabbrica · Una scuola  
   _Nato nel 1960 come cinema per iniziativa di alcuni parrocchiani, dal 1997 è una sala polifunzionale._ → `frazioni/tegoleto.html`
60. [c5767706] ●●○ `-n+` **Che cosa c'è nel recinto d'accesso al Palatium-torre della Rocca di Civitella?**  
   ✔ La cisterna per la raccolta dell'acqua · ✘ Una cappella affrescata · Le prigioni · Un forno per il pane  
   _Il Palatium è formato dalla torre vera e propria e dal recinto d'accesso con la cisterna._ → `frazioni/civitella.html`
61. [99db94ce] ●●○ `Pn=` **Quale via medievale transitava da Albergo?**  
   ✔ La via senese-aretina · ✘ La via Francigena · La via Emilia · La via Flaminia  
   _Dall'antico borgo transitava in epoca medievale la via senese-aretina._ → `frazioni/albergo.html`
62. [a6b92165] ●○○ `-d=` **Quale bene è tutelato da vincolo nazionale a Badia al Pino?**  
   ✔ La torre dell'antico castello · ✘ La stazione ferroviaria · Il palazzetto dello sport · Il monumento ai caduti  
   _La torre fa parte di ciò che resta, con la porta, dell'antico castello sorto intorno all'abbazia._ → `frazioni/badia-al-pino.html`
63. [855aa29c] ●○○ `-d=` **Che cosa prevede il Piano Strutturale per la Rocca di Civitella?**  
   ✔ Il restauro e un «museo» dedicato ai castelli del territorio · ✘ La demolizione dei ruderi · Un albergo di lusso · Un parcheggio panoramico  
   _Il Piano prevede il restauro della Rocca e un «museo» come punto di riferimento per visitare castelli, rocche, torri e antichi tracciati._ → `frazioni/civitella.html`
64. [5290f03d] ●●○ `-v+` **Quali stemmi si vedono sul Palazzo Pretorio di Civitella?**  
   ✔ Quelli dei podestà fiorentini · ✘ Quelli dei vescovi di Arezzo · Quelli dei granduchi di Lorena · Quelli dei Savoia  
   _Il Palazzo Pretorio è trecentesco, con un portico a cinque archi e gli stemmi dei podestà fiorentini._ → `frazioni/civitella.html`
65. [77e1c3f5] ●●● `Nn+` **In quale anno morì il notaio Becattini, che lasciò il suo palazzo per un ospedale dei poveri?**  
   ✔ 1877 · ✘ 1777 · 1917 · 1944  
   _Il notaio morì il 19 luglio 1877; dal 1978 il palazzo è del Comune._ → `frazioni/civitella.html`
66. [fd831df6] ●●● `Pv+` **Quali oratori si trovano nel borgo di Civitella?**  
   ✔ Quello della Santissima Trinità e quello della Madonna di Mercatale · ✘ Quello della Madonna della Costarella e quello di San Rocco · Quello della Madonna del Conforto e quello di Santa Croce · Quello di San Rocco e quello della Madonna del Rosario  
   _A Civitella ci sono gli oratori della Santissima Trinità e della Madonna di Mercatale; la Costarella è a Ciggiano._ → `frazioni/civitella.html`
67. [608aba01] ●●○ `-n+` **Quale bene storico di Albergo è censito nel Repertorio del Piano Strutturale?**  
   ✔ La fonte-cisterna · ✘ Un acquedotto romano · Una torre di avvistamento · Un mulino ad acqua  
   _Il Repertorio censisce la fonte-cisterna di Albergo e ne valorizza il centro storico._ → `frazioni/albergo.html`
68. [e6917851] ●○○ `-n=` **Che cosa ospita oggi il palazzetto settecentesco di Badia al Pino, sede comunale fino ai primi anni Settanta?**  
   ✔ La Biblioteca comunale · ✘ Il municipio · Un museo archeologico · La scuola primaria  
   _Fu sede comunale dal 1917 ai primi anni Settanta; oggi è la Biblioteca comunale._ → `frazioni/badia-al-pino.html`
69. [c435203b] ●●● `Nv+` **In quale anno fu inaugurato il monumento ai caduti nel piazzale della chiesa di Badia al Pino?**  
   ✔ 1951 · ✘ 1921 · 1946 · 1971  
   _Il monumento ai caduti delle due guerre fu inaugurato il 26 agosto 1951._ → `frazioni/badia-al-pino.html`
70. [d3fdc7c5] ●●○ `-v+` **Che cosa caratterizza Villa del Bosco, a Badia al Pino?**  
   ✔ Un parco con un filare di pini · ✘ Una limonaia del 1836 · Una torre-piccionaia · Una cappella con orologio  
   _Villa del Bosco ha un parco e un filare di pini._ → `frazioni/badia-al-pino.html`
71. [7c31e8d6] ●●● `Pv+` **A quali santi è dedicata la chiesa di San Bartolomeo a Badia al Pino?**  
   ✔ Bartolomeo, Martino e Filippo · ✘ Bartolomeo, Pietro e Paolo · Bartolomeo, Biagio e Rocco · Bartolomeo, Giorgio e Luca  
   _La chiesa, annessa all'antica abbazia, è dedicata ai santi Bartolomeo, Martino e Filippo._ → `frazioni/badia-al-pino.html`
72. [f996bc77] ●●● `Pv+` **Quale altare custodisce la chiesa di San Biagio a Ciggiano?**  
   ✔ L'altare Mazzeschi · ✘ L'altare Pecchioli · L'altare Barbolani · L'altare Becattini  
   _San Biagio custodisce l'altare Mazzeschi e una Santa Maria Maddalena attribuita ad Andrea Sansovino._ → `frazioni/ciggiano.html`
73. [2c5801d3] ●●○ `-v+` **Di quale secolo è il loggiato della chiesa della Madonna della Costarella, a Ciggiano?**  
   ✔ Del Settecento · ✘ Del Trecento · Del Cinquecento · Del Novecento  
   _La chiesa fu terminata nel 1635; il loggiato è settecentesco._ → `frazioni/ciggiano.html`
74. [48e6e4b6] ●●● `Nv+` **In quale anno la chiesa di San Pietro a Ciggiano ebbe l'intervento che le diede l'aspetto eclettico?**  
   ✔ 1836 · ✘ 1636 · 1736 · 1936  
   _La chiesa è di origine medievale; il suo aspetto eclettico è frutto di un intervento del 1836._ → `frazioni/ciggiano.html`
75. [eccf0f3a] ●●○ `-v+` **In quali registri compare già nel 1274 la chiesa di Sant'Angelo a Cornia?**  
   ✔ Nelle decime · ✘ Nel catasto leopoldino · Negli statuti di Siena · Nei registri dell'ISTAT  
   _La chiesa di San Michele Arcangelo compare nelle decime del 1274._ → `frazioni/cornia.html`
76. [d4b4fda3] ●●● `Nv+` **In quale anno fu ricostruita la chiesa di San Giovanni d'Oliveto?**  
   ✔ 1343 · ✘ 1243 · 1443 · 1643  
   _San Giovanni d'Oliveto compare nelle decime del 1274 e fu ricostruita nel 1343._ → `frazioni/oliveto.html`
77. [2c46b6c8] ●○○ `-d+` **Che cos'era in origine l'Oratorio di San Rocco, a Oliveto?**  
   ✔ Un tabernacolo, diventato cappella nell'Ottocento · ✘ Una torre di guardia · Un mulino · Una scuola  
   _L'oratorio nacque come tabernacolo e divenne cappella nell'Ottocento._ → `frazioni/oliveto.html`
78. [0c33c206] ●●● `Nv+` **Attorno a quale anno fu rifatta la Cappella della Compagnia di Oliveto?**  
   ✔ 1637 · ✘ 1337 · 1737 · 1937  
   _Secondo il Repertorio, la Cappella della Compagnia fu rifatta attorno al 1637._ → `frazioni/oliveto.html`
79. [49446c6c] ●○○ `-d=` **Di quali alberi è ricco il parco di Villa Oliveto?**  
   ✔ Cedri e lecci · ✘ Palme e agavi · Faggi e abeti · Pioppi e salici  
   _La villa, dei conti Barbolani di Montauto, ha un parco di ispirazione romantica ricco di cedri e lecci._ → `frazioni/oliveto.html`
80. [498b0966] ●●● `Nv=` **In quale anno morì Muriel Spark, che visse a Oliveto?**  
   ✔ 2006 · ✘ 1996 · 2001 · 2016  
   _Ricevette la cittadinanza onoraria nel 2005, morì nel 2006 ed è sepolta a Oliveto._ → `frazioni/oliveto.html`
81. [3bd4c74d] ●●● `Nv+` **In quale anno fu ampliata la chiesa di Santa Maria Assunta a Pieve a Maiano?**  
   ✔ 1865 · ✘ 1765 · 1824 · 1965  
   _La chiesa fu costruita dopo il 1824 e ampliata nel 1865._ → `frazioni/pieve-a-maiano.html`
82. [91087b87] ●●○ `Pv=` **Qual è il titolo della parrocchia di Pieve a Maiano?**  
   ✔ Santa Maria Assunta · ✘ San Biagio · San Martino · Sant'Andrea Apostolo  
   _La parrocchia di Pieve a Maiano è Santa Maria Assunta._ → `frazioni/pieve-a-maiano.html`
83. [253e4dff] ●●● `Nn+` **Da quale anno l'oratorio di Pieve al Toppo è dedicato alla Madonna del Conforto?**  
   ✔ 1906 · ✘ 1502 · 1806 · 1966  
   _L'oratorio sorge sul sito dell'antica pieve ed è dedicato alla Madonna del Conforto dal 1906._ → `frazioni/pieve-al-toppo.html`
84. [974228d6] ●●○ `-v+` **Qual è l'unico bene storico di Ponticino censito dal Repertorio del Piano?**  
   ✔ Il mulino · ✘ Il ponte romanico · La pieve · Il castello  
   _Il Repertorio censisce solo il Mulino di Ponticino; il «ponte romanico» non ha riscontri._ → `frazioni/ponticino.html`
85. [d9d80f19] ●●○ `-v+` **In quale comune ha sede la parrocchia dei Santi Iacopo e Cristoforo di Ponticino?**  
   ✔ Laterina Pergine Valdarno · ✘ Civitella in Val di Chiana · Arezzo · Bucine  
   _Secondo l'annuario della Diocesi la parrocchia ha sede nel comune di Laterina Pergine Valdarno._ → `frazioni/ponticino.html`
86. [3d4a15ba] ●●○ `-v+` **Quale elemento caratterizza Villa Pecchioli, a Spoiano?**  
   ✔ Una torre-piccionaia · ✘ Una limonaia del 1836 · Un filare di pini · Una cappella con orologio  
   _Villa Pecchioli è settecentesca, con una torre-piccionaia._ → `frazioni/spoiano.html`
87. [99f5bb0f] ●●○ `-n+` **In quale periodo dell'anno si tiene la stagione del Teatro Moderno di Tegoleto?**  
   ✔ Da ottobre a marzo · ✘ Da giugno ad agosto · Solo a dicembre · Da aprile a giugno  
   _Il TMT ha una stagione da ottobre a marzo._ → `frazioni/tegoleto.html`
88. [2f350987] ●●● `Nv+` **Quale tappa del Giro d'Italia 2004 arrivò a Tegoleto?**  
   ✔ La quarta · ✘ La prima · La decima · L'ultima  
   _Il 12 maggio 2004 vi arrivò la quarta tappa, vinta da Alessandro Petacchi._ → `frazioni/tegoleto.html`
89. [13de9716] ●●○ `Pv=` **Davanti a quale stabilimento si concluse la tappa del Giro d'Italia arrivata a Tegoleto nel 2004?**  
   ✔ Quello della Del Tongo · ✘ Quello della CEIA · Quello della Chimet · Quello della Kico  
   _La tappa fu vinta da Petacchi davanti allo stabilimento del mobilificio Del Tongo._ → `frazioni/tegoleto.html`
90. [ced4fecf] ●●○ `-v+` **Su quali beni di Tuori c'è un vincolo nazionale?**  
   ✔ Il cassero, la chiesa e il cimitero · ✘ Tutto il centro storico · Solo il Saracino · La villa e il suo parco  
   _Il vincolo riguarda cassero, chiesa e cimitero, non il centro storico._ → `frazioni/tuori.html`
91. [8288be8c] ●●○ `-v+` **Com'è fatto il portico del Saracino, presso Tuori?**  
   ✔ A tre archi a tutto sesto · ✘ A cinque archi a sesto acuto · A un solo grande arco · A colonne senza archi  
   _Il Saracino ha un portico a tre archi a tutto sesto e una loggia ad arco ribassato._ → `frazioni/tuori.html`
92. [b72de4ff] ●●● `Nv+` **In quale anno fu restaurata, con decorazioni pittoriche, la parte posteriore della Villa di Viciomaggio?**  
   ✔ 1868 · ✘ 1768 · 1836 · 1968  
   _La villa è settecentesca; la parte posteriore fu restaurata nel 1868, la limonaia è del 1836._ → `frazioni/viciomaggio.html`
93. [396551e5] ●●● `Pv+` **Di quale bottega è la Madonna con il Bambino del 1522 nel tabernacolo presso la Porta Senese di Civitella?**  
   ✔ Quella di Giovanni della Robbia · ✘ Quella di Donatello · Quella di Luca Signorelli · Quella del Sansovino  
   _È una terracotta invetriata del 1522 della bottega di Giovanni della Robbia._ → `frazioni/civitella.html`
94. [1447e0cc] ●○○ `-d=` **Che cosa raccoglie la Pinacoteca di Civitella?**  
   ✔ Dipinti e sculture d'arte contemporanea, dagli anni Settanta a oggi · ✘ Reperti etruschi e romani · Arte sacra medievale · Attrezzi della civiltà contadina  
   _La Pinacoteca d'arte contemporanea ospita dipinti e sculture dai primi anni Settanta alle opere degli artisti di oggi._ → `frazioni/civitella.html`
95. [f6ac606f] ●●○ `Pv=` **Quale porta di Civitella fu distrutta dalle bombe nel 1944?**  
   ✔ Porta Aretina · ✘ Porta Senese · Porta Fiorentina · Porta Romana  
   _Delle due porte del XIII secolo, Porta Aretina fu distrutta nel 1944; Porta Senese è rimasta integra._ → `frazioni/civitella.html`
96. [e8da5b98] ●●● `Pv+` **A chi donarono Palazzo Ninci i suoi proprietari nel 1917?**  
   ✔ Alla Fraternita dei Laici · ✘ Al Comune di Civitella · Alla diocesi di Arezzo · Alla Pro Loco  
   _Palazzo Ninci, in piazza Lazzeri, fu donato nel 1917 alla Fraternita dei Laici, che lo tenne fino al 1925._ → `frazioni/civitella.html`
97. [d1b0f93f] ●●● `Pv+` **A quale monastero fiorentino furono incorporate nel 1441 le chiese di Civitella e della Badia al Pino?**  
   ✔ Il monastero di Santa Brigida · ✘ L'abbazia di Vallombrosa · Il convento di San Marco · La basilica di Santa Croce  
   _Una bolla di papa Eugenio IV del 17 novembre 1441 le incorporò nel monastero di Santa Brigida presso Firenze (Repetti)._ → `frazioni/badia-al-pino.html`
98. [99383471] ●○○ `-d+` **Che cosa raffigurava il sigillo dell'antico Comune di Oliveto?**  
   ✔ Un olivo carico di frutti · ✘ Una torre merlata · Un leone rampante · Una croce rossa  
   _Il Repetti ricorda il sigillo del Comune di Oliveto: un olivo in pieno frutto._ → `frazioni/oliveto.html`
99. [56054fd7] ●●● `Pv+` **Di quale badia era il patronato su Cornia dal secolo XI, secondo il Repetti?**  
   ✔ La badia di Agnano · ✘ La Badia del Pino · L'abbazia di Vallombrosa · L'abbazia di Camaldoli  
   _Dal secolo XI Cornia era dei monaci della badia d'Agnano; nel 1350 l'abate la pose sotto l'accomandigia di Firenze._ → `frazioni/cornia.html`
100. [d3c01c7d] ●●○ `-v+` **Da quale località vicina doveva distinguersi «Vicione Maggiore», l'antico nome di Viciomaggio?**  
   ✔ Da Vicione Piccolo, cioè Battifolle · ✘ Da Vicchio di Mugello · Da Vicopisano · Da Vico d'Elsa  
   _Il Repetti spiega che Vicione Maggio si chiamava così per distinguerlo dal vicino Vicione Piccolo, cioè Battifolle._ → `frazioni/viciomaggio.html`
101. [65c7e281] ●●○ `-v+` **Con quale nome popolare era chiamata la Pieve al Toppo, secondo il Repetti?**  
   ✔ Pieve all'Intoppo · ✘ Pieve del Poggio · Pieve della Chiana · Pieve dei Pellegrini  
   _Il Repetti la registra come «Pieve al Toppo, volgarmente detta all'Intoppo»._ → `frazioni/pieve-al-toppo.html`
102. [4fc570fa] ●●● `Nn+` **Quante chiese dipendevano dalla pieve del Toppo, secondo il Repetti?**  
   ✔ 24 · ✘ 4 · 12 · 50  
   _Secondo il Repetti, prima della rovina del 1502 la pieve aveva 24 chiese dipendenti._ → `frazioni/pieve-al-toppo.html`
103. [84a6f9e7] ●●○ `-v+` **A quale Comunità apparteneva Majano nel 1833, secondo il Repetti?**  
   ✔ A quella di Arezzo · ✘ A quella di Civitella · A quella di Laterina · A quella di Bucine  
   _Nel 1833 i 91 abitanti di Majano erano nella Comunità di Arezzo, i 224 di Montoto in quella di Civitella; Pieve a Maiano entrò nel comune più tardi._ → `frazioni/pieve-a-maiano.html`
104. [845faf36] ●●● `Pv+` **Con quale nome il Repetti chiama la Pieve a Maiano del comune di Civitella?**  
   ✔ Majano di Valle Lunga · ✘ Majano di Lucardo · Majano di Fiesole · Majano al Toppo  
   _Il Repetti la chiama «Majano di Valle Lunga», nel Val d'Arno aretino, sulla strada regia aretina davanti alla gola dell'Imbuto._ → `frazioni/pieve-a-maiano.html`

## Borghi minori (38)

1. [cd56501b] ●○○ `-d=` **Per che cosa era noto il luogo di Matroia?**  
   ✔ Per una sorgente con acque ritenute medicamentose · ✘ Per una miniera d'argento · Per un castello dei Medici · Per una fornace di vetro  
   _Le acque, ritenute medicamentose, erano usate soprattutto per i lattanti._ → `frazioni/borghi-minori.html#matroia`
2. [e4363716] ●○○ `-d+` **Che cosa c'è oggi a Matroia, secondo il Piano Strutturale?**  
   ✔ Un allevamento di cavalli · ✘ Una cantina sociale · Un aeroporto · Una cava di marmo  
   _Il Piano prevede di trasformare l'allevamento in Centro di Equitazione._ → `frazioni/borghi-minori.html#matroia`
3. [dbcd5fc3] ●●○ `-v=` **Dove si trova oggi la campana del 1358 proveniente da Montoto?**  
   ✔ Nella chiesa di Pieve a Maiano · ✘ Nel Duomo di Arezzo · Nella Rocca di Civitella · Nel Museo del Bargello  
   _La campana di Montoto è conservata nella chiesa di Santa Maria Assunta a Pieve a Maiano._ → `frazioni/borghi-minori.html#montoto`
4. [0ea02fda] ●●● `Nv=` **In quale anno il castello di Montoto passò a Firenze?**  
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
8. [5356e1c0] ●●● `Pv+` **A chi appartenne Dorna a partire dal 1814?**  
   ✔ Alle suore Montalve · ✘ Ai Medici · Ai Gesuiti · Al Comune di Arezzo  
   _Nel XVIII secolo era dei Riccardi; dal 1814 fu delle suore Montalve._ → `frazioni/borghi-minori.html#dorna`
9. [144d50be] ●●● `Pv+` **A chi è dedicata l'attuale chiesa di San Martino in Poggio?**  
   ✔ Ai Santi Maria e Carlo · ✘ A San Martino e San Rocco · A San Biagio · A Sant'Andrea  
   _Il Repertorio scrive che la chiesa fu costruita con il patrimonio di Carlo Casini, da cui il titolo dei Santi Maria e Carlo._ → `frazioni/borghi-minori.html#san-martino-in-poggio`
10. [b4f36db1] ●●● `Pv+` **Grazie al patrimonio di chi fu costruita la chiesa dei Santi Maria e Carlo a San Martino in Poggio?**  
   ✔ Il nobile Carlo Casini · ✘ Il vescovo Guglielmino degli Ubertini · La famiglia Pecchioli · Il notaio Becattini  
   _La chiesa fu costruita con il patrimonio donato da Carlo Casini._ → `frazioni/borghi-minori.html#san-martino-in-poggio`
11. [d3a07030] ●○○ `-n=` **Come descrissero i fiorentini il castello di Gaenne, passato sotto il loro dominio nel 1385?**  
   ✔ «Un forte castello di sito e di muro» · ✘ «La più bella rocca di Toscana» · «Un castello senza difese» · «Il nido dei ghibellini»  
   _Nel 1385 Gaenne passò a Firenze, che lo descrisse come «un forte castello di sito e di muro»._ → `frazioni/borghi-minori.html#gaenne`
12. [0aeb1238] ●●○ `Pv=` **A chi apparteneva il castello di Gaenne nel 1069?**  
   ✔ Ai longobardi di Dorna · ✘ Ai Medici · Ai vescovi di Siena · Ai conti Guidi  
   _Nel 1069 apparteneva ai longobardi di Dorna, poi passò ai Tarlati._ → `frazioni/borghi-minori.html#gaenne`
13. [b8b3b4f1] ●●○ `-v=` **Tra quali frazioni si trova la località Le Caserosse?**  
   ✔ Tra Viciomaggio e Pieve al Toppo · ✘ Tra Cornia e Tuori · Tra Oliveto e Ciggiano · Tra Spoiano e Gebbia  
   _Le Norme del Piano parlano di «località Caserosse (fra Viciomaggio e Pieve al Toppo)»._ → `lavoro-e-sapori.html#industria`
14. [e4fa556c] ●●● `Pv+` **In quale materiale è il cippo romano trovato a Le Fosse?**  
   ✔ Travertino · ✘ Marmo di Carrara · Bronzo · Granito  
   _A Le Fosse il Repertorio registra un cippo romano in travertino._ → `frazioni/borghi-minori.html#malpertuso-le-fosse`
15. [20485c5d] ●●○ `-n+` **Su che cosa sorsero i poderi di Montoto, lungo via della Centrale?**  
   ✔ Su un fortilizio longobardo · ✘ Su una villa romana · Su un convento francescano · Su una fornace etrusca  
   _I poderi di Montoto sorsero su un fortilizio longobardo, passato a Firenze nel 1385._ → `frazioni/borghi-minori.html#montoto`
16. [2bad47c2] ●●● `Pv+` **A quale santo è dedicata la chiesetta di Matroia?**  
   ✔ San Michele Arcangelo · ✘ San Rocco · San Biagio · Sant'Andrea  
   _La chiesetta di San Michele Arcangelo è ciò che resta di un insediamento religioso che «fu sede di un convento»._ → `frazioni/borghi-minori.html#matroia`
17. [99c66c9f] ●●○ `-n+` **Che cosa si conserva a Tribbio, oltre al nome che ricorda un antico trivio?**  
   ✔ Un pozzo storico · ✘ Un arco romano · Una torre di guardia · Un ponte medievale  
   _Tribbio prende il nome da un trivio, un incrocio di tre strade, e conserva un vecchio pozzo censito tra i beni storici._ → `frazioni/borghi-minori.html#tribbio`
18. [7551f5ac] ●○○ `-n=` **Quando furono abbandonati i borghi medievali di Malpertuso e Le Fosse?**  
   ✔ Nel tardo Medioevo · ✘ Nell'Ottocento · Dopo il 1944 · In età romana  
   _Malpertuso e Le Fosse sono borghi medievali abbandonati nel tardo Medioevo._ → `frazioni/borghi-minori.html#malpertuso-le-fosse`
19. [d2a0a62f] ●●○ `-v=` **Di quale origine è il castello di Dorna?**  
   ✔ Longobarda · ✘ Etrusca · Normanna · Rinascimentale  
   _Dorna fu un castello longobardo (VIII–X secolo)._ → `frazioni/borghi-minori.html#dorna`
20. [a8e3eb8d] ●●● `Pv+` **Come è chiamata Dorna in un documento del 1181?**  
   ✔ Castrum Durna · ✘ Curtis Dornae · Villa Turna · Castellum Ornae  
   _Un documento del 1181 parla del castrum Durna; la torre è ricordata dal 1198._ → `frazioni/borghi-minori.html#dorna`
21. [e5f0dee8] ●●● `Pv+` **A quali santi era dedicata la chiesa documentata a Dorna nel 1182?**  
   ✔ Vito e Nicola · ✘ Pietro e Paolo · Cosma e Damiano · Giorgio e Luca  
   _Nel 1182 è documentata una chiesa dei Santi Vito e Nicola._ → `frazioni/borghi-minori.html#dorna`
22. [534d8c16] ●●● `Pv+` **A quale famiglia passò il castello di Gaenne dopo i longobardi di Dorna?**  
   ✔ I Tarlati · ✘ Gli Ubertini · I Medici · I conti Guidi  
   _Nel 1069 Gaenne apparteneva ai longobardi di Dorna, poi passò ai Tarlati._ → `frazioni/borghi-minori.html#gaenne`
23. [0574409f] ●●● `Nv+` **Da quale anno San Martino in Poggio è parrocchia?**  
   ✔ 1814 · ✘ 1700 · 1726 · 1917  
   _La chiesa dei Santi Maria e Carlo fu ampliata nel 1726 e divenne parrocchia con un decreto del vescovo del 30 maggio 1814._ → `frazioni/borghi-minori.html#san-martino-in-poggio`
24. [a085dfa8] ●●○ `Nd+` **A che altitudine si trova, all'incirca, San Martino in Poggio?**  
   ✔ Circa 540 metri · ✘ Circa 140 metri · Circa 940 metri · Circa 1.240 metri  
   _San Martino in Poggio si trova a circa 540 metri._ → `frazioni/borghi-minori.html#san-martino-in-poggio`
25. [e834399c] ●●○ `Nd+` **Quanto è lunga, all'incirca, la cinta muraria a secco di Poggio Castellare?**  
   ✔ Circa 300 metri · ✘ Circa 30 metri · Circa 3 chilometri · Circa 10 metri  
   _Sulla cima resta una cinta ellittica a secco di circa 300 metri; la datazione è discussa._ → `frazioni/borghi-minori.html#poggio-castellare`
26. [1af9c0f0] ●●○ `Nd+` **Quanto è spessa, all'incirca, la cinta muraria a secco di Poggio Castellare?**  
   ✔ Circa 1,60 metri · ✘ Circa 16 centimetri · Circa 6 metri · Circa 16 metri  
   _La cinta ellittica a secco è spessa 1,60 metri e lunga circa 300._ → `frazioni/borghi-minori.html#poggio-castellare`
27. [6762121d] ●●○ `-v+` **Per curare quali malati si attingeva l'acqua della sorgente di Matroia?**  
   ✔ I neonati colpiti da malattie gastroenteriche · ✘ Gli anziani con dolori articolari · Chi soffriva di malattie della pelle · Chi aveva i calcoli renali  
   _Alla sorgente, presso la cappella di San Michele Arcangelo, erano attribuite virtù salutari soprattutto per i neonati._ → `frazioni/borghi-minori.html#matroia`
28. [191e897a] ●●○ `-n+` **Dove si trova oggi il mulino di Montoto?**  
   ✔ Sommerso dall'invaso della Penna · ✘ Trasformato in museo · Inglobato nella villa di Montarfoni · Ricostruito a Pieve a Maiano  
   _Il mulino di Montoto è oggi sommerso dall'invaso della Penna, lungo l'antica strada di Vallelunga._ → `frazioni/borghi-minori.html#montoto`
29. [de37df18] ●●○ `-n+` **Che cosa è stato trovato a Le Fosse, oltre a un cippo romano in travertino?**  
   ✔ Reperti sporadici di età preistorica e romana · ✘ Una necropoli etrusca · Un tesoro di monete medievali · Un mosaico pavimentale  
   _Il Repertorio registra a Le Fosse un cippo romano in travertino e reperti sporadici di età preistorica e romana._ → `frazioni/borghi-minori.html#malpertuso-le-fosse`
30. [ff1c509f] ●○○ `-d+` **Che cosa prevede il Piano Strutturale per il borgo-fattoria e la villa di Montarfoni?**  
   ✔ Un «polo di eccellenza territoriale» · ✘ Un centro commerciale · Una zona industriale · Un campeggio  
   _Le Norme del Piano (art. 95) prevedono nel borgo-fattoria e nella villa un «polo di eccellenza territoriale»._ → `frazioni/borghi-minori.html#montarfoni`
31. [2e9fd6ab] ●●○ `-v+` **Di che cosa fu dotata la chiesa di San Martino in Poggio quando fu ampliata nel 1726?**  
   ✔ Di due nuovi altari · ✘ Di un campanile a vela · Di un organo · Di un portico a tre archi  
   _La chiesa dei Santi Maria e Carlo fu ampliata nel 1726 con due nuovi altari._ → `frazioni/borghi-minori.html#san-martino-in-poggio`
32. [8624b548] ●●○ `-v=` **Quale di questi luoghi, insieme a Poggio Castellare, è previsto come parco archeologico dalle Norme del Piano?**  
   ✔ Il castello di Gaenne · ✘ Matroia · Tribbio · Dorna  
   _Le Norme del Piano (art. 49) indicano come parchi archeologici il Castellare di Oliveto, Poggio Castellare e Gaenne._ → `frazioni/borghi-minori.html#poggio-castellare`
33. [dc8e4d56] ●●● `Pv+` **Quale Madonna era venerata a Matroia, legata al culto delle acque?**  
   ✔ La Madonna del Latte · ✘ La Madonna del Conforto · La Madonna della Costarella · La Madonna di Mercatale  
   _A Matroia era venerata una Madonna del Latte; l'acqua della sorgente si attingeva per i neonati._ → `frazioni/borghi-minori.html#matroia`
34. [1a6af485] ●●● `Pv+` **Sopra quale strada sorse il castello di Montarfoni?**  
   ✔ La strada Regia Aretina · ✘ La via Aurelia · La via Francigena · La Via Vecchia Senese  
   _Il castello sorse sopra la strada Regia Aretina; ne restano la porta e tratti delle mura._ → `frazioni/borghi-minori.html#montarfoni`
35. [f5c1d25c] ●●● `Pv+` **Con quale nome latino il Repetti registra Montoto?**  
   ✔ Mons tutus · ✘ Mons altus · Mons Othonis · Mons totus  
   _Il Repetti registra la voce come «Montoto (Mons tutus)»._ → `frazioni/borghi-minori.html#montoto`
36. [42bc1e10] ●●● `Pv+` **A quale monastero di Arezzo fu venduto nel 1051 un quarto del castello di Montoto?**  
   ✔ Ai Santi Flora e Lucilla · ✘ A Santa Maria della Pieve · A San Domenico · A San Francesco  
   _Il 2 marzo 1051 Golizo vendette all'abate Enrico dei Santi Flora e Lucilla un quarto del castello e della chiesa di San Giovanni Battista._ → `frazioni/borghi-minori.html#montoto`
37. [3bf8e1f2] ●●● `Pv+` **In quale privilegio del 1356 è ricordato il castello di Gaenne?**  
   ✔ In quello dell'imperatore Carlo IV alla città di Arezzo · ✘ Nella bolla di papa Eugenio IV · Negli statuti della Repubblica di Siena · Nel catasto del granduca Pietro Leopoldo  
   _Secondo il Repetti, Gaenna è ricordata nel privilegio dell'imperatore Carlo IV ad Arezzo del 1356._ → `frazioni/borghi-minori.html#gaenne`
38. [3cb5660e] ●●○ `-v+` **A chi pagava ancora un canone annuo, nell'Ottocento, il proprietario della tenuta di Dorna?**  
   ✔ Al capitolo di Arezzo · ✘ Al Comune di Civitella · Al granduca di Toscana · Al vescovo di Siena  
   _Secondo il Repetti, era l'eredità di una donazione fatta al capitolo nel 1181 da Rolandino di Mambilia._ → `frazioni/borghi-minori.html#dorna`

## Lavoro e sapori (25)

1. [fbceb884] ●○○ `-d-` **Che cosa produce l'azienda CEIA di Viciomaggio?**  
   ✔ Metal detector · ✘ Cucine componibili · Gioielli · Macchine agricole  
   _CEIA produce metal detector: per l'industria tessile dal 1962, per gli aeroporti dal 1975._ → `lavoro-e-sapori.html#industria`
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
   _Chimet recupera e affina metalli preziosi; il suo primo stabilimento aprì a Badia al Pino nel 1976._ → `lavoro-e-sapori.html#industria`
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
   _Nel 2022 il marchio Del Tongo fu acquisito dall'azienda Kico._ → `lavoro-e-sapori.html#del-tongo`
12. [6355b329] ●●● `Nv+` **In quali anni fu attiva la squadra ciclistica professionistica Del Tongo?**  
   ✔ Dal 1982 al 1991 · ✘ Dal 1954 al 1964 · Dal 1995 al 2005 · Dal 2004 al 2018  
   _La squadra corse tra i professionisti dal 1982 al 1991._ → `lavoro-e-sapori.html#del-tongo`
13. [92e0687d] ●●○ `Pv=` **Con quale corridore la squadra Del Tongo vinse il Giro d'Italia del 1983?**  
   ✔ Giuseppe Saronni · ✘ Francesco Moser · Fausto Coppi · Marco Pantani  
   _Saronni vinse il Giro 1983 con la Del Tongo; nello stesso anno la squadra vinse anche la Milano-Sanremo._ → `lavoro-e-sapori.html#del-tongo`
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

## Feste e sport (40)

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
   _Le proiezioni gratuite si tengono in piazza della Chiesa a Tegoleto, il mercoledì sera di luglio, dal 2018._ → `feste-e-associazioni.html#luglio`
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
25. [daf78ce6] ●●○ `Pv=` **Chi organizza la Sagra dei Baccelli di Spoiano?**  
   ✔ La Polisportiva Spoiano · ✘ La Pro Loco di Ciggiano · Il Circolo ARCI di Pieve al Toppo · La parrocchia di Spoiano  
   _La Sagra dei Baccelli è organizzata dalla Polisportiva Spoiano._ → `feste-e-associazioni.html`
26. [c3556ffe] ●●● `Nn+` **Quale edizione della Sagra dei Baccelli si è tenuta nel 2025?**  
   ✔ La 48ª · ✘ La 8ª · La 25ª · La 75ª  
   _Nel 2025 la Sagra dei Baccelli è arrivata alla 48ª edizione._ → `feste-e-associazioni.html`
27. [eb4598d2] ●●○ `Pv=` **Chi organizza la Sagra della Pesca di Pieve al Toppo?**  
   ✔ Il Circolo ARCI di Pieve al Toppo · ✘ L'U.S.D. Tegoleto · La Polisportiva Albergo Oliveto · La Pro Loco di Civitella  
   _La Sagra della Pesca, dedicata al frutto, è organizzata dal Circolo ARCI._ → `feste-e-associazioni.html`
28. [c9416e86] ●●○ `Pv=` **Chi organizza la Festa della Rosa di Viciomaggio?**  
   ✔ L'A.S.D. Viciomaggio · ✘ La parrocchia di San Martino · Il Circolo Paccinelli · Comunità & Tegoleto  
   _La Festa della Rosa, tra fine aprile e inizio maggio, è organizzata dall'A.S.D. Viciomaggio._ → `feste-e-associazioni.html`
29. [98eb66e1] ●●● `Pv+` **Chi organizza la Sagra del Cinghiale di Pieve a Maiano?**  
   ✔ L'U.S. Pieve a Maiano · ✘ La Pro Loco di Civitella · Il Circolo ARCI · Slow Food Valdichiana  
   _La Sagra del Cinghiale è organizzata dall'U.S. Pieve a Maiano._ → `feste-e-associazioni.html`
30. [da689784] ●●○ `Pv=` **Chi organizza la Festa dell'uva, del vino e dell'olio di Ciggiano?**  
   ✔ La Pro Loco di Ciggiano · ✘ La Società Filarmonica · La parrocchia di San Biagio · Il Comune con Slow Food  
   _La festa è organizzata dalla Pro Loco di Ciggiano._ → `feste-e-associazioni.html`
31. [9a5d061a] ●○○ `-n=` **In quale mese si tiene il Mercato del Cacio, nel borgo di Civitella?**  
   ✔ Maggio · ✘ Febbraio · Agosto · Novembre  
   _Il Mercato del Cacio si tiene a maggio ed è organizzato dal Comune con Slow Food._ → `feste-e-associazioni.html`
32. [11601917] ●○○ `-n=` **In quale mese si tiene la Sagra del Crostino di Albergo?**  
   ✔ Luglio · ✘ Marzo · Ottobre · Dicembre  
   _La Sagra del Crostino si tiene a luglio._ → `feste-e-associazioni.html`
33. [4c118d8f] ●●○ `-v=` **Chi organizza il Mercato del Cacio, Calici sotto la Torre e la Fiera del Miele?**  
   ✔ Il Comune con Slow Food Valdichiana · ✘ La Pro Loco di Ciggiano · Il Circolo ARCI · La Polisportiva Albergo Oliveto  
   _Queste manifestazioni sono organizzate dal Comune con Slow Food._ → `feste-e-associazioni.html`
34. [7f7108c7] ●●○ `-v+` **In quale giorno della settimana si tengono le proiezioni di Cinema sotto le Stelle a Tegoleto?**  
   ✔ Il mercoledì · ✘ Il lunedì · Il venerdì · La domenica  
   _Le proiezioni gratuite si tengono il mercoledì sera di luglio in piazza della Chiesa._ → `feste-e-associazioni.html`
35. [f146f2ed] ●●● `Nv+` **Da quale anno si tiene Cinema sotto le Stelle a Tegoleto?**  
   ✔ 2018 · ✘ 2008 · 2022 · 2025  
   _Le proiezioni sono nate nel 2018._ → `feste-e-associazioni.html`
36. [4be5e12f] ●●● `Nn+` **Quale edizione dell'Olio Novo si è tenuta nel 2025?**  
   ✔ La 28ª · ✘ La 5ª · La 50ª · La 100ª  
   _Nel 2025 L'Olio Novo è arrivato alla 28ª edizione._ → `feste-e-associazioni.html`
37. [8f738c40] ●○○ `-d-` **Che cosa sostituisce il cavallo nel Sarapino di Civitella?**  
   ✔ L'Ape, il motocarro · ✘ Un asino · Una bicicletta · Un trattore  
   _Il Sarapino è il Saracino corso con l'Ape al posto del cavallo: il nome unisce «saracino» e «ape»._ → `frazioni/civitella.html`
38. [fa85de56] ●○○ `-n=` **In quale mese si corre il Sarapino a Civitella?**  
   ✔ A giugno · ✘ A settembre · A dicembre · A febbraio, per Carnevale  
   _Il Sarapino si corre a metà giugno in piazza Lazzeri; la Pro Loco indica la seconda domenica, nel 2026 si è corso sabato 13 giugno._ → `frazioni/civitella.html`
39. [ef246798] ●●● `Pv+` **Come si chiama il premio che conquista il rione vincitore del Sarapino?**  
   ✔ Il «Retribuet» · ✘ Il «Palio» · Il «Drappo dei rioni» · La «Lancia d'oro»  
   _I quattro rioni corrono tre carriere ciascuno contro il buratto per conquistare il Retribuet._ → `frazioni/civitella.html`
40. [e65747b8] ●●● `Pv+` **Quale di questi è uno dei quattro rioni che corrono il Sarapino?**  
   ✔ Porta Senese · ✘ Porta Crucifera · Santo Spirito · Sant'Andrea  
   _I rioni del Sarapino sono San Francesco, Porta Aretina, Porta Senese e La Torre._ → `frazioni/civitella.html`
