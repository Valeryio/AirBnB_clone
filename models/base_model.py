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

    def __setattr__(self, name, value):
        """
            This method is called each time an atttribute of instance is
            created, so I modified it to update the instance each time
            this one is modified (have a new attribute by example)
        """
        if name != "updated_at":
        """
            This condition prevent recursion Error cause, the save() method
            update the attribute updated_at, and it calls the __setattr__
            dunder's method. Prevent the recursion with a condition
        """
            self.save()
        super().__setattr__(name, value)

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
            Change to dict the arg of the public instance
        """
        self.__dict__["__class__"] = type(self).__name__
        return self.__dict__

    def save(self):
        """
            This public method assign the current datetime when an instance
            is created and it will be updated every time the object changes.
        """
        self.updated_at = datetime.isoformat(datetime.today())
