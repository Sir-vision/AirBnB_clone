#!/usr/bin/python3
""" This module creates a class `FileStorage` """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
    Write a class FileStorage that serializes instances \
    to a JSON file and deserializes JSON file to instances:
"""


class FileStorage():
    """
        Representation of class storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary `__objects` """

        return self.__objects

    def new(self, obj):
        """ sets in `__objects` the `obj` with key `<obj class name>.id` """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes `__objects` to the JSON file """

        with open(self.__file_path, "w", encoding="utf-8") as f:
            j_file = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(j_file, f)

    def reload(self):
        """ Reloads the stored objects """

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
