#!/usr/bin/python3

""" City Module

    This module contains the definition, all the attributes
    and the methods of the class City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
        The class BaseModel

        Attributes:
            state_id (int): the id of the state
            name (str): the name of the state
    """
    
    state_id = ""
    name = ""

    def __init__(self):
        """This method init the class"""
        super().__init__()
