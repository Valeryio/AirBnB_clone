import unittest
from models.engine.file_storage import FileStorage

"""
    This is the test file for the file_storage class
"""


class TestFileStorage(unittest.TestCase):
    """This is the test class for the class FileStorage
    """

    def setUp(self):
        """This method sets up all the needed attributes
        for the others tests"""
        self.disk_1 = FileStorage()

    def test_objects(self):
        """This test checks for the __objects attribute"""
        self.assertEquals(self.disk_1.objects, {})
