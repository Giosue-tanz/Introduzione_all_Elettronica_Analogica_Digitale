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
% -- page 16 --
\begin{itemize}
    \item \textbf{esempio}: amplificatore non inverteute: $V_d = V_S - \beta V_{out} = V_S - \frac{R_1}{R_1 + R_2} V_{out} \rightarrow$ feedback$-$ ($\beta > 0$)
    \item \textbf{esempio}: amplificatore non inverteute triggerato: $V_d = - (V_S - \frac{R_1}{R_1 + R_2} V_{out}) \rightarrow$ feedback$+$ ($\beta < 0$)
\end{itemize}

\begin{important}
Il feedback positivo è un fenomeno NON LINEARE!!
\end{important}

\subsubsection*{Proprietà del feedback negativo}

\textbf{- Desensibilizzazione del guadagno:} 
$A = \left.\frac{V_{out}}{V_S}\right|_{\beta=0} = $ guadagno open-loop. \\
$A_f = \left.\frac{V_{out}}{V_S}\right|_{\beta>0} = $ guadagno closed-loop. \\
$\Rightarrow A_f = A (1 + \beta A)^{-1}$

$\hookrightarrow$ modifichiamo il circuito cercando di renderlo indipendente dai parametri costruttivi dei dispositivi che sono accompagnati da grande indeterminazione: $A \pm \sigma(A)$ \textcolor{gray}{grande}
\begin{align*}
    \Rightarrow \sigma(A_f) &= \left| \frac{\partial A_f}{\partial A} \right| \sigma(A) = \frac{\sigma(A)}{(1 + \beta A)^2} = \frac{A}{1 + \beta A} \frac{1}{1 + \beta A} \frac{\sigma(A)}{A} = \frac{A_f}{1 + \beta A} \frac{\sigma(A)}{A} \\
    \Rightarrow \sigma_{rel}(A_f) &= \frac{\sigma_{rel}(A)}{1 + \beta A} \ll \sigma_{rel}(A) \quad \text{se } A \gg 1.
\end{align*}
dove $\frac{1}{1 + \beta A}$ è il \textcolor{green}{fattore di desensibilizzazione del guadagno}.

$\ast$ anche se $A$ è fortemente indeterminato, fornisce solo il grado di approssimazione di $A_f$.

\textbf{- Adattamento delle impedenze:} \\
$\hookrightarrow$ modifichiamo $Z_{in F}$, $Z_{out F}$ rispetto a $Z_{in}$, $Z_{out}$.

\begin{figure}[H]
    \centering
    \begin{circuitikz}[american, transform shape]
        % Amplificatore
        \draw (0,0) rectangle (4,2.5);
        \node at (2,2) {$A_{V_{in}}$};
        \draw (0, 1.5) to[R, l=$Z_{in}$, v=$V_{in}$] (0, 0.5);
        \draw (4, 1.5) to[R, l_=$Z_{out}$] (2, 1.5) to[cV] (2, 0.5) to[short] (4, 0.5);
        
        % Rete di feedback
        \draw (0.5,-2) rectangle (3.5,-0.5) node[midway] {$\beta$};
        
        % Connessioni di ingresso (Serie)
        \draw (-2, 0.5) to[sV, l=$V_S$, i=$I_S$] (-2, 1.5) to[short] (0, 1.5);
        \draw (-2, 0.5) to[short] (-2, -1) to[short] (0.5, -1);
        \draw (0, 0.5) to[short] (0, -1.5) to[short] (0.5, -1.5);
        
        % Connessioni di uscita (Parallelo)
        \draw (4, 1.5) to[short] (5, 1.5) to[short, i=$I_{out}$] (6, 1.5) to[R, l=$R_L$] (6, 0.5) to[short] (5, 0.5) to[short] (4, 0.5);
        \node at (5, 1.5) [circle,fill,inner sep=1pt]{};
        \node at (5, 0.5) [circle,fill,inner sep=1pt]{};
        \draw (5, 1.5) to[short] (5, -1) to[short] (3.5, -1);
        \draw (5, 0.5) to[short] (5, -1.5) to[short] (3.5, -1.5);
        
        \node[right] at (6, 1.5) {$V_{out}$ sul carico};
        \node[right] at (6, 0.5) {$V_{out}$ su $R_L=\infty$};
        \node[right] at (6, -0.5) {$I_{out}$ su $R_L=0$};
    \end{circuitikz}
\end{figure}

\begin{itemize}
    \item $Z_{in F} = V_S / I_S$, $Z_{in} = V_{in} / I_S$ con $V_{in} = V_S - \beta V_{out}$ \\
          $= (1 + \beta A) Z_{in} \gg Z_{in}$ se $A \gg 1$.
    \item $Z_{out F} = V_{out} / I_{out}$, $Z_{out} = A V_{in} / I_{out}$ con $V_{out} = A_F V_S$, $V_{in} = V_S$ \\
          $= Z_{out} / (1 + \beta A) \ll Z_{out}$ se $A \gg 1$.
\end{itemize}

\begin{itemize}
    \item \textbf{esempio}: amplificatore non inverteute con $Z_{in} > 0$, $Z_{out} < \infty$
\end{itemize}

\begin{figure}[H]
    \centering
    \begin{circuitikz}[american, transform shape]
        \draw (0,0) node[op amp] (opamp) {};
        \draw (opamp.+) to[short] (-1.5, -0.5) node[left] {$V_S$};
        \draw (-1.5,-0.5) to[short, i=$I_S$] (opamp.+);
        \draw (opamp.-) to[short] (-1, 0.5) to[R, l=$R_1$] (-1, 2) node[ground] {};
        \draw (-1, 0.5) to[short] (-1, 1.5) to[R, l=$R_2$] (1.2, 1.5) to[short] (1.2, 0);
        \draw (opamp.out) to[R, l=$Z_{out}$] (2, 0) to[short, i=$I_{out}$] (3,0) to[R, l=$R_L$] (3,-2) node[ground] {};
        \node at (3,0) [right] {$V_{out}$};
        % Z_in internal to opamp
        \draw (opamp.+) to[short] (-0.5, -0.5) to[R, l=$Z_{in}$] (-0.5, 0.5) to[short] (opamp.-);
        \node at (1.5, -1.5) {\textcolor{green}{caso limite}};
    \end{circuitikz}
\end{figure}

\begin{itemize}
    \item $Z_{in F} = V_S / I_S = \infty$ perché considero $A_d = \infty \rightarrow$ CCV: $I_S = 0$ \\
          $\Rightarrow V_- = R_1 / (R_2 + R_1) V_{out} = V_+ = V_S \Rightarrow V_{out} = (1 + R_2/R_1) V_S$
    \item $Z_{out F} = V_{out} / I_{out} = 0$ perché $0 \neq V_- \propto V_{out} \rightarrow I_{out} = \infty$ per CCV
\end{itemize}

$\ast$ si può fare la stessa cosa ma con un generatore di corrente.
'''

final_content = parts[0] + new_content + '\n' + end_marker + parts[1]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_content)

print('Page 16 appended.')