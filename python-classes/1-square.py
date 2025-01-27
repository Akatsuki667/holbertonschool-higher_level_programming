#!/usr/bin/python3
"""
Module `1-square`

Ce module définit une classe `Square` qui représente un carré
"""


class Square:
    """
    Classe qui représente un carré

    Attribut privé:
    __size: La taille du carré (initialisé lors de l'instanciation)
    """

    def __init__(self, size):
        """
        Constructeur pour initialiser un carré avec une taille donnée

        Args:
        size(int): La taille du carré
        """
        self.__size = size
