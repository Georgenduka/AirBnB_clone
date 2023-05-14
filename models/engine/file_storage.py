#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
            return self.__objects

    def new(self, obj):
            key = obj.__class__.__name__ + '.' + obj.id
            self. __objects[key] = obj

    def save(self):
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dicti()

            with open(self.__file_path, mode='w+', encoding="utf-8") as f:
                json.dump(new_dict, f)

    def reload(self):
            try:
                with open(self.__file_path, mode='r') as f:
                    new_dict = json.load(f)
                    for value in new_dict.values():
                        class_name = value["__class__"]
                        del value["__class__"]
                        self.new(eval(class_name)(**value))
            except FileNotFoundError:
                return
