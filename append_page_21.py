import sys
import re

filepath = '/home/giosue/Scrivania/Elettronica digitale/Elettronica analogica digitale.tex'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_text = r"""
\begin{align*}
    &= \cancel{\frac{F(0)}{s}} + \frac{1}{s}\mathcal{L}(f) \\[-0.5em]
    &\quad \makebox[0pt][l]{$\smash{\xrightarrow{\text{se } f \text{ è regolare in } t=0}}$} \notag
\end{align*}

\begin{itemize}
    \item $f(t) = e^{at} \implies \tilde{f} = \int_{0}^{+\infty} e^{at}e^{-st}dt = \mathcal{L}(1)\big|_{s-a} = \frac{1}{s-a}$
    \item $f(t) = \cos(\omega t) = \frac{1}{2}\left(e^{j\omega t} + e^{-j\omega t}\right)$
    
    $\implies \mathcal{L}(\cos(\omega t)) = \frac{1}{2}\left[\mathcal{L}(e^{j\omega t}) + \mathcal{L}(e^{-j\omega t})\right] = \frac{1}{2} \left[ \frac{1}{s-j\omega} + \frac{1}{s+j\omega} \right] = \frac{1}{2} \frac{s+j\omega + s - j\omega}{s^2 + \omega^2} = \frac{s}{s^2 + \omega^2}$
    
    \item $f(t) = \sin(\omega t) = \omega \left[ \int \cos(\omega t) \, dt \right]$
    
    $\implies \mathcal{L}(\sin(\omega t)) = \omega \frac{1}{s} \mathcal{L}(\cos(\omega t)) = \frac{\omega}{\cancel{s}} \frac{\cancel{s}}{s^2+\omega^2} = \frac{\omega}{s^2+\omega^2}$
    
    \item $f \in C^1(\mathbb{R}^+) \implies f' = \frac{df}{dt}$
    
    $\mathcal{L}(f') = \int_{0}^{+\infty} \frac{df}{dt} e^{-st} \, dt = \left. f e^{-st} \right|_0^{+\infty} + s \int_0^{+\infty} f e^{-st} \, dt = -f(0^+) + s\tilde{f}(s)$
\end{itemize}

Ad esempio:

\begin{fitcenter}
\begin{circuitikz}[american, transform shape]
    \draw (0,0) to[battery1, l=$V_0$] (0,2)
    to[nos] (1,2)
    to[R=$R$] (3,2)
    to[C=$C$] (3,0) -- (0,0);
    \draw (3,2) -- (4,2);
    \draw (3,0) -- (4,0);
    \draw[<->] (4,0.2) -- (4,1.8) node[midway, right] {$V_{\text{out}}$};
    \draw (4,0) circle (2pt);
    \draw (4,2) circle (2pt);
\end{circuitikz}
\end{fitcenter}
"""

anchor = r"\part{Elettronica Digitale}"
if anchor in content:
    content = content.replace(anchor, new_text + "\n\n" + anchor)
else:
    print("Anchor not found!")
    sys.exit(1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Page 21 appended successfully.')