import sys

filepath = '/home/giosue/Scrivania/Elettronica digitale/Elettronica analogica digitale.tex'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(r'\usepackage{amsmath,amssymb}', r'\usepackage{amsmath,amssymb,mathtools,extpfeil}')

new_env = r'''
\usepackage[skins,breakable]{tcolorbox}
\newenvironment{important}
{\begin{tcolorbox}[colback=notered!5!white,colframe=notered!75!black,title=\textbf{Importante}]}
{\end{tcolorbox}}
'''
content = content.replace(r'\usepackage{ccicons}', r'\usepackage{ccicons}' + '\n' + new_env)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Preamble fixed.')