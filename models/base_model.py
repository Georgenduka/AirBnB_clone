#!/usr/bin/python3
import cmd
import uuid
from datetime import datetime

class BaseModel():

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == __class__:
                    continue
                elif key == "created_at" or key == "updated_at":
                    format = '%Y %m %dT %H:%M:%S.%f'
                    self.__dict__[key] = datetime.strptime(self.__dict__[value], format)
                else:
                    self.__dict__[key] = value

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
