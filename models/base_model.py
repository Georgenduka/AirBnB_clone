#!/usr/bin/python3
"""Module defines a base class for other classes"""
import cmd
import uuid
from datetime import datetime
#from models.engine.file_storage import FileStorage


class BaseModel():
    """Class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Instantiates a new object with variable number of arguments"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    format = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[key] = datetime.strptime(value, format)
                else:
                    self.__dict__[key] = value


        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns string representation of object"""
        return ("[{}] ({}) {}".format(
                    self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Updates current datetime when changes are made to object"""
        self.updated_at = datetime.now()
#        storage.save()

    def to_dict(self):
        """Returns dictionary containing key/
            value pairs of __dict__ attribute of object"""
        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
