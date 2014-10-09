# !/usr/bin/python
# -*- coding: utf-8 -*-

# Práctica 3. SMIL, XML en Python
# Ejercicio 4. Lee archivo .smil y devuelve lista con etiquetas y atributos
# Autor: Álvaro Moles Vinader

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import os

# Toma de datos del usuario
try:
    my_file = sys.argv[1]
except IndexError:
    print ("Usage: python karaoke.py file.smil")

# Parseo del fichero SMIL
parser = make_parser()
smilHandler = smallsmilhandler.SmallSMILHandler()
parser.setContentHandler(smilHandler)
parser.parse(open(my_file))

# Creación de lista
tag_list = smilHandler.get_tags()

# Impresión de lista con formato
for element in tag_list:
    # Si el índice es par el elemento es etiqueta, si es impar es atributo
    if not tag_list.index(element) % 2:
        print element + '\t',
    else:
        for key in element:
            if key == 'src':
                # Si el atributo es remoto descargamos y acortamos nombre
                if element[key].split(":")[0] == 'http':
                    resource = element[key]
                    os.system("wget -q " + resource)
                    element[key] = element[key].split("/")[-1]
            print '%s= "%s"\t' % (key, element[key]),
        print
