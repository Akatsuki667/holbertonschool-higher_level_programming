# Python - Serialization

## 0. Basic Serialization
Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

### Instructions
Write a Python module named `task_00_basic_serialization.py` with the following functions:
```python3
def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    pass

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    pass
```
- The function `serialize_and_save_to_file` take 2 parameters:
	- `data`: A Python Dictionary with data
	- `filename`: The filename of the output JSON file. If the output file already exists it should be replaced.
- The function `load_and_deserialize` take 1 `parameters`:
	- `filename`: The filename of the input JSON file This function returns a Python Dictionary with the deseialized JSON data from the file.

### Expectation
```python3
#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as f:
        serialized_data = json.dumps(data)
        f.write(serialized_data)


def load_and_deserialize(filename):
    with open(filename, "r") as f:
        data = f.read()
        return json.loads(data)
```
### Result
```bash
Data serialized and saved to 'data.json'.
Deserialized Data:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
```

## 1. Pickling Custom Classes
Learn how to serialize and deserialize custom Python objects using the pickle module.

### Instructions
- Create a custom Python class named CustomObject. This class should have the following attributes:
	- `name` (a string)
	- `age` (an integer)
	- `is_student` (a boolean)
- Implement two methods within this class:
    - `serialize(self, filename)`: This method will take a filename as its parameter. Using the `pickle` module, it will serialize the current instance of the object and save it to the provided filename.
    - `@classmethod deserialize(cls, filename)`: This class method will take a filename as its parameter. Using the pickle module, it will load and return an instance of the `CustomObject` from the provided filename.

### Expectation
```python3
#!/usr/bin/python3
import pickle


class CustomObject:

    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is_tudent: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle_data = pickle.dump(self, f)  # self = obj à sérialiser

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
```
### Result
```bash
Original Object:
Name: John
Age: 25
Is Student: True

Deserialized Object:
Name: John
Age: 25
Is Student: True
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