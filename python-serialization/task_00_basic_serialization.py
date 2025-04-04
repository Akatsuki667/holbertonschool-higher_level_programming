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
