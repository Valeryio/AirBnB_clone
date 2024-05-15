#!/usr/bin/python3

import uuid
from datetime import datetime

"""
    This is the module for the base model of all the class we will use
    through this project
"""

class BaseModel():
    """
        This is the BaseMOdel class

    Attributes:
       id (str) : an uid assigned to each instance created
       created_at (datetime) : the date of creation of the instance
       updated_at (datetime) : the date of updating of the instance
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.isoformat(datetime.today())

    def __str__(self):
        return "{self.__name__} + {self.id} <{self.__dict__}>"

    def to_dict(self):
        """
            Change to dict the arg of the public instance
        """
        pass

    def save(self):
        """
            This public method assign the current datetime when an instance
            is created and it will be updated every time the object changes.
        """
        pass

