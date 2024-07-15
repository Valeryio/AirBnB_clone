#!/usr/bin/python3

"""This module tests the State Class we have in our console
    program"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """This class tests all the attributes and properties of
        the class State

        Attributes:
            @benin (obj): A state object
    """

    def setUp(self):
        """This method sets up all the different attributes we need
            for the tests"""
        self.benin = State

    def test_name(self):
        """This test checks for the State.name attribute"""
        self.assertEquals(self.benin.name, "")
