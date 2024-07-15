#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
# from models.user import User


class FileStorage(BaseModel):
    """A class for serializing and deserializing objects to a JSON file."""

    def __init__(self):
        """This is the constructor of the class"""
        super().__init__()
        self.file_path = "file.json"
        self.objects = {}

    @property
    def file_path(self):
        """This is the getter of the __file_path private attribute"""
        return self.__file_path

    @property
    def objects(self):
        """This is the getter of the __objects private attribute"""
        return self.__objects

    @file_path.setter
    def file_path(self, path):
        """This is the setter of the private attribute __file_path

        Arguments:
            @path: (str), the path to the file to use by the class

        Raises:
            TypeError: If the path given is not a string
        """
        if type(path) is not str:
            raise TypeError()
        else:
            self.__file_path = path

    @objects.setter
    def objects(self, obj):
        """This is the setter of the private attribute __objects

        Arguments:
            @obj: (BaseModel), the new object to add
        """
        self.__objects = obj

    def all(self):
        """Returns the dictionary containing all stored objects."""
        return self.__objects

    def new(self, obj):
        """Stores a new object in the __objects attribute dictionary """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def update(self, obj):
        """Updates an object at this actual state in the program """
        for key, value in self.__objects.items():
            current_key = str(obj.__class__)+"."+obj.id
            if key == current_key:
                """The object is updated with the to_dict() method
                    which take in account all the new parameters of this
                    one """
                updated_obj = obj.to_dict()
                self.__objects[key] = updated_obj

    def save(self):
        """Serializes the objects dictionary to a JSON file."""
        new_object = {}

        """This loop return the object's value to their 'dict form'
            to do the serialisation
        """
        #
        # for key, value in self.__objects.items():
        #     if type(value) is BaseModel:
        #         new_object[key] = value.to_dict()

        for key, value in self.__objects.items():
            new_object[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(new_object, file, indent=4)

    def reload(self):
        """Deserializes the JSON file back to the objects dictionary
        (if it exists)"""
        try:
            with open(self.__file_path, "r") as file:
                reloaded_obj = json.load(file)
                for key, value in reloaded_obj.items():
                    self.__objects[key] = BaseModel(value)

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
            pass
