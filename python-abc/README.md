# Python - Abstract Classes and Interfaces

## 0. Abstract Animal Class and its Subclasses
1. Create an abstract class named `Animal` using the `ABC` package. This class should have an abstract method called `sound`.

2. Create two subclasses of `Animal`: `Dog` and `Cat`. Implement the `sound` method in each subclass to return the strings “Bark” and “Meow” respectively.

### Instructions
__Setting up the Abstract Class__:
- Import the necessary components from the `abc` module.
- Define the `Animal` class, ensuring it inherits from `ABC` to mark it as abstract.
- Inside the `Animal` class, declare an abstract method named `sound` using the `@abstractmethod` decorator.

__Implementing the Subclasses__:
- Create a subclass named `Dog` that inherits from the `Animal` class.
	- Implement the `sound` method in the `Dog` class to return the string “Bark”.
- Similarly, create a subclass named `Cat` that also inherits from the `Animal` class.
	- Implement the `sound` method in the `Cat` class to return the string “Meow”.

### Expectation
```python3
#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        return "Bark"


class Cat(Animal):

    def sound(self):
        return "Meow"
```
### Result
```bash
Bark
Meow
Traceback (most recent call last):
  File "/Users/altyt/Akatsuki667/holbertonschool-higher_level_programming/python-abc/./main_00_abc.py", line 10, in <module>
    animal = Animal()
TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'sound'
```

##
### Instructions
### Expectation
```python3
```
### Result
```bash
```

##
### Instructions
### Expectation
```python3
```
### Result
```bash
```

##
### Instructions
### Expectation
```python3
```
### Result
```bash
```

##
### Instructions
### Expectation
```python3
```
### Result
```bash
```

##
### Instructions
### Expectation
```python3
```
### Result
```bash
```
