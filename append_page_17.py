import sys

filepath = '/home/giosue/Scrivania/Elettronica digitale/Elettronica analogica digitale.tex'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

end_marker = '\\part{Elettronica Digitale}'
parts = content.split(end_marker)

if len(parts) != 2:
    print('Error: Could not find exactly one instance of the split marker.')
    sys.exit(1)

new_content = r'''
% -- page 17 --
\section{Trasformata di Laplace}

$f(t) \mapsto \tilde{f}(s) = \int k(s, t) f(t) dt$

$f(t): \mathbb{R}^+ \rightarrow \mathbb{C}$ (o definita sul semiasse reale positivo, eventualmente tale che $f(t) = 0$ per $t < 0 \rightarrow$ causalità).

Laplace: $k(s, t) = \text{nucleo} = e^{-st}, \quad s \in \mathbb{C}$

$\Rightarrow$ trasformata di Laplace di $f(t) = \mathcal{L}(f) = \tilde{f}(s) = \int_0^{+\infty} e^{-st} f(t) dt$

$\Rightarrow$ trasformata di Fourier (se esiste) $\equiv$ restrizione di $\tilde{f}(s)$ sull'asse immaginario ($s = j\omega, \omega \in \mathbb{R}$)

\begin{itemize}
    \item \textbf{Proprietà}
    \begin{itemize}
        \item lineare: $f_1(t), f_2(t) \Rightarrow \mathcal{L}(a_1 f_1 + a_2 f_2) = a_1 \mathcal{L}(f_1) + a_2 \mathcal{L}(f_2)$
        \item dominio connesso $\equiv$ "semipiano di convergenza"
    \end{itemize}
\end{itemize}

Supponiamo che $\exists s_o = \sigma_o + j\omega_o$ tale che esista:
\[ \tilde{f}(s_o) = \int_0^{+\infty} e^{-s_o t} f(t) dt \Rightarrow |\tilde{f}(s_o)| < \int_0^{+\infty} e^{-\sigma_o t} |f(t)| dt \]

Allora l'integrale converge (ed è quindi definita la $\mathcal{L}$-trasformata) $\forall s \in \mathbb{C}$ tale che $Re(s) \geq \sigma_o = Re(s_o)$

\[ \tilde{f}(s) = \int_0^{+\infty} e^{-st} f(t) dt = \int_0^{+\infty} e^{-\sigma t} e^{-j\omega t} f(t) dt \]
'''

final_content = parts[0] + new_content + '\n' + end_marker + parts[1]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_content)

print('Page 17 appended.')