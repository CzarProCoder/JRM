#!/user/bin/python3
'''
Modules containing class Member
'''
from datetime import datetime, date

from sqlalchemy import create_engine, ForeignKey, Column
from sqlalchemy import String, Integer, CHAR, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Date
from sqlalchemy.dialects.mysql import ENUM


Base = declarative_base()


class Members(Base):
    '''
    Class defining all the member details
    '''


    __tablename__ = "members"


    __table__ = Base.metadata.tables[__tablename__]

    member_id = Column("member_id", Integer, primary_key=True)
    first_name = Column("first_name", String(45), nullable=False)
    second_name = Column("second_name", String(45), nullable=False)
    last_name = Column("last_name", String(45), nullable=False)
    id_no = Column("id_no", String(20), unique=True)        # String so that it can accomodate "0" at the beginning
    kra_pin = Column("kra_pin", String(45), unique=True)
    dob = Column("dob", Date)
    gender = Column("gender", ENUM('M', 'F'))
    registration_date = Column("registration_date", DateTime, default=DateTime.today())
    email = Column("email", String(45))
    phone = Column("phone", String(45), nullable=False)         # String so that it can accomodate "0" at the beginning
    membership_status = Column("membership_status", ENUM('active','withdrawn','dormant','suspended'))
    loan_Eligibility= Column("loan_eligibility", Numeric(precision=15, scale=2), default=0.00)

    def __init__(self, member_id, first_name, second_name, last_name,
                 id_no, kra_pin, dob, gender, registration_date=date.today(),
                 email=None, phone=None, membership_status=None, loan_eligibility=0.0):
        self.member_id = member_id
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.id_no = id_no
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender
        self.email = email
        self.phone = phone
        self.membership_status = membership_status
        self.loan_eligibility = loan_eligibility
        self.registration_date = registration_date

    def __repr__(self):
        '''
        Returns a representation of a member
        '''
        return (f"""
                Member_id: {self.member_id} \n
                Name: {self.first_name} {self.second_name} {self.last_name} \n
                ID_No: {self.id_no} \n
                KRA_Pin: {self.kra_pin} \n
                Date_of_Birth: {self.dob} \n
                Gender: {self.gender} \n
                Email: {self.email} \n
                Phone: {self.phone} \n
                Membership_status: {self.membership_status} \n
                loan_eligibility: {self.loan_eligibility} \n
                Registration_date: {self.registration_date}""")


'''
engine = create_engine("mysql:///hyraxsacco.db", echo=True)
Base.Metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)
session = Session()
'''
