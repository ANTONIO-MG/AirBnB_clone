#!/usr/bin/python3
"""Defines the BaseModel class for the AirBnB clone"""

import uuid
from datetime import datetime

class BaseModel:
  """Represents the base model for the AirBnB clone project"""

  def __init__(self):
    """Initialize a new BaseModel instance"""
    self.id = str(uuid.uuid4())
    self.created_at = datetime.now()
    self.updated_at = datetime.now()

  def __str__(self):
    """Return string representation of BaseModel class"""
    ...
  
  def save(self):
    """Update the updated_at attribute with current time"""
    ...
    
  def to_dict(self):
    """Return dict representation of BaseModel instance"""
    ...
    
    # code ends here _______________________________________________

        
