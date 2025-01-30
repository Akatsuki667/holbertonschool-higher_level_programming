#!/usr/bin/python3
"""
Ce module définit une classe square (ou carré)
"""


class Square:
    """
    Cette classe représente un carré
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter pour l'attribut __size.
        Retourne la valeur de __size.
        """
        return self.__size

    @property
    def position(self):
        """
        Getter pour l'attribut __position.
        Retourne la valeur de __position.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Setter pour l'attribut __size.
        Vérifie que value est un entier >= 0 avant de l'affecter.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
        Setter pour l'attribut __position.
        Vérifie que value est un tuple de 2 entiers positifs.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print a square of size self.__size.
        """
        if self.__size == 0:
                print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range (self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
