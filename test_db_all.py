#!/user/bin/python3

from models import storage

print(models.storage.all(Members))
print(models.storage.all(Documents))
print(models.storage.all(Accounts))
print(models.storage.all(Transactions))
print(models.storage.all(Loans))
