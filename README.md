# Elettronica analogica digitale

Il presente repository ospita i codici sorgente in formato LaTeX e la relativa documentazione dell'opera tecnica *Elettronica analogica digitale*.

## **Stato del Progetto**
L'opera si trova attualmente in fase di redazione preliminare. Allo stato attuale dei lavori, la trattazione verte in via esclusiva sui fondamenti dell'**Elettronica Digitale** (comprendente l'analisi dei segnali, l'algebra di Boole, la sintesi delle reti logiche e l'implementazione fisica dei dispositivi). L'elaborazione e la conseguente integrazione della sezione dedicata all'elettronica analogica sono formalmente previste per le successive fasi editoriali.

## Compilazione
Per clonare il repository e compilare il PDF, esegui i seguenti comandi da terminale:

```bash
git clone https://github.com/Giosue-tanz/Introduzione_all_Elettronica_Analogica_Digitale.git
cd Introduzione_all_Elettronica_Analogica_Digitale
pdflatex "Elettronica analogica digitale.tex"
pdflatex "Elettronica analogica digitale.tex"
```

## Struttura del progetto
Il file `Elettronica analogica digitale.tex` è il documento principale: contiene preambolo, frontespizio e bibliografia, e include i singoli capitoli dalla cartella `capitoli/` tramite `\input{}` (un file per capitolo, numerato in ordine di lettura). Per modificare un capitolo è sufficiente editare il file corrispondente in `capitoli/`; non è necessario toccare il file principale.

## Licenza
Questo progetto è distribuito sotto licenza Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). L'uso commerciale è vietato. Per maggiori dettagli, consulta il file LICENSE allegato o visita https://creativecommons.org/licenses/by-nc/4.0/.
