#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Initialize FileStorage instance"""
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self): 
        """Delete test JSON file"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test all method"""
        self.assertEqual(len(self.storage.all()), 0)
        self.storage.new(self.model)
        self.assertEqual(len(self.storage.all()), 1)

    def test_new(self):
        """Test new method"""
        self.storage.new(self.model)
        self.assertIn("BaseModel." + self.model.id, self.storage.all())

    def test_save(self):
        """Test save method"""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test reload method"""
        self.storage.save()
        storage2 = FileStorage()
        storage2.reload()
        self.assertEqual(len(storage2.all()), 1)

if __name__ == "__main__":
    unittest.main()
    