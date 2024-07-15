#!/usr/bin/python3
"""Place Module

This Module inherits from BaseModel class.
Place Module contains the attributes to be assigned
to the Place.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class

    Attributes:
        name (str): The State name
        city_id (int): id of the city
        user_id (int): id of the user
        name (string): name of the place
        description (string): Description of the place
        number_rooms (int): number of rooms of the place
        number_bathrooms (int): number of bathrooms at the place
        max_guest (int): number of guest at the place
        price_by_night (int): the price for a night at the place
        latitude (float): the latitude of the place
        longitude (float): the longitude of the place
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self):
        """This methods init the class"""
        super().__init__()
