# !/usr/bin/python
# -*- coding: utf-8 -*-

# Práctica 3. SMIL, XML en Python
# Ejercicio 4.
# Autor: Álvaro Moles Vinader

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys

# Toma de datos del usuario
try:
	my_file = sys.argv[1]
except IndexError:
	print ("Usage: python karaoke.py file.smil")

parser = make_parser()
smilHandler = smallsmilhandler.SmallSMILHandler()
parser.setContentHandler(smilHandler)
parser.parse(open(my_file))

print smilHandler.get_tags()
