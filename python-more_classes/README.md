# Python - More Classes and Objects

## 0. Simple rectangle
Write an empty class `Rectangle` that defines a rectangle:

### Objectives
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3
"""
Module `0-rectangle`

Ce module définit une classe `Rectangle`, qui, pour l'instant ne fais rien.
"""


class Rectangle:
    """
    Représente un rectangle

    Cette classe est vide, sert de base pour fonctionnalités futures.
    """
    pass
```
### Result
```bash
<class '0-rectangle.Rectangle'>
{}
```

## 1. Real definition of a rectangle
Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)

### Objectives
- Private instance attribute: `width`:
	- property `def width(self):` to retrieve it
	- property setter `def width(self, value):` to set it:
		- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
		- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
	- property `def height(self):` to retrieve it
	- property setter `def height(self, value):` to set it:
		- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
		- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3
"""
Module `1-rectangle`

Ce module définit une classe `Rectangle` qui définit un rectangle
"""


class Rectangle:
    """
    Classe qui représente un rectangle

    Attribut privé:
    __width: largeur du rectangle (initialisé lors de l'instanciation)
    __height: longueur dur rectangle (initialisé lors de l'instanciation)
    """

    def __init__(self, width=0, height=0):
        """
        Constructeur pour initialiser un rectangle avec une `width` et `height`

        Args:
        width(int): Largeur du rectangle
        height(int): Longueur du rectangle
        """
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
```
### Result
```bash
{'_Rectangle__width': 2, '_Rectangle__height': 4}
{'_Rectangle__width': 10, '_Rectangle__height': 3}
```

## 2. Area and Perimeter
Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)

### Objectives
- Private instance attribute: `width`:
	- property `def width(self):` to retrieve it
	- property setter `def width(self, value):` to set it:
		- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
		- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
	- property `def height(self):` to retrieve it
	- property setter `def height(self, value):` to set it:
		- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
		- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
	- if `width` or `height` is equal to `0`, perimeter is equal to `0`
- You are not allowed to import any module

### Expectation
```python3
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
            return (2 * (self.__width + self.__height))
```
### Result
```bash
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```