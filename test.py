#!/user/bin/python3
'''
Test file containing test data
'''
from models.members import Members
import models
from sqlalchemy.exc import IntegrityError

Julius = Members(id = 478573,
                     first_name = "Julius", 
                     second_name = "Kinyua",
                     last_name = "Njeri",
                     national_id = "32748284",
                     kra_pin = "A7389847284C",
                     dob = "1994, 6, 25",
                     address="00100 Nairobi, Kenya",
                     gender = "M",
                     created_at = None,
                     email = "juliusczar36@gmail.com",
                     phone = "+254703873717",
                     membership_status = "active",
                     loan_eligibility = 100000.00)

Ambrose = Members(id = 478575,
                     first_name = "Ambrose", 
                     second_name = "Matata",
                     last_name = "Pro",
                     national_id = "46635273",
                     kra_pin = "A738483843C",
                     dob = "1994, 8, 13",
                     address="00100 Nairobi, Kenya",
                     gender = "M",
                     created_at = None,
                     email = "ambrose.matata@gmail.com",
                     phone = "+254707057151",
                     membership_status = "active",
                     loan_eligibility = 160050.25)

def add_member(name):
    try:
        name.save()
        name.close()
        print(f"""{name.first_name} has been added successfully. \n
              \t Confirm the details below: """)
        print(Julius)
    except IntegrityError as e:
        print("Duplicate Entry! Member_id, ID and KRA_pin must be Unique")


models.storage.reload()

add_member(Julius)
add_member(Ambrose)
