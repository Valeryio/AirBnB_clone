#!/usr/bin/python3

"""This module tests the User Class we have in our console
    program"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """This class tests all the attributes and properties of
        the class User

        Attributes:
            @tom (obj): A user object
    """

    def setUp(self):
        """This method sets up all the different attributes we need
            for the tests"""
        self.tom = User

    def test_email(self):
        """This test checks for the User.email attribute"""
        self.assertEquals(self.tom.email, "")

    def test_password(self):
        """This test checks for the User.password attribute"""
        self.assertEquals(self.tom.password, "")

    def test_first_name(self):
        """This test checks for the User.first_name attribute"""
        self.assertEquals(self.tom.first_name, "")

    def test_last_name(self):
        """This test checks for the User.last_name attribute"""
        self.assertEquals(self.tom.last_name, "")