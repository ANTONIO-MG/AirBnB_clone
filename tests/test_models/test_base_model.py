#!/usr/bin/python3
"""Unit tests for BaseModel class of AirBnB clone"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
  """Test cases for BaseModel class"""

  def test_init(self):
    """Test initialization of BaseModel instance"""
    model = BaseModel()
    self.assertEqual(type(model.id), str)
  
  def test_save(self):
    """Test save method updates updated_at"""
    ...