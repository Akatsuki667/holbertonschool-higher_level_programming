#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 115, "city": "Los Angeles"}}

@app.route("/")
def home():
    return ("Welcome to the Flask API!")

@app.route("/data")
def data():
    return jsonify(users)

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
        data.get('username'): {
            key: value for key, value in data.items() if key != "username"}}
    users.update(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__": app.run()