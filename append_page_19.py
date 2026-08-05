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
% -- page 19 --
\[ = -\mathcal{L}(t f(t)) \rightarrow \text{converge sul semipiano di convergenza di } f(t) \]
\[ \frac{d^n\tilde{f}}{ds^n} = \dots = \mathcal{L}((-1)^n t^n f(t)) \rightarrow \text{stesso semipiano di } f(t) \]

$\Rightarrow$ nel semipiano di convergenza di $f(t)$, $\tilde{f}(s)$ è analitica

$\Rightarrow \tilde{f}(s)$, se ha singolarità, le ha a sinistra del semipiano di convergenza (o al più sulla sua frontiera)

\begin{itemize}
    \item \textbf{Traslazione (in frequenza)}
    \[ f(t) \xrightarrow{\mathcal{L}} \tilde{f}(s) \qquad \mathcal{L}(e^{at} f(t)) = \tilde{f}(s-a), \quad a \in \mathbb{C} \]
    
    Infatti:
    \[ \int_0^{+\infty} e^{at} e^{-st} f(t) dt = \int_0^{+\infty} e^{-(s-a)t} f(t) dt = \tilde{f}(s-a) \]
    
    Se $\overline{\sigma} \equiv$ ascissa di conv. di $f(t)$, allora l'ascissa di conv. di $e^{at} f(t) \equiv \overline{\sigma} + Re(a)$
    
    \item \textbf{Traslazione temporale}
    \[ \mathcal{L}(f(t-t_o)) = \int_0^{+\infty} f(t-t_o) e^{-st} dt = \int_0^{+\infty} f(\tau) e^{-s\tau} e^{-st_o} d\tau \qquad (\tau = t - t_o) \]
    \[ = e^{-st_o} \mathcal{L}(f(t)) \]
    
    \item \textbf{Convoluzione}
    \[ f, g \qquad h(t) = \int_0^{+\infty} f(\tau) g(t-\tau) d\tau = f * g \]
\end{itemize}
'''

final_content = parts[0] + new_content + '\n' + end_marker + parts[1]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_content)

print('Page 19 appended.')