'''
Script de limpieza (Python 3). Borra las extensiones producidas
al generar las imagenes y mueve los .pdf's resultantes a la carpeta
'../pdf/'
'''

import os
from path import Path

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))

files = dir_path.walkfiles('*')

ext = ['.aux','latexmk','.fls','.log','gz']
ext = ['*' + e for e in ext]

for e in ext:
    files = dir_path.walkfiles(e)
    for file in files:
        file.remove()

pdfs = dir_path.walkfiles('*.pdf')

for file in pdfs:
    os.rename(file,'../pdf')
