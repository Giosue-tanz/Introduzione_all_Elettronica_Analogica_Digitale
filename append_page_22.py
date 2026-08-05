import sys

filepath = '/home/giosue/Scrivania/Elettronica digitale/Elettronica analogica digitale.tex'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_text = r"""
\begin{align*}
    V_0 &= R\underbrace{(C \dot{V}_{\text{out}})}_{I} + V_{\text{out}} \implies
    \begin{cases}
        \dot{V}_{\text{out}} + \frac{1}{RC} V_{\text{out}} = \frac{V_0}{RC} \\[0.5em]
        V_{\text{out}}(0^+) = \frac{Q(0)}{C}
    \end{cases}
\end{align*}
Applicando la trasformata di Laplace ad ambo i membri: $\mathcal{L}(\dots) = \mathcal{L}(\dots)$
\begin{align*}
    & s \tilde{V}_{\text{out}} - V_{\text{out}}(0^+) + \frac{1}{\tau} \tilde{V}_{\text{out}} = \frac{V_0}{\tau} \frac{1}{s} \\[0.5em]
    \implies& \left(s + \frac{1}{\tau}\right) \tilde{V}_{\text{out}} = \frac{V_0}{\tau s} + V_{\text{out}}(0^+) \\[0.5em]
    & s\left(s + \frac{1}{\tau}\right) \tilde{V}_{\text{out}} = \frac{V_0}{\tau} + sV_{\text{out}}(0^+) \\[0.5em]
    \implies& \tilde{V}_{\text{out}} = \frac{\frac{V_0}{\tau} + sV_{\text{out}}(0^+)}{s\left(s + \frac{1}{\tau}\right)} = \frac{V_0}{\tau s\left(s + \frac{1}{\tau}\right)} + \frac{V_{\text{out}}(0^+)}{s + \frac{1}{\tau}} = \\[0.5em]
    &= V_0 \left[ \frac{1}{s} - \frac{1}{s + \frac{1}{\tau}} \right] + \frac{V_{\text{out}}(0^+)}{s + \frac{1}{\tau}}
\end{align*}
Antitrasformando:
\begin{align*}
    \implies V_{\text{out}}(t) &= V_0 \left[ 1 - e^{-\frac{t}{\tau}} \right] + V_{\text{out}}(0^+) e^{-\frac{t}{\tau}} = \\[0.5em]
    &= V_0 \left[ 1 - e^{-\frac{t}{\tau}} \right] + \frac{Q(0)}{C} e^{-\frac{t}{\tau}}
\end{align*}

\vspace{0.5cm}
\noindent\hrulefill
\vspace{0.5cm}

\subsection*{Funzione di trasferimento in trasformata di Laplace e impedenze complesse}
\begin{align*}
    Z_C &= \frac{1}{j\omega C}, & I_C &= C \dot{V}_C \implies \tilde{I}_C = C s \tilde{V}_C = sC \tilde{V}_C \\[0.5em]
    Z_L &= j\omega L, & V_L &= L \dot{I}_L \implies \tilde{V}_L = sL \tilde{I}_L
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

print('Page 22 appended successfully.')