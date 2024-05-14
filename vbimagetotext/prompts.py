
prompt_assertion_reason = r"""
Please analyze the image provided and extract any questions present in the text. Format the questions in LaTeX format. If there are any diagrams present, please create only the TikZ environment with a node "Diagram" only, in the center environment. If there are any multiple-choice questions, please put the options in a tasks environment. If there are any assertion-reason type questions, use this code as reference
\begin{enumerate}
    \item[1. Assertion:] This is an assertion.
    \item[Reason:] This is a reason.
\end{enumerate}
Please provide only the enumerated part of the LaTeX file, not the whole LaTeX file.
"""

prompt_mcq = r"""
Please analyze the image provided and extract text from it and format it into latex. For question use \item , if there are any diagrams present, place it after \item part. For the options use tasks environment.
Use this code as reference for multiple-choice questions
    \item This is a question.
        \begin{center}
            \begin{tikzpicture}
                \node at (0, 0) {Diagram};
            \end{tikzpicture}
        \end{center}
        \begin{tasks}(2)
            \task Shorter Option 1
            \task Shorter Option 2
            \task Shorter Option 3\ans
            \task Shorter Option 4
        \end{tasks}

Please provide only the part above formatted of the LaTeX file, not the whole LaTeX document.
"""


prompt_mcq_list = r"""
Please analyze the image provided and extract any questions present in the text. Format the questions in LaTeX format. If there are any diagrams present, please create only the TikZ environment with a node "Diagram" only, in the center environment. If there are any multiple-choice questions, please put the options in a tasks environment.
Use this code as reference for multiple-choice questions
\begin{enumerate}
    \item This is a question.
        \begin{tasks}(2)
            \task Shorter Option 1
            \task Shorter Option 2
            \task Shorter Option 3\ans
            \task Shorter Option 4
        \end{tasks}
    \item This is another question.
        \begin{tasks}(1)
            \task Longer Option 1
            \task Longer Option 2
            \task Longer Option 3
            \task Longer Option 4\ans
        \end{tasks}
\end{enumerate}

Please provide only the enumerated part of the LaTeX file, not the whole LaTeX file.
"""

prompt_mcq_solution = r"""
Please analyze the image provided and extract any questions present in the text. Format the questions in LaTeX format. If there are any diagrams present, please create only the TikZ environment with a node "Diagram" only, in the center environment. If there are any multiple-choice questions, please put the options in a tasks environment.
Use this code as reference for multiple-choice questions
\begin{enumerate}
    \item This is a question.
        \begin{tasks}(2)
            \task Shorter Option 1
            \task Shorter Option 2
            \task Shorter Option 3\ans
            \task Shorter Option 4
        \end{tasks}
    \item This is another question.
        \begin{tasks}(1)
            \task Longer Option 1
            \task Longer Option 2
            \task Longer Option 3
            \task Longer Option 4\ans
        \end{tasks}
\end{enumerate}
Also if possible solve the problem and provide the solution in LaTeX format as well. Just below each question, use this code as reference for solutions
\begin{solution}
    \begin{align*}
        \intertext{Momentum of the ball will change only along the normal($x$ direction).}
        \vec{J} &= \vec{p}_f-\vec{p}_i\\
        &= m\vec{v}_f-m\vec{v}_i\\
        &= m\left(\dfrac{3}{4}v_0\hat{i}\right)-m\left(v_0\hat{i}\right)\\
        &= -\dfrac{1}{4}mv_0\hat{i}\\
        &= -\dfrac{5}{4}mv_0\hat{i}
    \end{align*}
\end{solution}
Try not to use any derived formula if possible, go with fundamentals and basics. Also if possible use align* environment for solutions. You can add descriptive text in between using \intertext{} command. Solve every question and provide the solution as well. Don't separate the question and solution. Solution should be just below the question.
Try to use the \ans command at the end of the correct option, but check the answer for sure before marking. 

Please provide only the enumerated part of the LaTeX file, not the whole LaTeX file.
"""


prompt_subjective = r"""
Please analyze the image provided and extract the texts from it and format it into latex. For question use \item , if there are any diagrams present, place it after \item part. Use this code as reference:

\item This is a sample question for subjective type. \underline{\hspace{2.5cm}}.
    \begin{center}
        \begin{tikzpicture}
            \node at (0, 0) {Diagram};
        \end{tikzpicture}
    \end{center}

Please provide only the part above formatted of the LaTeX file, not the whole LaTeX document.
"""

prompt_subjective_irodov = r"""
Please analyze the image provided and extract the texts from it and format it into latex. For question use \item , if there are any diagrams present, place it after \item part. If there are subquestions put them in enumerate env just below diagram or main question if diagram not available. Use this code as reference:

\item This is a sample question for subjective type.
    \begin{center}
        \begin{tikzpicture}
            \node at (0, 0) {Diagram};
        \end{tikzpicture}
    \end{center}
    \begin{enumerate}
        \item This is a subquestion.
        \item This is another subquestion.
    \end{enumerate}

Please provide only the part above formatted of the LaTeX file, not the whole LaTeX document.
"""

prompt_subjective_list = r"""
Extract Questions from Image and Format in LaTeX
Please analyze the image provided and extract any questions present in the text. Format the questions in LaTeX format. If there are any diagrams present, please create only the TikZ environment with a node "Diagram" only, put it within the center environment. For horizontal line use \underline{\hspace{2.5 cm}}. Please provide only the enumerated part of the LaTeX file, not the whole LaTeX file.
"""

prompt_match = r"""
Please analyze the image provided and extract the texts. Format these texts in LaTeX format like this, first put question in \item command, then diagram in tikz env nested within center env if there is any diagram present, then make the table for list/column/anything, then after put the options in a tasks environment. Use this below code as reference:

\item This is a sample question for matching type questions. There are two columns. Match column I with coulmn II. 

\begin{center}
    \begin{tikzpicture}
        \pic {frame=5cm};
    \end{tikzpicture}
\end{center}

\begin{center}
    \renewcommand{\arraystretch}{2}
    \begin{table}[h]
        \centering
        \begin{tabular}{p{0.25cm}p{8cm}|p{0.25cm}p{5cm}}
        \hline
        & Column I & &Column II \\
        \hline
        (a)& When the velocity of $3\kg$ block is $\dfrac{2}{3}\mps$ & (p) &Velocity of center of mass is $\dfrac{2}{3}\mps$\\
        (b)& When the velocity of $6\kg$ block is $\dfrac{2}{3}\mps$ & (q) &Deformation of the spring is zero\\
        (c)& When the speed of $3\kg$ block is minimum  & (r) &Deformation of the spring is maximum\\
        (d)& When the speed of $6\kg$ block is maximum & (s) &Both the blocks are at rest with respect to each other\\
        \hline
        \end{tabular}
    \end{table}
\end{center}

\begin{tasks}(2)
    \task $P \rightarrow 1$, $Q \rightarrow 2$, $R \rightarrow 3$, $S \rightarrow 4$
    \task $P \rightarrow 2$, $Q \rightarrow 1$, $R \rightarrow 4$, $S \rightarrow 3$
    \task $P \rightarrow 3$, $Q \rightarrow 4$, $R \rightarrow 1$, $S \rightarrow 2$
    \task $P \rightarrow 4$, $Q \rightarrow 3$, $R \rightarrow 2$, $S \rightarrow 1$
\end{tasks}

Please provide only the above described part of the LaTeX file, not the whole LaTeX file.
"""


prompt_comprehension = r"""
Please analyze the image provided and extract the texts. Format these texts in LaTeX format like this, first put a title in center env use \textsc for passage/comprehension/Paragraph/Question Stem title, then put the paragraph text without any env, then diagram in tikz env nested within center env if there is any diagram present, then questions each in \item command and for each question put the options in a tasks environment. Use this code as reference  

\begin{center}
    \textsc{Comprehension-II}
\end{center}

A uniform wire frame of linear mass density $\lambda$ having three sides each of length $2a$ is kept on a smooth horizontal surface. An impulse $J$ is applied at one end as shown in the figure. $P$ is the midpoint of $AB$. Now answer the following questions. 

\begin{center}
    \begin{tikzpicture}
        \pic[rotate=180] at (0, 0) {frame=3cm};
    \end{tikzpicture}
\end{center} 

\item The angular velocity of the system just after the impulse is
    \begin{tasks}(4)
        \task $\dfrac{3J}{22\lambda a^2}$\ans
        \task $\dfrac{J}{22\lambda a^2}$
        \task $\dfrac{2J}{22\lambda a^2}$
        \task $\dfrac{4J}{22\lambda a^2}$
    \end{tasks}

\item The velocity of point $P$ just after the impulse is
    \begin{tasks}(4)
        \task $\dfrac{J}{\lambda a}\hat{j}$
        \task $\dfrac{J}{6\lambda a}\hat{j}$
        \task $\dfrac{J}{\lambda a}\left(\dfrac{2}{11}\hat{i} + \dfrac{1}{6}\hat{j}\right)$
        \task $\dfrac{J}{\lambda a}\left(\dfrac{1}{11}\hat{i} + \dfrac{1}{6}\hat{j}\right)$\ans
    \end{tasks} 


Please provide only the above formatted part of the LaTeX file, not the whole LaTeX file.
"""


prompt_answer = """
Please analyze the image provided and extract the answers exercisewise in latex format. If possible use enumerate environment for answers. Give me only the document part of the LaTeX file, so that i can include it as a separate file into other document not the whole LaTeX file.
"""

prompt_solution = r"""
Following problem in in latex format, Please analyze the following question and if possible solve the problem and provide the solution in LaTeX format as well. Use this code as reference for solution
\begin{solution}
    \begin{align*}
        \intertext{Momentum of the ball will change only along the normal($x$ direction).}
        \vec{J} &= \vec{p}_f-\vec{p}_i\\
        &= m\vec{v}_f-m\vec{v}_i\\
        &= m\left(\dfrac{3}{4}v_0\hat{i}\right)-m\left(v_0\hat{i}\right)\\
        &= -\dfrac{1}{4}mv_0\hat{i}\\
        &= -\dfrac{5}{4}mv_0\hat{i}
        \interttext{Option (a) is correct.}
    \end{align*}
\end{solution}

Try not to use any derived formula if possible, go with fundamentals and basics also do not put numerical value at every step derive expression symbolically then at the end put numerical values. Also if possible use align* environment for solutions. You can add descriptive text in between using \intertext{} command.

Please provide only the solution part of the LaTeX file, not the whole LaTeX file.
"""


def switch_prompt(value):
    if value == "match":
        return prompt_match
    elif value == "mcq":
        return prompt_mcq
    elif value == "mcq_list":
        return prompt_mcq_list
    elif value == "mcq_solution":
        return prompt_mcq_solution
    elif value == "subjective":
        return prompt_subjective
    elif value == "subjective_list":
        return prompt_subjective_list
    elif value == "comprehension":
        return prompt_comprehension
    elif value == "assertion_reason":
        return prompt_assertion_reason
    elif value == "answer":
        return prompt_answer
    elif value == "solution":
        return prompt_solution
    elif value == "subjective_irodov":
        return prompt_subjective_irodov
    else:
        return value
