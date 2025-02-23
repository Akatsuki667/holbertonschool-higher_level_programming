# RESTful API

## 2. Consuming and processing data from an API using Python
- At the end of this exercise, students should be able to:
    - Utilize the `requests` library to send HTTP requests and process responses.
    - Parse and manipulate JSON data using Python.
    - Convert structured data into other formats, e.g., CSV.

### Instructions
- If not installed, install the `requests` library using pip: `pip install requests`.
- Write a basic Python script to fetch posts from JSONPlaceholder using `requests.get()`.
- Create a function `fetch_and_print_posts()` that fetches all post from JSONPlaceholder.
    - Print the status code of the response i.e. `Status Code: 200`
    - If the request was sucessfull, parse the fetched data into a JSON object using the .json() method of the response object.
    - Iterate through the parsed JSON data and print out the titles of all the posts.
- Create a function `fetch_and_save_posts()` that fetches all post from JSONPlaceholder.
    - If the request was sucessfull, instead of printing titles, structure the data into a list of dictionaries, where each dictionary represents a post with keys and values for `id`, `title`, and `body`.
    - Using Python’s `csv` module, write this data into a CSV file called `posts.csv` with columns corresponding to the dictionary keys.

### Expectation
```python
#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code:{response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        filtered_posts = [{
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        } for post in posts]

        with open("posts.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(filtered_posts)

    else:
        print("Échec de la requête, code:", response.status_code)
```
### Result
```bash
Status Code: 200
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
ea molestias quasi exercitationem repellat qui ipsa sit aut
eum et est occaecati
nesciunt quas odio
...
```

## 3. Develop a simple API using Python with the `http.server` module
- At the end of this exercise, students should be able to:
    - Set up a basic web server using the `http.server` module.
    - Handle different types of HTTP requests (GET, POST, etc.).
    - Serve JSON data in response to specific endpoints.

### Instructions
- Setting Up a Basic HTTP Server:
    - Use the `http.server` module to set up a simple HTTP server. Start by creating a subclass of `http.server.BaseHTTPRequestHandler`.
    - Implement the `do_GET` method to handle GET requests. Within this method, send a simple text response back to the client: “Hello, this is a simple API!”.
    - Start the server on a specific port (8000) and test it by visiting `http://localhost:8000` in your browser or using `curl`.
- Serving JSON Data:
    - Modify the do_GET method in your server class to serve a sample JSON data when the endpoint `/data` is accessed.
    - You should return a simple dataset: `{"name": "John", "age": 30, "city": "New York"}`.
    - Ensure that the correct content type (`application/json`) header is set in the response.
- Handling Different Endpoints:
Add an /status endpoint to check the API status. It shoud return `OK`.
Implement error handling. If the user tries to access an undefined endpoint, return a 404 Not Found status with an appropriate message.

### Expectation
```python
#!/usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def AccesServer():
    PORT = 8000
    server = HTTPServer(('', PORT), SimpleAPIHandler)
    print(f"Server running on port {PORT}")
    server.serve_forever()


if __name__ == "__main__":
    AccesServer()
```

## 4. Develop a Simple API using Python with Flask
At the end of this exercise, students should be able to: 1. Set up a Flask application and run a development server. 2. Define and handle routes with Flask to respond to different endpoints. 3. Serve JSON data using Flask. 4. Understand the basics of request handling and response formation in Flask. 5. Handle POST requests to add new data to the API.

### Instructions
- Setting Up Flask:
    - Install Flask using pip: `pip install Flask`.
    - Create a new Python file and import Flask: `from flask import Flask`.
    - Instantiate a Flask web server from the Flask module: `app = Flask(__name__)`.
- Creating Your First Endpoint:
    Define a route for the root URL (“/”) and create a function (`def home():`) to handle this route. Within the function, return a string: “Welcome to the Flask API!”.
    Run the Flask development server with: `if __name__ == "__main__": app.run()`.
    Visit `http://localhost:5000` in your browser or use `curl` to see the message.
- Serving JSON Data:
    - Import the `jsonify` function from Flask: `from flask import jsonify`.
    - Create a new route `/data` and associate a function with it. Inside this function, return a JSON response using `jsonify()`. This should return a list of all the usernames stored in the API.
    - Users will be stored in memory using a dictionary with `username` as the key and the whole object (dictionary) as the value.
    - Example dictionary: `users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}`
- Expanding Your API:
    - Add a few more endpoints to simulate different functionalities:
    - `/status`: It should return `OK`.
    - `/users/<username>`: Returns the full object corresponding to the provided `username`. (Hint: Use Flask’s dynamic route feature)
- Handling POST Requests:
    - Import the request object from Flask: from flask import request.
    - Create a new route `/add_user` that accepts POST requests.
    - This route should:
        - Parse the incoming JSON data. Example data: `{"username": "john", "name": "John", "age": 30, "city": "New York"}`
        - Add the new user to the users dictionary using `username` as the key.
        - Return a confirmation message with the added user’s data.

### Expectation
```python
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
```


## 5. API Security and Authentication Techniques
- At the end of this exercise, students should be able to:
    - Understand the importance of API security.
    - Implement basic authentication using Flask.
    - Set up token-based authentication with JSON Web Tokens (JWT).
    - Differentiate between authentication and authorization.

### Instructions
_Basic Authentication_:
__Install Flask-HTTPAuth__:
    - Run: `pip install Flask-HTTPAuth`.
__Set up Basic HTTP Authentication__:
    - Create a list of users and their hashed passwords.
    - Use the `werkzeug.security` library for password hashing and verification.
__Protect Routes with Basic Authentication__:
    - Use the `@auth.login_required` decorator to protect certain routes.
_Token-based Authentication with JWT_:
__Install Flask-JWT-Extended__:
    - Run: `pip install Flask-JWT-Extended`.
__Set up JWT-based Authentication__
    - Use a secret key for token generation and validation.
    - Create a route `/login` where users can log in with their credentials and receive a JWT token.
__Protect Routes with JWT Tokens__:
    - Use the `@jwt_required()` decorator to protect certain routes.
__Implement Role-based Access Control__:
    - Add roles (e.g., `admin`, `user`) to your users.
    - Create routes that should only be accessible to certain roles.
    - Implement checks to ensure the user’s role matches the required role for accessing specific routes.

### Expectation
```python
#!/usr/bin/env python3

from flask import request
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1", "password": generate_password_hash
              ("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash
               ("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={'username': username,
                                                     'role': user['role']})

        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
```