#!/usr/bin/python3
"""
Ceci est `3-say_my_name` module

Ce module contient une fonction `say_my_name(first_name, last_name="")`

Cette fonction affiche "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    affiche "My name is <first name> <last name>"

    Paramètres:
    first_name(str): Nom
    last_name(str): Prénom

    Raises:
    TypeError: Si first_name ou last_name ne sont pas de type str

    Exemples:
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
    >>> say_my_name(12, "White")
    TypeError: first_name must be a string
    """

    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")

    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
