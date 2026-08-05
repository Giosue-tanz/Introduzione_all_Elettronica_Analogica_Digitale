import os

file_path = "/home/giosue/Scrivania/Elettronica digitale/Elettronica analogica digitale.tex"

content_to_insert = r"""avrebbe una variazione di fase di $-\frac{\pi}{2} m_k$.

\begin{itemize}
    \item se $z_k < 0 \implies$ variazione di fase di $\frac{\pi}{2} m_k$
    \item \textbf{Poli} ($<0$)
\end{itemize}
\[
    j\omega - p_k \implies 
    \begin{cases}
        \omega \ll |p_k| \implies \arg(j\omega - p_k) = 0 \\
        \omega \gg |p_k| \implies \arg(\dots) = \frac{\pi}{2}
    \end{cases}
\]
$\implies$ nell'attraversamento di un polo del primo ordine $\phi$ ha un incremento di $-\frac{\pi}{2}$ (o di $-\frac{\pi}{2} m_k$ se l'ordine è $m_k > 1$).

\vspace{1em}
\textbf{Filtro passa-basso:} $\tilde{A}(s) = \frac{1}{1+sRC}$

\begin{fitcenter}
\begin{tikzpicture}
\begin{axis}[
    width=7cm, height=4.5cm,
    xmode=log,
    xlabel={$\log_{10} \omega$},
    ylabel={$20 \log_{10} |A|$},
    axis lines=middle,
    xmin=0.1, xmax=100,
    ymin=-40, ymax=10,
    xtick={1}, xticklabels={$\frac{1}{RC}$},
    ytick={-3}, yticklabels={$-3$},
    domain=0.1:100, samples=100,
    every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},
    every axis y label/.style={at={(ticklabel* cs:1)},anchor=south},
]
\addplot[blue, thick] {20*log10(1/sqrt(1+(x)^2))};
\addplot[dashed] coordinates {(0.1,0) (1,0) (100,-40)};
\draw[dashed] (1, -3) -- (1, 0);
\end{axis}
\end{tikzpicture}
%
\begin{tikzpicture}
\begin{axis}[
    width=7cm, height=4.5cm,
    xmode=log,
    xlabel={$\log_{10} \omega$},
    ylabel={$\phi$},
    axis lines=middle,
    xmin=0.1, xmax=100,
    ymin=-100, ymax=10,
    xtick={0.1, 1, 10}, xticklabels={$\frac{0.1}{RC}$, $\frac{1}{RC}$, $\frac{10}{RC}$},
    ytick={-45, -90}, yticklabels={$-\frac{\pi}{4}$, $-\frac{\pi}{2}$},
    domain=0.1:100, samples=100,
    every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},
    every axis y label/.style={at={(ticklabel* cs:1)},anchor=south},
]
\addplot[blue, thick] {-atan(x)};
\addplot[dashed] coordinates {(0.1,0) (1,-45) (10,-90)};
\end{axis}
\end{tikzpicture}
\end{fitcenter}

\vspace{1em}
\textbf{Filtro passa-alto:} $\tilde{A}(s) = \frac{sRC}{1+sRC}$

\begin{fitcenter}
\begin{tikzpicture}
\begin{axis}[
    width=7cm, height=4.5cm,
    xmode=log,
    xlabel={$\log_{10} \omega$},
    ylabel={$|A|_{\text{dB}}$},
    axis lines=middle,
    xmin=0.1, xmax=100,
    ymin=-40, ymax=10,
    xtick={1}, xticklabels={$\frac{1}{RC}$},
    ytick={-3}, yticklabels={$-3$},
    domain=0.1:100, samples=100,
    every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},
    every axis y label/.style={at={(ticklabel* cs:1)},anchor=south},
]
\addplot[blue, thick] {20*log10(x/sqrt(1+(x)^2))};
\addplot[dashed] coordinates {(0.1,-20) (1,0) (100,0)};
\end{axis}
\end{tikzpicture}
%
\begin{tikzpicture}
\begin{axis}[
    width=7cm, height=4.5cm,
    xmode=log,
    xlabel={$\log_{10} \omega$},
    ylabel={$\phi$},
    axis lines=middle,
    xmin=0.1, xmax=100,
    ymin=0, ymax=100,
    xtick={0.1, 1, 10}, xticklabels={$\frac{0.1}{RC}$, $\frac{1}{RC}$, $\frac{10}{RC}$},
    ytick={45, 90}, yticklabels={$\frac{\pi}{4}$, $\frac{\pi}{2}$},
    domain=0.1:100, samples=100,
    every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},
    every axis y label/.style={at={(ticklabel* cs:1)},anchor=south},
]
\addplot[blue, thick] {90 - atan(x)};
\end{axis}
\end{tikzpicture}
\end{fitcenter}

\vspace{1em}
\textbf{Filtro passa-banda:}
\[
    \tilde{A}(s) = K \frac{s R_1 C_1}{(1+s R_1 C_1)(1+s R_2 C_2)}
\]

\begin{fitcenter}
\begin{tikzpicture}
\begin{axis}[
    width=7cm, height=4.5cm,
    xmode=log,
    xlabel={$\log_{10} \omega$},
    ylabel={$|A|_{\text{dB}}$},
    axis lines=middle,
    xmin=0.01, xmax=1000,
    ymin=-40, ymax=10,
    xtick={0.1, 100}, xticklabels={$\frac{1}{R_1 C_1}$, $\frac{1}{R_2 C_2}$},
    domain=0.01:1000, samples=100,
    every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},
    every axis y label/.style={at={(ticklabel* cs:1)},anchor=south},
]
\addplot[blue, thick] {20*log10( (x) / sqrt((1+(x*10)^2)*(1+(x/100)^2)) )};
\addplot[dashed] coordinates {(0.01,-40) (0.1,0) (100,0) (1000,-20)};
\end{axis}
\end{tikzpicture}
%
\begin{tikzpicture}
\begin{axis}[
    width=7cm, height=4.5cm,
    xmode=log,
    xlabel={$\log_{10} \omega$},
    ylabel={$\phi$},
    axis lines=middle,
    xmin=0.01, xmax=1000,
    ymin=-100, ymax=100,
    xtick={0.1, 100}, xticklabels={$\frac{1}{R_1 C_1}$, $\frac{1}{R_2 C_2}$},
    ytick={-90, 90}, yticklabels={$-\frac{\pi}{2}$, $\frac{\pi}{2}$},
    domain=0.01:1000, samples=100,
    every axis x label/.style={at={(ticklabel* cs:1)},anchor=west},
    every axis y label/.style={at={(ticklabel* cs:1)},anchor=south},
]
\addplot[blue, thick] {90 - atan(x*10) - atan(x/100)};
\end{axis}
\end{tikzpicture}
\end{fitcenter}


\section*{Riepilogo: Trasformata di Laplace}
\textit{(11/11/2025)}

\begin{important}
\[
    F(s) = \int_0^\infty f(t) e^{-st} \, dt
\]
La trasformata di Fourier è una restrizione della trasformazione di Laplace in quanto si ottiene valutando quest'ultima sull'asse immaginario.
\end{important}

\begin{itemize}
    \item \textbf{Proprietà}:
    \begin{itemize}
        \item Linearità: $\mathcal{L}(a f(t) + b g(t)) = a F(s) + b G(s)$
        \item Convergenza: l'integrale converge per $\text{Re}(s) > \alpha$
        \item Analiticità: $F(s)$ è analitica per $\text{Re}(s) > \alpha$
        \item Traslazione in $s$: $\mathcal{L}(e^{at} f(t)) = F(s-a)$
        \item Convoluzione: $\mathcal{L}(f * g) = F(s) \cdot G(s)$
    \end{itemize}
    \item \textbf{Trasformate notevoli}:
    \begin{align*}
        \delta(t) &\xrightarrow{\mathcal{L}} 1 \\
        1 &\xrightarrow{\mathcal{L}} \frac{1}{s} \\
        t &\xrightarrow{\mathcal{L}} \frac{1}{s^2} \\
        t^n &\xrightarrow{\mathcal{L}} \frac{n!}{s^{n+1}} \\
        e^{at} &\xrightarrow{\mathcal{L}} \frac{1}{s-a} \\
        \cos(\omega t) &\xrightarrow{\mathcal{L}} \frac{s}{s^2 + \omega^2} \\
        \sin(\omega t) &\xrightarrow{\mathcal{L}} \frac{\omega}{s^2 + \omega^2} \\
        f'(t) &\xrightarrow{\mathcal{L}} s F(s) - f(0)
    \end{align*}
    
    \item \textbf{Esempio: integratore passa-basso}
    \[
        Z_C = \frac{1}{sC} \quad Z_L = sL
    \]
    Filtro passa-basso: $\tilde{A}(s) = \frac{1}{1 + sRC}$ \\
    Filtro passa-alto: $\tilde{A}(s) = \frac{sRC}{1 + sRC}$
\end{itemize}


\chapter{Applicazioni non lineari degli Op-Amp}
\textit{(14/11/2025)}

\begin{itemize}
    \item \textbf{Feedback negativo}: circuiti lineari
    \item \textbf{Feedback positivo}: circuiti non lineari
\end{itemize}

Applicazioni principali: comparatori (discriminatori, trigger), generatori di onde.

\section{Comparatori}
Un \textbf{comparatore} è un circuito a 2 livelli di uscita che dipendono dal confronto di un ingresso con una soglia. Negli op-amp, l'uscita va in saturazione:
\begin{itemize}
    \item $V_S > V_{\text{thr}}, \, V_d > 0 \implies V_{\text{out}} = V_{OH}$
    \item $V_S < V_{\text{thr}}, \, V_d < 0 \implies V_{\text{out}} = V_{OL}$
\end{itemize}

\begin{fitcenter}
\begin{circuitikz}[american, transform shape]
    \draw (0,0) node[op amp] (opamp) {};
    \draw (opamp.+) to[short, -o] (-2,0.5) node[left] {$V_S$};
    \draw (opamp.-) to[short, -o] (-2,-0.5) node[left] {$V_{\text{thr}}$};
    \draw (-2,-0.5) to[short] (-2, -1) node[ground]{};
    \draw (opamp.out) to[short, -o] (1.5,0) node[right] {$V_{\text{out}}$};
    \node at (0, -1) {opamp ideale, $A_d = \infty$};
\end{circuitikz}
\end{fitcenter}

\begin{note}
Negli allarmi serve che il segnale sia ON o OFF senza vie di mezzo (da approfondire).
\end{note}

\subsection{Caso 1: Trigger non invertente}
Per migliorare le prestazioni ed eliminare l'effetto causato dal rumore si usa il \textbf{Trigger di Schmitt}, che è un comparatore con isteresi. Si usa un \textbf{feedback positivo} che causa la non linearità.

\begin{fitcenter}
\begin{circuitikz}[american, transform shape]
    \draw (0,0) node[op amp] (opamp) {};
    \draw (opamp.-) to[short] (-1.2,-0.5) node[ground] {};
    \draw (opamp.+) to[R=$R_1$] (-3,0.5) node[left] {$V_S$};
    \draw (opamp.+) -- (-1.2,1.5) to[R=$R_2$] (1.2,1.5) -- (opamp.out);
    \draw (opamp.out) to[short, -o] (1.5,0) node[right] {$V_{\text{out}}$};
\end{circuitikz}
\end{fitcenter}

\begin{itemize}
    \item $V_{\text{out}} = V_{OH} \iff V_d > 0 \implies V_S > -\frac{R_1}{R_2} V_{\text{out}} = V_{\text{thr}}^- < 0$
\end{itemize}
Quando $V_S$ raggiunge $V_{\text{thr}}^-$, l'uscita viene forzatamente spostata al livello negativo (basso) di saturazione. Stessa cosa per l'altro caso.

\begin{fitcenter}
\begin{tikzpicture}
    \draw[->] (-3,0) -- (3,0) node[right] {$V_S$};
    \draw[->] (0,-3) -- (0,3) node[above] {$V_{\text{out}}$};
    \draw[thick, blue, arrows={->[scale=1.5]}] (3, 2) -- (0, 2);
    \draw[thick, blue, arrows={->[scale=1.5]}] (0, 2) -- (-1.5, 2);
    \draw[thick, blue, arrows={->[scale=1.5]}] (-1.5, 2) -- (-1.5, -2);
    \draw[thick, blue, arrows={->[scale=1.5]}] (-1.5, -2) -- (0, -2);
    \draw[thick, blue, arrows={->[scale=1.5]}] (0, -2) -- (1.5, -2);
    \draw[thick, blue, arrows={->[scale=1.5]}] (1.5, -2) -- (1.5, 2);
    \draw[thick, blue] (1.5, 2) -- (3, 2);
    \draw[thick, blue] (-3,-2) -- (-1.5,-2);
    \draw[dashed] (1.5,0) node[below] {$V_{\text{thr}}^+$} -- (1.5,2);
    \draw[dashed] (-1.5,0) node[above] {$V_{\text{thr}}^-$} -- (-1.5,-2);
    \node[left] at (0,2) {$V_{OH}$};
    \node[right] at (0,-2) {$V_{OL}$};
    
    \fill[green!20, opacity=0.5] (-1.5,-2) rectangle (1.5,2);
    \node at (0, -2.5) {Dead Zone};
\end{tikzpicture}
\end{fitcenter}
La zona colorata rappresenta la \textbf{dead zone} (zona morta). L'intervallo è legato alla sensibilità al rumore: se le oscillazioni intorno al valore centrale sono minori di $V_{\text{thr}}$, non hanno alcun effetto sulla commutazione; quindi basta sceglierli sufficientemente grandi in funzione di quello che vogliamo misurare.

\subsection{Caso 2: Trigger invertente}
\begin{fitcenter}
\begin{circuitikz}[american, transform shape]
    \draw (0,0) node[op amp, yscale=-1] (opamp) {}; 
    \draw (opamp.+) to[short, -o] (-2,-0.5) node[left] {$V_S$};
    \draw (opamp.-) to[R=$R_1$] (-2,0.5) node[ground] {};
    \draw (opamp.-) -- (-1.2,1.5) to[R=$R_2$] (1.2,1.5) -- (opamp.out);
    \draw (opamp.out) to[short, -o] (1.5,0) node[right] {$V_{\text{out}}$};
    \node at (3,0) {$\equiv \text{ in } \triangleright \text{ out}$};
\end{circuitikz}
\end{fitcenter}

\begin{itemize}
    \item $V_{\text{out}} = V_{OH} \iff V_d > 0 \implies V_S < \frac{R_1}{R_1+R_2} V_{\text{out}} = V_{\text{thr}}^+ > 0$
\end{itemize}
Quando $V_S$ raggiunge $V_{\text{thr}}^+$, l'uscita viene forzatamente spostata al livello negativo (basso) di saturazione. Stessa cosa per l'altro caso.

\begin{fitcenter}
\begin{tikzpicture}
    \draw[->] (-3,0) -- (3,0) node[right] {$V_S$};
    \draw[->] (0,-3) -- (0,3) node[above] {$V_{\text{out}}$};
    
    \draw[thick, blue, arrows={->[scale=1.5]}] (-3, 2) -- (0, 2);
    \draw[thick, blue, arrows={->[scale=1.5]}] (0, 2) -- (1.5, 2);
    \draw[thick, blue, arrows={->[scale=1.5]}] (1.5, 2) -- (1.5, -2);
    \draw[thick, blue, arrows={->[scale=1.5]}] (1.5, -2) -- (0, -2);
    \draw[thick, blue, arrows={->[scale=1.5]}] (0, -2) -- (-1.5, -2);
    \draw[thick, blue, arrows={->[scale=1.5]}] (-1.5, -2) -- (-1.5, 2);
    \draw[thick, blue] (-1.5, 2) -- (-3, 2);
    \draw[thick, blue] (3,-2) -- (1.5,-2);
    
    \draw[dashed] (1.5,0) node[below] {$V_{\text{thr}}^+$} -- (1.5,-2);
    \draw[dashed] (-1.5,0) node[above] {$V_{\text{thr}}^-$} -- (-1.5,2);
    \node[left] at (0,2) {$V_{OH}$};
    \node[right] at (0,-2) {$V_{OL}$};
    
    \fill[green!20, opacity=0.5] (-1.5,-2) rectangle (1.5,2);
    \node at (0, -2.5) {Dead Zone};
\end{tikzpicture}
\end{fitcenter}

\begin{important}
\textbf{Differenza Schmitt invertente / non invertente:}
L'isteresi ruota in senso antiorario ($\circlearrowleft$) nel caso invertente, e in senso orario ($\circlearrowright$) nel caso non invertente.
\begin{itemize}
    \item Segno soglia e segnale per $V_d > 0$: $V_{\text{thr}}^- / V_{\text{out}}^-$ (non inv.) e $V_{\text{thr}}^+ / V_{\text{out}}^+$ (inv.)
    \item Segno soglia e segnale per $V_d < 0$: $V_{\text{thr}}^+ / V_{\text{out}}^-$ (non inv.) e $V_{\text{thr}}^- / V_{\text{out}}^+$ (inv.)
\end{itemize}
\end{important}

\section{Generatori di onde}
\textit{(17/11/2025)}

\textbf{Generatore di onde}: configurazione ad anello formato da un \textbf{Trigger di Schmitt} e un \textbf{circuito integratore} (con segno opposto al trigger). L'uscita del trigger non è stabile, commuta periodicamente fra le due saturazioni a causa dell'anello di feedback.

\[
    \implies \text{Produzione di }
    \begin{cases}
        \text{onda quadra} & \text{all'uscita del Trigger} \\
        \text{onda triangolare} & \text{all'uscita dell'integratore}
    \end{cases}
\]

\subsection{Esempio: multivibratore astabile}
Circuito con integratore di Miller.

\begin{fitcenter}
\begin{circuitikz}[american, transform shape]
    % Primo Op-amp (Trigger)
    \draw (0,0) node[op amp] (op1) {};
    \draw (op1.out) to[short, -o] (1,0) node[right] {out trig};
    \draw (op1.+) -- (-1.2, 0.5) to[R=$R_1$] (-1.2, -1.5) node[ground]{};
    \draw (-1.2, 0.5) -- (-1.2, 1.5) to[R=$R_2$] (0.5, 1.5) -- (0.5, 0);
    
    % Secondo Op-amp (Integratore)
    \draw (6,0) node[op amp] (op2) {};
    \draw (op2.out) to[short, -o] (7,0) node[right] {out integr};
    \draw (op2.+) to[short] (4.8, -0.5) node[ground]{};
    \draw (op2.-) -- (4.8, 0.5) to[R=$R$] (2, 0.5) -- (2, 0) -- (1,0);
    \draw (4.8, 0.5) -- (4.8, 1.5) to[C=$C$] (6.5, 1.5) -- (6.5, 0);
    
    % Feedback
    \draw (7,0) -- (7, -2) -- (-2, -2) -- (-2, -0.5) -- (op1.-);
\end{circuitikz}
\end{fitcenter}

\begin{itemize}
    \item Suppongo che $V_{\text{out trig}} = V_{OH}$ per $t > 0$, quindi asintoticamente $V_-(t \to \infty) \to V_{OH}$.
    \item Inoltre $V_+ = \frac{R_1}{R_1+R_2} V_{OH} < V_-$, quindi asintoticamente $V_d < 0$, che è incompatibile con le caratteristiche dell'op-amp. 
    \item $\implies \exists T_H$ trascorso il quale l'uscita del Trigger switcha a $V_{OL}$ e analogamente esiste $T_L$ dopo cui switcha a $V_{OH}$.
\end{itemize}

\textbf{Calcolo di $T_H, T_L$}:
\begin{itemize}
    \item $t \in [0, T_H]$: 
    $V_-(t) = A + B \exp(-t/\tau)$ con $\tau = RC$, $A = V_{OH}$, $B = \frac{R_1}{R_1+R_2} V_{OL} - V_{OH}$ \\
    $T_H \mid V_-(T_H) = V_{\text{in}}(T_H) = V_{\text{thr}}^+ = \frac{R_1}{R_1+R_2} V_{OH}$ \\
    $\implies \frac{R_1}{R_1+R_2} V_{OH} = V_{OH}\left(1 - \exp(-T_H/\tau)\right) + V_{OL} \frac{R_1}{R_1+R_2} \exp(-T_H/\tau)$ \\
    $\implies T_H = RC \ln \left[ 1 + \frac{R_1}{R_2} \left( 1 - \frac{V_{OL}}{V_{OH}} \right) \right] = RC \ln\left(1 + 2\frac{R_1}{R_2}\right)$ (se $V_{OL} = -V_{OH}$)
    
    \item $t \in [T_H, T_H + T_L]$:
    Speculare a sopra, scambiando $V_{OH} \leftrightarrow V_{OL}$ \\
    $\implies T_L = RC \ln \left[ 1 + \frac{R_1}{R_2} \left( 1 - \frac{V_{OH}}{V_{OL}} \right) \right] = RC \ln\left(1 + 2\frac{R_1}{R_2}\right)$ (se $V_{OL} = -V_{OH}$)
\end{itemize}

Quando un'onda quadra ha i livelli di saturazione simmetrici ($V_{OH} = -V_{OL}$) allora è simmetrica, cioè ha un duty-cycle = 50\%.


\chapter{Stabilità e Criterio di Nyquist}
\textit{(21/11/2025)}

\section{Criteri di stabilità di un amplificatore}
Considerando un amplificatore con guadagno ad anello chiuso $A_f(s) \equiv A_v(s)$ e retroazione $\beta(s)$:
\begin{itemize}
    \item $\beta A \le -1$: condizione sufficiente per \textbf{non} linearità ($\implies$ circuito non lineare).
    \item $\beta A > -1$: condizione necessaria per linearità (circuito lineare $\implies \beta A > -1$).
\end{itemize}

\begin{enumerate}
    \item Per avere un sistema lineare, in assenza di segnale in ingresso ($x_S = 0$), è necessario che la risposta alla perturbazione sia un transiente:
    \[
        \text{Sistema stabile} \implies \text{risposta al rumore = transiente}
    \]
    $\tilde{x}_{\text{out}}(s) = A(s) \tilde{x}_S(s) \quad (\omega \to s)$ \\
    $x_{\text{out}}(t) = \int_{-\infty}^{+\infty} A(t-t') x_S(t') \, dt'$ \\
    $x_S' = x_S + x_n$ (rumore aleatorio deterministico) \\
    Lineare $\implies \tilde{x}_{\text{out}}' = A (\tilde{x}_S') = A \tilde{x}_S + A \tilde{x}_n \implies x_{\text{out}}' = \mathcal{L}^{-1}(\tilde{x}_{\text{out}}') = \mathcal{L}^{-1}(\tilde{x}_n) \to 0$ se $\tilde{x}_S = 0$ e $t \to \infty$.

    \item Per avere un amplificatore stabile (cioè lineare) è necessario che la risposta a un segnale impulsivo ($\delta$ di Dirac) sia un transiente:
    \[
        \text{Sistema stabile} \implies \text{risposta a un impulso = transiente}
    \]
    $x_n(t) = \delta(t) \xrightarrow{\mathcal{L}} \mathcal{L}(x_n) = 1 \implies \tilde{x}_{\text{out}} = A \implies x_{\text{out}} = \mathcal{L}^{-1}(A) \to 0$ se $t \to \infty$.

    \item Per avere un sistema stabile, la trasformata di Laplace della funzione di trasferimento deve avere \textbf{tutti i poli nel semipiano con parte reale negativa}. Se anche solo un polo è non negativo allora il sistema è instabile (non lineare):
    \[
        \text{Sistema stabile} \iff \text{Trasformata di Laplace di } A_v \text{ e } A_f \text{ hanno } \text{Re}(p_k) < 0
    \]
\end{enumerate}

\begin{note}
\textbf{Teorema di traslazione sulle frequenze}: \\
$\mathcal{L}(e^{pt} f(t)) = \int_0^\infty e^{pt} f(t) e^{-st} \, dt = \int_0^\infty f(t) e^{-(s-p)t} \, dt = \tilde{f}(s-p)$

Applicazione:
\[
    A = \frac{\tilde{x}_{\text{out}}}{\tilde{x}_S} = \frac{N(s)}{D(s)} = K \frac{\prod(s-z_i)^{\alpha_i}}{\prod(s-p_i)^{\beta_i}} \quad \text{con } \deg N \le \deg D
\]
In risposta a un rumore $x_n(t) = \delta(t)$: $x_{\text{out}}(t) = \mathcal{L}^{-1}(A)$.
\[
    \mathcal{L}^{-1}\left( \frac{1}{(s-p_i)^{\beta_i}} \right) = \int_0^\infty \frac{\exp(-st)}{(s-p_i)^{\beta_i}} \, dt = (\text{integro } n\text{-volte per parti}) = \frac{t^{\beta_i-1}}{(\beta_i-1)!} e^{p_i t}
\]
$\implies x_{\text{out}}(t) = \sum_k a_k \frac{t^{\beta_k-1}}{(\beta_k-1)!} e^{p_k t} \to 0$ per $t \to \infty$ se $\text{Re}(p_k) < 0$.
\end{note}


\section*{Riepilogo: Stabilità e Diagrammi di Bode}
\textit{(24/11/2025)}

\textbf{Amplificatori reazionati:}
\[
    \tilde{x}_{\text{out}} = A_F(s) \tilde{x}_S \quad ; \quad A_F(s) = \frac{A(s)}{1 \pm \beta(s) A(s)} = \frac{A(s)}{1 \pm L(s)}
\]
\begin{itemize}
    \item $+\beta > 0$: feedback negativo
    \item $-\beta < 0$: feedback positivo
    \item $A(s) =$ guadagno dello stadio
    \item $\beta(s) =$ guadagno di feedback = frazione di segnale riportata all'ingresso
    \item $L(s) = \beta(s) A(s) =$ loop gain = guadagno del segnale dopo un giro dell'anello
    \item $A_F(s) =$ guadagno ad anello chiuso, complessivo del circuito: da studiare per saperne la stabilità.
\end{itemize}

Poli di $A_F$ = poli di $A$ + zeri di $1 \pm \beta A$. L'amplificatore è stabile $\iff A_F$ ha solo poli con $\text{Re}(p) < 0$.

Se l'amplificatore è stabile allora il semipiano di convergenza di $A(s)$ include $s=j\omega \implies \exists \mathcal{F}(A) = \hat{A}(\omega) = \tilde{A}(j\omega) = \mathcal{L}(A)$. Dipendenza dalla frequenza dei plot di Bode a partire da $A(s)$ in maniera asintotica:
\[
    A(j\omega) = K \frac{\prod (j\omega - z_i)^{\alpha_i}}{\prod (j\omega - p_i)^{\beta_i}}
\]

\textbf{Bode in ampiezza:} 
\[
    |A(j\omega)| = |K| \frac{\prod |j\omega - z_i|^{\alpha_i}}{\prod |j\omega - p_i|^{\beta_i}}
\]
\[
    A_{\text{dB}} = 20 \log|K| + 20 \sum \left( \alpha_i \log|j\omega-z_i| - \beta_i \log|j\omega-p_i| \right)
\]

\textbf{Bode in fase:}
\begin{itemize}
    \item Zeri: $\phi = \arg(j\omega - z) \simeq \begin{cases} \arg(-z) & \omega \ll |z| \\ \arg(j\omega) & \omega \gg |z| \end{cases} = \begin{cases} 0 & \omega \ll |z| < 0 \\ \pi & \omega \ll |z| > 0 \\ \pi/2 & \omega \gg |z| \end{cases}$
    \item Poli (solo nel semipiano negativo): $\phi = \arg(j\omega - p) = \arg(j\omega + |p|) \simeq \begin{cases} 0 & \omega \ll |p| \\ \pi/2 & \omega \gg |p| \end{cases}$
\end{itemize}

La fase aumenta/diminuisce di $\pi/2$ attraversando uno zero con $\alpha=1$ a seconda che sia positivo/negativo. In generale avremo $\Delta \phi_Z = \pm \alpha \frac{\pi}{2}$ con $z \lessgtr 0$ e $\alpha \in \mathbb{N}$, e analogamente $\Delta \phi_P = -\beta \frac{\pi}{2}$ con $p < 0$ e $\beta \in \mathbb{N}$.

\subsection{Esempio: Circuito sfasatore variabile}

\begin{fitcenter}
\begin{circuitikz}[american, transform shape]
    \draw (0,0) node[op amp] (opamp) {};
    \draw (opamp.-) to[R=$R'$] (-2,0.5) node[left] {$V_S$};
    \draw (opamp.-) -- (-1.2,1.5) to[R=$R'$] (1.2,1.5) -- (opamp.out);
    \draw (opamp.+) to[R=$R$, -*] (-2,-0.5) -- (-2, 0.5);
    \draw (opamp.+) to[C=$C$] (0,-1.5) node[ground]{};
    \draw (opamp.out) to[short, -o] (1.5,0) node[right] {$V_{\text{out}}$};
\end{circuitikz}
\end{fitcenter}

\[
    V_{\text{out}} = V_S \left( \frac{2}{1+sRC} - 1 \right) \implies A_v = \frac{1-sRC}{1+sRC}
\]
\begin{itemize}
    \item Zeri: $s = \omega_0 = \frac{1}{RC}, \quad \alpha=1$.
    \item Poli: $s = -\omega_0, \quad \beta=1$.
\end{itemize}

Nel dominio delle frequenze reali $s=j\omega$ abbiamo $|A_v| = 1 \quad \forall \omega$:
\begin{itemize}
    \item $\omega = \omega_0 : A_v = -j \implies |A_v|=1$
    \item $\omega \ll \omega_0 : V_+ = V_S = V_- \text{ (open)} \implies A_v = 1, \, \phi = 0$
    \item $\omega \gg \omega_0 : V_+ = 0 \text{ (short)} \implies A_v = -1, \, \phi = -\pi$
\end{itemize}

\section{Criterio di Stabilità di Nyquist}
Molto utile per studiare i poli nel semipiano positivo delle frequenze; serve prima dimostrare il \textbf{Teorema dell'argomento (indicatore logaritmico)}.

\begin{important}
\textbf{Teorema:} Data $\gamma: [0,1] \to \mathbb{C}$ curva chiusa, $f: A \to \mathbb{C}$ aperto con $\gamma \subset A$ e zeri/poli $\notin \gamma$, allora $\Gamma = f(\gamma)$ gira intorno all'origine $N = N_Z - N_P$ volte. (Zeri e poli di $f$ all'interno di $\gamma$ pesati ciascuno col suo ordine).
\end{important}

Dimostrazione (tramite residui e calcolo integrale lungo cammini): \\
$f(s) = |f| e^{i\phi} \implies \Delta\phi = \oint d\phi = 2\pi N$. \\
Sia $f_L = \frac{d}{ds}(\log f) = \frac{f'}{f}$. \\
Se $\deg(z)=\alpha \implies \exists I_Z \mid f = (s-z)^\alpha \Psi_Z(s) \implies f_L = \frac{\alpha}{s-z} + \frac{\Psi_Z'}{\Psi_Z} \implies \lim_{s\to z} (s-z) f_L = \alpha \implies \deg(\text{polo } f_L)=1$ con residuo $=\alpha$. \\
Se $\deg(p)=\beta \implies \exists I_P \mid f = \frac{\Psi_P(s)}{(s-p)^\beta} \implies f_L = \frac{-\beta}{s-p} + \frac{\Psi_P'}{\Psi_P} \implies \lim_{s\to z} (s-z) f_L = -\beta \implies \deg(\text{polo } f_L)=1$ con residuo $=-\beta$.

Applicando Cauchy a $f_L$:
\[
    \oint_\gamma f_L(s) \, ds = 2\pi i \sum \text{res}(f_L) = 2\pi i (N_Z - N_P) = 2\pi i N = \oint_\Gamma i \, d\phi = \oint_\gamma \left( \frac{d}{ds} \log |f| + i \frac{d\phi}{ds} \right) \, ds = \oint_\Gamma f_L \, ds \quad \square
\]
"""

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

target = "$-$ se $z_k > 0$, allora nell'attraversamento si\n\n\\part{Elettronica Digitale}"
if target in text:
    replacement = content_to_insert + "\n\n\\\part{Elettronica Digitale}"
    new_text = text.replace(target, replacement)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Insertion complete.")
else:
    # Try different whitespace combinations
    target2 = "$-$ se $z_k > 0$, allora nell'attraversamento si\n\n\n\\part{Elettronica Digitale}"
    if target2 in text:
        replacement = content_to_insert + "\n\n\\\part{Elettronica Digitale}"
        new_text = text.replace(target2, replacement)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_text)
        print("Insertion complete.")
    else:
        print("Could not find the target string.")
