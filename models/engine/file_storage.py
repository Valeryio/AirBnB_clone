#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
#from models.user import User


class FileStorage:
    """A class for serializing and deserializing objects to a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """Returns the dictionary containing all stored objects."""
        return self.__objects

    def new(self, obj):
        """Stores a new object in the internal dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        print("Here we have : ", obj.to_dict())
        self.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes the objects dictionary to a JSON file."""
        #obj_dict = {obj: obj.to_dict() for obj in self.__objects.keys()}

        #print("Our object is : ", self.__objects)
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file, indent=4)

    def reload(self):
        """Deserializes the JSON file
        back to the objects dictionary (if it exists).
        """
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
            """
                class_mapping = {"User": User}  # Example class mapping
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    del value["__class__"]  # Remove "__class__"
                    if cls_name in class_mapping:
                        self.new(class_mapping[cls_name](**value))
                    else:
                        print(f"Unknown class: {cls_name}")
            """
        except FileNotFoundError:
            pass  # Ignore if file doesn't exist
