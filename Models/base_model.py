#!/usr/bin/python3

'''
Module containng the base class from which all other classes inherit from
'''
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, DateTime
from os import getenv
# import json
from sqlalchemy import create_engine

Base = declarative_base()

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    '''Base class from which all other classes inherit from'''

    id = Column(VARCHAR(45), primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self, id, created_at, updated_at=None):
        self.id = id
        if created_at is None:
            self.created_at = datetime.now()
        else:
            self.created_at = datetime.strptime(created_at, time)
        if updated_at is None:
            self.updated_at = datetime.now()
        else:
            self.updated_at = updated_at

    def reload(self):
        models.storage.reload()

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)
    
    def get_attributes(self):
        # Define a list of attributes to exclude
        excluded_attributes = [
            '_sa_class_manager',
            '_sa_instance_state',
            '_sa_registry',
            'metadata',
            'registry',
            'members',  # Example attribute, add more if needed
        ]

        # Create a dictionary to store the filtered attributes
        attributes_dict = {}

        # Iterate through the object's attributes
        for key, value in self.__dict__.items():
            if key not in excluded_attributes:
                attributes_dict[key] = value

        return attributes_dict

    def close(self):
        models.storage.close()
