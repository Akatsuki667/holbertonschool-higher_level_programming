#!/usr/bin/python3
"""
Module `4-inherits_from`

Contient la fonction `inherits_from`
"""


def inherits_from(obj, a_class):
    """
    Vérifie si un objet est une instance d'une sous-classe de `a_class`
    (sans être une instance directe de `a_class`).

    Args:
    obj (any): L'objet à vérifier.
    a_class (type): La classe de référence.

    Returns:
    bool: True si `obj` est une instance d'une sous-classe de `a_class`,
        mais pas une instance directe de `a_class`. Sinon, False.
    """
    return not issubclass(a_class, type(obj))
