#!/usr/bin/python3

import unittest

# This module contains the test for the basic model_base

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.b1 = BaseModel()

    def test_uuid(self):
        """
            This is a simple test to check if the id is well written
        """
        self.assertIsNot(self.b1.id, None)


