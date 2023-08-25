#!/usr/bin/python3

'''
Module containng the base class from which all other classes inherit from
'''
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, String, DateTime

Base = declarative_base()


class BaseModel:
    '''Base class from which all other classes inherit from'''
    id = Column(VARCHAR(45), primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        if updated_at is None:
            self.updated_at = datetime.now
        else:
            self.updated_at = updated_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__repr__}"

    def save(self):
        self.updated_at = datetime.now()
        models.Storage.new(self)
        models.Storage.save()
    
    def close(self):
       models.Storage.close()

    def delete(self):
        models.Storage.delete(self)
