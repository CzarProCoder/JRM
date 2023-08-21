#!/user/bin/python3
'''
Modules containing class Member details
'''
from datetime import time
from sqlalchemy import create_engine, ForeignKey, Column
from sqlalchemy import String, Integer, CHAR, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class MemberDetails:
    '''
    Class defining all the member details
    '''
    __tablename__ = "memberDetails"

    memberid = Column("Memberid", Integer, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    id_no = Column("id_no", Integer)
    kra_pin = Column("kra_pin", String)
    dob = Column("dob", DateTime)
    gender = Column("gender", CHAR)
    registration_date = Column("registration date", DateTime, default=DateTime.today())
    email = Column("email", String)
    phone = Column("phone", Integer)
    membership_status = Column("membership_status", String)
    savings_acc_balance = Column("savings_acc_balance", Numeric(precision=15, scale=2))
    eligible_loan= Column("eligible_loan", Numeric(precision=15, scale=2), default=0.00)

    def __init__(self, memberid, first_name, last_name,
                 id_no, kra_pin, dob, gender, registration_date=None,
                 email=None, phone=None, membership_status=None,
                 savings_acc_balance=0.0, eligible_loan=0.0):
        self.memberid = memberid
        self.first_name = first_name
        self.last_name = last_name
        self.id_no = id_no
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender
        self.email = email
        self.phone = phone
        self.membership_status = membership_status
        self.savings_acc_balance = savings_acc_balance
        self.eligible_loan = eligible_loan
        if registration_date is None:
            self.registration_date = time.now()
        else:
            self.registration_date = registration_date

    def __repr__(self):
        '''
        Returns a representation of a member
        '''
        return (f"""Member_id: {self.memberid} \n,
                Name: {self.first_name} {self.last_name} \n,
                ID_No: {self.id_no} \n,
                KRA_Pin: {self.kra_pin} \n,
                Date_of_Birth: {self.dob} \n,
                Gender: {self.gender} \n,
                Email: {self.email} \n,
                Phone: {self.phone} \n,
                Membership_status: {self.membership_status} \n,
                Savings_Acc_Balance: {self.savings_acc_balance} \n,
                Eligible_loan: {self.loan_eligibility}""")


engine = create_engine("mysql:///hyraxsacco.db", echo=True)
Base.Metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)
session = Session()

