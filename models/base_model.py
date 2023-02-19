#!/usr/bin/python3
"""This module defines our BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This defines all common attributes/methods for other classes"""

    timestamp = datetime.now()
    class_name = 'BaseModel'

    def __init__(self):
        """Initalizes a new instance"""
        self.id = uuid4().hex
        self.created_at = self.timestamp
        self.updated_at = self.timestamp

    def __str__(self):
        """String representation of the instance"""
        return ('[{}] ({}) {}'.format(self.class_name, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = self.timestamp

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        dict_repr = self.__dict__
        dict_repr['__class__'] = self.class_name
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr
