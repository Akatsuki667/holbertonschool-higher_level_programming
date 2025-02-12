#!/usr/bin/python3

import json


def load_from_json_file(filename):
    """
    Charge un objet Python à partir d'un fichier au format JSON.

    Cette fonction lit fichier JSON, désérialise son contenu en un objet Python

    Args:
    filename (str): Le nom du fichier JSON à lire.

    Returns:
    object: L'objet Python résultant de la désérialisation du fichier JSON.

    Example:
    >>> data = load_from_json_file('data.json')
    >>> print(data)
    {'name': 'Alice', 'age': 30}
    """
    with open(filename, "r") as f:
        return json.load(f)
