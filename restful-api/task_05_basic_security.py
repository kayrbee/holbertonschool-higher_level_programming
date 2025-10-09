#!/usr/bin/python3
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()


users = {"user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
         "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}}


@auth.verify_password
def verify_password(username, password):
    if username in users.keys() and \
            check_password_hash(users.get(username), password):
        return username


@app.route("/basic-protected")
@auth.login_required
def home():
    return "Basic Auth: Access Granted"


# Run server
if __name__ == "__main__":
    app.run()
