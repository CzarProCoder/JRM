#!/user/bin/python3
'''
Test file containing test data
'''
from models.members import Members
from models.loans import Loans
import models
from sqlalchemy.exc import IntegrityError

Julius = Members(id=478573,
                 first_name="Julius",
                 second_name="Kinyua",
                 last_name="Njeri",
                 national_id="3xxxxx4",
                 kra_pin="AxxxxyyyyyC",
                 dob="1994, 6, 25",
                 address="00100 Nairobi, Kenya",
                 gender="M",
                 created_at=None,
                 email="jyyyyxxxx987@gmail.com",
                 phone="+25412345677",
                 membership_status="active",
                 loan_eligibility=500000.00)

Ambrose = Members(id=478575,
                  first_name="Ambrose",
                  second_name="Matata",
                  last_name="Pro",
                  national_id="4xxxxcccc3",
                  kra_pin="AxxxxyyyyC",
                  dob="1994, 8, 13",
                  address="00100 Nairobi, Kenya",
                  gender="M",
                  created_at=None,
                  email="affddccccc76@gmail.com",
                  phone="+254000000111",
                  membership_status="active",
                  loan_eligibility=760050.25)


Loan1 = Loans(id=8477584,
              loan_amount=250740,
              loan_balance=250740,
              loan_type='personal',
              interest_rate=0.12,
              loan_status='pending',
              created_at=None,
              due_date="2024, 8, 13",
              guarantor_id=38784758,
              member_id=478573)

loan2 = Loans(id=8477585,
              loan_amount=320453,
              loan_balance=320453,
              loan_type='development',
              interest_rate=0.12,
              loan_status='approved',
              created_at=None,
              due_date="2025, 8, 13",
              guarantor_id=3848754,
              member_id=478573)


def add_obj(obj):
    try:
        obj.save()
        obj.close()
        print(f"""{obj.__class__} ID:{obj.id} has been added successfully. \n
              \t Confirm the details below: """)
        print(obj)
    except IntegrityError as e:
        print("Duplicate Entry! Member_id, ID and KRA_pin must be Unique")


models.storage.reload()

add_obj(Julius)
add_obj(Ambrose)

add_obj(Loan1)
add_obj(loan2)
