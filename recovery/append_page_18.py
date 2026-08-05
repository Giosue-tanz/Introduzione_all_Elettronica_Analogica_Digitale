import sys

filepath = '/home/giosue/Scrivania/Elettronica digitale/recovery/Elettronica analogica digitale.tex'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

end_marker = '\\part{Elettronica Digitale}'
parts = content.split(end_marker)

if len(parts) != 2:
    print('Error: Could not find exactly one instance of the split marker.')
    sys.exit(1)

new_content = r'''
% -- page 18 --
\[ |\tilde{f}(s)| \leq \int_0^{+\infty} e^{-\sigma t} |f(t)| dt \leq \int_0^{+\infty} e^{-\sigma_o t} |f(t)| dt < +\infty \]

$\Rightarrow \exists$ un'ascissa $\overline{\sigma}$ (dipendente da $f(t)$) tale che l'integrale converga $\forall s \in \mathbb{C}$ tale che $Re(s) > \overline{\sigma} \equiv$ \textbf{ascissa di convergenza}.

\begin{figure}[H]
    \centering
    \begin{tikzpicture}
        \begin{scope}
            \clip (-1.5, -2.5) rectangle (4, 2.5);
            \foreach \x in {-5, -4, ..., 4} {
                \draw (\x, -3) -- (\x+5.5, 2.5);
            }
        \end{scope}
        
        \draw[->, thick] (-3,0) -- (4,0) node[below] {$\sigma$};
        \draw[->, thick] (0,-2.5) -- (0,2.5) node[left] {$j\omega$};
        
        \draw[dashed, thick] (-1.5, -2.5) -- (-1.5, 2.5);
        \node[above left] at (-1.5, 0) {$\overline{\sigma}$};
    \end{tikzpicture}
    \caption{Semipiano di convergenza}
\end{figure}

\textbf{Alcuni esempi:}
\begin{itemize}
    \item $f(t) = a_n t^n + \dots + a_0 \qquad \overline{\sigma} = 0$
    \item $f(t) = e^{at} \qquad \overline{\sigma} = a$
    \item $f(t) = e^{-bt^2}, b > 0 \qquad \overline{\sigma} = -\infty \rightarrow \mathcal{L}$-trasformata definita su tutto $\mathbb{C}$
    \item $f(t) = e^{ct^2}, c > 0 \qquad \overline{\sigma} = +\infty \rightarrow$ non esiste $\mathcal{L}$-trasformata in alcun punto
\end{itemize}

\begin{itemize}
    \item \textbf{Analiticità}
\end{itemize}
\[ \frac{d\tilde{f}}{ds} = \frac{d}{ds} \int_0^{+\infty} e^{-st} f(t) dt = \int_0^{+\infty} \left( \frac{d}{ds} e^{-st} \right) f(t) dt = - \int_0^{+\infty} t f(t) e^{-st} dt \]
'''

final_content = parts[0] + new_content + '\n' + end_marker + parts[1]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_content)

print('Page 18 appended.')