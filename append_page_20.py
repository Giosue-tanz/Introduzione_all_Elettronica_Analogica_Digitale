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
% -- page 20 --
$\Rightarrow$ sul semipiano intersezione dei semipiani di conv. di $f, g$ ($\Rightarrow$ ascissa di conv. di $h = \max(\sigma_f, \sigma_g)$) è definita $\tilde{h} = \mathcal{L}(h)$ e 
\[ \tilde{h} = \tilde{f} \tilde{g} \]

\textbf{Trasformate notevoli}
\begin{itemize}
    \item $\delta(t) \xrightarrow{\mathcal{L}} \int_0^{+\infty} e^{-st} \delta(t) dt = 1$
\end{itemize}

$\Rightarrow$ la $\mathcal{L}$-trasf. di un sistema fisico lineare, causale e t-invariante è la $\mathcal{L}$-trasf. della sua uscita in risposta ad un ingresso di natura impulsiva ($\delta(t)$).

\begin{itemize}
    \item $f(t) = 1 \rightarrow \int_0^{+\infty} e^{-st} dt = \left[ - \frac{1}{s} e^{-st} \right]_0^{+\infty} = \frac{1}{s}$
    \item $f(t) = t \rightarrow \int_0^{+\infty} t e^{-st} dt = \cancel{\left[ - t \frac{1}{s} e^{-st} \right]_0^{+\infty}} + \int_0^{+\infty} \frac{1}{s} e^{-st} dt = \frac{1}{s^2}$
    \item $f(t) = t^n \rightarrow \int_0^{+\infty} t^n e^{-st} dt = \dots = \frac{n!}{s^{n+1}}$
    \item $f(t) \rightarrow F(t) = \int_{t_o}^t f(t') dt'$
    \[ \mathcal{L}(F) = \int_0^{+\infty} e^{-st} F(t) dt = \left[ -\frac{1}{s} e^{-st} F(t) \right]_0^{+\infty} + \frac{1}{s} \int_0^{+\infty} e^{-st} f(t) dt \]
\end{itemize}
'''

final_content = parts[0] + new_content + '\n' + end_marker + parts[1]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_content)

print('Page 20 appended.')