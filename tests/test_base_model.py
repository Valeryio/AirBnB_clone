#!/usr/bin/python3

import unittest

# This module contains the test for the basic model_base

from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_attributes(self):
        """
            This is a simple test to check if the id is well written
        """
        self.assertIsInstance(self.b1.id, str)
        self.assertNotEqual(self.b1.id, self.b2.id)
        
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)

    def test_str(self):
        """
            This is a test for the str dundle method
        """
        result = f"[{type(self.b2).__name__}] ({self.b2.id}) {self.b2.__dict__}"
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
