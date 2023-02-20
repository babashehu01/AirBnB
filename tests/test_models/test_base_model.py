#!/usr/bin/python3
"""Defines unittest for models/base_model.py"""

import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel_instantiation(unittest.TestCase):
    """Testing A new Model is instantiated correctly"""
    my_model1 = BaseModel()
    my_model2 = BaseModel()

    def test_id(self):
        """Testing that I get a unique Id each time an instance is created"""
        self.assertNotEqual(self.my_model1.id, self.my_model2.id)

    def test_datetimes(self):
        """Testing to see datetime is created correctly"""
        self.assertIsInstance(self.my_model1.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model1.updated_at, datetime.datetime)


class TestBaseModel_save(unittest.TestCase):
    """Testing the save method of my BaseModel"""

    def test_update(self):
        """Testing if the update time is updated"""
        self.my_model = BaseModel()
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)
