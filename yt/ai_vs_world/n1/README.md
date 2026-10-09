# AI vs World — Episodio 1

Materiali del confronto tra Google Fogli, uno script Python e un agente AI.
I dati sono fittizi e servono per un esercizio didattico.

## Contenuto

- dipendenti.csv: 260 dipendenti.
- presenze.csv: 1.408 rilevazioni mensili.
- classic_solution/main.py: script Python mostrato nel video.
- ai_solution/main.py: esempio con OpenAI Responses API e Code Interpreter.
- sheets_solution/: risultato esportato da Google Fogli.

## Eseguire lo script classico

Richiede Python 3. Estrai il pacchetto, apri un terminale nella cartella AI_vs_World_01 e poi esegui:

    cd classic_solution
    python main.py

Su alcuni sistemi il comando e' python3. I percorsi dei CSV nello script sono relativi alla directory di lavoro: avvialo dalla cartella classic_solution.

Il totale atteso e' 3.512 ore. I valori per reparto sono:
Customer Support 709; Direzione 42; Engineering 980; Finance 195;
Marketing 108; Operations 1034; People 71; Sales 373.

## Eseguire l'esempio AI

Nella cartella principale crea il tuo ambiente virtuale e attivalo. Installa:

    python -m pip install -r requirements.txt

Rinomina .env.example in .env nella cartella principale e inserisci la tua chiave API. Non distribuire il file .env. L'utilizzo dell'API e del relativo strumento puo' comportare costi e richiede un modello disponibile sul tuo account che supporti Code Interpreter; il codice allegato conserva il modello mostrato nel video.
Dal terminale nella cartella principale esegui:

    cd ai_solution
    python main.py

Domanda d'esempio:
Ritornami il totale degli straordinari per reparto.

## Google Fogli

Importa i due CSV usando il separatore punto e virgola. Usa impostazioni che riconoscano il punto decimale. Il reparto e' la colonna D di dipendenti.csv; l'ID e' la colonna A in entrambi i file. Aggiungi il reparto alle presenze tramite XLOOKUP/CERCA.X, poi crea una tabella pivot con reparto nelle righe e somma di ore_straordinario nei valori.

## Limiti dell'esempio

Gli script sono esempi introduttivi, non un gestionale HR pronto per la produzione. Nel dataset allegato gli straordinari sono interi: lo script classico usa int(). Se impieghi altri dati con ore frazionarie, aggiorna la conversione e definisci come trattare duplicati, ID mancanti, valori vuoti e righe in bozza. La corrispondenza dei risultati su questo esercizio non garantisce la correttezza su altri dataset.

Le credenziali e l'ambiente virtuale del computer dell'autore sono stati esclusi dalla copia distribuibile. I due CSV, gli script e il risultato del foglio sono conservati come nel pacchetto ricevuto.
