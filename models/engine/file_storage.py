#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        slef.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                # for key, value in obj_dict.items():
                #     cls_name, obj_id = key.split('.')
                #     cls = BaseModel
                #     if cls_name == "User":
                #         from models.user import User
                #         cls = User
                #     obj = cls(**value)
                #     self.__objects[key] = obj
        except FileNotFoundError:
            pass
