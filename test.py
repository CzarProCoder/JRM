#!/user/bin/python3
'''
Test file containing test data
'''
from models.members import Members
from models.loans import Loans
from models.accounts import Accounts
from models.transactions import Transactions
from models.documents import Documents
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
                 membership_status="Active",
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
                  membership_status="Active",
                  loan_eligibility=760050.25)

Julius_ID_Copy = Documents(id = 47563884,
                           doc_type="ID",
                           path="models/files/",
                           description= "ID For Julius K",
                           member_id=478573,
                           created_at=None)

Julius_KRA_Copy = Documents(id = 47563885,
                            doc_type="KRA_Pin",
                            path="models/files/",
                            description="Julius Kinyua KRA_Pin",
                            member_id=478573,
                            created_at=None)

Julius_Passport = Documents(id = 47563886,
                            doc_type="Passport",
                            path="models/files/",
                            description="Passport Photo",
                            member_id=478573,
                            created_at=None)

Julius_acc = Accounts(id='0847858434323',
                      member_id=478573,
                      account_type="Savings",
                      balance=350030.00,
                      created_at=None,
                      account_status="Active")

Julius_acc2 = Accounts(id='0847858434324',
                      member_id=478573,
                      account_type="Shares",
                      balance=22043.00,
                      created_at=None,
                      account_status="Active")

Ambrose_acc = Accounts(id='0047858474787',
                      member_id=478575,
                      account_type="Savings",
                      balance=430500.00,
                      created_at=None,
                      account_status="Active")


Ambrose_acc2 = Accounts(id='0047858474788',
                      member_id=478575,
                      account_type="Shares",
                      balance=143890.00,
                      created_at=None,
                      account_status="Active")

julius_transaction1 = Transactions(id=38758485,
                                   created_at=None,
                                   account_no="0847858434323",
                                   transaction_type="Deposit",
                                   amount=50000.00,
                                   description="Monthly savings for Oct")

julius_transaction2 = Transactions(id=38758486,
                                   created_at=None,
                                   account_no="0847858434323",
                                   transaction_type="Withdrawal",
                                   amount=10000.00,
                                   description="Personal Expense")

Ambrose_transaction1 = Transactions(id=38758487,
                                   created_at=None,
                                   account_no="0047858474787",
                                   transaction_type="Deposit",
                                   amount=60000.00,
                                   description="")

Ambrose_transaction2 = Transactions(id=38758488,
                                   created_at=None,
                                   account_no="0047858474787",
                                   transaction_type="Withdrawal",
                                   amount=10000.00,
                                   description="")

Loan1 = Loans(id=8477584,
              loan_amount=250740,
              loan_balance=250740,
              loan_type='Personal',
              interest_rate=0.12,
              installment_amount = 30000.00,
              loan_status='Pending',
              created_at=None,
              due_date="2024, 8, 13",
              guarantor_id=38784758,
              member_id=478573)

loan2 = Loans(id=8477585,
              loan_amount=320453,
              loan_balance=320453,
              loan_type='Development',
              interest_rate=0.12,
              installment_amount = 32000.00,
              loan_status='Approved',
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
        return (class_name[:-1])
    else:
        return None

def add_obj(obj):
    obj_class = extract_class_name(str(obj.__class__))
    try:
        obj.save()
        obj.close()
        print(f"{obj_class} ID:{obj.id} has been added successfully. \n")
        # print ("Confirm the details below: ")
        # print(obj)
    except IntegrityError as e:
        print(f"Duplicate Entry! {obj_class}.id and unique must not have duplicates")


add_obj(Julius)
add_obj(Ambrose)

add_obj(Julius_ID_Copy)
add_obj(Julius_KRA_Copy)
add_obj(Julius_Passport)

add_obj(Julius_acc)
add_obj(Julius_acc2)
add_obj(Ambrose_acc)
add_obj(Ambrose_acc2)

add_obj(julius_transaction1)
add_obj(julius_transaction2)
add_obj(Ambrose_transaction1)
add_obj(Ambrose_transaction2)

add_obj(Loan1)
add_obj(loan2)

print(models.storage.all(Members))
print(models.storage.all(Documents))
print(models.storage.all(Accounts))
print(models.storage.all(Transactions))
print(models.storage.all(Loans))
