#!/usr/bin/python3
'''
Module defining class Transactions
'''
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import VARCHAR, Numeric, ForeignKey, Column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import ENUM
from models.members import time


class Transactions(BaseModel, Base):

    __tablename__ = "transactions"

    transaction_type = Column(ENUM('Deposit', 'Withdrawal', 'Loan_payment',
                                   'Loan_disbursement', 'Loan_interest',
                                   'Transfer', 'Penalty', 'Fees'))
    amount = Column(Numeric(precision=15, scale=2), nullable=False)
    description = Column(VARCHAR(45))
    account_no = Column(VARCHAR(45), ForeignKey("accounts.id"))

    accounts = relationship("Accounts", back_populates="transactions")

    def __init__(self, id, created_at, account_no, transaction_type,
                 amount, description):
        """
        Initializes a transaction

        Args:
            id (Integer):           Transaction id
            created_at (datetime):  Transaction date and time
            Transaction_type (Str): Type of Transaction
            amount (Float):         Amount transacted
            Account_no (Int):       Account Number for the transaction
        """
        if created_at is None:
            self.created_at = datetime.now()
        else:
            self.created_at = datetime.strptime(created_at, time)

        updated_at = self.created_at

        super().__init__(id, created_at, updated_at)

        self.account_no = account_no
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description

    def __str__(self):
        '''
        Returns a string representation of loans
        '''
        return (f"""
          Transaction ID: {self.id} \n
             Account NO.: {self.account_no} \n
        Transaction Type: {self.transaction_type} \n
                  Amount: {self.amount} \n
             Description: {self.description} \n
              Created on: {self.created_at} \n
              Updated_at: {self.updated_at} \n""")
