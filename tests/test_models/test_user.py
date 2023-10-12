#!/usr/bin/python3
"""
This module defines the User class for AirBnB objects
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    User class for AirBnB objects
    """
    def __init__(self):
        """
        Initialize a new instance of the User class
        """
        super().__init__()  # Call the constructor of the BaseModel
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

