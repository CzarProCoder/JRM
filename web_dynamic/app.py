#!/usr/bin/python3

'''
Entry point for flask app
'''
import sys
import os

# Get the parent directory of the current script (app.py)
current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path
sys.path.append(parent_directory)


from datetime import datetime
from models import storage
from models.members import Members, time
from models.accounts import Accounts
from flask import Flask, render_template, url_for, redirect, request
from sqlalchemy.exc import IntegrityError
import re


date_format = "%Y-%m-%d"

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
        # print(f"{obj_class} ID:{obj.id} has been added successfully. \n")
        # print ("Confirm the details below: ")
        # print(obj)
    except IntegrityError as e:
        print(f"Duplicate Entry! {obj_class}.id and unique must not have duplicates")

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    return render_template('index.html')

@app.route("/home", strict_slashes=False)
def home():
    return redirect(url_for('index'))

@app.route("/dashboard", strict_slashes=False)
def dashboard():
    return render_template('dashboard/dashboard_base.html')

@app.route("/dashboard/members", strict_slashes=False)
def members():
    members = storage.all(Members)
    return render_template('dashboard/members.html', members=members)

@app.route("/dashboard/accounts", strict_slashes=False)
def accounts():
    accounts = storage.all(Accounts)
    return render_template('dashboard/accounts.html', accounts=accounts)

@app.route("/addmember", methods = ['POST'], strict_slashes=False)
def addmember():
    if request.method == 'POST':
        new_member = Members(id=request.form['member_id'],
        first_name=request.form['first_name'],
        second_name=request.form['second_name'],
        last_name=request.form['last_name'],
        national_id=request.form['national_id'],
        kra_pin=request.form['kra_pin'],
        dob=datetime.strptime(request.form['dob'], date_format).date(),
        address=request.form['Address'],
        gender=request.form['gender'],
        created_at=None,
        # created_at=datetime.strptime(request.form['created_at'], time),
        email=request.form['email'],
        phone=request.form['phone'],
        membership_status=request.form['membership_status'],
        loan_eligibility=request.form['loan_eligibility'])
        
        add_obj(new_member)

        return redirect(url_for('members'))
    
@app.route("/addaccount", methods = ['POST'], strict_slashes=False)
def addaccount():
    if request.method == 'POST':
        new_account = Accounts(id=request.form['id'],
        member_id=request.form['member_id'],
        account_type=request.form['account_type'],
        balance=request.form['balance'],
        # created_at=request.form['created_at'],
        created_at=None,
        account_status=request.form['account_status'])
        
        add_obj(new_account)

        return redirect(url_for('accounts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
