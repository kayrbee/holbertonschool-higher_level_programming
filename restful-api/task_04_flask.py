#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Run server
if __name__ == "__main__": app.run()
