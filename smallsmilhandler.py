# !/usr/bin/python
# -*- coding: utf-8 -*-

# Práctica 3. SMIL, XML en Python.
# Ejercicio 3. Definición de la clase SmallSMILHandler
# Autor: Álvaro Moles Vinader

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    """
    Clase SmallSMILHander
    """

    def __init__(self):
        """
        Constructor. Inicializa la lista de etiquetas y atributos.
        """
        self.tag_list = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            self.tag_list.append(name)

            width = attrs.get('width', "")
            height = attrs.get('height', "")
            backgnd_color = attrs.get('background-color', "")
            root_layout_attrs = {'width': width, 'height': height,
                'background-color': backgnd_color}

            self.tag_list.append(root_layout_attrs)

        elif name == 'region':
            self.tag_list.append(name)

            ident = attrs.get('id', "")
            top = attrs.get('top', "")
            bottom = attrs.get('bottom', "")
            left = attrs.get('left', "")
            right = attrs.get('right', "")
            region_attrs = {'id': ident, 'top': top, 'bottom': bottom,
                'left': left, 'right': right}

            self.tag_list.append(region_attrs)

        elif name == 'img':
            self.tag_list.append(name)

            src = attrs.get('src', "")
            region = attrs.get('region', "")
            begin = attrs.get('begin', "")
            dur = attrs.get('dur', "")
            img_attrs = {'src': src, 'region': region, 'begin': begin,
                'dur': dur}

            self.tag_list.append(img_attrs)

        elif name == 'audio':
            self.tag_list.append(name)

            src = attrs.get('src', "")
            begin = attrs.get('begin', "")
            dur = attrs.get('dur', "")
            audio_attrs = {'src': src, 'begin': begin, 'dur': dur}

            self.tag_list.append(audio_attrs)

        elif name == 'textstream':
            self.tag_list.append(name)

            src = attrs.get('src', "")
            region = attrs.get('region', "")
            textstream_attrs = {'src': src, 'region': region}

            self.tag_list.append(textstream_attrs)

    def get_tags(self):
        """
        Método que devuelve lista con etiquetas, atributos y contenido de ellos
        """
        return self.tag_list
