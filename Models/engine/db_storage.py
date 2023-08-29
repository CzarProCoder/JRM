#!/usr/bin/python3

'''
Module defining the type of storage in use
'''

import models
# from models.members import Members
# from models.savings_accounts import SavingsAccounts
# from models.loans import Loans
# from models.payments import Payments
# from models.transactions import Transactions
# from models.documents import Documents
from models.base_model import Base
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine, ForeignKey, Column
from sqlalchemy import String, Integer, CHAR, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


# classes = {"members": Members,
#            "savings_accounts": SavingsAccounts,
#            "documents": Documents,
#            "loans": Loans,
#            "payments": Payments,
#            "transactions": Transactions}

class DBStorage:
    '''
    '''
    __engine = None
    __session = None

    def __init__(self):
       JRM_MYSQL_USER = getenv('JRM_MYSQL_USER')
       JRM_MYSQL_PWD = getenv('JRM_MYSQL_PWD')
       JRM_MYSQL_HOST = getenv('JRM_MYSQL_HOST')
       JRM_MYSQL_DB = getenv('JRM_MYSQL_DB')
       self.__engine = create_engine(f'mysql+mysqldb://{JRM_MYSQL_USER}:{JRM_MYSQL_PWD}@{JRM_MYSQL_HOST}/{JRM_MYSQL_DB}')
       
       Base.metadata.create_all(self.__engine)
       sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
       Session = scoped_session(sess_factory)
       self.__session = Session




    def all(self, obj):
        pass

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


    def reload(self):
        '''
        '''
        pass


    def close(self):
        ''' Call remove method on the private session attribute '''
        self.__session.remove()

    def get(self, cls, id):
        '''
        Return the object based on class name and its ID
        or None id not found
        '''
        pass
