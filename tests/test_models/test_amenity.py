#!/usr/bin/python3

"""This module tests the Amenity Class we have in our console
    program"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """This class tests all the attributes and properties of
        the class Amenity

        Attributes:
            @amenity (obj): A amenity object
    """

    def setUp(self):
        """This method sets up all the different attributes we need
            for the tests"""
        self.amenity = Amenity

    def test_name(self):
        """This test checks for the Amenity.name attribute"""
        self.assertEquals(self.amenity.name, "")