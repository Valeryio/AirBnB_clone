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
        # print("Here we have : ", obj.to_dict())
        self.__objects[key] = obj.to_dict()

    def update(self, obj):
        """
            This function updates an object at this actual
            state in the program
        """
        # print("Id of the objet : ", obj.id)
        for key, value in self.__objects.items():
            if value['id'] == obj.id:      
                # print("This obj exist")
                updated_obj = obj.to_dict()
                self.__objects[key] = updated_obj

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
            with open(self.__file_path, "r") as file:
                reloaded_obj = json.load(file)
                self.__objects = reloaded_obj

            """
                simplified_obj = {}

                print("This is our object : ", reloaded_obj)

                for key, value in reloaded_obj.items():
                    tmp_dict = {}
                    for second_key, second_value in value.items():
                        if second_key != "__class__":
                            tmp_dict[second_key] = second_value
                    simplified_obj[key] = tmp_dict
                
                self.__objects = simplified_obj
            """
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
            print("The file have not been found!")
            pass  # Ignore if file doesn't exist
