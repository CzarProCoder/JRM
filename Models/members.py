#!/user/bin/python3
'''
Modules containing class Member
'''
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column
from sqlalchemy.orm import relationship
from sqlalchemy import VARCHAR, Numeric
from sqlalchemy.types import Date
from sqlalchemy.dialects.mysql import ENUM

time = "%Y-%m-%dT%H:%M:%S.%f"
date_format = "%Y, %m, %d"


class Members(BaseModel, Base):
    '''
    Class defining all the member details
    '''
    __tablename__ = "members"

    first_name = Column(VARCHAR(45), nullable=False)
    second_name = Column(VARCHAR(45), nullable=False)
    last_name = Column(VARCHAR(45), nullable=False)
    national_id = Column(VARCHAR(20), unique=True)
    kra_pin = Column(VARCHAR(45), unique=True)
    dob = Column(Date)
    address = Column(VARCHAR(200))
    gender = Column(ENUM('M', 'F'))
    email = Column(VARCHAR(45))
    phone = Column(VARCHAR(45), nullable=False)
    membership_status = Column(ENUM('Active', 'Withdrawn',
                                    'Dormant', 'Suspended'))
    loan_eligibility = Column(Numeric(precision=15, scale=2), default=0.00)

    loans = relationship("Loans", back_populates="members")
    accounts = relationship("Accounts", back_populates="members")

    def __init__(self, id, first_name, second_name, last_name,
                 national_id, kra_pin, dob, address, gender,
                 created_at=datetime.now(), email=None, phone=None,
                 membership_status=None, loan_eligibility=0.0):

        if created_at is None:
            self.created_at = datetime.now()
        else:
            self.created_at = datetime.strptime(created_at, time)

        updated_at = self.created_at

        super().__init__(id, created_at, updated_at)

        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.national_id = national_id
        self.kra_pin = kra_pin
        self.dob = dob
        # self.dob = datetime.strptime(dob, date_format).date()
        self.address = address
        self.gender = gender
        self.email = email
        self.phone = phone
        self.membership_status = membership_status
        self.loan_eligibility = loan_eligibility

    # def __repr__(self):
    #     '''
    #     Returns a string representation of a member
    #     '''
    #     full_name = f"{self.first_name} {self.second_name} {self.last_name}"
    #     dict_obj = {"Member_id": self.id,
    #                 "Name": full_name,
    #                 "National_ID": self.national_id,
    #                 "KRA_Pin": self.kra_pin,
    #                 "Date_of_Birth": self.dob,
    #                 "Address": self.address,
    #                 "Gender": self.gender,
    #                 "Email": self.email,
    #                 "Phone": self.phone,
    #                 "Membership_status": self.membership_status,
    #                 "loan_eligibility": self.loan_eligibility,
    #                 "created_at": self.created_at,
    #                 "Updated_at": self.updated_at}
    #     return dict_obj
    
    def __str__(self):
        full_name = f"{self.first_name} {self.second_name} {self.last_name}"
        return (f"""Member_id:{self.id},
Name:{full_name},
National_ID:{self.national_id},
KRA_Pin:{self.kra_pin},
Date_of_Birth:{self.dob},
Address:'{self.address}',
Gender:{self.gender},
Email:{self.email},
Phone:{self.phone},
Membership_status:{self.membership_status},
loan_eligibility:{self.loan_eligibility},
created_at:{self.created_at},
Updated_at:{self.updated_at}""").replace("\n", "")
