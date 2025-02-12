#!/usr/bin/python3

import json


def from_json_string(my_str):
    """
    Convertit une chaîne de caractères au format JSON en un objet Python.

    Cette fonction utilise le module `json` pour désérialiser une chaîne JSON
    en un objet Python. La chaîne doit être au format JSON valide.

    Args:
        my_str (str): La chaîne de caractères au format JSON à convertir.

    Returns:
        object: L'objet Python résultant de la conversion de la chaîne JSON.

    Example:
        >>> from_json_string('{"name": "Alice", "age": 30}')
        {'name': 'Alice', 'age': 30}
        >>> from_json_string('["apple", "banana", "cherry"]')
        ['apple', 'banana', 'cherry']
    """
    return json.loads(my_str)
