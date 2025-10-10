#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import JWTManager


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "my-demo-key"
jwt = JWTManager(app)

# Demo data
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Implements basic auth
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

# Implements JWT auth


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = users.get(username)
    pw_hash = user["password"]
    role = user["role"]
    if not user or not username or not password:
        return jsonify({"message": "Username and password required"}), 400

    if username in users and check_password_hash(pw_hash, password):
        access_token = create_access_token(
            identity={"username": username, "role": role})
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Error handling


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# Run server
if __name__ == "__main__":
    app.run()
