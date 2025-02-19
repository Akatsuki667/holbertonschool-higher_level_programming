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

##

### Instructions

### Expectation
```python3
```
### Result
```bash
```

##

### Instructions

### Expectation
```python3
```
### Result
```bash
```
