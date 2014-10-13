# !/usr/bin/python
# -*- coding: utf-8 -*-

# Práctica 3. SMIL, XML en Python
# Ej 6. Lee archivo .smil, descarga recursos remotos e imprime lista.
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
        parser = make_parser()
        smilHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(smilHandler)
        parser.parse(open(my_file))

        self.tag_list = smilHandler.get_tags()

    def __str__(self):
        """
        Método que imprime lista de etiquetas y atributos.
        """
        tag_list = ""
        for element in self.tag_list:
            # Índice par: etiqueta; índice impar: atributo
            if not self.tag_list.index(element) % 2:
                tag_list += element + '\t'
            else:
                for key in element:
                    if element[key] != "":
                        tag_list += '%s="%s"\t' % (key, element[key])
                tag_list += '\n'
        return tag_list

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
    print karaoke

    # Descarga de atributos remotos e impresión de lista con recursos en local
    karaoke.do_local()
    print karaoke
