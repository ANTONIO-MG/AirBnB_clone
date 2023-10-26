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


class BaseModel():
    """
    The base class for the air B&B project

    attributes:
        id (str): the unique ID attributed to each object created
        created_at (str): the date and time of the object created
        updated_at (str): the date and time of the object's last modification
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of the base class
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            created_at = datetime.now()
            updated_at = datetime.now()
            self.created_at = created_at
            self.updated_at = updated_at
        else:
            for key, value in kwargs.items():
                if (key == "__class__"):
                    pass
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

    def save(self):
        """
        update the updated_at attribute
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        takes a python and converts it to a dictionary

        return:
            returns the dictionary representation of the object
        """
        new_dict = self.__dict__
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        # self.__dict__["id"] = str(self.id)
        return new_dict

    def __str__(self):
        """
        the string representation of the object

        returns:
            the string representation of the BaseModel
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    
