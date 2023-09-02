#!/usr/bin/python3
'''
Module defining class Loans
'''
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import VARCHAR, Numeric, ForeignKey, Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from sqlalchemy.dialects.mysql import ENUM
from models.members import time, date_format


class Loans(BaseModel, Base):
    '''
    Defines the attributes and methods of class loans
    '''
    __tablename__ = "loans"

    loan_amount = Column(Numeric(precision=15, scale=2), nullable=False)
    loan_balance = Column(Numeric(precision=15, scale=2))
    loan_type = Column(ENUM('emergency', 'personal',
                            'education', 'development'))
    interest_rate = Column(Numeric(precision=4, scale=2), nullable=False)
    installment_amount = Column(Numeric(precision=15, scale=2))
    loan_status = Column(ENUM('pending', 'approved', 'rejected'))
    due_date = Column(Date)
    guarantor_id = Column(VARCHAR(20))
    member_id = Column(VARCHAR(45), ForeignKey("members.id"))

    members = relationship("Members", back_populates="loans")

    def __init__(self, id, loan_amount, loan_balance, loan_type,
                 interest_rate, installment_amount, loan_status, created_at,
                 due_date, guarantor_id, member_id):

        if created_at is None:
            self.created_at = datetime.now()
        else:
            self.created_at = datetime.strptime(created_at, time)

        updated_at = self.created_at

        super().__init__(id, created_at, updated_at)

        self.loan_amount = loan_amount
        self.loan_balance = loan_balance
        self.loan_type = loan_type
        self.interest_rate = interest_rate
        self.installment_amount = installment_amount
        self.loan_status = loan_status
        self.due_date = datetime.strptime(due_date, date_format).date()
        self.guarantor_id = guarantor_id
        self.member_id = member_id

    def __str__(self):
        '''
        Returns a string representation of loans
        '''
        return (f"""
        Loan ID: {self.id} \n
        Loan Amount: {self.loan_amount} \n
        Loan Balance: {self.loan_balance} \n
        Loan Type: {self.loan_type} \n
        Interest Rate: {self.interest_rate} \n
        Loan Status: {self.loan_status} \n
        Due Date: {self.due_date} \n
        Guarantor ID: {self.guarantor_id} \n
        Issued_on: {self.created_at} \n
        Updated_at: {self.updated_at} \n""")
