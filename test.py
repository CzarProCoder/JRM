#!/user/bin/python3
'''
Test file containing test data
'''
from models.members import Members

new_member = Members(id = 478573,
                     first_name = "Julius", 
                     second_name = "Kinyua",
                     last_name = "Njeri",
                     national_id = "28748284",
                     kra_pin = "A7389847284C",
                     dob = "1994, 6, 25",
                     gender = "M",
                     created_at = None,
                     email = "juliusczar36@gmail.com",
                     phone = "+254703873717",
                     membership_status = "active",
                     loan_eligibility = 100000.00)

print(new_member)

new_member.reload()

new_member.save()

new_member.close()
