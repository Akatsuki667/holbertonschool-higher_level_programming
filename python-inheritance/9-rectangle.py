#!/usr/bin/python3
"""
Module contenant la classe Rectangle qui hérite de BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe représentant un rectangle, héritant de BaseGeometry.

    Hérite des fonctionnalités de BaseGeometry et ajoute
    la gestion des attributs de largeur et de hauteur.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur validées.

        Args:
        width (int): La largeur du rectangle, doit être un entier positif.
        height (int): La hauteur du rectangle, doit être un entier positif.

        Raises:
        TypeError: Si width ou height ne sont pas des entiers.
        ValueError: Si width ou height ne sont pas positifs.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.

        Returns:
        int: L'aire du rectangle (largeur × hauteur).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne du rectangle.

        Returns:
        str: Une chaîne de la forme "[Rectangle] width/height".
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
