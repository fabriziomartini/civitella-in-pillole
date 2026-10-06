"""Difficoltà delle domande del quiz, calcolata con una regola esplicita.

Ogni domanda ha un codice di tre caratteri, uno per criterio:

1. Che cosa chiede la domanda
   N = un anno, una data o un numero preciso            +2
   P = un nome proprio poco noto (persona, ente, opera)  +1
   - = un luogo, un fatto o un concetto                   0
2. Come sono le risposte sbagliate
   v = vicine alla giusta (anni vicini, nomi dello stesso tipo e plausibili)   +1
   n = normali                                                                  0
   d = almeno una si scarta subito                                             -1
3. Quanto è noto il fatto
   + = dettaglio, citato di passaggio in una pagina      +1
   = = normale                                            0
   - = celebre o in evidenza sul sito                     -1

Somma: 0 o meno = facile (1), 1-2 = media (2), 3 o più = difficile (3).

Chiave: id della domanda (le prime 8 cifre dell'MD5 del testo, vedi tools/genera_quiz.py).
Se si riformula una domanda cambia il suo id: va aggiornato anche qui (genera_quiz.py lo segnala).

DATI raccoglie i livelli ricavati dalle statistiche reali del foglio Google
(vedi tools/calibra_difficolta.py): quando una domanda ha abbastanza risposte, il suo livello
viene da lì e prevale sul codice.
"""

PUNTI = [{"N": 2, "P": 1, "-": 0}, {"v": 1, "n": 0, "d": -1}, {"+": 1, "=": 0, "-": -1}]


def livello(codice):
    somma = sum(PUNTI[i][codice[i]] for i in range(3))
    return 1 if somma <= 0 else 2 if somma <= 2 else 3


# Livelli dalle statistiche reali (id: livello). Generato da tools/calibra_difficolta.py.
DATI = {}

CODICI = {
    "5a86694d": "Nv=",  # Quanti residenti contava il comune al censimento ISTAT del 2021?
    "ebc792a8": "-v=",  # Qual è il centro abitato più popoloso del comune?
    "eec92ec8": "-v=",  # Quale centro è il secondo per numero di abitanti, dopo Pieve al Toppo?
    "3224d171": "Nn=",  # Quanto è esteso, all'incirca, il territorio comunale?
    "e4b714c5": "-n=",  # Dove si trova Civitella in Val di Chiana rispetto ad Arezzo?
    "b23a93db": "-v=",  # Con quale di questi comuni confina Civitella in Val di Chiana?
    "e3946457": "-v=",  # Quale di questi comuni NON confina con Civitella in Val di Chiana?
    "4746e93c": "Pd=",  # Su quali colline sorge il capoluogo storico, secondo Wikipedia e Tosca
    "f2064462": "Pd-",  # Tra quali valli si trova il colle di Civitella?
    "75a8fc8f": "Pd=",  # Quale di questi torrenti scorre nel territorio comunale?
    "e2f25241": "Pn=",  # Una parte del territorio comunale rientra in quale riserva naturale?
    "e65e12bd": "-d-",  # Quale fiume protegge la Riserva naturale di Ponte a Buriano e Penna?
    "96d34023": "-v+",  # Quale frazione il Piano Strutturale indica come «porta d'accesso» meri
    "1a05018c": "Pd=",  # Quale vino si produce sulle colline del comune?
    "607cb6d7": "-d=",  # Come sono sistemati, tradizionalmente, gli oliveti sui pendii collinar
    "878f8be1": "Nn+",  # Circa quanti abitanti del comune vivono in case sparse, fuori dai cent
    "b051cf1f": "-v=",  # Quale frazione è divisa tra Civitella e il comune di Laterina Pergine 
    "7a620330": "Pn+",  # Con quale comune tedesco è gemellato Civitella in Val di Chiana?
    "608e57f8": "Nn=",  # Da quando Civitella fa parte della rete Cittaslow?
    "f5a0d8d3": "Nn+",  # In quale anno Civitella è entrata nell'associazione Città dell'Olio?
    "db28ef0d": "-d-",  # Che cosa era il colle di Civitella in epoca longobarda?
    "3dd6026e": "Pv=",  # Quale vescovo di Arezzo scelse nel 1248 la rocca di Civitella come pro
    "d6478a7e": "-d+",  # Che aspetto aveva la rocca di Civitella nel 1182, secondo il Repertori
    "2fd2d624": "Nv=",  # In quale anno Firenze fece di Civitella il capoluogo di una propria po
    "edd96569": "Pv=",  # Da quale podesteria fu staccata Civitella nel 1385?
    "b9e45476": "Nv=",  # Fino a quale anno durò la podesteria di Civitella?
    "77748394": "Nv=",  # In quale anno le comunità di Ciggiano, Viciomaggio e Badia al Pino e i
    "b929883a": "Nv-",  # In quale anno la sede comunale fu trasferita da Civitella a Badia al P
    "4ffa7202": "-d=",  # Perché nel 1917 la sede comunale fu trasferita a Badia al Pino?
    "32504015": "Nv-",  # In quale anno fu combattuta la battaglia di Pieve al Toppo?
    "1e4dc6a7": "-v=",  # Chi vinse la battaglia di Pieve al Toppo del 1288?
    "571968bf": "Pn-",  # Quale poeta ricorda la battaglia di Pieve al Toppo come le «giostre de
    "1230b87b": "Nv+",  # In quale canto dell'Inferno Dante ricorda le «giostre del Toppo»?
    "a95227b3": "Pv+",  # Quale personaggio, caduto nella battaglia di Pieve al Toppo, compare n
    "224669b9": "-d-",  # Che cosa distrusse la rocca di Civitella durante la seconda guerra mon
    "fb55e686": "Nv=",  # In quale anno a Villa Oliveto fu istituito un campo di internamento?
    "b5f15efd": "-n=",  # Chi era internato soprattutto nel campo di Villa Oliveto?
    "71ecaade": "Pv=",  # Dove furono deportate nel 1944 le famiglie internate a Villa Oliveto?
    "bebf7d33": "-v=",  # Da quale espressione latina deriva il nome di Viciomaggio?
    "26c46d87": "-n=",  # Di quale origine è, quasi sicuramente, il toponimo «Toppo»?
    "d150c402": "-n=",  # Da che cosa deriva il nome «Maiano»?
    "bb0a87e4": "-d=",  # Da che cosa prende il nome Tribbio?
    "3e37b695": "Nv-",  # In quale data avvenne la strage nazista di Civitella?
    "75f82986": "Pv=",  # Quale festa si celebrava a Civitella il giorno della strage del 1944?
    "3440c37a": "-v=",  # Quale di queste località NON fu colpita dalla strage del 29 giugno 194
    "e98abd07": "Pv=",  # Quale reparto tedesco compì le stragi del 29 giugno 1944?
    "ae2d129c": "-v=",  # Di quale comune fa parte San Pancrazio, colpito dalla strage del 1944?
    "d650b33d": "-v=",  # Dove arriva la Marcia per la pace che parte da Civitella?
    "76c00bc0": "-v=",  # Con quale comune è organizzata la Marcia per la pace?
    "ab4e24ee": "Pd=",  # Quale associazione ha allestito la Sala della Memoria a Civitella?
    "7461cfc3": "Pd=",  # Come si chiama il monumento sul muro accanto alla chiesa di Civitella?
    "471dce11": "Nv=",  # In quale anno fu realizzato il portale in bronzo di Bino Bini per la c
    "b6c6fc75": "Nv+",  # In quale data le SS fucilarono a Ciggiano i partigiani Marmo e Marapit
    "9b2fcfcf": "Nv+",  # In quale anno fu eretto il cippo dell'eccidio di Cornia?
    "9677ff56": "Nn+",  # Quanti nomi riporta la lastra dei martiri di Cornia?
    "24c8d8bd": "-n+",  # Chi era Giovanni Cau, catturato a Gebbia nel 1944?
    "a6b8c90b": "-v-",  # In quale frazione ha sede il Comune?
    "3f92e789": "Pv=",  # A quali santi era dedicata l'antica abbazia del Pino?
    "0542f44e": "Pv=",  # Qual è il titolo della parrocchia di Badia al Pino?
    "e6beb218": "Pv+",  # Quale santo è titolare delle parrocchie sia di Ciggiano sia di Tegolet
    "a36520a9": "Pv+",  # Quale santo è titolare delle parrocchie sia di Spoiano sia di Pieve al
    "120e1846": "Pv=",  # A quale santo è dedicata la parrocchia di Viciomaggio?
    "f2907c6a": "Pv=",  # A quale santo è dedicata la parrocchia di Oliveto?
    "080e4e41": "Nn+",  # In quale anno è già attestato Tuori, secondo il Repertorio?
    "c686859b": "Nn+",  # In quale anno fu progettata la moderna chiesa parrocchiale di Pieve al
    "c2c65bab": "Nn+",  # In quale anno la chiesa di San Biagio a Ciggiano fu elevata a pieve?
    "b555e58c": "Pv=",  # A quale scultore è attribuita la Santa Maria Maddalena della chiesa di
    "d971761e": "-v=",  # In quale frazione si trova la chiesa della Madonna della Costarella, t
    "8d375aa0": "-v+",  # Quale borgo collinare si trova a circa 360 metri, su un colle tra le v
    "264f4207": "-n=",  # Quale attività artigianale esisteva un tempo a Cornia?
    "7460edf6": "Pn=",  # A quale santo è dedicata la chiesa di Cornia, detta di Sant'Angelo?
    "c1b2389e": "-v+",  # Quale frazione è la più alta tra queste, a circa 560 metri?
    "d02d06cf": "Pv=",  # Di quale famiglia fu dimora Villa Oliveto, già Villa Mazzi?
    "782eea04": "Pd-",  # Quale scrittrice scozzese visse a Oliveto ed è sepolta nel suo cimiter
    "f98ae568": "Pd-",  # Quale romanzo ha scritto Muriel Spark, che visse a Oliveto?
    "ae843126": "Nn=",  # In quale anno Muriel Spark ricevette la cittadinanza onoraria di Civit
    "4570545d": "Nn+",  # Da quale anno si tiene il Presepe Vivente di Oliveto?
    "605f6a96": "-d=",  # Dove è allestita la Natività del Presepe Vivente di Oliveto?
    "8c3a7f97": "-d=",  # Che cosa è stato trovato al Podere Casella, presso Pieve a Maiano?
    "f229085c": "Pv+",  # Di quale imperatore è la moneta d'oro trovata a Pieve a Maiano?
    "9ed31f21": "-v=",  # Vicino a quale frazione si trova il podere Spedaluccio?
    "91b7689b": "-d=",  # Che cosa si produceva nelle fornaci romane di località I Ponti, a Piev
    "ac4c5d0d": "Nn=",  # Da quale anno Ponticino ha una stazione ferroviaria?
    "21a4f930": "-n=",  # Su quale linea ferroviaria si trova la stazione di Ponticino?
    "1938aa25": "Nn+",  # In quale anno un referendum approvò la fusione tra Laterina e Pergine 
    "b126f10e": "-v=",  # Con quali comuni Civitella si divideva Ponticino prima del 2018?
    "86a6174e": "Pv=",  # Quale villa settecentesca si trova a Spoiano?
    "d00da1ec": "-n+",  # Che cosa divenne Villa Pecchioli, a Spoiano, nel 1928?
    "bd1eb40f": "-v+",  # Quale paese è al centro del libro «Un uomo dabbene per davvero» di Giu
    "e7c2c418": "-v=",  # Chi ricostruì la torre di Tegoleto alla fine del Trecento?
    "1086aa45": "Pv+",  # A quale ordine passò la fattoria di Tegoleto nel 1783?
    "3e486f3c": "Nn=",  # In quale anno nacque il Teatro Moderno di Tegoleto?
    "91b9c111": "Pn=",  # Chi gestisce il Teatro Moderno di Tegoleto?
    "7c7d8c24": "Nn=",  # In quale anno a Tegoleto arrivò una tappa del Giro d'Italia?
    "c1817196": "Pv=",  # Chi vinse la tappa del Giro d'Italia arrivata a Tegoleto nel 2004?
    "d7a4e134": "Nn+",  # In quale anno fu trovata a Viciomaggio un'urna cineraria etrusca con i
    "8b92c31b": "-v=",  # In quale frazione si trova la villa padronale settecentesca con una li
    "1d45bdf1": "Pv=",  # Su quale linea ferroviaria si trova la stazione di Albergo?
    "daf0e244": "-d=",  # Quale strada romana passava da Albergo, secondo l'itinerario del Comun
    "cc15f4f6": "-v=",  # A quale ordine religioso apparteneva il priorato da cui nacque la chie
    "2a3e555c": "Nn=",  # In quale anno fu completata in stile romanico la chiesa di Santa Maria
    "bdcb792b": "Nn+",  # Quanti archi ha il portico del Palazzo Pretorio di Civitella?
    "dedef337": "-n=",  # Per quale scopo il notaio Becattini lasciò il suo palazzo alla Confrat
    "8a7414cd": "Nn+",  # Da quale anno Palazzo Becattini è di proprietà del Comune?
    "4881de19": "Pd=",  # In quale piazza di Civitella si trova la cisterna medievale?
    "584e621e": "Pv+",  # A quale ente apparteneva il Saracino, la casa colonica cinquecentesca 
    "cd56501b": "-d=",  # Per che cosa era noto il luogo di Matroia?
    "e4363716": "-d+",  # Che cosa c'è oggi a Matroia, secondo il Piano Strutturale?
    "dbcd5fc3": "-v=",  # Dove si trova oggi la campana del 1358 proveniente da Montoto?
    "0ea02fda": "Nv=",  # In quale anno il castello di Montoto passò a Firenze?
    "ba3dff5e": "-d=",  # Che cosa resta sulla cima di Poggio Castellare?
    "f06a2f2d": "-n=",  # Da che cosa deriva il nome di Montarfoni?
    "d9e63c28": "-d=",  # Che cosa conserva oggi Montarfoni, oltre alla villa seicentesca?
    "5356e1c0": "Pv+",  # A chi appartenne Dorna a partire dal 1814?
    "144d50be": "Pv+",  # A chi è dedicata l'attuale chiesa di San Martino in Poggio?
    "b4f36db1": "Pv+",  # Grazie al patrimonio di chi fu costruita la chiesa dei Santi Maria e C
    "d3a07030": "-n=",  # Come descrissero i fiorentini il castello di Gaenne, passato sotto il 
    "0aeb1238": "Pv=",  # A chi apparteneva il castello di Gaenne nel 1069?
    "b8b3b4f1": "-v=",  # Tra quali frazioni si trova la località Le Caserosse?
    "e4fa556c": "Pv+",  # In quale materiale è il cippo romano trovato a Le Fosse?
    "fbceb884": "-d-",  # Che cosa produce l'azienda CEIA di Viciomaggio?
    "84695b7e": "Nv=",  # In quale anno fu costituita la società CEIA?
    "da81be25": "-v=",  # Per quale industria CEIA brevettò nel 1962 i suoi primi metal detector
    "d00c385a": "-d=",  # Dal 1975 CEIA produce metal detector per quale settore?
    "4fbe35df": "-d=",  # Di che cosa si occupa Chimet?
    "ec632da2": "Nv=",  # In quale anno fu fondata Chimet?
    "15d7a73c": "-v=",  # Dove aprì Chimet il suo primo stabilimento, nel 1976?
    "aaba5c69": "-d-",  # Che cosa produceva l'azienda Del Tongo di Tegoleto?
    "4825255e": "Nv=",  # In quale anno fu fondata la Del Tongo?
    "51f555d3": "Nn=",  # In quale anno fallì la Del Tongo?
    "005b6b8c": "Pv+",  # Quale azienda acquisì nel 2022 il marchio Del Tongo?
    "6355b329": "Nv+",  # In quali anni fu attiva la squadra ciclistica professionistica Del Ton
    "92e0687d": "Pv=",  # Con quale corridore la squadra Del Tongo vinse il Giro d'Italia del 19
    "6c2a3e07": "Pv+",  # Con quale corridore la squadra Del Tongo vinse il Giro d'Italia del 19
    "fbd430a4": "Pv=",  # Quale celebre velocista esordì tra i professionisti con la maglia Del 
    "5ea5e45a": "Pv=",  # Quale di queste è una varietà tradizionale di olivo del territorio?
    "a04d9971": "Pd=",  # A quale Strada del Vino appartiene il Comune di Civitella?
    "92190992": "-v=",  # Dove ha sede la condotta Slow Food Valdichiana?
    "fd5f1067": "Pn=",  # Come si chiama il progetto di educazione alimentare che Slow Food port
    "d16bdeb0": "-v=",  # In quale frazione si tiene la Sagra della Bistecca?
    "3116bcad": "Pv+",  # Chi organizza la Sagra della Bistecca?
    "f0be8eb1": "-v=",  # In quale frazione si tiene la Sagra del Crostino?
    "4422dd68": "Pv+",  # Chi organizza la Sagra del Crostino di Albergo?
    "2d7782fe": "-v=",  # In quale frazione si tiene la Sagra dei Baccelli?
    "b7b8833c": "-n=",  # In quale mese si tiene la Sagra dei Baccelli?
    "35bf8000": "-v=",  # In quale frazione si tiene la Sagra del Cinghiale?
    "18b90576": "-v=",  # In quale frazione si tiene la Festa dell'uva, del vino e dell'olio?
    "e1d94892": "Nn+",  # Quale edizione della Festa dell'uva di Ciggiano si è tenuta nel 2026?
    "3102235c": "-d=",  # A che cosa è dedicata la Sagra della Pesca di Pieve al Toppo?
    "642f3ac8": "-n=",  # Quando si tiene la Fiera del Miele di Pieve al Toppo?
    "3a131b5f": "-v=",  # In quale frazione si tiene la Fiera del Miele?
    "f220d5ea": "-v=",  # Dove si tiene il Mercato del Cacio?
    "beec873c": "-d=",  # Che cosa si degusta a Calici sotto la Torre?
    "2e7141f4": "-v=",  # In quale frazione si tiene la Festa della Rosa?
    "23617f63": "-v=",  # In quale frazione si tiene il RioFest?
    "8e949863": "Nv+",  # In quale anno si è tenuta la prima edizione del RioFest?
    "260bd43e": "Pv=",  # Quale associazione organizza il RioFest e Cinema sotto le Stelle?
    "253c5d99": "-n=",  # Dove si svolgono le proiezioni di Cinema sotto le Stelle?
    "4a402844": "-v=",  # In quale frazione si tiene il Mercato dei Sapori e della Terra?
    "044286f0": "-n=",  # In quale periodo si tiene la rassegna L'Olio Novo?
    "20356cbe": "-v=",  # In quale frazione si tiene il Presepe Vivente?
    "87a41003": "Pv+",  # Chi organizza la Festa al Tegoleto?
    "2f520af4": "-v=",  # In quale frazione ha sede la Società Filarmonica, la banda del paese?
    "410b1cb5": "Nn=",  # In quale anno il titolo di pieve e il fonte battesimale passarono dall
    "c87b3b73": "Nn+",  # In quale anno fu soppressa la Badia del Pino?
    "7a384985": "Nn=",  # In quale anno furono distrutti la pieve e l'ospedale per i pellegrini 
    "cb2abf6f": "Pd=",  # Sotto quali valichi si trova Ciggiano, che ne fecero un nodo strategic
    "96a6f855": "-n=",  # Che cos'era la «calla» che i pastori facevano a Ciggiano?
    "523cea0b": "Pv+",  # Le truppe di quale condottiero assediarono e saccheggiarono Ciggiano n
    "01491e5c": "Pv=",  # Quale granduca soppresse nel 1783 la Compagnia di Santa Croce di Ciggi
    "f4c98a78": "Pv+",  # Quali famiglie, tornate proprietarie del feudo, riedificarono nel Seic
    "4fcbea87": "-d+",  # Che cosa diventò all'inizio dell'Ottocento la piazza d'armi del castel
    "8bc58b2b": "-v+",  # In quale frazione si trova Palazzo Santini-Paccinelli, villa settecent
    "19907f55": "-n=",  # Quale reliquia custodisce la chiesa della Compagnia di Santa Croce a C
    "43d14c27": "Pv+",  # Quale pittore dipinse la Madonna del Rosario conservata nella chiesa d
    "b4c51f53": "Nn=",  # In quale anno Villa Oliveto fu ceduta al Comune di Civitella?
    "4bfffd85": "Pn+",  # Chi fuse nel 1358 la campana oggi nel campanile della chiesa di Pieve 
    "1f3abaaa": "-n=",  # Che cos'era anticamente il podere Spedaluccio, vicino a Pieve a Maiano
    "21e2abd1": "Nn+",  # Da quale anno è documentato l'antico ospizio dello Spedaluccio?
    "388b792d": "-n=",  # Su che cosa sorge l'Oratorio della Madonna del Conforto a Pieve al Top
    "0ff18981": "-d=",  # Che cos'era all'inizio, nel 1960, il Teatro Moderno di Tegoleto?
    "c5767706": "-n+",  # Che cosa c'è nel recinto d'accesso al Palatium-torre della Rocca di Ci
    "99db94ce": "Pn=",  # Quale via medievale transitava da Albergo?
    "a6b92165": "-d=",  # Quale bene è tutelato da vincolo nazionale a Badia al Pino?
    "dad49b73": "-d=",  # Che cosa raccoglie la Sala della Memoria allestita a Civitella dall'as
    "38fd6d61": "-d+",  # Che cosa è stato trovato nel 2004 in località La Cascinella, presso Ci
    "c7eef4ea": "-d+",  # Secondo Visit Tuscany, che cosa è stato trovato nella chiesa di San Pi
    "eab967e7": "Nd+",  # Fino a che spessore arrivano i muri del Castellare di Sant'Angelo, pre
    "1526724b": "Pn+",  # Su segnalazione di chi furono scoperte le fornaci romane in località I
    "5b8c6dd0": "-n+",  # Quale reperto da Viciomaggio è conservato al Museo Archeologico Nazion
    "dc640362": "-d=",  # Che cosa prevede il Piano Strutturale per l'area di Cornia?
    "20b4867a": "-d=",  # Tra quali località si estende il tratto dell'Arno protetto dalla Riser
    "848435e4": "Nd=",  # Tra quali quote si trovano i centri abitati del comune, secondo Cittas
    "4298beed": "-v-",  # La pianura del comune è la parte settentrionale di quale valle?
    "a852afc3": "Pd=",  # Quale di questi è uno dei torrenti principali del comune, insieme a Es
    "4d63ebae": "Nn+",  # Quanti residenti contava Pieve al Toppo, il centro più popoloso del co
    "52faadf9": "-v+",  # Quale centro è il terzo per numero di abitanti, dopo Pieve al Toppo e 
    "729c801a": "Nv+",  # Quanti residenti contava il borgo di Civitella, il capoluogo storico, 
    "2a6d43b8": "-v+",  # Quale di queste località era la meno popolosa al censimento del 2021?
    "dc924e7d": "-v+",  # Quale frazione contava circa 950 residenti al censimento del 2021?
    "3589ff26": "-v+",  # Di quale epoca sono gli strumenti in pietra trovati al Podere Casella,
    "414fd435": "-v+",  # Dove è stato individuato un insediamento romano del I-II secolo d.C. a
    "e19b1b46": "Pv+",  # In quale località di Pieve a Maiano c'era una fornace romana?
    "aae10fe5": "-n+",  # Quale ritrovamento attesta l'origine romana di Spoiano?
    "3b033cf0": "Pv+",  # A quale epoca risale l'urna etrusca con iscrizione trovata a Viciomagg
    "1ab2c013": "Pd=",  # Di quale catena collinare è una propaggine la zona collinare del comun
    "7a62a739": "Nv+",  # In quale giorno fu combattuta la battaglia di Pieve al Toppo del 1288?
    "18947b6d": "-v=",  # Di quale parte erano i senesi sconfitti al Toppo nel 1288?
    "4497e778": "-d=",  # In quali epoche fu frequentato il colle di Civitella, prima di diventa
    "4c4023b6": "Pv=",  # A presidio di chi sorgevano, dall'XI secolo, le strutture sul colle di
    "6869ff95": "Pv-",  # Quale città acquisì Arezzo e il suo contado prima di fare di Civitella
    "cf547452": "Pv+",  # Quale castello fu aggregato alla Comunità di Civitella nel 1774, insie
    "6a7032b1": "Nv+",  # In quale anno Ciggiano subì un altro assedio, dopo il saccheggio di Ni
    "5ff357cf": "Pv+",  # Quale altro titolo, oltre a quello di pieve, passò a Badia al Pino nel
    "d1c40d05": "Nv+",  # In quale anno un documento chiama l'abbazia «Badia di S. Martino e S. 
    "572b6b97": "-n=",  # Che cosa c'era accanto all'antica pieve del Toppo?
    "7d7a33f9": "Pv+",  # A chi apparteneva anticamente la pieve del Toppo, con il suo ospedale 
    "3fa9492f": "Nv+",  # In quale mese del 1940 fu istituito il campo di internamento di Villa 
    "4dc5acd4": "Pv+",  # Quale reparto operò a Gebbia il 29 giugno 1944, insieme alla divisione
    "5c286059": "-n+",  # Secondo l'Archivio della Memoria, che cosa uccisero i tedeschi a Gebbi
    "7ec5aac3": "-v+",  # Dove furono fucilati gli uomini presi a Gebbia, secondo l'Archivio del
    "15cc1db8": "Nv+",  # In quale giorno furono uccisi Giovanni Cau e la moglie Helga Elmqvist,
    "320d4828": "Nv+",  # Fino a quale giorno arrivano le morti ricordate dalla lastra dei marti
    "e6acc20f": "Pv+",  # Chi fucilò a Ciggiano, il 16 aprile 1944, i partigiani Giovanni Marmo 
    "5b3d98f6": "Pv=",  # Quale luogo della memoria si trova a Civitella, oltre alla «Pietà del 
    "d69a35d2": "-v+",  # Dove si rifugiavano durante la guerra gli abitanti di Viciomaggio?
    "f6883e41": "-n+",  # Chi era Hazbi Ismail, tra le vittime elencate dall'Atlante per «Cornia
    "cdce2f79": "-d=",  # Che cosa ricorda il portale in bronzo di Bino Bini nella chiesa di Civ
    "855aa29c": "-d=",  # Che cosa prevede il Piano Strutturale per la Rocca di Civitella?
    "5290f03d": "-v+",  # Quali stemmi si vedono sul Palazzo Pretorio di Civitella?
    "77e1c3f5": "Nn+",  # In quale anno morì il notaio Becattini, che lasciò il suo palazzo per 
    "fd831df6": "Pv+",  # Quali oratori si trovano nel borgo di Civitella?
    "608aba01": "-n+",  # Quale bene storico di Albergo è censito nel Repertorio del Piano Strut
    "e6917851": "-n=",  # Che cosa ospita oggi il palazzetto settecentesco di Badia al Pino, sed
    "c435203b": "Nv+",  # In quale anno fu inaugurato il monumento ai caduti nel piazzale della 
    "d3fdc7c5": "-v+",  # Che cosa caratterizza Villa del Bosco, a Badia al Pino?
    "7c31e8d6": "Pv+",  # A quali santi è dedicata la chiesa di San Bartolomeo a Badia al Pino?
    "f996bc77": "Pv+",  # Quale altare custodisce la chiesa di San Biagio a Ciggiano?
    "2c5801d3": "-v+",  # Di quale secolo è il loggiato della chiesa della Madonna della Costare
    "48e6e4b6": "Nv+",  # In quale anno la chiesa di San Pietro a Ciggiano ebbe l'intervento che
    "eccf0f3a": "-v+",  # In quali registri compare già nel 1274 la chiesa di Sant'Angelo a Corn
    "d4b4fda3": "Nv+",  # In quale anno fu ricostruita la chiesa di San Giovanni d'Oliveto?
    "2c46b6c8": "-d+",  # Che cos'era in origine l'Oratorio di San Rocco, a Oliveto?
    "0c33c206": "Nv+",  # Attorno a quale anno fu rifatta la Cappella della Compagnia di Oliveto
    "49446c6c": "-d=",  # Di quali alberi è ricco il parco di Villa Oliveto?
    "498b0966": "Nv=",  # In quale anno morì Muriel Spark, che visse a Oliveto?
    "3bd4c74d": "Nv+",  # In quale anno fu ampliata la chiesa di Santa Maria Assunta a Pieve a M
    "91087b87": "Pv=",  # Qual è il titolo della parrocchia di Pieve a Maiano?
    "253e4dff": "Nn+",  # Da quale anno l'oratorio di Pieve al Toppo è dedicato alla Madonna del
    "974228d6": "-v+",  # Qual è l'unico bene storico di Ponticino censito dal Repertorio del Pi
    "d9d80f19": "-v+",  # In quale comune ha sede la parrocchia dei Santi Iacopo e Cristoforo di
    "3d4a15ba": "-v+",  # Quale elemento caratterizza Villa Pecchioli, a Spoiano?
    "99f5bb0f": "-n+",  # In quale periodo dell'anno si tiene la stagione del Teatro Moderno di 
    "2f350987": "Nv+",  # Quale tappa del Giro d'Italia 2004 arrivò a Tegoleto?
    "13de9716": "Pv=",  # Davanti a quale stabilimento si concluse la tappa del Giro d'Italia ar
    "ced4fecf": "-v+",  # Su quali beni di Tuori c'è un vincolo nazionale?
    "8288be8c": "-v+",  # Com'è fatto il portico del Saracino, presso Tuori?
    "b72de4ff": "Nv+",  # In quale anno fu restaurata, con decorazioni pittoriche, la parte post
    "20485c5d": "-n+",  # Su che cosa sorsero i poderi di Montoto, lungo via della Centrale?
    "2bad47c2": "Pv+",  # A quale santo è dedicata la chiesetta di Matroia?
    "99c66c9f": "-n+",  # Che cosa si conserva a Tribbio, oltre al nome che ricorda un antico tr
    "7551f5ac": "-n=",  # Quando furono abbandonati i borghi medievali di Malpertuso e Le Fosse?
    "d2a0a62f": "-v=",  # Di quale origine è il castello di Dorna?
    "a8e3eb8d": "Pv+",  # Come è chiamata Dorna in un documento del 1181?
    "e5f0dee8": "Pv+",  # A quali santi era dedicata la chiesa documentata a Dorna nel 1182?
    "534d8c16": "Pv+",  # A quale famiglia passò il castello di Gaenne dopo i longobardi di Dorn
    "0574409f": "Nv+",  # Da quale anno San Martino in Poggio è parrocchia?
    "a085dfa8": "Nd+",  # A che altitudine si trova, all'incirca, San Martino in Poggio?
    "e834399c": "Nd+",  # Quanto è lunga, all'incirca, la cinta muraria a secco di Poggio Castel
    "27480726": "Pn=",  # Chi fondò nel 1954 la Del Tongo?
    "ef327bd3": "Pv+",  # Quale classica del ciclismo vinse la squadra Del Tongo nel 1983?
    "b2e17c50": "Nn+",  # Quante tappe del Giro d'Italia vinse la squadra ciclistica Del Tongo?
    "8ee7c334": "-v+",  # Dove aprì Chimet il suo secondo stabilimento, negli anni Ottanta?
    "d8488735": "Pd=",  # Quali varietà di olivo sono tipiche del territorio, insieme al moraiol
    "8cac38d7": "Pv=",  # Quale indicazione geografica ha l'olio extravergine del territorio?
    "daf78ce6": "Pv=",  # Chi organizza la Sagra dei Baccelli di Spoiano?
    "c3556ffe": "Nn+",  # Quale edizione della Sagra dei Baccelli si è tenuta nel 2025?
    "eb4598d2": "Pv=",  # Chi organizza la Sagra della Pesca di Pieve al Toppo?
    "c9416e86": "Pv=",  # Chi organizza la Festa della Rosa di Viciomaggio?
    "98eb66e1": "Pv+",  # Chi organizza la Sagra del Cinghiale di Pieve a Maiano?
    "da689784": "Pv=",  # Chi organizza la Festa dell'uva, del vino e dell'olio di Ciggiano?
    "9a5d061a": "-n=",  # In quale mese si tiene il Mercato del Cacio, nel borgo di Civitella?
    "11601917": "-n=",  # In quale mese si tiene la Sagra del Crostino di Albergo?
    "4c118d8f": "-v=",  # Chi organizza il Mercato del Cacio, Calici sotto la Torre e la Fiera d
    "7f7108c7": "-v+",  # In quale giorno della settimana si tengono le proiezioni di Cinema sot
    "f146f2ed": "Nv+",  # Da quale anno si tiene Cinema sotto le Stelle a Tegoleto?
    "4be5e12f": "Nn+",  # Quale edizione dell'Olio Novo si è tenuta nel 2025?
    "748416c9": "-v=",  # Da chi fu assediata la rocca di Civitella tra il 1284 e il 1285?
    "4fe3b32c": "Nv+",  # Quanti piccoli comuni furono aggregati alla Comunità di Civitella nel 
    "67e04d32": "-n=",  # Perché la rocca di Civitella fu bombardata dagli Alleati?
    "1af9c0f0": "Nd+",  # Quanto è spessa, all'incirca, la cinta muraria a secco di Poggio Caste
    "6762121d": "-v+",  # Per curare quali malati si attingeva l'acqua della sorgente di Matroia
    "191e897a": "-n+",  # Dove si trova oggi il mulino di Montoto?
    "de37df18": "-n+",  # Che cosa è stato trovato a Le Fosse, oltre a un cippo romano in traver
    "ff1c509f": "-d+",  # Che cosa prevede il Piano Strutturale per il borgo-fattoria e la villa
    "2e9fd6ab": "-v+",  # Di che cosa fu dotata la chiesa di San Martino in Poggio quando fu amp
    "8624b548": "-v=",  # Quale di questi luoghi, insieme a Poggio Castellare, è previsto come p
    "d46d4a3e": "-n+",  # Come morì Mario Mannelli, ricordato da un monumento a Viciomaggio?
    "dc8e4d56": "Pv+",  # Quale Madonna era venerata a Matroia, legata al culto delle acque?
    "1a6af485": "Pv+",  # Sopra quale strada sorse il castello di Montarfoni?
    "396551e5": "Pv+",  # Di quale bottega è la Madonna con il Bambino del 1522 nel tabernacolo 
    "34e88f74": "-n=",  # Chi era don Alcide Lazzeri, ucciso il 29 giugno 1944?
    "68125a92": "-v+",  # Quale incarico aveva Guido Mammoli, ucciso nell'eccidio del 29 giugno 
    "0b47361b": "-v=",  # Quale onorificenza ricevette nel 1963 la comunità di Civitella?
    "f1973bd5": "-d=",  # A chi è intitolata la piazza centrale di Civitella?
    "53ade602": "Pv+",  # Come si chiamava la formazione partigiana che il 18 giugno 1944 tese u
    "6060fc7e": "Pv+",  # Verso quale località furono spinte le donne e i bambini di Civitella i
    "c840099b": "Pv+",  # Quale tribunale condannò all'ergastolo, nel 2006, il sergente tedesco 
    "3ff855bb": "Pv+",  # Da quale vicariato dipendeva Civitella sotto i granduchi di Toscana?
    "2dab9df8": "-v=",  # Secondo il piano paesaggistico regionale, il monte di Civitella segna 
    "cb9f19ff": "-d=",  # Da che cosa deriva la pianura della Val di Chiana?
    "1447e0cc": "-d=",  # Che cosa raccoglie la Pinacoteca di Civitella?
    "8f738c40": "-d-",  # Che cosa sostituisce il cavallo nel Sarapino di Civitella?
    "fa85de56": "-n=",  # In quale mese si corre il Sarapino a Civitella?
    "ef246798": "Pv+",  # Come si chiama il premio che conquista il rione vincitore del Sarapino
    "37978868": "Pv+",  # Quale podestà di Arezzo assediò e rase al suolo Civitella nel 1252, se
    "fd4ef637": "-d=",  # Quale di questi comuni fu soppresso e unito a Civitella nel 1774?
    "274cd667": "-d=",  # Con quale nome fu ribattezzata Civitella quando, nell'XI secolo, passò
    "8885f433": "Nn+",  # In quale anno fu firmata a Civitella la «Pace di Civitella», secondo l
    "e65747b8": "Pv+",  # Quale di questi è uno dei quattro rioni che corrono il Sarapino?
    "f6ac606f": "Pv=",  # Quale porta di Civitella fu distrutta dalle bombe nel 1944?
    "e8da5b98": "Pv+",  # A chi donarono Palazzo Ninci i suoi proprietari nel 1917?
    "ccfe4a64": "Nv+",  # In quale giorno del 1774 fu emanato il provvedimento che assegnò nove 
    "42c23bec": "Pv+",  # Secondo il Repetti, quale comune con il riordino del 1774 passò alla C
    "41b02c31": "Pv=",  # Chi difese Civitella nel 1554 dall'assalto delle truppe senesi di Pier
    "7f8563ab": "Nv+",  # Quanti abitanti contava la Comunità di Civitella nel 1833, secondo il 
    "d1b0f93f": "Pv+",  # A quale monastero fiorentino furono incorporate nel 1441 le chiese di 
    "99383471": "-d+",  # Che cosa raffigurava il sigillo dell'antico Comune di Oliveto?
    "84b5459a": "-v+",  # A chi consegnò Azzone degli Ubertini il castello di Oliveto nel settem
    "094fa249": "-n+",  # Che cosa ordinò Firenze nel 1433 per i castelli di Oliveto e Ciggiano,
    "56054fd7": "Pv+",  # Di quale badia era il patronato su Cornia dal secolo XI, secondo il Repetti?
    "a4286437": "Nv+",  # In quale data il popolo di Tegoleto si sottomise alla Repubblica fiore
    "418b0da7": "-v+",  # Chi si accampò a Ciggiano nel 1307, secondo il Repetti?
    "d3c01c7d": "-v+",  # Da quale località vicina doveva distinguersi «Vicione Maggiore», l'ant
    "a4e2efc3": "-v+",  # Che cosa fu firmato il 20 aprile 1261 nella chiesa della Badia al Pino
    "97b3e142": "-d+",  # Che cosa accadeva alle acque della Chiana presso il Toppo nell'XI seco
    "65c7e281": "-v+",  # Con quale nome popolare era chiamata la Pieve al Toppo, secondo il Rep
    "4fc570fa": "Nn+",  # Quante chiese dipendevano dalla pieve del Toppo, secondo il Repetti?
    "84a6f9e7": "-v+",  # A quale Comunità apparteneva Majano nel 1833, secondo il Repetti?
    "845faf36": "Pv+",  # Con quale nome il Repetti chiama la Pieve a Maiano del comune di Civit
    "bf03cb86": "Pv+",  # Da quale espressione latina deriva il nome di Montoto, secondo il Repe
    "42bc1e10": "Pv+",  # A quale monastero di Arezzo fu venduto nel 1051 un quarto del castello
    "3bf8e1f2": "Pv+",  # In quale privilegio del 1356 è ricordato il castello di Gaenne?
    "3cb5660e": "-v+",  # A chi pagava ancora un canone annuo, nell'Ottocento, il proprietario d
    "cc3c0e44": "Nv=",  # In quale anno di censimento il comune ha contato più abitanti?
    "2a62011f": "Nd=",  # Quanti abitanti contava il comune al primo censimento dell'Italia uni
    "60dff0f2": "-n=",  # Come cambiò la popolazione del comune tra il censimento del 1951 e qu
    "ede3b0e0": "Nn=",  # In quale anno fu inaugurata la ferrovia Arezzo–Sinalunga, che ha una 
    "4b7efa1f": "-d+",  # Con quale trazione funzionarono i treni della Arezzo–Sinalunga fin dal
}
