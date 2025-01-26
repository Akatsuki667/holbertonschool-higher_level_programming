#!/usr/bin/python3
"""
Ceci est `5-text_indentation` module

Ce module contient la fonction `text_indentation(text)`

Cette fonction affiche un texte avec 2 lignes
avec ces caractères `. ? :` 
"""


def text_indentation(text):
    """
    Cette fonction affiche un texte avec 2 lignes
    avec ces caractères `. ? :` 

    Paramètre:
    text(str): Texte à formater et afficher

    Raises:
    TypeError: Si le texte n'est pas de type str

    Exemples:
    >>> text_indentation("Hello. How are you? Fine:")
    Hello.

    How are you?

    Fine:
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    skip_space = False

    for char in text:
        if char in ".:?":
            result += char + "\n\n"
            skip_space = True
        elif char == " " and skip_space:
            continue
        else:
            result += char
            skip_space = False
    print(result.strip(), end="")
