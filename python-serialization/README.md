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

## 2. Converting CSV Data to JSON Format
The objective of this exercise is to gain experience in reading data from one format (CSV) and converting it into another format (JSON) using serialization techniques.

### Instructions
- Begin by importing the required modules: `python import csv import json`
- Define a function named `convert_csv_to_json` that takes the CSV filename as its parameter and writes the JSON data to `data.json`.
- Inside this function:
    - Use Python’s `csv` module to open the CSV file and read the data. Use the `DictReader` class to convert each row into a dictionary.
    - Serialize the list of dictionaries using the `json` module.
    - Write the serialized JSON data to `data.json`.
- The function should return `True` if the conversion was successful.
- Handle exceptions, such as `file not found`. Function should return `False` in this case.

### Expectation
```python3
#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
        print(data)

    with open("data.json", "w") as f:
        json.dump(data, f)
```
### Result
```bash
[{'name': 'John', 'age': '28', 'city': 'New York'}, {'name': 'Alice', 'age': '24', 'city': 'Los Angeles'}, {'name': 'Bob', 'age': '22', 'city': 'Chicago'}, {'name': 'Eve', 'age': '30', 'city': 'San Francisco'}]
```

## 3. Serializing and Deserializing with XML
In this exercise we’ll explore serialization and deserialization using XML as an alternative format to JSON.

### Instructions
- Begin by importing the required modules. You can use the `xml.etree.ElementTree` module which is a part of Python’s standard library for XML processing:

- Define two main functions:
- `serialize_to_xml(dictionary, filename)`: This will take a Python dictionary and a filename as parameters. It should serialize the dictionary into XML and save it to the given filename.
- `deserialize_from_xml(filename)`: This will take a filename as its parameter, read the XML data from that file, and return a deserialized Python dictionary.

- For `serialize_to_xml`:
- Create a root element, e.g., `<data>`.
- Iterate through the dictionary items and add them as child elements to the root.
- Write the XML tree to the provided filename using the ET.ElementTree class.

- For `deserialize_from_xml`:
- Parse the XML file using `ET.parse`.
- Navigate through the XML elements to reconstruct the dictionary.
- Return the constructed dictionary.

- Be cautious about data types. XML doesn’t differentiate between numbers and strings, etc., like Python does. You might need to manage type conversions.

### Expectation
```python3
#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionnary, filename):

    root = ET.Element("data")

    for key, value in dictionnary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):

    tree = ET.parse(filename)
    root = tree.getroot()

    dictionnary = {child.tag: child.text for child in root}
    return dictionnary
```
### Result
```bash
Dictionary serialized to data.xml

Deserialized Data:
{'name': 'John', 'age': '28', 'city': 'New York'}
```
