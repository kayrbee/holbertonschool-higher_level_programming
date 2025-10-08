#!/usr/bin/python3
from flask import Flask
from flask import jsonify

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    names = []
    user_keys = users.keys()
    for key in user_keys:
        names.append(users[key]["name"])
    return jsonify(names)

# Run server
if __name__ == "__main__": 
    app.run()
