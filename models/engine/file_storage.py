#!/usr/bin/python3

from models.base_model import BaseModel


class FileStorage(BaseModel):
    """
        This is the storage class that inherits from the BaseModel

        Attributes:
            __file_path (str): the path to the files
            __objects (obj): the object to store
    """

    def __init__(self):
        pass