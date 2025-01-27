#!/usr/bin/python3
"""
Module `2-square.py`

Ce module définit une classe `Square` qui représente un carré
"""


class Square:
    """
    Classe qui représente un carré

    Attribut privé:
    __size: La taille du carré (initialisé lors de l'instanciation)
    """

    def __init__(self, size=0):
        """
        Constructeur pour initialiser un carré avec une taille donnée

        Args:
        size(int): La taille du carré

        Raises:
        TypeError: Si le type de size n'est pas un entier
        ValueError: Si la valeur de size est inférieur à zéro
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
