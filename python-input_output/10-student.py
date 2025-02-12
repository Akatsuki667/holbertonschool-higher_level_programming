#!/usr/bin/python3
"""File I/O Module.

This module provides functionality for writing text content to files using
UTF-8 encoding.
"""


class Student:
    """
    Class representing a student.

    A simple student class with basic personal information that can be
    converted to a JSON-compatible dictionary format.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
        first_name (str): First name of the student.
        last_name (str): Last name of the student.
        age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert Student instance to dictionary representation.

        Returns:
        dict: Dictionary containing all instance attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {key: value for key, value in self.__dict__.items()
                if key in attrs}
        return self.__dict__
