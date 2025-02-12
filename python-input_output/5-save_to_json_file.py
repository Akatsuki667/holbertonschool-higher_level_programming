#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    """
    Sauvegarde un objet Python dans un fichier au format JSON.

    Cette fonction sérialise un objet Python en JSON et l'écrit dans un fichier
    Si le fichier existe déjà, il sera écrasé.

    Args:
    my_obj: L'objet Python à sauvegarder.
    filename (str): Le nom du fichier où l'objet sera sauvegardé.

    Example:
    >>> save_to_json_file({'name': 'Alice', 'age': 30}, 'data.json')
    # Le fichier 'data.json' contiendra maintenant:{"name": "Alice", "age": 30}
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
