import sys
import re

filepath = '/home/giosue/Scrivania/Elettronica digitale/Elettronica analogica digitale.tex'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# I need to find where the bad -- page 14 -- starts and remove up to \part{Elettronica Digitale}
start_marker = '% -- page 14 --'
end_marker = '\\part{Elettronica Digitale}'

idx_start = content.find(start_marker)
idx_end = content.find(end_marker)

if idx_start != -1 and idx_end != -1 and idx_start < idx_end:
    # Remove the corrupted section
    content = content[:idx_start] + content[idx_end:]

parts = content.split(end_marker)
if len(parts) != 2:
    print('Error: Could not find exactly one instance of the split marker.')
    sys.exit(1)

new_content = r'''
% -- page 14 --
\subsection{Filtri attivi con Op-Amp}
Siano nelle condizioni di poter applicare il principio CCV: linearità e idealità dell'Op-Amp.

\begin{figure}[H]
    \centering
    \begin{circuitikz}[american, transform shape]
        \draw (0,0) node[op amp] (opamp) {};
        \draw (opamp.+) node[ground] {};
        \draw (opamp.-) to[short] (-1.5, 0.5) to[generic, l=$Z_1$] (-3, 0.5) node[left] {$V_S$};
        \draw (-1.5, 0.5) to[short] (-1.5, 2) to[generic, l=$Z_2$] (1.2, 2) to[short] (1.2, 0) to[short] (opamp.out);
        \draw (opamp.out) to[short] (2, 0) node[right] {$V_{out}$};
    \end{circuitikz}
    \caption{Configurazione inverteute per filtri attivi}
\end{figure}

\begin{itemize}
    \item $V_d = V_{out} / A_d = 0$ ; $A_V = - Z_2 / Z_1$
\end{itemize}

\subsubsection*{Caso 1: $Z_1 = R, Z_2 = (i \omega C)^{-1}$}
\textbf{Integratore ideale (anche a bassa frequenza)}

\begin{figure}[H]
    \centering
    \begin{circuitikz}[american, transform shape]
        \draw (0,0) node[op amp] (opamp) {};
        \draw (opamp.+) node[ground] {};
        \draw (opamp.-) to[short] (-1.5, 0.5) to[R, l=$R$] (-3, 0.5) node[left] {$V_S$};
        \draw (-1.5, 0.5) to[short] (-1.5, 2) to[C, l=$C$] (1.2, 2) to[short] (1.2, 0) to[short] (opamp.out);
        \draw (opamp.out) to[short] (2, 0) node[right] {$V_{out}$};
    \end{circuitikz}
    \caption{Integratore ideale}
\end{figure}

\begin{itemize}
    \item $A_V(\omega) = - (i \omega R C)^{-1}$ nel dominio della frequenza.
    \item $V_{out}(t) = - \frac{1}{RC} \int V_S(t') dt'$ nel dominio del tempo.
\end{itemize}

Limiti di funzionamento: $A_V(\omega \to 0) \to \infty$, quindi la componente continua di $V_S$ deve essere nulla.

\textbf{Integratore reale} ($Z_1 = R_1, Z_2 = R_2 \parallel (i \omega C)^{-1}$)

\begin{figure}[H]
    \centering
    \begin{circuitikz}[american, transform shape]
        \draw (0,0) node[op amp] (opamp) {};
        \draw (opamp.+) node[ground] {};
        \draw (opamp.-) to[short] (-1.5, 0.5) to[R, l=$R_1$] (-3, 0.5) node[left] {$V_S$};
        \draw (-1.5, 0.5) to[short] (-1.5, 2);
        \draw (-1.5, 2) to[short] (-1.5, 2.5) to[R, l=$R_2$] (1.2, 2.5) to[short] (1.2, 2);
        \draw (-1.5, 2) to[C, l=$C$] (1.2, 2);
        \draw (1.2, 2) to[short] (1.2, 0) to[short] (opamp.out);
        \draw (opamp.out) to[short] (2, 0) node[right] {$V_{out}$};
    \end{circuitikz}
    \caption{Integratore reale (filtro passa-basso)}
\end{figure}

\begin{itemize}
    \item $A_V(\omega) = - \frac{R_2}{R_1} (1 + i \omega R_2 C)^{-1} \rightarrow$ \textcolor{green}{filtro passa basso} $f_L = (2 \pi R_2 C)^{-1}$
    \item $A_{VMAX} = R_2 / R_1 > 1$
\end{itemize}

\subsubsection*{Caso 2: $Z_1 = (i \omega C)^{-1}, Z_2 = R$}
\textbf{Derivatore ideale (anche ad alta frequenza)}

\begin{figure}[H]
    \centering
    \begin{circuitikz}[american, transform shape]
        \draw (0,0) node[op amp] (opamp) {};
        \draw (opamp.+) node[ground] {};
        \draw (opamp.-) to[short] (-1.5, 0.5) to[C, l=$C$] (-3, 0.5) node[left] {$V_S$};
        \draw (-1.5, 0.5) to[short] (-1.5, 2) to[R, l=$R$] (1.2, 2) to[short] (1.2, 0) to[short] (opamp.out);
        \draw (opamp.out) to[short] (2, 0) node[right] {$V_{out}$};
    \end{circuitikz}
    \caption{Derivatore ideale}
\end{figure}

\begin{itemize}
    \item $A_V(\omega) = - i \omega R C$ nel dominio della frequenza.
    \item $V_{out}(t) = - R C \frac{d}{dt} V_S(t)$ nel dominio del tempo.
\end{itemize}

Limiti di funzionamento: $A_V(\omega \to \infty) \to \infty$, quindi serve un limite alla banda dello spettro di $V_S$.

\textbf{Derivatore reale} ($Z_1 = R_1 + (i \omega C)^{-1}, Z_2 = R_2$)

\begin{figure}[H]
    \centering
    \begin{circuitikz}[american, transform shape]
        \draw (0,0) node[op amp] (opamp) {};
        \draw (opamp.+) node[ground] {};
        \draw (opamp.-) to[short] (-1.5, 0.5) to[R, l=$R_1$] (-2.5, 0.5) to[C, l=$C$] (-4, 0.5) node[left] {$V_S$};
        \draw (-1.5, 0.5) to[short] (-1.5, 2) to[R, l=$R_2$] (1.2, 2) to[short] (1.2, 0) to[short] (opamp.out);
        \draw (opamp.out) to[short] (2, 0) node[right] {$V_{out}$};
    \end{circuitikz}
    \caption{Derivatore reale (filtro passa-alto)}
\end{figure}

\begin{itemize}
    \item $A_V(\omega) = - \frac{R_2}{R_1} i \omega R_1 C (1 + i \omega R_1 C)^{-1} \rightarrow$ \textcolor{green}{filtro passa-alto} $f_H = (2 \pi R_1 C)^{-1}$
    \item $A_{VMAX} = R_2 / R_1$
\end{itemize}

\begin{important}
A guadagni massimi elevati corrispondono:
\begin{itemize}
    \item $f_L$ basse: per il $GBW = A_{MAX} f_L = invariante$.
    \item $f_H$ alte: per riduzione della banda passante.
\end{itemize}
\end{important}

\subsection{Caratteristiche reali degli Op-Amp}

\textbf{1. Capacità parassita in parallelo allo stadio di guadagno} $\Rightarrow$ effetto = filtro passa-basso ($f_L$).
\begin{itemize}
    \item $A_d(\omega) = \frac{A_0}{\sqrt{1 + i \omega / \omega_0}}$ per il teorema di Miller.
\end{itemize}

Esempio: amplificatore non inverteute.
\begin{align*}
    V_- &= \frac{R_1}{R_1 + R_2} V_{out} \equiv \beta V_{out}, \quad V_+ = V_S \Rightarrow V_{out} = \frac{A_d}{1 + \beta A_d} V_S \\
    &\Rightarrow \text{guadagno massimo: } A_M = A_0 / (1 + \beta A_0) < A_0 = \text{guadagno di centro-banda} \\
    &\Rightarrow \text{frequenza di taglio: } f_L = f_0 (1 + \beta A_0) > f_0 = \text{frequenza del filtro}
\end{align*}

Invarianza del prodotto GBW: $GBW = A_M f_L = A_0 f_0 = invariante$.

\textbf{2. Capacità parassita + corrente limitata in uscita} $\Rightarrow$ effetto = slew-rate.
$C \frac{dV_C}{dt} = I_C < \infty \Rightarrow \frac{dV_C}{dt} < \infty \Rightarrow$ non c'è una variazione immediata nei segnali di ingresso allo stadio di guadagno: c'è un riverbero in tutti gli stadi successivi, quindi $V_{out}$ cambia fronte d'onda con una pendenza limitata $\Rightarrow SR = \max \left(\frac{dV_{out}}{dt}\right)$.

\textbf{3. Asimmetria nei Transistor dello stadio di ingresso} $\Rightarrow$ effetto = offset di $\sim 10^{-1}$ mV su $V_d$.

% -- page 15 --
\subsection{Altri amplificatori con Op-Amp}

\textbf{6. Amplificatore Inverteute 2.0}

\begin{figure}[H]
    \centering
    \begin{circuitikz}[american, transform shape]
        \draw (0,0) node[op amp] (opamp) {};
        \draw (opamp.+) node[ground] {};
        \draw (opamp.-) to[short] (-1.5, 0.5) node[above] {$I_S$};
        \draw (-1.5, 0.5) to[R, l=$R$] (-3, 0.5) node[left] {$V_S$};
        \draw (-1.5, 0.5) to[short] (-1.5, 2) to[R, l=$aR$] (0.5, 2) node[above] {$I$};
        \draw (0.5, 2) to[short] (0.5, 2.5) to[R, l=$R$] (2.5, 2.5) to[short] (2.5, 2) node[above] {$I'$};
        \draw (0.5, 2) to[R, l=$R'$] (0.5, 0) to[short] (opamp.out);
        \draw (opamp.out) to[short] (2.5, 0) node[right] {$V_{out}$};
        \draw (2.5, 2) to[short] (2.5, 0);
        \draw (2.5, 0) node[ground] {};
    \end{circuitikz}
    \caption{Amplificatore inverteute 2.0}
\end{figure}

$V_a = -V_S \Rightarrow A_V = - (2 + R/R')$

Differenze con 1:
\begin{itemize}
    \item 2.0: $|A_V| \geq 2$; nell'altro: $|A_V| < 1$ anche.
    \item 2.0: $Z_{in} = R$; nell'altro: $Z_{in} = R_1$.
    \item 2.0: $A_V (R\uparrow) \uparrow$; nell'altro: $A_V (R_1\uparrow) \downarrow$.
\end{itemize}

\textbf{7. Amplificatore non inverteute 2.0 = NIC}

\begin{figure}[H]
    \centering
    \begin{circuitikz}[american, transform shape]
        \draw (0,0) node[op amp] (opamp) {};
        \draw (opamp.+) to[short] (-1, -0.5) to[R, l=$R_3$] (opamp.out);
        \draw (-1, -0.5) to[short] (-1.5, -0.5) node[left] {$V_S$};
        \draw (-1.5, -0.5) node[above] {$I_S$};
        \draw (opamp.-) to[short] (-1, 0.5) to[R, l=$R_1$] (-1, 2) node[ground] {};
        \draw (-1, 0.5) to[short] (-1, 1.5) to[R, l=$R_2$] (1.2, 1.5) to[short] (1.2, 0) to[short] (opamp.out);
        \draw (opamp.out) to[short] (2, 0) node[right] {$V_{out}$};
    \end{circuitikz}
    \caption{Amplificatore non inverteute 2.0 (NIC)}
\end{figure}

$\Rightarrow A_V = \frac{R_1 + R_2}{R_1}$

Differenze con 2:
\begin{itemize}
    \item 2.0: $Z_{in} = - \frac{R_1 R_3}{R_2}$; nell'altro $Z_{in} = \infty$.
\end{itemize}
\begin{important}
Il generatore assorbe potenza, compensata da $V_{CC}, V_{EE}$.
\end{important}

\textbf{8. Amplificatore inverteute di corrente}

\begin{figure}[H]
    \centering
    \begin{circuitikz}[american, transform shape]
        \draw (0,0) node[op amp] (opamp) {};
        \draw (opamp.+) to[short] (-1, -0.5) to[short] (-1, -1.5) to[short] (-2.5, -1.5) node[ground] {};
        \draw (opamp.-) to[short] (-1, 0.5) to[short] (-1, 1.5) to[short] (-2.5, 1.5);
        \draw (-2.5, -0.5) node[left] {$I_S$};
        \draw (-2.5, 1.5) to[I, l=$I_S$] (-2.5, -1.5);
        
        \draw (opamp.out) to[short] (1.2, 0) to[R, l=$R_3$, i=$I_{out}$] (3, 0) to[R, l=$R_L$] (3, -2) node[ground] {};
        
        \draw (-1, 0.5) to[R, l=$R_1$, i=$I_1$] (1.2, 0.5) to[short] (1.2, 0);
        \draw (1.2, 0) to[short] (1.2, -1) to[R, l=$R_2$, i=$I_2$] (1.2, -2) node[ground] {};
    \end{circuitikz}
    \caption{Amplificatore inverteute di corrente}
\end{figure}

\begin{itemize}
    \item Ideale: $R_L = 0 \rightarrow Z_{in} = 0 \rightarrow Z_{out} = \infty$
    \item Reale: $R_L > 0$
\end{itemize}

$R_1 I_1 + R_2 I_2 = 0$, $I_{out} = I_2 - I_1 \Rightarrow A_I = - \frac{R_1 + R_2}{R_2}$

\begin{important}
È ideale in zona lineare.
\end{important}

\subsection{Feedback degli amplificatori}

\begin{figure}[H]
    \centering
    \begin{circuitikz}[american, transform shape]
        \draw (0,0) node[op amp] (opamp) {};
        \draw (opamp.+) to[short] (-1, -0.5) to[short] (-1.5, -0.5) node[left] {$V_S$};
        \draw (opamp.-) to[short] (-1, 0.5) to[R, l=$R_1$] (-2.5, 0.5) node[ground] {};
        \draw (-1, 0.5) to[short] (-1, 1.5) to[R, l=$R_2$] (1.2, 1.5) to[short] (1.2, 0) to[short] (opamp.out);
        \draw (opamp.out) to[short] (2, 0) node[right] {$V_{out}$};
        \node at (-1, -1.5) {Circuito lineare causale};
    \end{circuitikz}
\end{figure}

$V_d$ dipende dalla stessa $V_{out}$: $V_d = V_S - \frac{R_1}{R_1 + R_2} V_{out}$

\begin{figure}[H]
    \centering
    \begin{tikzpicture}
        \draw[->] (-2,0) node[left] {$X_{S}$} -- (-1,0);
        \draw (0,0) circle (10pt) node {$+$};
        \node at (-0.3,-0.3) {$-$};
        \draw[->] (0.35,0) -- (1,0) node[midway, above] {$X_{in}$};
        \draw (1,-0.5) rectangle (2.5,0.5) node[midway] {$A$};
        \node at (1.75, 0.7) {Guadagno};
        \draw[->] (2.5,0) -- (4,0) node[right] {$X_{out}$};
        \draw[->] (3.25,0) -- (3.25,-1.5) -- (2.5,-1.5);
        \draw (1,-2) rectangle (2.5,-1) node[midway] {$\beta$};
        \node at (1.75, -2.2) {Fattore di feedback (Anello di controllo)};
        \draw[->] (1,-1.5) -- (0,-1.5) -- (0,-0.35);
        \node at (-1.5,-1.5) {$X_{in} = X_S - \beta X_{out}$};
    \end{tikzpicture}
\end{figure}

\begin{itemize}
    \item $X_{in}(0) = X_S$, $X_{out}(0) = A X_{in}(0) = A X_S(0)$
    \item $X_{in}(1) = X_S - \beta X_{out}(0)$, $X_{out}(1) = A X_{in}(1)$
    \item $X_{in}(n) = X_S - \beta X_{out}(n-1)$, $X_{out}(n) = A X_{in}(n)$ : se $n \to \infty$ $X_{out}(n) \to X_{out} < \infty$ quindi $X_{out}(n-1) \simeq X_{out}(n)$
    \item $\hookrightarrow X_{out} = A (X_S - \beta X_{out}) \rightarrow X_{out} = X_S A / (1 + \beta A)$
\end{itemize}

\textbf{La successione in funzione di $\beta, A$:}
\begin{itemize}
    \item $A > 0, A\beta < -1 \Rightarrow$ la successione è monotona \textcolor{green}{crescente ($A X_S > 0$)} o \textcolor{green}{decrescente ($A X_S < 0$)}.
    \item $\Downarrow$
    \item divergente a valori $> 0$, divergente a valori $< 0$.
\end{itemize}

\begin{important}
Interpretazione fisica: il segnale esce dalla zona di linearità quando $X_{out}(n) \to \infty$ anche per la situazione di equilibrio (instabile) $A X_S = 0$.
\end{important}

Rumore = qualsiasi condizione di tipo aleatorio che può perturbare il segnale in ingresso.
$\Rightarrow$ Anche all'equilibrio ($A X_S = 0$), l'anello di controllo può essere animato dal rumore.
\begin{itemize}
    \item La successione è convergente $\Rightarrow \beta A > -1$ \textcolor{gray}{condizione necessaria per la convergenza}
\end{itemize}

\begin{important}
Interpretazione geometrica:
\begin{itemize}
    \item $X_{out} = A X_{in}$ relazione fra $X_{out}$ e $X_{in}$
    \item $X_{out} = \frac{X_S}{\beta} - \frac{X_{in}}{\beta}$ retta di carico
\end{itemize}
\textcolor{red}{gilbertina cara ricordati che se hai un valore $<0$ indicato da una lettera anche se il $-$ non lo vedi, cmq c'è :)}

\begin{itemize}
    \item $A > 0, \beta > 0, \beta A \leq -1 \Rightarrow \beta \leq -1/A < 0 \Rightarrow$ \textbf{nessuna retta così}
    \item $A > 0, \beta < 0, \beta A \leq -1 \Rightarrow \beta \leq -1/A < 0 \Rightarrow -1/\beta \leq A$: 1/3 intersezioni (1/2 sat)
    \item $A > 0, \beta > 0, \beta A > -1 \Rightarrow \beta > 0 > -1/A \Rightarrow -1/\beta < A$: 1 intersezione (lin/sat)
    \item $A > 0, \beta < 0, \beta A > -1 \Rightarrow 0 > \beta > -1/A \Rightarrow -1/\beta > A$: 1 intersezione (lin/sat)
\end{itemize}
\end{important}

\subsection{Applicazione ai circuiti con l'Op-Amp}
Caso ideale: $A_d = +\infty \Rightarrow \beta > -1/A_d = 0 \Rightarrow$ pendenza della retta di carico $< 0 \Rightarrow$ feedback negativo ($X_{in} = X_S - |\beta| X_{out}$).
'''

final_content = parts[0] + new_content + '\n' + end_marker + parts[1]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_content)

print('File repaired successfully.')