#!/usr/bin/python3

"""This module tests the Place Class we have in our console
    program"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """This class tests all the attributes and properties of
        the class Place

        Attributes:
            @novotel (obj): A place object
    """

    def setUp(self):
        """This method sets up all the different attributes we need
            for the tests"""
        self.novotel = Place

    def test_state_id(self):
        """This test checks for the Place.state_id attribute"""
        self.assertEquals(self.novotel.city_id, "")

    def test_user_id(self):
        """This test checks for the Place.user_id attribute"""
        self.assertEquals(self.novotel.user_id, "")

    def test_name(self):
        """This test checks for the Place.name attribute"""
        self.assertEquals(self.novotel.name, "")

    def test_description(self):
        """This test checks for the Place.description attribute"""
        self.assertEquals(self.novotel.description, "")

    def test_number_rooms(self):
        """This test checks for the Place.number_rooms attribute"""
        self.assertEquals(self.novotel.number_rooms, 0)

    def test_number_bathrooms(self):
        """This test checks for the Place.number_bathrooms attribute"""
        self.assertEquals(self.novotel.number_bathrooms, 0)

    def test_guest(self):
        """This test checks for the Place.guest attribute"""
        self.assertEquals(self.novotel.guest, 0)

    def test_price_by_night(self):
        """This test checks for the Place.price_by_night attribute"""
        self.assertEquals(self.novotel.price_by_night, 0)

    def test_latitude(self):
        """This test checks for the Place.latitude attribute"""
        self.assertEquals(self.novotel.latitude, 0.0)

    def test_longitude(self):
        """This test checks for the Place.longitude attribute"""
        self.assertEquals(self.novotel.guest, 0.0)


    def test_amenity_ids(self):
        """This test checks for the Place.amenity_ids attribute"""
        self.asertEquals(self.novotel.amenity_ids, [])