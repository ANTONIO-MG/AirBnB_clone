#!/usr/bin/python3
"""
This module defines the BaseModel class for AirBnB objects
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    Base class for all AirBnB objects
    """
    def __init__(self):
        """
        Initialize a new instance of the BaseModel class
        """
        self.id = str(uuid.uuid4())  # Generate a unique ID for the object
        self.created_at = datetime.now()  # Set the creation time
        self.updated_at = datetime.now()  # Set the last update time

    def __str__(self):
        """
        Return a string representation of the BaseModel instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute to the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the instance
        """
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
