# Python - Input/Output

## 0. Read file
Write a function that reads a text file (`UTF8`) and prints it to stdout:

### Objectives
- Prototype: `def read_file(filename=""):`
- You must use the `with` statement
- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
- You are not allowed to import any module
### Expectation
```python3
#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        contenu = f.read()
        print(contenu, end="")
```
### Result
```bash
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers.

A school every software engineer would have dreamt of!%                                                                       
```

## 1. Write to a file
Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

### Objectives
- Prototype: `def write_file(filename="", text=""):`
- You must use the `with` statement
- You don’t need to manage file permission exceptions.
- Your function should create the file if doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
```
### Result
```bash
24
```

## 2. Append to a file
Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:

### Objectives
- Prototype: `def append_write(filename="", text=""):`
- If the file doesn’t exist, it should be created
- You must use the `with` statement
- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        f.write("\n" + text)
        return len(text)
```
### Result
```bash
24
```

## 3. To JSON string
Write a function that returns the JSON representation of an object (string):

### Objectives
Prototype: `def to_json_string(my_obj):`
You don’t need to manage exceptions if the object can’t be serialized.

### Expectation
```python3
#!/usr/bin/python3

import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
```
### Result
```bash
[1, 2, 3]
<class 'str'>
{"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": true, "info": {"age": 36, "average": 3.14}}
<class 'str'>
[TypeError] Object of type set is not JSON serializable
```

## 4. From JSON string to Object
Write a function that returns an object (Python data structure) represented by a JSON string:

### Objectives
- Prototype: `def from_json_string(my_str):`
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.

### Expectation
```python3
#!/usr/bin/python3

import json


def from_json_string(my_str):
    return json.loads(my_str)
```
### Result
```bash
[1, 2, 3]
<class 'list'>
{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
<class 'dict'>
[JSONDecodeError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
```

## 5. Save Object to a file
Write a function that writes an Object to a text file, using a JSON representation:

### Objectives
- Prototype: `def save_to_json_file(my_obj, filename):`
You must use the `with` statement
You don’t need to manage exceptions if the object can’t be serialized.
You don’t need to manage file permission exceptions.

### Expectation
```python3
#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        json.dump(my_obj, f)
```
### Result
```bash
guillaume@ubuntu:~/$ ./5-main.py
[TypeError] Object of type set is not JSON serializable
guillaume@ubuntu:~/$ cat my_list.json ; echo ""
[1, 2, 3]
guillaume@ubuntu:~/$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
guillaume@ubuntu:~/$ cat my_set.json ; echo ""

```

## 6. Create object from a JSON file
Write a function that creates an Object from a “JSON file”:

### Objectives
- Prototype: `def load_from_json_file(filename):`
- You must use the `with` statement
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
- You don’t need to manage file permissions / exceptions.

### Expectation
```python3
#!/usr/bin/python3

import json


def load_from_json_file(filename):
    with open(filename, "r") as f:
        return json.load(f)
```
### Result
```bash
guillaume@ubuntu:~/$ cat my_list.json ; echo ""
[1, 2, 3]
guillaume@ubuntu:~/$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
guillaume@ubuntu:~/$ cat my_fake.json ; echo ""
{"is_active": true, 12 }
guillaume@ubuntu:~/$ ./6-main.py
[1, 2, 3]
<class 'list'>
{'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active': True}
<class 'dict'>
[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
[JSONDecodeError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```