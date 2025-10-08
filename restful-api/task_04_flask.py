#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}
# For testing
users = {
    "jane":
    {"username": "jane",
     "name": "Jane",
     "age": 28,
     "city": "Los Angeles"
     },
    "john":
    {"username": "john",
     "name": "John",
     "age": 30,
     "city": "New York"
     }
}


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


# Run server
if __name__ == "__main__":
    app.run()
