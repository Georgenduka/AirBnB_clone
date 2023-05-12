#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage():
    def __init__(self):
        __file_path = "file.json"
        __objects = {}

    def all(self):
            return __objects

    def new(self, obj):
            key = obj.__class__.__name__ + '.' + obj.id
            __objects[key] = obj.__dict__

    def save(self):
            with open(__file_path, 'w+', encoding="utf-8") as f:
                json.dump(__objects, f)

    def reload(self):
            try:
                with open(__file_path, 'r+', encoding="utf-8") as f:
                    json.load(__objects, f)
            except FileNotFoundError:
                return
