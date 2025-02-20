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


##

### Instructions

### Expectation
```python3
```
### Result
```bash
```
