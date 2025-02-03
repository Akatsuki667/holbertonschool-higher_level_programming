#!/usr/bin/python3
"""
Module `2-is_same_class`

Contient la fonction `is_same_class`
"""


def is_same_class(obj, a_class):
    """
    Vérifie si un objet est exactement une instance d'une classe donnée.

    Args:
    obj (any): L'objet à vérifier.
    a_class (type): La classe de référence.

    Returns:
    bool: True si `obj` est exactement une instance de `a_class`, sinon False.
    """
    return type(obj) is a_class
