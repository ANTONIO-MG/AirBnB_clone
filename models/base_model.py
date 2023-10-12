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

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
    

