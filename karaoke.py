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


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):
    """
    Clase KaraokeLocal
    """

    def __init__(self, my_file):
        """
        Constructor. Parsea el fichero SMIL y obtiene etiquetas y atributos.
        """
        # Parseo del fichero SMIL
        parser = make_parser()
        smilHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(smilHandler)
        parser.parse(open(my_file))

        # Creación de lista con etiquetas y atributos
        self.tag_list = smilHandler.get_tags()

    def __str__(self):
        """
        Método que imprime lista de etiquetas y atributos.
        """
        for element in self.tag_list:
            # Índice par: etiqueta; índice impar: atributo
            if not self.tag_list.index(element) % 2:
                print element + '\t',
            else:
                for key in element:
                    print '%s= "%s"\t' % (key, element[key]),
                print

    def do_local(self):
        """
        Método que descarga recursos remotos e indica recurso en local.
        """
        for element in self.tag_list:
            # Miramos índices impares (atributos)
            if self.tag_list.index(element) % 2:
                for key in element:
                    if key == 'src':
                        if element[key].split(":")[0] == 'http':
                            os.system("wget -q " + element[key])
                            element[key] = element[key].split("/")[-1]

if __name__ == "__main__":
    # Toma de datos del usuario
    try:
        my_file = sys.argv[1]
    except IndexError:
        print ("Usage: python karaoke.py file.smil")

    # Instanciación del objeto
    karaoke = KaraokeLocal(my_file)

    # Impresión de lista de etiquetas y atributos
    tag_list = karaoke.__str__()

    # Descarga de atributos remotos e impresión de lista con recursos en local
    print
    tag_list = karaoke.do_local()
    tag_list = karaoke.__str__()
