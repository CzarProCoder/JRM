#!/usr/bin/python3

'''
Module containng the base class from which all other classes inherit from
'''
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, String, DateTime

Base = declarative_base()

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    '''Base class from which all other classes inherit from'''

    id = Column(VARCHAR(45), primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self, id: str, created_at: datetime, updated_at: datetime = None):
        self.id = id
        if created_at is None:
            self.created_at = datetime.now()
        else:
            self.created_at = datetime.strptime(created_at, time)
        if updated_at is None:
            self.updated_at = datetime.now()
        else:
            self.updated_at = updated_at

    def __str__(self):  
        return f"[{self.__class__.__name__}] ({self.id}) {self.__repr__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)

    def close(self):
       models.storage.close()
