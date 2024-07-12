#!/usr/bin/env python3

import uuid
import models
from datetime import datetime

"""This is the module for the base model of all the class we will use
    through this project"""


class BaseModel:
    """This is the BaseModel class

        Attributes:
            id (str) : an uid assigned to each instance created
            created_at (datetime) : the date of creation of the instance
            updated_at (datetime) : the date of updating of the instance
    """

    def __init__(self, *args, **kwargs):
        """This is the constructor method

            Attributes:
                *args (list): a list of attribute
                **kwargs (dict): a dict of values
        """
        dformat = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        # If there is *args arguments, let's convert them to **kwargs...
        if args is not None and len(args) == 1:
            kwargs = args[0]

        if kwargs:
            known_args = ["created_at", "updated_at"]
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in known_args:
                        value = datetime.strptime(value, dformat)
                    self.__setattr__(key, value)
            # models.storage.new(self)
        # else:

            # models.storage.new(self)

    def __str__(self):
        """String representation of the class BaseModel"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """Returns a new customised __dict__ of the BaseModel current 
        object"""
        dtime_args = ["created_at", "updated_at"]
        new_dict = self.__dict__.copy()
        for i in dtime_args:
            new_dict[i] = datetime.isoformat(new_dict[i])

        new_dict["__class__"] = type(self).__name__
        return new_dict

    def save(self):
        """Assign the current datetime when an instance is created. This date
        will be updated every time the object changes"""
        self.updated_at = datetime.today()
        # models.storage.new(self)
        # models.storage.update(self)
        # models.storage.save()
