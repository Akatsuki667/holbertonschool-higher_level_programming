#!/usr/bin/python3
"""
Module `4-square`

Ce module définit une classe `Square` qui représente un carré
"""


class Square:
    """
    Classe qui représente un carré

    Attribut privé:
    __size: La taille du carré (initialisé lors de l'instanciation)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructeur pour initialiser un carré avec une taille donnée

        Args:
        size(int): La taille du carré

        Raises:
        TypeError: Si le type de size n'est pas un entier
        ValueError: Si la valeur de size est inférieur à zéro
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter pour l'attribut size

        Returns:
        int: La taille du carré
        """
        return self.__size

    @property
    def position(self):
        """
        Setter pour l'attribut size

        Args:
        value(int): Nouvelle taille du carré

        Raises:
        TypeError: Si value n'est pas un entier
        ValueError: Si value est inférieure à zéro
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
        Calcule et retourne l'aire du carré

        Returns:
        int: L'aire du carré
        """
        return self.__size ** 2

    def my_print(self):
        """
        Affiche le carré représenté par le caractère `#`.

        Si la taille du carré est 0, la méthode affiche une ligne vide.
        Sinon, elle affiche un carré de `#`, dont le nb de lignes et colonnes
        correspond à la valeur de `__size`.

        Exemple:
        Si `__size = 3`, la sortie sera:
        ###
        ###
        ###

        Si `__size = 0`, la sortie sera une ligne vide.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
