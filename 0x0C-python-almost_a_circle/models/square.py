#!/usr/bin/python3
"""
Module containing the class 'Square' that inherits from the class 'Rectangle'
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """ A Square is a special Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ instantiation """
        super().__init__(size, size, x, y, id)
