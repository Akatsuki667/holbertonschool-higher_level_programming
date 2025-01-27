# Python - Classes and Objects

## 0. My first square
Write an empty class `Square` that defines a square:

### Objectives
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3
"""
Module 0-square

Ce module définit une classe Square qui, pour l'instant, ne fait rien.
"""


class Square:
    """
    Représente un carré.

    Cette classe est vide, sert de base pour fonctionnalités futures.
    """

    pass
```
### Result
```bash
<class '0-square.Square'>
{}
```

## 1. Square with size
Write a class `Square` that defines a square by: (based on `0-square.py`)

### Objectives
- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)
- You are not allowed to import any module

#### Why ?
Why `size` is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

### Expectation
```python3
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
```
### Result
```bash
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
```

## 2. Size validation
Write a class `Square` that defines a square by: (based on `1-square.py`)

### Objectives
- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
	- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
	- if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- You are not allowed to import any module
### Expectation
```python3
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
```
### Result
```bash
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
```

## 3. Area of a square
Write a class `Square` that defines a square by: (based on `2-square.py`)

### Objectives
- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
	- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
	- if `size` is less than `0`, raise a `ValueError` exception with the message size must be >= 0
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3
"""
Module `3-square`

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
```
### Result
```bash
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
```

## 4. Access and update private attribute
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
