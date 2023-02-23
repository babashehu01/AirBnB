#!/usr/bin/python3
"""This module defines our BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This defines all common attributes/methods for other classes"""

    def __init__(self, **kwargs):
        """Initalizes a new instance"""
        self.id = uuid4().hex
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if key != '__class__':
                if key in ['created_at', 'updated_at']:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

    def __str__(self):
        """String representation of the instance"""
        return ('[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        dict_repr = self.__dict__
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr
