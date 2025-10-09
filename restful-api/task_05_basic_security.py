#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
# app.config["JWT_SECRET_KEY"] = "secret-key"
jwt = JWTManager(app)


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


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"message": "bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route("/jwt-protected", methods=["GET", "POST"])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


# Run server
if __name__ == "__main__":
    app.run()
