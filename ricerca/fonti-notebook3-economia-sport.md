# Notebook 3: economia, lavoro, sport e associazioni

Obiettivo: raccogliere fonti per due nuove sezioni del sito.
- **Economia e lavoro:** settori, aziende storiche, agricoltura e prodotti tipici.
- **Sport e associazioni:** società sportive, impianti, associazioni.

**Criterio:** raccontiamo storia, settori e realtà che hanno segnato il territorio, non un elenco commerciale di aziende. Usiamo solo fonti pubbliche e in tono neutrale.

---

## ⚡ Blocchi pronti da incollare ("+ Aggiungi → Sito web")

### Blocco E: economia e lavoro
```
https://www.cittaslow.it/citta/civitella-val-di-chiana
https://www.cittadellolio.it/citta/civitella-in-val-di-chiana/
https://www.chimet.com/it/company/about-us
https://it.fashionnetwork.com/news/Chimet-compie-50-anni-all-insegna-di-sostenibilita-e-consolidamento-del-fatturato-a-4-3-miliardi-di-euro,1632451.html
https://www.firenzepost.it/2018/01/30/civitella-val-di-chiana-ar-in-liquidazione-la-del-tongo-storica-azienda-di-cucine/
https://www.arezzonotizie.it/economia/del-tongo-marchio-aggiudicato-kico.html
https://it.wikipedia.org/wiki/Del_Tongo-MG_Boys_Maglificio
https://www.artigianiarezzo.it/comunicati-stampa/zone-creative-di-badia-al-pino-dona-100-mila-mascherine-ai-pensionati-di-confartigianato/
https://it.wikipedia.org/wiki/Civitella_in_Val_di_Chiana
```

### Blocco S: sport e associazioni
```
https://www.comune.civitella-in-val-di-chiana.ar.it/amministrazione/enti_e_fondazioni/ente_15.html
http://www.halleyweb.com/c051016/zf/index.php/servizi-aggiuntivi/index/index/idtesto/58
https://usdtegoleto.it/
https://usdtegoleto.it/festa-al-tegoleto/
https://www.dovefaresport.it/TDatiDfsView/18508
https://arezzonotizie.it/attualita/riqualificazione-palestra-stadio-badia-pino.html
https://www.centritalianews.it/civitella-in-val-di-chiana-nuove-aree-sportive-a-fruizione-libera-nel-territorio-del-comune/
```
**Da aggiungere a mano:** sul sito del Comune, alla voce *Amministrazione → Enti e fondazioni*, c'è l'elenco delle associazioni. La scheda della Polisportiva Albergo Oliveto è `ente_15`: le altre hanno numeri vicini (`ente_1` … `ente_40`). Incolla le schede di società sportive, Pro Loco, circoli e associazioni culturali.

### PDF da scaricare e caricare ("+ Aggiungi → Carica")
Dal portale del Piano Strutturale e del Piano Operativo (https://cloud.ldpgis.it/civitellavaldichiana/ps e https://cloud.ldpgis.it/civitellavaldichiana/po):
```
https://cloud.ldpgis.it/sites/civitellavaldichiana/files/ps/b8_6_6_caratterizzazione_socio_economica_e_colturale_delle_zone_agricole.pdf
https://cloud.ldpgis.it/sites/civitellavaldichiana/files/ps/b8_1_4b_caratterizzazione_funzionale_degli_insediamenti.pdf
```
- Relazione illustrativa del **Piano Operativo** (sezione "Piano Operativo" del portale): aree produttive, commercio, servizi.
- Le **Norme Tecniche del PS**, che hai già, servono anche qui: lo Schema Direttore 3 tratta "le isole della produzione".
- Facoltativo, molto grande: Regione Toscana, Piano paesaggistico, scheda d'ambito 15 "Piana di Arezzo e Val di Chiana": https://www.regione.toscana.it/documents/10180/11377097/Ambito+15+Piana+Arezzo+Valdichiana.pdf/0dda665f-0b68-4cd5-8b20-8da273d97342

---

## Prompt da usare nel notebook 3

**Prompt 0: controllo delle fonti**
```
Elenca tutte le fonti caricate. Per ciascuna indica in una riga: titolo, argomento, e se è vuota, è una pagina di errore o non riguarda Civitella in Val di Chiana.
```

**Prompt 1: economia**
```
Per ogni risposta cita il passaggio testuale e il titolo della fonte; se un'informazione non c'è scrivi "NON PRESENTE NELLE FONTI". Non dedurre.

1. Quali sono i settori economici principali del comune (industria, artigianato, agricoltura, commercio, servizi)? Dove si trovano le aree produttive?
2. Storia e ruolo delle aziende più rilevanti citate nelle fonti: fondazione, sede, settore, numero di addetti, eventi principali (per esempio Chimet, Del Tongo, imprese del settore orafo).
3. Agricoltura e prodotti tipici: olio, vino, Chianina, allevamenti, adesione a Città dell'Olio, Strada del Vino, Cittaslow.
4. Esiste una "Fiera dell'uva, dell'olio e del vino" o una festa analoga? Dove e da quando?
5. Cosa prevedono il Piano Strutturale e il Piano Operativo per le aree produttive (Schema Direttore 3, polo per l'innovazione di Viciomaggio)?
```

**Prompt 2: sport e associazioni**
```
Per ogni risposta cita il passaggio testuale e il titolo della fonte; se un'informazione non c'è scrivi "NON PRESENTE NELLE FONTI". Non dedurre.

1. Elenca le società sportive del comune: nome, sport, sede o impianto, frazione, anno di fondazione se presente.
2. Quali impianti sportivi esistono (stadi, palestre, palazzetti, aree a fruizione libera) e in quali frazioni?
3. Quali associazioni culturali, ricreative e di volontariato sono citate (Pro Loco, circoli, polisportive), e quali feste organizzano?
4. Storia sportiva del territorio: la squadra ciclistica Del Tongo, la tappa del Giro d'Italia del 2004 a Tegoleto, altri eventi.
```
