#!/usr/bin/python3

'''
Module defining class Dcouments
'''

from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import VARCHAR, Numeric, ForeignKey, Column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import ENUM
from models.members import time


class Documents(BaseModel, Base):

    __tablename__ = "documents"

    doc_type = Column(ENUM('ID', 'KRA_Pin', 'Passport'))
    path = Column(VARCHAR(200), nullable=False)
    description = Column(VARCHAR(200))
    member_id = Column(VARCHAR(45), ForeignKey("members.id"))

    def __init__(self, id, doc_type, path, description, member_id, created_at):

        if created_at is None:
            self.created_at = datetime.now()
        else:
            self.created_at = datetime.strptime(created_at, time)

        updated_at = self.created_at

        super().__init__(id, created_at, updated_at)

        self.doc_type = doc_type
        self.path = path
        self.description = description
        self.member_id = member_id

    def __str__(self):
        '''
        Returns a string representation of loans
        '''
        return (f"""
        Document ID: {self.id} \n
           Doc Type: {self.doc_type} \n
           Doc Path: {self.path} \n
        Description: {self.description} \n
          Member ID: {self.member_id} \n
        Uploaded On: {self.created_at} \n
         Updated On: {self.updated_at} \n""")
