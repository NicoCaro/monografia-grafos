'''
Script de limpieza (Python 3). Borra las extensiones producidas
al generar las imagenes y mueve los .pdf's resultantes a la carpeta
'../pdf/'

Se Agrega Try + catch para compatiblidad con Windows. En linux
basta con os.rename, en Windows es neceesario eliminar el pdf
previo.
'''

import os
from path import Path

dir_path     = os.path.dirname(os.path.realpath(__file__))
dir_path , _ = os.path.split(dir_path)

tikz_folder = Path(dir_path + '\\tikz\\')
pdf_folder  = Path(dir_path + '\\pdf\\')

files = tikz_folder.walkfiles('*')

ext = ['.aux','latexmk','.fls','.log','gz']
ext = ['*' + e for e in ext]

for e in ext:
    files = tikz_folder.walkfiles(e)
    for file in files:
        file.remove()

pdfs = tikz_folder.walkfiles('*.pdf')
for file in pdfs:
    _ , name = os.path.split(file)
    try:
        os.rename(file, pdf_folder+name)
    except:
        os.remove(pdf_folder + name)
        os.rename(file, pdf_folder + name)
