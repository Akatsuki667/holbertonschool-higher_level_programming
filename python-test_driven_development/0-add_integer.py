#!/usr/bin/python3
"""
Ceci est `0-add_intger.py` module

Ce module contient une fonction `add_integer(a, b=98)`

Cette fonction additionne valeur de `type_int`
"""

def add_integer(a, b=98):
    """
    Additionne deux paramètres de `type_int`

    Paramètres:
    a(int, float): premier nombre
    b(int, float): second nombre

    Return:
    int: somme de l'addition

    Raises:
    TypeError: Si a et b ne sont pas des entiers

    Exemples:
    >>> add_integer(5, 2)
    7
    >>> add_integer(5, 2.5)
    7
    >>> add_integer(2)
    100
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
