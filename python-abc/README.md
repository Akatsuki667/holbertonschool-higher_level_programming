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

## 1. Shapes, Interfaces, and Duck Typing
1. Create an abstract class named `Shape` with two abstract methods: `area` and `perimeter`.
2. Implement two concrete classes: `Circle` and `Rectangle`, both inheriting from Shape. Each class should provide implementations for the `area` and `perimeter` methods.
3. Write a standalone function named `shape_info` that accepts an object of type `Shape` (by duck typing) and prints its area and perimeter.
4. Test the `shape_info` function with instances of both `Circle` and `Rectangle`.

### Instructions
__Shape Abstract Class__:
- Define an abstract class `Shape` using the `ABC` package.
- Within Shape, declare two abstract methods: `area` and `perimeter`.

__Circle and Rectangle Classes__:
- Create a `Circle` class that inherits from `Shape`. The constructor (__init__) should accept a radius. Implement the `area` and `perimeter` methods.
- Create a `Rectangle` class, also inheriting from `Shape`. Its constructor should accept the width and height. Implement the `area` and `perimeter` methods.

__shape_info Function__:
- Define a function named `shape_info` that takes a single argument.
- Without explicitly checking the type of the argument, call its `area` and `perimeter` methods (relying on duck typing).
- Print the area and perimeter of the shape passed to the function.

__Testing__:
Instantiate a `Circle` and a `Rectangle`.
Pass each object to the `shape_info` function and observe the output.

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
