#!/usr/bin/python3
"""
Module `3-rectangle`

Ce module définit une classe `Rectangle` qui définit un rectangle
"""


class Rectangle:
    """
    Classe qui représente un rectangle

    Attribut privé:
    __width: largeur du rectangle (initialisé lors de l'instanciation)
    __height: longueur dur rectangle (initialisé lors de l'instanciation)
    """
    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        aire_rect_1 = rect_1.area()
        aire_rect_2 = rect_2.area()

        if aire_rect_1 >= aire_rect_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """
        Constructeur pour initialiser un rectangle avec une `width` et `height`

        Args:
        width(int): Largeur du rectangle
        height(int): Longueur du rectangle
        """
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter attribut width

        Return:
        int: largeur width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter attribut width

        Args:
        value(int): valeur de la width

        Raises:
        TypeError: Si `value` n'est pas un entier
        ValueError: Si `value` est inférieur à zéro
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter attribut height

        Return:
        int: largeur Height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter attribut height

        Args:
        value(int): valeur de la height

        Raises:
        TypeError: Si `value` n'est pas un entier
        ValueError: Si `value` est inférieur à zéro
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calcule l'aire du rectangle

        Return:
        int: L'aire du rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calcule le périmètre d'un rectangle

        Return:
        int: L'aire d'un rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """
        Affiche chaîne de caractères `#` représentant le rectangle

        Return
        str: chaîne de caractères `#` représentant le rectangle
        """
        rectangle_str = ""

        if self.__width == 0 or self.__height == 0:
            return rectangle_str

        for i in range(self.__height):
            rectangle_str += (str(self.print_symbol) * self.__width)
            if i is not self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """
        Affiche chaîne de caractères `#` représentant le rectangle

        Return
        str: chaîne de caractères `#` représentant le rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Affiche "By rectangle..."
        """
        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")
