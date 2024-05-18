#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage(BaseModel):
    """
        This is the storage class that inherits from the BaseModel

        Attributes:
            __file_path (str): the path to the files
            __objects (obj): the object to store
    """

    def __init__(self):
        """
            This is the constructor method

            Attributes:

        """
        self.__file_path = "file.json"
        self.__objects = ""


    def all(self):
        """
            Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            Sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[obj.id] = obj

    def save(self): 
        """
            Serializes __objects to the JSON file (path: __file_path)
        """
        try:
            with open(self.__file_path, "w") as file:
                json.dump(self.__objects, file)
        except FileNotFoundError:
            print("File not found")
            pass

    def reload(self): 
        """
            Deserializes the JSON file to __objects (only if the JSON file 
            (__file_path) exists ; otherwise, do nothing. If the file doesn’t
            exist, no exception should be raised)
        """
        try:
            with open(self.__file_path) as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            print("File not found")
            pass