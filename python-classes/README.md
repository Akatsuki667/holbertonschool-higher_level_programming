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
