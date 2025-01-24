# Python - Test-driven development

## 0. Integers addition
Write a function that adds 2 integers.

### Objectives
- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
- `a` and `b` must be first casted to integers if they are float
- Returns an integer: the addition of `a` and `b`
- You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
"""
Ceci est `0-add_intger.py` module

Ce module contient une fonction `add_integer(a, b=98)`

Cette fonction additionne valeur de `type_int`
"""

def add_integer(a, b=98):
    """
    Additionne deux paramètres de `type_int`

    Paramètres:
    a(int, float): premier nombre
    b(int, float): second nombre

    Return:
    int: somme de l'addition

    Raises:
    TypeError: Si a et b ne sont pas des entiers

    Exemples:
    >>> add_integer(5, 2)
    7
    >>> add_integer(5, 2.5)
    7
    >>> add_integer(2)
    100
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
```
### Result
```bash
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
guillaume@ubuntu:~/$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
```

##
### Objectives
### Expectation
```Python
```
### Result
```bash
```

##
### Objectives
### Expectation
```Python
```
### Result
```bash
```

##
### Objectives
### Expectation
```Python
```
### Result
```bash
```

##
### Objectives
### Expectation
```Python
```
### Result
```bash
```

##
### Objectives
### Expectation
```Python
```
### Result
```bash
```
