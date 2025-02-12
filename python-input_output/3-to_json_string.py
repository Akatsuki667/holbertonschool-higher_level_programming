#!/usr/bin/python3

def to_json_string(my_obj):
    """
    Convertit un objet Python en une chaîne de caractères au format JSON.

    Cette fonction utilise le module `json` pour sérialiser un objet Python
    en une chaîne JSON. L'objet doit être sérialisable (par exemple, un
    dictionnaire, une liste, un tuple, une chaîne, un entier, etc.).

    Args:
    my_obj: L'objet Python à convertir en chaîne JSON.

    Returns:
    str: Une chaîne de caractères représentant l'objet au format JSON.

    Example:
    >>> to_json_string({'name': 'Alice', 'age': 30})
    '{"name": "Alice", "age": 30}'
    >>> to_json_string(['apple', 'banana', 'cherry'])
    '["apple", "banana", "cherry"]'
    """
    return json.dumps(my_obj)
