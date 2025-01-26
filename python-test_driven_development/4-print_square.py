#!/usr/bin/python3
"""
Ceci est `4-print_square.py` module

Ce module contient la fonction `print_square(size)`

Cette fonction affiche un carré en utilisant `#`
"""


def print_square(size):
    """
    Affiche un carré en utilisant `#`

    Paramètre:
    size(int): la taille de la longueur du carré

    Raises:
    TypeError: Si la taille n'est ps `int`
    ValueError: Si la taille est plus petite que 0

    Exemples:
    >>> print_square(2)
    ##
    ##
    >>> print_square(4)
    ####
    ####
    ####
    ####
    """

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
