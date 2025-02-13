#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open("data.json", "w") as f:
            json.dump(data, f)
        return True
    except Exception as e:
        print(f"{e}")
        return False
