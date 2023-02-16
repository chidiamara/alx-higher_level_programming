#!/usr/bin/python3
"""
Module containing one class: "Base" which will be the base of all
other classes in this project
"""
import json

class Base:
    """
    class goal: to manage "id" attribute in all future classes and to avoid
    duplicating the same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiation """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
