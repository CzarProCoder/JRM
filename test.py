#!/user/bin/python3
'''
Test file containing test data
'''
from models.members import Members
from models.loans import Loans
from models.accounts import Accounts
import models
from sqlalchemy.exc import IntegrityError
import re

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

Julius_acc = Accounts(id='0847858434323',
                      member_id=478573,
                      account_type="savings",
                      balance=350000.00,
                      created_at=None,
                      account_status="active")

Julius_acc2 = Accounts(id='0847858434324',
                      member_id=478573,
                      account_type="shares",
                      balance=350000.00,
                      created_at=None,
                      account_status="active")

Ambrose_acc = Accounts(id='0047858474787',
                      member_id=478575,
                      account_type="savings",
                      balance=350000.00,
                      created_at=None,
                      account_status="active")

Ambrose_acc2 = Accounts(id='0047858474788',
                      member_id=478575,
                      account_type="shares",
                      balance=350000.00,
                      created_at=None,
                      account_status="active")


Loan1 = Loans(id=8477584,
              loan_amount=250740,
              loan_balance=250740,
              loan_type='personal',
              interest_rate=0.12,
              installment_amount = 30000.00,
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
              installment_amount = 32000.00,
              loan_status='approved',
              created_at=None,
              due_date="2025, 8, 13",
              guarantor_id=3848754,
              member_id=478573)

def extract_class_name(object_class):
    # Use regular expression to find the class name pattern
    match = re.search(r"<class\s+'models\.(\w+)\.(\w+)'>", object_class)
    
    if match:
        # The first group in the match contains the class name
        class_name = match.group(2)
        # Make the first letter of the class name uppercase
        class_name = class_name.capitalize()
        return class_name
    else:
        return None

def add_obj(obj):
    obj_class = extract_class_name(str(obj.__class__))
    try:
        obj.save()
        obj.close()
        print(f"{obj_class} ID:{obj.id} has been added successfully. \n")
        print ("Confirm the details below: ")
        print(obj)
    except IntegrityError as e:
        print(f"Duplicate Entry! {obj_class}.id and unique must not have duplicates")


models.storage.reload()

add_obj(Julius)
add_obj(Ambrose)

add_obj(Julius_acc)
add_obj(Julius_acc2)
add_obj(Ambrose_acc)
add_obj(Ambrose_acc2)

add_obj(Loan1)
add_obj(loan2)
