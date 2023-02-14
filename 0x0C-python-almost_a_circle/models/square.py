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

    def __str__(self):
        """ the string representation of an object  """""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value
