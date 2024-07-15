#!/usr/bin/python3
"""Review Module

This Module inherits from BaseModel class.
Review Module contains the attributes to be assigned
to the Review.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class

    Attributes:
        place_id (str): The id of the place
        user_id (str): The id of the user
        text (str): the review of the user
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        """This methods init the class"""
        super().__init__()
