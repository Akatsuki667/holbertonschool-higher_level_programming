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
