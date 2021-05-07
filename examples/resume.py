#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/7 15:56
# @Author : 詹荣瑞
# @File : resume.py
# @desc : 本代码未经授权禁止商用
import os

from bonelate import render


def url(s):
    return render(r"\url{{{url}}}", {"url": s})


def figure(src):
    return render(r"""
    \begin{figure}
      \hfill
      \includegraphics[width=0.6\columnwidth]{{{src}}}
      \vspace{-7cm}
    \end{figure}
    """, {"src": src})


template = r"""
\documentclass[a4paper,12pt,final]{memoir}

% misc
\renewcommand{\familydefault}{bch}  % font
\pagestyle{empty}          % no pagenumbering
\setlength{\parindent}{0pt}      % no paragraph indentation


% required packages (add your own)
\usepackage{flowfram}                    % column layout
\usepackage{ctex}  
\usepackage[top=1cm,left=1cm,right=1cm,bottom=1cm]{geometry}% margins
\usepackage{graphicx}                    % figures
\usepackage{url}                      % URLs
\usepackage[usenames,dvipsnames]{xcolor}          % color
\usepackage{multicol}                    % columns env.
  \setlength{\multicolsep}{0pt}
\usepackage{paralist}                    % compact lists
\usepackage{tikz}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Create column layout
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% define length commands
\setlength{\vcolumnsep}{\baselineskip}
\setlength{\columnsep}{\vcolumnsep}

% frame setup (flowfram package)
% left frame
\newflowframe{0.2\textwidth}{\textheight}{0pt}{0pt}[left]
  \newlength{\LeftMainSep}
  \setlength{\LeftMainSep}{0.2\textwidth}
  \addtolength{\LeftMainSep}{2\columnsep}
% right frame
\newflowframe{0.7\textwidth}{\textheight}{\LeftMainSep}{0pt}[main01]

% horizontal rule between frames (using TikZ)
\renewcommand{\ffvrule}[3]{%
\hfill
\tikz{%
  \draw[loosely dotted,color=RoyalBlue,line width=1.5pt,yshift=-#1] 
  (0,0) -- (0pt,#3);}%
\hfill\mbox{}}
\insertvrule{flow}{1}{flow}{2}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% define macros (for convience)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Sep}{\vspace{1.5em}}
\newcommand{\SmallSep}{\vspace{0.5em}}

\newenvironment{AboutMe}
  {\ignorespaces\textbf{\color{RoyalBlue} 关于我}}
  {\Sep\ignorespacesafterend}

\newcommand{\CVSection}[1]
  {\Large\textbf{#1}\par
  \SmallSep\normalsize\normalfont}

\newcommand{\CVItem}[1]
  {\textbf{\color{RoyalBlue} #1}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Begin document
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{document}

% Left frame
%%%%%%%%%%%%%%%%%%%%
{{left}}
\framebreak

% Right frame
%%%%%%%%%%%%%%%%%%%%
{{right}}

\end{document}
"""
left = r"""
{{photo}}

\begin{flushright}\small
  {{name}}\\
  {{!infos}}
    {{.}}\\
  {{/infos}}
\end{flushright}\normalsize
"""
right = r"""
\Huge\bfseries {\color{RoyalBlue} {{name}}} \\
\Large\bfseries  {{occupation}} \\

\normalsize\normalfont

% About me
\begin{AboutMe}
  {{about}}
\end{AboutMe}

% Experience
{{!sections}}
    \CVSection{{{title}}}
    {{!items}}
        \CVItem{{{title}}}\\
        {{content}}
        \SmallSep
    {{/items}}
    \Sep
{{/sections}}

% Skills
\CVSection{技能}
\begin{multicols}{2}
  \begin{compactitem}[\color{RoyalBlue}$\circ$]
    {{!skills}}
        \item {{.}}
    {{/skills}}
  \end{compactitem}
\end{multicols}
"""


def generate_resume(data):
    return render(template, {
        "left": render(left, data),
        "right": render(right, data)
    })


if __name__ == '__main__':
    data = {
        "name": r"Bone\TeX{}",
        "infos": [url("bonetex@qq.com")],
        "occupation": "Python 项目",
        "about": r"Bone\TeX{} 是一个高效的LaTeX代码生成工具",
        "photo": figure("BoneTeX-LOGO.png"),
        "sections": [{
            "title": "经历",
            "items": [{
                "title": "睡觉",
                "content": "睡了三天",
            }],
        }, {
            "title": "获奖",
            "items": [{
                "title": "睡觉锦标赛",
                "content": "睡觉锦标赛获得第一名",
            }],
        }, ],
        "skills": [
            "优秀",
            "还是优秀",
        ]
    }

    with open("./.temp/temp.tex", mode="w", encoding="utf-8") as file:
        file.write(generate_resume(data))
    os.chdir(os.path.join(os.getcwd(), "./.temp"))
    os.system("xelatex ./temp.tex")
