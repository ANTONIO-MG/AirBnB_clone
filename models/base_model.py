#!/usr/bin/python3
"""
This is the base or parent class for the Air B&B project, all the other classes
will inharit from this class, it is the main blueprint of the application

We use the UUID an the DATETIME packages, for creating a unique ID 
and date and time respectively

This model will be used to manipulate the console
"""

import uuid
from datetime import datetime
import json

class BaseModel():
    """
    The base class for the air B&B project
    
    attributes:
        id (str): the unique ID attributed to each object created
        created_at (str): the date and time of the object created
        updated_at (str): the date and time of the object's last modification
        
    """
    
    
    def __init__(self, id=None, created_at=None, updated_at=None):
        """
        initialisation of the baser class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    # def save(self):
        
    
    def to_dict(self, object):
        """
        takes a python and converts it to a dictionary
        
        args:
            object: the object to convert to a dictionary
        
        return:
            returns the dictionary representation of the object
        """
        pass
        
    
    
    def __str__(self):
        """
        the string representation
        
        returns:
            the string representation of the BaseModel
        """
        return "{} ({}) {}".format(BaseModel, self.id, self.__dict__)
        