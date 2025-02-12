#!/usr/bin/python3

def class_to_json(obj):
    """
    Convertit un objet en un dictionnaire représentant ses attributs.

    Cette fonction prend un objet et retourne un dictionnaire contenant
    tous les attributs de cet objet et leurs valeurs associées.
    Cela peut être utile pour sérialiser un objet en JSON.

    Args:
    obj: L'objet dont les attributs doivent être convertis en dictionnaire.

    Returns:
    dict: Un dictionnaire représentant les attributs de l'objet.

    Example:
    >>> class Person:
    ...     def __init__(self, name, age):
    ...         self.name = name
    ...         self.age = age
    >>> person = Person('Alice', 30)
    >>> class_to_json(person)
    {'name': 'Alice', 'age': 30}
    """
    return obj.__dict__
