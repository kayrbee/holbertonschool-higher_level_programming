#!/usr/bin/python3
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
auth = HTTPBasicAuth()


users = {"user1": {"username": "user1", "password": generate_password_hash(os.getenv('USER_PW')), "role": "user"},
         "admin1": {"username": "admin1", "password": generate_password_hash(os.getenv('ADMIN_PW')), "role": "admin"}}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if username in users.keys() and \
            check_password_hash(user["password"], password):
        return username


@app.route("/basic-protected")
@auth.login_required
def home():
    return "Basic Auth: Access Granted"


# Run server
if __name__ == "__main__":
    app.run()
