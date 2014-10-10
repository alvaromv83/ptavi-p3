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
        Constructor. Inicializamos las variables.
        """
        self.root_layout_attrs = {}
        self.region_attrs = {}
        self.img_attrs = {}
        self.audio_attrs = {}
        self.textstream_attrs = {}

        self.tag_list = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            self.tag_list.append(name)

            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.backgnd_color = attrs.get('background-color', "")
            self.root_layout_attrs = {'width': self.width,
                'height': self.height, 'background-color': self.backgnd_color}

            self.tag_list.append(self.root_layout_attrs)

        elif name == 'region':
            self.tag_list.append(name)

            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            self.region_attrs = {'id': self.id, 'top': self.top,
                'bottom': self.bottom, 'left': self.left, 'right': self.right}

            self.tag_list.append(self.region_attrs)

        elif name == 'img':
            self.tag_list.append(name)

            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.img_attrs = {'src': self.src, 'region': self.region,
                'begin': self.begin, 'dur': self.dur}

            self.tag_list.append(self.img_attrs)

        elif name == 'audio':
            self.tag_list.append(name)

            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.audio_attrs = {'src': self.src, 'begin': self.begin,
                'dur': self.dur}

            self.tag_list.append(self.audio_attrs)

        elif name == 'textstream':
            self.tag_list.append(name)

            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.textstream_attrs = {'src': self.src, 'region': self.region}

            self.tag_list.append(self.textstream_attrs)

    def get_tags(self):
        """
        Método que devuelve lista con etiquetas, atributos y contenido de ellos
        """
        return self.tag_list
