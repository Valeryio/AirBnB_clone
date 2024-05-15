#!/usr/bin/python3

import uuid

"""
    This is the module for the base model of all the class we will use
    through this project
"""

class BaseModel():
    """
        This is the BaseMOdel class

    Attributes:
       id (str) : an uid assigned to each instance created
    """

    def __init__(self):
        self.id = str(uuid.uuid4())


    def created_at(self):
        """
            This public method assign the current datetime when an instance
            is created
        """
        pass

    def updated_at(self):
        """
            This public method assign the current datetime when an instance
            is created and it will be updated every time the object changes.
        """
        pass

