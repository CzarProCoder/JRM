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

from models import storage
from models.members import Members
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    return render_template('index.html')

@app.route("/home", strict_slashes=False)
def home():
    return redirect(url_for('index'))

@app.route("/dashboard", strict_slashes=False)
def dashboard():
    return redirect(url_for('members'))

@app.route("/dashboard/members", strict_slashes=False)
def members():
    members = storage.all(Members)
    return members
    return render_template('dashboard/members.html', members=members)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
