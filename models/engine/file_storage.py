#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel

class FileStorage:
    """A class for serializing and deserializing objects to a JSON file."""

    __file_path: str = "file.json"
    __objects: dict = {}

    def all(self) -> dict:
        """Returns the dictionary containing all stored objects."""
        return self.__objects

    def new(self, obj):
        """Stores a new object in the internal dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes the objects dictionary to a JSON file."""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file back to the objects dictionary (if it exists)."""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass  # Ignore if file doesn't exist


