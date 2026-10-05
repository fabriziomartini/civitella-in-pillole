# Fonti da caricare in NotebookLM — verifica dei contenuti del sito

Obiettivo: un notebook di sole fonti autorevoli, con cui verificare ogni affermazione del sito
e correggere errori e allucinazioni. Le fonti sono in ordine di priorità.

**Regola d'uso:** chiedere sempre a NotebookLM le **citazioni testuali** e dire esplicitamente
quando un'informazione *non* è presente nelle fonti. Ciò che non trova riscontro va tolto dal sito
o segnato come non verificato.

---

## ⚡ Blocchi pronti da incollare

In NotebookLM: **+ Aggiungi → Sito web**, poi incollare un blocco intero. I link sono uno per riga
perché NotebookLM separa gli indirizzi con uno spazio o un a capo, non con la virgola. Se un link
dà errore, eliminarlo dalla lista e caricarlo con "Testo copiato".

### Blocco A: sito del Comune
```
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/itinerari/itinerario_1.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/itinerari/itinerario_2.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/itinerari/itinerario_3.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/itinerari/itinerario_4.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_1.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_15.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_23.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_24.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_30.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_31.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_32.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_33.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_34.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_35.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_36.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_37.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_38.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_39.html
https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_40.html
http://www.halleyweb.com/c051016/zf/index.php/servizi-aggiuntivi/index/index/idtesto/71
http://www.halleyweb.com/c051016/zf/index.php/servizi-aggiuntivi/index/index/idtesto/77
```
Nota: `itinerario_1/3/4` e `luogo_30/32/35/37/40` sono indirizzi dedotti dalla numerazione e
non verificati. Se non esistono o non riguardano Civitella e le frazioni, eliminarli dal notebook.

### Blocco B: storia, chiese, beni culturali
```
https://www.treccani.it/enciclopedia/pieve-al-toppo_(Enciclopedia-Dantesca)/
https://diocesi.arezzo.it/chiese-parrocchiali/
https://diocesi.arezzo.it/ciggiano/
http://www.chieseitaliane.chiesacattolica.it/SCHEDA=50726&Chiesa_di_San_Biagio__Ciggiano,_Civitella_in_Val_di_Chiana
http://www.chieseitaliane.chiesacattolica.it/SCHEDA=50716&Chiesa_di_Santa_Maria_Assunta__Civitella_in_Val_di_Chiana
https://catalogo.beniculturali.it/detail/ArchitecturalOrLandscapeHeritage/09iccd_modi_4749768586751
https://catalogo.beniculturali.it/detail/ArchitecturalOrLandscapeHeritage/09iccd_modi_3625118586751
http://dati.san.beniculturali.it/SAN/produttore_SIUSA_san.cat.sogP.61110
http://dati.san.beniculturali.it/SAN/produttore_SIUSA_san.cat.sogP.61101
https://siusa-archivi.cultura.gov.it/cgi-bin/siusa/pagina.pl?TipoPag=cons&Chiave=11220
```

### Blocco C: 1944 e Novecento
```
https://www.archiviodellamemoriacivitellavaldichiana.it/en/i-luoghi-della-strage/
https://www.archiviodellamemoriacivitellavaldichiana.it/gebbia/
https://www.regione.toscana.it/-/villa-oliveto
https://www.storiaememorie.it/villaoliveto/ShedeCampi/VillaOliveto.htm
```

### Blocco D: Wikipedia (solo per il controllo incrociato)
```
https://it.wikipedia.org/wiki/Civitella_in_Val_di_Chiana
https://it.wikipedia.org/wiki/Badia_al_Pino
https://it.wikipedia.org/wiki/Giostre_del_Toppo
https://it.wikipedia.org/wiki/Villa_Oliveto
```

### PDF da scaricare e caricare con "+ Aggiungi → Carica"
Aprire ogni link nel browser, salvare il file e caricarlo. Incollati come "Sito web", i PDF spesso
non vengono letti bene.
```
https://www.straginazifasciste.it/wp-content/uploads/schede/CIVITELLA%20IN%20VAL%20DI%20CHIANA%2029.06.1944.pdf
https://www.straginazifasciste.it/wp-content/uploads/schede/SAN%20PANCRAZIO%20BUCINE%2029.06.1944.pdf
https://diocesi.arezzo.it/wp-content/uploads/sites/2/2022/03/ANNUARIO-PARROCCHIE-2022.pdf
https://cloud.ldpgis.it/sites/civitellavaldichiana/files/ps/b_pieve_al_toppo.pdf
https://cloud.ldpgis.it/civitellavaldichiana/sites/civitellavaldichiana/files/ps/l_viciomaggio.pdf
https://cloud.ldpgis.it/sites/civitellavaldichiana/files/ps/m_tuori.pdf
```
Dal portale https://cloud.ldpgis.it/civitellavaldichiana/ps scaricare anche:
- le Norme Tecniche del PS;
- il Repertorio dei beni di interesse storico;
- le schede degli edifici storici delle altre frazioni.

### Da caricare con "Testo copiato"
Le voci del Repetti (http://www.archeogr.unisi.it/repetti/): Civitella, Oliveto, Ciggiano,
Viciomaggio, Tuori, Badia al Pino, Pieve al Toppo, Tegoleto, Albergo, Cornia, Spoiano. Una voce per
fonte, intitolata "Repetti – voce X".

---

## 1. Fonti istituzionali del Comune (priorità massima)

### Schede "Luoghi" del sito comunale
| Pagina del sito | URL |
|---|---|
| Ciggiano | https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_31.html |
| Pieve al Toppo | https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_33.html |
| Spoiano | https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_34.html |
| Tegoleto | https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_36.html |
| Pieve a Maiano | https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_38.html |
| Viciomaggio | https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_39.html |
| Porta Senese (capoluogo) | https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_24.html |
| Palazzo Ninci (capoluogo) | https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_15.html |
| Scorcio Via della Costarella (capoluogo) | https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_23.html |
| Sede comunale (Badia al Pino) | https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/luoghi/luogo_1.html |

Da cercare a mano nell'elenco *Vivere il comune → Luoghi*: le schede di **Albergo, Badia al Pino,
Cornia, Oliveto, Tuori, Matroia, Ponticino, Gebbia** e del **capoluogo**. La numerazione delle
frazioni sembra stare tra 30 e 40: provare `luogo_30`, `luogo_32`, `luogo_35`, `luogo_37`, `luogo_40`.

### Itinerari del sito comunale
- 2° itinerario, Valdarno–Civitella: https://www.comune.civitella-in-val-di-chiana.ar.it/vivere_il_comune/itinerari/itinerario_2.html
- Gli altri itinerari ("i nuclei di collina", "i nuclei di piano", 3° itinerario): provare `itinerario_1.html`, `itinerario_3.html`, `itinerario_4.html`.

### Vecchio portale comunale (Halleyweb), con pagine descrittive delle frazioni
- Viciomaggio: http://www.halleyweb.com/c051016/zf/index.php/servizi-aggiuntivi/index/index/idtesto/77
- Altra pagina descrittiva: http://www.civichiana.it/c051016/zf/index.php/servizi-aggiuntivi/index/index/idtesto/71
- Le altre frazioni hanno probabilmente `idtesto` vicini (70–80).

## 2. Piano Strutturale e Piano Operativo (fonte tecnica ufficiale)

NotebookLM spesso non importa le pagine del portale GIS: **scaricare i PDF e caricarli come file.**

- Portale del Piano Strutturale (elenco completo degli elaborati): https://cloud.ldpgis.it/civitellavaldichiana/ps
- Norme Tecniche del PS: https://cloud.ldpgis.it/civitellavaldichiana/indice_normativa_ps&normativa=_ps?q=indice_normativa_ps&normativa=_ps&sottoalbero=16&id_variante=1
- **Schedatura degli edifici di impianto storico, un PDF per frazione** (giugno 2015). Esempi:
  - Pieve al Toppo: https://cloud.ldpgis.it/sites/civitellavaldichiana/files/ps/b_pieve_al_toppo.pdf
  - Viciomaggio: https://cloud.ldpgis.it/civitellavaldichiana/sites/civitellavaldichiana/files/ps/l_viciomaggio.pdf
  - Tuori: https://cloud.ldpgis.it/sites/civitellavaldichiana/files/ps/m_tuori.pdf
  - Gli altri (Albergo, Ciggiano, Oliveto, Tegoleto…) hanno la stessa forma `lettera_frazione.pdf`: prenderli dall'elenco del portale PS.
- **Repertorio dei beni di interesse storico, culturale, architettonico, ambientale** (allegato al Quadro conoscitivo): sul portale PS.
- Caratterizzazione funzionale degli insediamenti: https://cloud.ldpgis.it/sites/civitellavaldichiana/files/ps/b8_1_4b_caratterizzazione_funzionale_degli_insediamenti.pdf
- Piano Operativo, relazione illustrativa e NTA: https://cloud.ldpgis.it/civitellavaldichiana/po

## 3. Fonti storiche di riferimento

- **Repetti, *Dizionario geografico fisico storico della Toscana*** (1833–1846). È la fonte storica
  classica per ogni località toscana: ha voci per Civitella, Oliveto, Ciggiano, Viciomaggio, Tuori,
  Badia al Pino, Pieve al Toppo, Tegoleto e altre.
  - Versione online dell'Università di Siena: http://www.archeogr.unisi.it/repetti/
  - PDF dei volumi (Portale Antenati): https://antenati.cultura.gov.it/inventari/Dizionari_storico_geografici/003_Granducato_Toscana/001a_Repetti_1833_t.pdf
  - Consiglio: copiare il testo delle singole voci in un documento e caricare quello, perché i volumi interi sono enormi.
- **SIUSA, archivi storici delle antiche comunità** (date di soppressione, podesterie):
  - Comunità di Viciomaggio: http://dati.san.beniculturali.it/SAN/produttore_SIUSA_san.cat.sogP.61110
  - Comunità di Badia al Pino: http://dati.san.beniculturali.it/SAN/produttore_SIUSA_san.cat.sogP.61101
  - Archivio storico comunale: https://siusa-archivi.cultura.gov.it/cgi-bin/siusa/pagina.pl?TipoPag=cons&Chiave=11220
- **Treccani, Enciclopedia Dantesca, voce "Pieve al Toppo"**: https://www.treccani.it/enciclopedia/pieve-al-toppo_(Enciclopedia-Dantesca)/

## 4. Chiese e beni culturali

- **Diocesi di Arezzo-Cortona-Sansepolcro**, annuario delle parrocchie (titoli ufficiali delle chiese): https://diocesi.arezzo.it/wp-content/uploads/sites/2/2022/03/ANNUARIO-PARROCCHIE-2022.pdf
- Elenco delle chiese parrocchiali della diocesi: https://diocesi.arezzo.it/chiese-parrocchiali/
- **Censimento delle chiese della CEI** (schede storiche):
  - San Biagio, Ciggiano: http://www.chieseitaliane.chiesacattolica.it/SCHEDA=50726&Chiesa_di_San_Biagio__Ciggiano,_Civitella_in_Val_di_Chiana
  - Santa Maria Assunta, Civitella: http://www.chieseitaliane.chiesacattolica.it/SCHEDA=50716&Chiesa_di_Santa_Maria_Assunta__Civitella_in_Val_di_Chiana
  - Le schede delle altre parrocchie si trovano cercando sul sito per comune.
- **Catalogo generale dei Beni Culturali**:
  - Parco della Rimembranza di Tuori (cita la chiesa dei SS. Giorgio e Luca): https://catalogo.beniculturali.it/detail/ArchitecturalOrLandscapeHeritage/09iccd_modi_4749768586751
  - Parco della Rimembranza di Ciggiano: https://catalogo.beniculturali.it/detail/ArchitecturalOrLandscapeHeritage/09iccd_modi_3625118586751

## 5. Eccidio del 1944 e Novecento

- Atlante delle stragi naziste e fasciste, scheda di Civitella: https://www.straginazifasciste.it/wp-content/uploads/schede/CIVITELLA%20IN%20VAL%20DI%20CHIANA%2029.06.1944.pdf
- Atlante, scheda di San Pancrazio (Bucine): https://www.straginazifasciste.it/wp-content/uploads/schede/SAN%20PANCRAZIO%20BUCINE%2029.06.1944.pdf
- Archivio della Memoria di Civitella, i luoghi della strage: https://www.archiviodellamemoriacivitellavaldichiana.it/en/i-luoghi-della-strage/
- Villa Oliveto, campo di internamento:
  - Regione Toscana: https://www.regione.toscana.it/-/villa-oliveto
  - Scheda storica: https://www.storiaememorie.it/villaoliveto/ShedeCampi/VillaOliveto.htm

## 6. Wikipedia: solo per il controllo incrociato

Utile per trovare riferimenti, **non** come prova. La voce inglese elenca ad esempio San Pancrazio
tra le frazioni, ma San Pancrazio è nel comune di Bucine.
- https://it.wikipedia.org/wiki/Civitella_in_Val_di_Chiana
- https://it.wikipedia.org/wiki/Badia_al_Pino
- https://it.wikipedia.org/wiki/Giostre_del_Toppo
- https://it.wikipedia.org/wiki/Villa_Oliveto

**Da non caricare:** aggregatori come indettaglio, comuniecitta, siti di B&B o turistici generici.
Copiano tra loro e propagano gli errori.

---

## Errori sospetti già individuati (da verificare per primi)

1. **Ciggiano ↔ Albergo:** le chiese tolte da Albergo (Santa Maria del 1635 con i portici per i
   pastori, San Pietro rifatta nel 1836) compaiono **identiche** nella pagina di Ciggiano. Va capito
   a quale frazione appartengono davvero, se a una delle due. In più "Via della Costarella" è nel
   **capoluogo** (scheda `luogo_23`), quindi anche "Santa Maria della Costarella" a Ciggiano è sospetta.
2. **Numero delle vittime del 1944:** il sito dice 244 (115 Civitella + 58 Cornia + 71 San Pancrazio,
   Gebbia esclusa). La scheda dell'Atlante per l'episodio di Civitella (Civitella + Cornia + Gebbia)
   riporta 146 vittime. Le cifre vanno ricostruite località per località.
3. **Montoto:** compare sia in Pieve a Maiano sia in Ponticino ("antico guado di Montoto", fortilizio
   del VII-VIII secolo, chiesa di San Giovanni Battista e San Martino). Va verificato dove si trova e
   se la datazione ha una fonte.
4. **Dati di popolazione** (Pieve al Toppo 1.531, Viciomaggio 905, Spoiano 31, Matroia "una
   trentina", Tuori 120-130): manca una fonte. Usare i dati ISTAT per località (censimento) o toglierli.
5. **Badia al Pino:** soppressione dell'abbazia nel 1441 o nel 1446; trasferimento della sede comunale
   nel 1917.
6. **Tuori:** chiesa dei "Santi Giorgio e Luca" o "Giorgio e Lucia". Il Catalogo dei Beni Culturali
   riporta Giorgio e **Luca**.

## Domande da fare al notebook, pagina per pagina

**Storia (storia.html)**
- Civitella era abitata in epoca etrusco-romana? È stata roccaforte longobarda? Nell'XI secolo
  passò al vescovo di Arezzo con il nome "Civitella del Vescovo"?
- È documentata una distruzione nel XIII secolo e una ricostruzione nel 1272? È documentato il
  passaggio a Firenze nel 1348 come podesteria?
- Il legame con Dante è documentato, e in che termini?
- Quante sono le vittime del 29 giugno 1944, località per località?

**Geografia (geografia.html)**
- Distanza da Arezzo, altitudine del capoluogo (525 m) e della pianura (250-270 m).
- Quale vino DOCG/DOC si produce nel territorio (Chianti, Chianti Colli Aretini)?

**Per ogni frazione**
- Quali chiese, con il titolo esatto, e quali monumenti le fonti attribuiscono alla frazione? Con quali date?
- Quali eventi storici e quali date sono documentati?
- Le fonti spiegano l'origine del toponimo?
- C'è un dato di popolazione, e di che anno?
- Le sagre e le feste citate sul sito (Sagra del Crostino, della Bistecca, del Cinghiale, dei
  Baccelli, Festa dell'uva di Ciggiano, Fiera del Miele, Festa Sportiva Tegoleto) sono confermate da qualche fonte?

**Domande specifiche**
- Ciggiano: la statua della Maddalena attribuita ad Andrea Sansovino, l'altare Mazzeschi, la
  promozione a pieve nel 1465, il cippo romano di località La Villa.
- Oliveto: la distruzione del castello nel 1318 a opera di Guido Tarlati, l'autonomia fino al 1774,
  la Madonna del Rosario di Orazio Porta, il campo di internamento (date, internati, deportazione a Bergen-Belsen).
- Pieve al Toppo: la distruzione della pieve e dell'ospedale nel 1502, l'Oratorio della Madonna del
  Conforto, il complesso di Mugliano.
- Ponticino: la Tabula Peutingeriana, la stazione del 1866, il referendum del 2017.
- Viciomaggio: il toponimo *Vicus maius*, l'atto del 1024, Villa Milioni, Poggio Castellare, la
  strage del 29 marzo 1944 (Mario Mannelli).
- Tuori: il "terzo anello" difensivo aretino, il Cassero del XIV secolo, Sasso Saracino.
- Tegoleto: la "corte di Tegoleto" attorno all'anno 1000, la chiesa di San Biagio parrocchia nel X secolo, la torre.
- Cornia e Gebbia: il numero e i nomi delle vittime, il cippo del 1969.
