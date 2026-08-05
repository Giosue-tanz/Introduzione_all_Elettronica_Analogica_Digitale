import re

file_path = "/home/giosue/Scrivania/Elettronica digitale/recovery/Elettronica analogica digitale.tex"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Modelli dei Componenti e Quadripoli
text = text.replace(
    r"\section{Relazioni Tensione-Corrente e Modelli}",
    r"\chapter{Modelli dei Componenti e Quadripoli}" + "\n" + r"\section{Relazioni Tensione-Corrente e Modelli}"
)

# 2. Transistor BJT (Bipolar Junction Transistor)
# Change section to chapter
text = text.replace(
    r"\section{Transistor BJT (Bipolar Junction Transistor)}",
    r"\chapter{Transistor BJT (Bipolar Junction Transistor)}"
)
# Change specific subsections in the BJT chapter to sections
bjt_subs = [
    r"\subsection{Amplificatore di Tensione a Emettitore Comune}",
    r"\subsection{Configurazioni del BJT}",
    r"\subsection{Riepilogo dei Modelli Equivalenti degli Amplificatori}",
    r"\subsection{Amplificatore CE con Resistenza di Emettitore ($R_E$)}",
    r"\subsection{Configurazione CC (Collettore Comune — \emph{Emitter Follower})}",
    r"\subsection{Cascata CE\,\texorpdfstring{$\to$}{->}\,CC e Rete di Polarizzazione}",
    r"\subsection{Calcolo del Punto di Quiescenza (Bias Point)}",
    r"\subsection{BJT ad Alta Frequenza — Capacità Parassite}",
    r"\subsection{Teorema di Miller}",
    r"\subsection{Transistor Darlington}"
]
for sub in bjt_subs:
    new_sec = sub.replace(r"\subsection{", r"\section{")
    text = text.replace(sub, new_sec)

# 3. Amplificatori Operazionali
text = text.replace(
    r"\section{Amplificatori Operazionali (Op-Amp)}",
    r"\chapter{Amplificatori Operazionali e Retroazione}" + "\n" + r"\section{Introduzione agli Op-Amp}"
)
opamp_subs = [
    r"\subsection{Filtri attivi e circuiti lineari}",
    r"\subsection{Caratteristiche reali degli Op-Amp}",
    r"\subsection{Altri amplificatori con Op-Amp}",
    r"\subsection{Applicazione ai circuiti con l'Op-Amp}"
]
for sub in opamp_subs:
    new_sec = sub.replace(r"\subsection{", r"\section{")
    text = text.replace(sub, new_sec)

# 4. Laplace e Bode
text = text.replace(
    r"\section{Trasformata di Laplace e Diagrammi di Bode}",
    r"\chapter{Trasformata di Laplace e Diagrammi di Bode}"
)
bode_subs = [
    r"\subsection*{Funzione di trasferimento in trasformata di Laplace e impedenze complesse}",
    r"\subsection{Diagrammi di Bode}"
]
for sub in bode_subs:
    new_sec = sub.replace(r"\subsection", r"\section")
    text = text.replace(sub, new_sec)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Reorganization of Analog section complete.")
