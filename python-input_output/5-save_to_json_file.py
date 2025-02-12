#!/usr/bin/python3
"""
JSON string parsing module.

This module provides functionality to parse JSON strings into their Python
object representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    méthode pour ajouter du texte dans un fichier
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
