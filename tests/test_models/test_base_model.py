#!/usr/bin/python3

# This module contains the test for the basic model_base

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_id(self):
        """This test checks for the BaseMode.id attribute"""
        self.assertIsInstance(self.b1.id, str)
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_created_at(self):
        """This test checks for the BaseModel.created_at attribute"""
        self.assertIsInstance(self.b1.created_at, datetime)

    def test_updated_at(self):
        """This test checks for the BaseMode.updated_at attribute"""
        self.assertIsInstance(self.b1.updated_at, datetime)

    def test_attributes(self):
        """
            This is a simple test to check if the id is well written
        """
        pass

    def test_str(self):
        """
            This is a test for the str dundle method
        """
        result = (f"[{type(self.b2).__name__}] ({self.b2.id})"
                  f"{self.b2.__dict__}\n")
        self.assertEqual(self.b2.__str__(), result)

    def test_save(self):
        """
            That is the test for the save method
        """
        previous_update = self.b2.updated_at
        self.b2.save()
        current_update = self.b2.updated_at
        self.assertNotEqual(previous_update, current_update)

    def test_to_dict(self):
        result = self.b2.to_dict()
        self.assertIsInstance(result['updated_at'], str)
        self.assertIsInstance(result['created_at'], str)
