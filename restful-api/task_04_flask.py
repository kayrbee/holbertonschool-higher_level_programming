#!/usr/bin/python3
from flask import Flask
from flask import jsonify

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    usernames = list(users.keys())
    return jsonify(usernames)

# Run server
if __name__ == "__main__": 
    app.run()
