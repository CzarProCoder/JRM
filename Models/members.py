#!/user/bin/python3
'''
Modules containing class Member
'''
from datetime import datetime, date
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, ForeignKey, Column
from sqlalchemy import VARCHAR, Integer, CHAR, DateTime, Numeric
from sqlalchemy.types import Date
from sqlalchemy.dialects.mysql import ENUM

time = "%Y-%m-%dT%H:%M:%S.%f"

class Members(BaseModel, Base):
    '''
    Class defining all the member details
    '''
    __tablename__ = "members"

    first_name = Column(VARCHAR(45), nullable=False)
    second_name = Column(VARCHAR(45), nullable=False)
    last_name = Column(VARCHAR(45), nullable=False)
    national_id = Column(VARCHAR(20), unique=True)        # VARCHAR so that it can accomodate "0" at the beginning
    kra_pin = Column(VARCHAR(45), unique=True)
    dob = Column(Date)
    gender = Column(ENUM('M', 'F'))
    email = Column(VARCHAR(45))
    phone = Column(VARCHAR(45), nullable=False)         # VARCHAR so that it can accomodate "0" at the beginning
    membership_status = Column(ENUM('active','withdrawn','dormant','suspended'))
    loan_eligibility= Column(Numeric(precision=15, scale=2), default=0.00)


    def __init__(self, id, first_name, second_name, last_name,
                 national_id, kra_pin, dob, gender, created_at=datetime.now(),
                 email=None, phone=None, membership_status=None, loan_eligibility=0.0):
        
        date_format = "%Y, %m, %d"

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
        self.dob = datetime.strptime(dob, date_format).date()
        self.gender = gender
        self.email = email
        self.phone = phone
        self.membership_status = membership_status
        self.loan_eligibility = loan_eligibility

    def __repr__(self):
        '''
        Returns a representation of a member
        '''
        return (f"""
                Member_id: {self.id} \n
                Name: {self.first_name} {self.second_name} {self.last_name} \n
                National_ID: {self.national_id} \n
                KRA_Pin: {self.kra_pin} \n
                Date_of_Birth: {self.dob} \n
                Gender: {self.gender} \n
                Email: {self.email} \n
                Phone: {self.phone} \n
                Membership_status: {self.membership_status} \n
                loan_eligibility: {self.loan_eligibility} \n
                created_at: {self.created_at} \n
                Updated_at: {self.updated_at} \n""")
