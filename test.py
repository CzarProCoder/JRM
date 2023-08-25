#!/user/bin/python3
'''
Test file containing test data
'''
from models.members import Members
from models.engine.db_storage import DBStorage

member = {"member_id": 478573,
          "f_name": "Julius",
          "s_name": "Kinyua",
          "l_name": "Njeri",
          "id_no": "28748284",
          "kra_pin": "A7389847284C",
          "dob": "1994, 6, 25",
          "gender": "M",
          "reg_date": None,
          "email": "juliusczar36@gmail.com",
          "phone": "+254703873717",
          "status": "active",
          "loan_eligibility": 100000.00}

new_member = Members(member["member_id"], member["f_name"],
                     member["s_name"], member["l_name"],
                     member["id_no"], member["kra_pin"], member["dob"],
                     member["gender"], member["reg_date"], member["email"],
                     member["phone"], member["status"],
                     member["loan_eligibility"])

print(new_member)

new_member.save()

print("New Member has been saved to db")

DBStorage.close()
