#!/usr/bin/python3
"""This module is the file storage class for AirBnB clone"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file
    Attributes:
        __file_path: path to the JSON file
        __objects: storage for objects
        """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of instantiated objects in __objects.

        if a cls is specified, the dictionary of the object is returned.
        else, return the __objects dictionary
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
                    return (dic)
                else:
                    return self.__objects

    def new(self, obj):
        """Sets __objects to obj"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Directs file path to JSON"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
            with open(self.__file_path, 'w', encoding="UTF-8") as f:
                json.dump(my_dict, f)

    def reload(self):
        """Loads storage dictionary from file
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f).items ():
                        value = eval(value["__class__"])(**value)
                        self.__objects[key] = value
        except FileNotFoundError:
            pass

        def delete(self, obj=None):
        """delete an existing element
        """
        if obj:
        key = "{}.{}".format(type(obj).__name__, obj.id)
        del self.__objects[key]

            def close(self):
                """reloads by using the reload method"""
                self.reload()
