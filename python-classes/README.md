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
Write a class `Square` that defines a square by: (based on `3-square.py`)

### Objectives
- Private instance attribute: `size`:
    - property `def size(self)`: to retrieve it
    - property setter `def size(self, value)`: to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module

#### Why ?
Why a getter and setter?

Reminder: `size` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

### Expectation
```python3
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
```
### Result
```bash
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
```

## 5. Printing a square
Write a class `Square` that defines a square by: (based on `4-square.py`)

### Objectives
- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    - if `size` is equal to 0, print an empty line
- You are not allowed to import any module

### Expectation
```python3
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
```
### Result
```bash
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
```

## 6. Coordinates of a square
Write a class `Square` that defines a square by: (based on `5-square.py`)

### Objectives
- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Private instance attribute: `position`:
    - property `def position(self):` to retrieve it
    - property setter `def position(self, value):` to set it:
        - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    - if `size` is equal to 0, print an empty line
    - `position` should be use by using space - Don’t fill lines by spaces when `position[1] > 0`
- You are not allowed to import any module

### Expectation
```python3
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
        position(int): tuple d'entiers positifs

        Raises:
        TypeError: Si le type de size n'est pas un entier
        ValueError: Si la valeur de size est inférieur à zéro
        TypeError: Si position est un tuple de 2 entiers positifs
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if not all(isinstance(x, int) and x >= 0 for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

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

```
### Result
```bash
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$

```
