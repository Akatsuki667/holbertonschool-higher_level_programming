#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est instance d'une classe ou classe parente.

    Args:
    obj (any): L'objet à vérifier.
    a_class (type): La classe de référence.

    Returns:
    bool: True`obj` instance de `a_class`/ classe parente`a_class`,sinon False.
    """
    return isinstance(obj, a_class)
