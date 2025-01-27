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

    def area(self):
        """
        Calcule et retourne l'aire du carré

        Returns:
        int: L'aire du carré
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter pour l'attribut size

        Returns:
        int: La taille du carré
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter pour l'attribut size

        Args:
        value(int): Nouvelle taille du carré

        Raises:
        TypeError: Si value n'est pas un entier
        ValueError: Si value est inférieure à zéro
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

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
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
