#!/usr/bin/python3
'''
Module containg class SavingsAccounts
'''
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import VARCHAR, Numeric, ForeignKey, Column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import ENUM
from models.members import time


class Accounts(BaseModel, Base):
    """
    Defines the attributes and methods of class savings_accounts
    """
    __tablename__ = "accounts"

    account_type = Column(ENUM('savings', 'shares'))
    balance = Column(Numeric(precision=15, scale=2))
    account_status = Column(ENUM('active', 'closed', 'suspended', 'dormant'))
    member_id = Column(VARCHAR(45), ForeignKey("members.id"))

    members = relationship("Members", back_populates="accounts")

    def __init__(self, id, member_id, account_type, balance,
                 created_at, account_status):
        """
        Initilaizes a savings account

        Args:
            id (Integer):           Account Number (VARCHAR in sql)
            member_id (Int):        Member id
            account_bal (Int):      Account Balance
            interest_rate (float)   Interest Rate
            created_at (datetime):  Account creation date
            account_status (String):Status of account
                                    'active','closed','suspended','dormant'
            balance (Float):        Account balance
        """

        if created_at is None:
            self.created_at = datetime.now()
        else:
            self.created_at = datetime.strptime(created_at, time)

        updated_at = self.created_at

        super().__init__(id, created_at, updated_at)

        self.member_id = member_id
        self.account_type = account_type
        self.balance = balance
        self.account_status = account_status

    def __str__(self):
        '''
        Returns a string representation of loans
        '''
        return (f"""
        account ID: {self.id} \n
        member Id: {self.member_id} \n
        Account Type: {self.account_type} \n
        Account Balance: {self.balance} \n
        Account Status: {self.account_status} \n
        Created on: {self.created_at} \n
        Updated_at: {self.updated_at} \n""")
