#!/usr/bin/python3
"""User Module

This Module inherits from BaseModel class.
User Module contains the user information.

"""

from models.base_model import BaseModel
from models import storage
from datetime import datetime


class User(BaseModel):
    """
    Represents a User in the Airbnb application.

    Attributes:
        email:  (str) The email of the user.
        password: (str) The password of the user (hashed).
        first_name: (str) The first name of the user.
        last_name: (str) The last name of the user.
    """

    def __init__(self):
        """This method init a user class
        """
        super().__init__()
        print(self.__class__.__name__)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""


