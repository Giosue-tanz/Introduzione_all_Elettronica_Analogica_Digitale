import sys

filepath = '/home/giosue/Scrivania/Elettronica digitale/Elettronica analogica digitale.tex'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_text = r"""
\begin{itemize}
    \item \textbf{Plot di Bode} (a partire dalla $\mathcal{L}$-trasformata)
\end{itemize}
$\tilde{A}(s) \to \text{calcolo per freq. reali } s = j\omega = j2\pi f \quad (f > 0)$

In generale, per tutti gli esempi considerati:
\begin{align*}
    \tilde{A}(s) &= \frac{N(s)}{D(s)} \quad 
    \begin{cases} 
        N(s) = \text{polinomio di grado } m \text{ a coeff. reali} \\
        D(s) = \text{polinomio di grado } n \text{ a coeff. reali}
    \end{cases} \\[0.5em]
    &= K \frac{\prod (s-z_k)}{\prod (s-p_k)} \quad 
    \begin{cases}
        z_k = \text{zero di } \tilde{A} \\
        p_k = \text{poli di } \tilde{A}
    \end{cases}
\end{align*}

\[
    \implies A(j\omega) = K \frac{\prod (j\omega - z_k)}{\prod (j\omega - p_k)}
\]

A grandi linee (andamenti asintotici) ottenibili per i plot di Bode in:
\begin{itemize}
    \item \textbf{ampiezza}
    \[
        A_{\text{dB}} = 20 \log_{10} |A(\omega)| = 20 \log_{10} |K| + 20 \left( \sum \log_{10} |j\omega - z_k| - \sum \log_{10} |j\omega - p_k| \right)
    \]
\end{itemize}

\textbf{Caso 1)} $z_k = \text{zero del primo ordine reale} = \sigma_k$
\[
    |j\omega - z_k| = \sqrt{\sigma_k^2 + (\cancel{\text{Im}(z_k)} - \omega)^2} = \sqrt{\omega^2 + \sigma_k^2}
\]
\begin{align*}
    \omega \ll |\sigma_k| &\implies |j\omega - z_k|^{m_k} \simeq |\sigma_k|^{m_k} \implies 20 \log_{10} |j\omega - z_k|^{m_k} \simeq 20 \log_{10} |\sigma_k|^{m_k} \\
    \omega \gg |\sigma_k| &\implies |j\omega - z_k|^{m_k} \simeq \omega^{m_k} \implies 20 \log_{10} |j\omega - z_k|^{m_k} \simeq 20 \log_{10} \omega^{m_k} \simeq 20 m_k \underbrace{\log_{10} \omega}_{=x}
\end{align*}

$\implies$ nell'attraversamento di uno zero del primo ordine la pendenza del plot di Bode incrementa di $20 \text{ dB/dec} = 6 \text{ dB/oct}$. \\
Se l'ordine dello zero è $m_k$, allora l'incremento è di $20 m_k \text{ dB/dec}$.

\begin{itemize}
    \item \textbf{Polo reale (negativo) di ordine $n_k$}
\end{itemize}
\[
    |j\omega - p_k|^{n_k} = \left(\sqrt{\omega^2 + p_k^2}\right)^{n_k}
\]
\begin{align*}
    \omega \ll |p_k| &\implies |j\omega - p_k|^{n_k} \simeq |p_k|^{n_k} \implies 20 \log_{10} |p_k|^{n_k} \\
    \omega \gg |p_k| &\implies |j\omega - p_k|^{n_k} \simeq \omega^{n_k} \implies 20 n_k \log_{10} \omega = 20 n_k x
\end{align*}
$\implies$ nell'attraversamento di un polo reale negativo di ordine $n_k$ il plot di Bode in ampiezza ha una variazione di pendenza di $-20 n_k \text{ dB/dec}$.

\begin{itemize}
    \item \textbf{fase}
\end{itemize}
\[
    \phi(\omega) = \arg(\tilde{A}(j\omega)) = \arg(K) + \sum \arg(j\omega - z_k) - \sum \arg(j\omega - p_k)
\]

\textbf{Zeri:}
\[
    j\omega - z_k \implies 
    \begin{cases}
        \omega \ll |z_k| \implies \arg = \pi \left( \frac{1 + \text{sgn}(z_k)}{2} \right) \\
        \omega \gg |z_k| \implies \arg = \frac{\pi}{2}
    \end{cases}
\]

$-$ se $z_k > 0$, allora nell'attraversamento si
"""

anchor = r"\part{Elettronica Digitale}"
if anchor in content:
    content = content.replace(anchor, new_text + "\n\n" + anchor)
else:
    print("Anchor not found!")
    sys.exit(1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Page 24-25 appended successfully.')