#!/user/bin/python3
'''
Modules containing class Member
'''
from datetime import datetime, date
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, ForeignKey, Column
from sqlalchemy import VARCHAR, String, Integer, CHAR, DateTime, Numeric
from sqlalchemy.types import Date
from sqlalchemy.dialects.mysql import ENUM
from models.engine.db_storage import DBStorage

time = "%Y-%m-%dT%H:%M:%S.%f"

class Members(BaseModel, Base):
    '''
    Class defining all the member details
    '''
    __tablename__ = "members"

    first_name = Column("first_name", VARCHAR(45), nullable=False)
    second_name = Column("second_name", VARCHAR(45), nullable=False)
    last_name = Column("last_name", VARCHAR(45), nullable=False)
    id_no = Column("id_no", VARCHAR(20), unique=True)        # String so that it can accomodate "0" at the beginning
    kra_pin = Column("kra_pin", VARCHAR(45), unique=True)
    dob = Column("dob", Date)
    gender = Column("gender", ENUM('M', 'F'))
    email = Column("email", VARCHAR(45))
    phone = Column("phone", VARCHAR(45), nullable=False)         # String so that it can accomodate "0" at the beginning
    membership_status = Column("membership_status", ENUM('active','withdrawn','dormant','suspended'))
    loan_eligibility= Column("loan_eligibility", Numeric(precision=15, scale=2), default=0.00)


    def __init__(self, member_id, first_name, second_name, last_name,
                 id_no, kra_pin, dob, gender, registration_date=datetime.now(),
                 email=None, phone=None, membership_status=None, loan_eligibility=0.0):
        
        date_format = "%Y, %m, %d"

        if registration_date is None:
            self.registration_date = datetime.now()
        else:
            self.registration_date = datetime.strptime(registration_date, time)

        updated_at = self.registration_date

        super().__init__(member_id, registration_date, updated_at)

        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.id_no = id_no
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
                ID_No: {self.id_no} \n
                KRA_Pin: {self.kra_pin} \n
                Date_of_Birth: {self.dob} \n
                Gender: {self.gender} \n
                Email: {self.email} \n
                Phone: {self.phone} \n
                Membership_status: {self.membership_status} \n
                loan_eligibility: {self.loan_eligibility} \n
                Registration_date: {self.created_at} \n""")
