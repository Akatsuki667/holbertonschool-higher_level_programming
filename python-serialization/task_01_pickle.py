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
