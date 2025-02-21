#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return ("Welcome to the Flask API!")

@app.route("/data")
def data():
    return jsonify(list(users.key()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        dictionary = users[username]
        dictionary.update({"username": username})
        return jsonify(dictionary)
    else:
        return {"error": "User not found"}, 404

@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    new_user = {
        "username": data.get('username'),
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }

    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201

if __name__ == "__main__": app.run(debug=True)