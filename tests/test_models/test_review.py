#!/usr/bin/python3

"""This module tests the Review Class we have in our console
    program"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """This class tests all the attributes and properties of
        the class Review

        Attributes:
            @comment (obj): A review object
    """

    def setUp(self):
        """This method sets up all the different attributes we need
            for the tests"""
        self.comment = Review

    def test_place_id(self):
        """This test checks for the Review.place_id attribute"""
        self.assertEquals(self.comment.place_id, "")

    def test_user_id(self):
        """This test checks for the Review.user_id attribute"""
        self.assertEquals(self.comment.user_id, "")

    def test_name(self):
        """This test checks for the Review.text attribute"""
        self.assertEquals(self.comment.text, "")