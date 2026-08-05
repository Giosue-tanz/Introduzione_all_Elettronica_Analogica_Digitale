import re
import sys

filename = '/home/giosue/Scrivania/Elettronica digitale/Elettronica analogica digitale.tex'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Section Reorganization
content = content.replace(r'\subsection{Filtri attivi con Op-Amp}', r'\section{Amplificatori Operazionali (Op-Amp)}' + '\n' + r'\subsection{Filtri attivi e circuiti lineari}')
content = content.replace(r'\subsection{Feedback degli amplificatori}', r'\section{Retroazione (Feedback) negli Amplificatori}')
content = content.replace(r'\section{Trasformata di Laplace}', r'\section{Trasformata di Laplace e Diagrammi di Bode}')

# Bode plot subsection
bode_old = r'\begin{itemize}' + '\n' + r'    \item \textbf{Plot di Bode} (a partire dalla $\mathcal{L}$-trasformata)' + '\n' + r'\end{itemize}'
bode_new = r'\subsection{Diagrammi di Bode}' + '\n' + r'\textbf{Plot di Bode} (a partire dalla $\mathcal{L}$-trasformata)'
content = content.replace(bode_old, bode_new)

bode_old_2 = r'\item \textbf{Plot di Bode} (a partire dalla $\mathcal{L}$-trasformata)'
if bode_old not in content and bode_old_2 in content:
    # Just insert subsection before
    content = content.replace(bode_old_2, r'\end{itemize}' + '\n' + r'\subsection{Diagrammi di Bode}' + '\n' + r'\begin{itemize}' + '\n' + r'    ' + bode_old_2)

# 2. Text and Circuit Corrections
content = content.replace('inverteute', 'invertente')
content = content.replace('Inverteute', 'Invertente')

# i \omega to j \omega
content = content.replace('i \\omega', 'j \\omega')

# Personal note
note_old = r"\textcolor{red}{gilbertina cara ricordati che se hai un valore <0 indicato da una lettera anche se il - non lo vedi, cmq c'è :)}"
note_new = r'\begin{important}' + '\n' + r'Ricorda: se un parametro letterale rappresenta un valore negativo, il segno meno è intrinseco nel valore stesso anche se non esplicitato nella formula.' + '\n' + r'\end{important}'
content = content.replace(note_old, note_new)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modifiche completate.")