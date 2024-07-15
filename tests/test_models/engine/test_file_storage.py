import unittest
from models import storage
from models.engine.file_storage import FileStorage

"""This is the test file for the file_storage class"""


class TestFileStorage(unittest.TestCase):
    """This is the test class for the class FileStorage
    """

    def setUp(self):
        """This method sets up all the needed attributes
        for the others tests"""
        self.disk_1 = FileStorage()

    def test_objects(self):
        """This test checks for the FileStorage.__objects attribute"""
        self.assertEquals(self.disk_1.objects, {})

    def test_file_path(self):
        """THis test checks for the FileStorage.__file_path attribute"""
        pass

    def test_all(self):
        """This test checks for the FileStorage.all() method"""
        self.assertEqual(self.disk_1.all(), {})

    def test_new(self):
        """This test checks for the FileStorage.new() method"""
        pass

    def test_update(self):
        """This test checks for the FileStorage.update() method"""
        pass

    def test_save(self):
        """This test checks for the FileStorage.save() method"""
        pass

    def test_reload(self):
        """This test checks for the FileStorage.reload() method"""
        pass
