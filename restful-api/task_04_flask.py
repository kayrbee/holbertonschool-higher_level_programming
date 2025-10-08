#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}
# # For testing
# users = {
#     "jane":
#     {"username": "jane",
#      "name": "Jane",
#      "age": 28,
#      "city": "Los Angeles"
#      },
#     "john":
#     {"username": "john",
#      "name": "John",
#      "age": 30,
#      "city": "New York"
#      }
# }


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def user(username):
    if username in users.keys():
        return jsonify({
            "username": users[username]["username"],
            "name": users[username]["name"],
            "age": users[username]["age"],
            "city": users[username]["city"]
        })
    else:
        error = {"error": "User not found"}
        return jsonify(error), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    new_user = request.get_json()

    if not new_user:
        return jsonify({"Error": "Missing JSON body"}), 400

    required_fields = ["username", "name", "age", "city"]

    for field in required_fields:
        if field not in new_user:
            if field == "username":
                return jsonify({"error": f"Username is required"}), 400
            else:
                return jsonify({"error": f"{field} is required"}), 400

    username = new_user["username"]

    if username in users:
        return jsonify({"Error": "User already exists"}), 409

    users[username] = {
        "username": username,
        "name": new_user["name"],
        "age": new_user["age"],
        "city": new_user["city"]
    }
    return jsonify({"message": "User added", "user": new_user}), 201


# Run server
if __name__ == "__main__":
    app.run()
