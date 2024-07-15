#!/usr/bin/python3
"""Amenity Module

This Module inherits from BaseModel class.
Amenity Module contains the attributes to be assigned
to the amenities.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """State Class

    Attributes:
        name (str): The State name

    """
    name = ""

    def __init__(self):
        """This methods init the class"""
        super().__init__()
