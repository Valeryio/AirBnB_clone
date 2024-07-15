#!/usr/bin/python3

"""This module tests the City Class we have in our console
    program"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """This class tests all the attributes and properties of
        the class City

        Attributes:
            @cotonou (obj): A city object
    """

    def setUp(self):
        """This method sets up all the different attributes we need
            for the tests"""
        self.cotonou = City

    def test_state_id(self):
        """This test checks for the City.state_id attribute"""
        self.assertEquals(self.cotonou.state_id, "")

    def test_name(self):
        """This test checks for the City.name attribute"""
        self.assertEquals(self.cotonou.name, "")
