# RESTful API

## 2. Consuming and processing data from an API using Python
Python, due to its readability and a vast library ecosystem, is a popular choice for interacting with web services and APIs. The `requests` library simplifies HTTP communication and allows users to send HTTP requests using Python. Once the data is fetched, Python’s built-in libraries and tools enable effortless data manipulation and processing.

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


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = posts = response.json()

    for post in posts:
        print(post['title'])


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = posts = response.json()

        filtered_posts = []

        for post in posts:
            filtered_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            filtered_posts.append(filtered_post)

        for post in filtered_posts[:5]:  # Afficher les 5 premiers posts
            print(post)

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

##

### Instructions

### Expectation
```python3
```
### Result
```bash
```
