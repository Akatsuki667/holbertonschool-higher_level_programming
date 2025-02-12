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

## 7. Load, add, save
Write a script that adds all arguments to a Python list, and then save them to a file:

### Objectives
- You must use your function `save_to_json_file` from `5-save_to_json_file.py`
- You must use your function `load_from_json_file` from `6-load_from_json_file.py`
- The list must be saved as a JSON representation in a file named `add_item.json`
- If the file doesn’t exist, it should be created
- You don’t need to manage file permissions / exceptions.

### Expectation
```python3
#!/usr/bin/python3

from sys import argv  # importation ARGV de SYS
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():

    filename = "add_item.json"  # Définit nom du fichier JSON

    try:
        args = load_from_json_file(filename)  # Charger données fichier JSON
    except FileNotFoundError:
        args = []

    args.extend(argv[1:])  # Ajout argv CLI sauf le premier
    save_to_json_file(args, filename)


# Vérification script exécuté (et non importé comme module)
if __name__ == "__main__":
    add_item()
```
### Result
```bash
guillaume@ubuntu:~/$ cat add_item.json
cat: add_item.json: No such file or directory
guillaume@ubuntu:~/$ ./7-add_item.py
guillaume@ubuntu:~/$ cat add_item.json ; echo ""
[]
guillaume@ubuntu:~/$ ./7-add_item.py Best School
guillaume@ubuntu:~/$ cat add_item.json ; echo ""
["Best", "School"]
guillaume@ubuntu:~/$ ./7-add_item.py 89 Python C
guillaume@ubuntu:~/$ cat add_item.json ; echo ""
["Best", "School", "89", "Python", "C"]
guillaume@ubuntu:~/$ 
```

## 8. Class to JSON
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

### Objectives
- Prototype: `def class_to_json(obj):`
- `obj` is an instance of a Class
- All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3

def class_to_json(obj):
    return obj.__dict__

```
### Result
```bash
guillaume@ubuntu:~/$ ./8-main.py 
<class '8-my_class.MyClass'>
[MyClass] John - 89
<class 'dict'>
{'name': 'John', 'number': 89}
guillaume@ubuntu:~/$ ./8-main_2.py 
<class '8-my_class_2.MyClass'>
[MyClass] John - 4 => 1
<class 'dict'>
{'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}
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