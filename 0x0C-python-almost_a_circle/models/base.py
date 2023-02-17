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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        l = []
        if list_objs is not None:
            for i in list_objs:
                l.append(i.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Square":
            m = cls(5)
        elif cls.__name__ == "Rectangle":
            m = cls(5, 5)
        m.update(**dictionary)
        return m



