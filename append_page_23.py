import sys

filepath = '/home/giosue/Scrivania/Elettronica digitale/Elettronica analogica digitale.tex'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_text = r"""
\begin{align*}
    \implies Z_C &= \frac{1}{sC} = \frac{\tilde{V}_C}{\tilde{I}_C} \\[0.5em]
    Z_L &= sL = \frac{\tilde{V}_L}{\tilde{I}_L}
\end{align*}

\begin{itemize}
    \item \textbf{Filtro passa-basso}
    \[
        \tilde{A}_{\text{LP}}(s) = \frac{Z_C}{Z_C + R} = \frac{\frac{1}{sC}}{\frac{1}{sC} + R} = \frac{1}{1 + sRC} = \hat{A} \quad \text{per } s=j\omega
    \]
    $\implies 1 \text{ polo del } 1^\circ \text{ ordine in } s = -\frac{1}{RC} = -\frac{1}{\tau}$
    
    \item \textbf{Filtro passa-alto}
    \[
        \tilde{A}_{\text{HP}}(s) = \frac{R}{R + Z_C} = \dots = \frac{sRC}{1 + sRC} \implies
        \begin{cases}
            1 \text{ zero del } 1^\circ \text{ ordine in } s=0 \\
            1 \text{ polo del } 1^\circ \text{ ordine in } s=-\frac{1}{\tau}
        \end{cases}
    \]
\end{itemize}

Studio della dipendenza della funzione di trasferimento dalla frequenza ($s=j\omega$) possibile se e solo se i poli di $\tilde{A}(s)$ sono confinati nel semipiano con $\text{Re}(s) < 0$ (al contrario l'amplificatore non potrebbe in alcun modo essere lineare).

\begin{itemize}
    \item \textbf{Circuito integratore}
\end{itemize}

\begin{fitcenter}
\begin{circuitikz}[american, transform shape]
    \draw (0,0) node[op amp] (opamp) {};
    \draw (opamp.-) to[R=$R_1$] (-3,0.5) node[left] {$V_S$};
    \draw (opamp.+) to[short] (-1.2,-0.5) node[ground] {};
    \draw (opamp.-) -- (-1.2,1.5) to[C=$C$] (1.2,1.5) -- (opamp.out);
    \draw (-1.2,1.5) -- (-1.2, 2.5) to[R=$R_2$] (1.2,2.5) -- (1.2,1.5);
    \draw (opamp.out) to[short, -o] (1.5,0) node[right] {$V_{\text{out}}$};
\end{circuitikz}
\end{fitcenter}

\begin{align*}
    \hat{A}(\omega) &= -\frac{R_2}{R_1} \frac{1}{1 + j\omega R_2 C} \\[0.5em]
    \implies \tilde{A}(s) &= -\frac{R_2}{R_1} \frac{1}{1 + s R_2 C} \xrightarrow{R_2 \to \infty} -\frac{1}{s R_1 C} \\[0.5em]
    \implies \tilde{V}_{\text{out}} &= -\frac{1}{s R_1 C} \tilde{V}_s \\[0.5em]
    \implies V_{\text{out}}(t) &= -\frac{1}{R_1 C} \int_{t_0}^t V_s(t') \, dt'
\end{align*}
"""

anchor = r"\part{Elettronica Digitale}"
if anchor in content:
    content = content.replace(anchor, new_text + "\n\n" + anchor)
else:
    print("Anchor not found!")
    sys.exit(1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Page 23 appended successfully.')