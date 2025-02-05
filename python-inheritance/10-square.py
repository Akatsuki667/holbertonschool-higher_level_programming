#!/usr/bin/python3
"""
Module contenant la classe Square qui hérite de Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe représentant un carré, héritant de Rectangle.

    Hérite des fonctionnalités de Rectangle et assure que
    la largeur et la hauteur sont égales (propriété d'un carré).
    """

    def __init__(self, size):
        """
        Initialise un carré avec une taille validée.

        Args:
        size (int): La taille du côté du carré, doit être un entier positif.

        Raises:
        TypeError: Si size n'est pas un entier.
        ValueError: Si size n'est pas positif.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns:
        int: L'aire du carré (size × size).
        """
        return self.__size * self.__size
