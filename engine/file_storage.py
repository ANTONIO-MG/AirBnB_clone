#!/usr/bin/python3
import json
import os

class FileStorage:
    """File storage class for handling objects"""

    # The path to the JSON file where objects will be serialized
    __file_path = "path/to/your/json/file.json"

    # Dictionary to store objects in memory
    __objects = {}

    def all(self):
        """Return all objects as a dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the dictionary of objects"""
        # Generate a unique key for the object by combining class name and ID
        key = obj.__class__.__name__ + "." + obj.id
        # Store the object in the dictionary using the generated key
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file"""
        # Prepare a dictionary to hold object data
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

        # Write the object data to the JSON file
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize objects from the JSON file"""
        if os.path.exists(FileStorage.__file_path):
            # If the JSON file exists, read its contents
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Iterate through the data and reconstruct objects
            for key, value in data.items():
                # Extract class name and ID from the key
                class_name, obj_id = key.split(".")
                class_ = class_name

                # Dynamically import the class
                cls = __import__("models." + class_name, fromlist=[class_name])
                obj = cls()

                # Set object attributes using the deserialized data
                for k, v in value.items():
                    setattr(obj, k, v)

                # Store the reconstructed object in the dictionary
                FileStorage.__objects[key] = obj
