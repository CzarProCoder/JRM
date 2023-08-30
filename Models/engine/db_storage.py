#!/usr/bin/python3

'''
Module defining the type of storage in use
'''

import models
from models.members import Members
from models.savings_accounts import SavingsAccounts
from models.loans import Loans
from models.payments import Payments
from models.transactions import Transactions
from models.documents import Documents
from models.base_model import Base
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine, ForeignKey, Column
from sqlalchemy import String, Integer, CHAR, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


classes = {"Members": Members,
           "SavingsAccounts": SavingsAccounts,
           "Documents": Documents,
           "Loans": Loans,
           "Payments": Payments,
           "Transactions": Transactions}

class DBStorage:
    '''
    Class defining the database storage setup and configurations
    '''
    __engine = None
    __session = None

    def __init__(self):
       JRM_MYSQL_USER = getenv('JRM_MYSQL_USER')
       JRM_MYSQL_PWD = getenv('JRM_MYSQL_PWD')
       JRM_MYSQL_HOST = getenv('JRM_MYSQL_HOST')
       JRM_MYSQL_DB = getenv('JRM_MYSQL_DB')
       self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(JRM_MYSQL_USER,
                                             JRM_MYSQL_PWD,
                                             JRM_MYSQL_HOST,
                                             JRM_MYSQL_DB))
       
    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session


    def all(self, cls):
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)


    def new(self, obj):
        '''Add an object to the current DB Session'''
        self.__session.add(obj)


    def save(self):
        '''Commit all changes of the current database session'''
        self.__session.commit()


    def delete(self, obj=None):
        '''Delete an object from current database session if obj is not none'''
        if obj is not None:
            self.session.delete(obj)


    def close(self):
        ''' Call remove method on the private session attribute '''
        self.__session.remove()

    def get(self, cls, id):
        '''
        Return the object based on class name and its ID
        or None id not found
        '''
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
