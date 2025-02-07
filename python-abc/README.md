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
#!/usr/bin/python3

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(value):
    print(f"Area: {value.area()}")
    print(f"Perimeter: {value.perimeter()}")
```
### Result
```bash
Area: 78.53981633974483
Perimeter: 31.41592653589793
Area: 28
Perimeter: 22
```

## 2. Extending the Python List with Notifications
Create a class named `VerboseList` that extends the Python `list` class. This custom class should print a notification message every time an item is added (using the `append` or `extend` methods) or removed (using the `remove` or `pop` methods).

### Instructions
__Setting up the VerboseList Class__:
Define a class `VerboseList` that inherits from the built-in `list` class.
Within `VerboseList`, override the methods that modify the list: `append`, `extend`, `remove`, and `pop`.

__Implementing Notifications__:
For the `append` method: After adding the item to the list, print a message like “Added [item] to the list.”
For the `extend` method: After extending the list, print a message like “Extended the list with [x] items.” where [x] is the number of items added.
For the `remove` method: Before removing the item from the list, print a message like “Removed [item] from the list.”
For the `pop` method: Before popping the item from the list, print a message like “Popped [item] from the list.” If the index is not specified, default behavior is to pop the last item.

__Testing__:
Instantiate a `VerboseList` object.
Test all the overridden methods (`append`, `extend`, `remove`, and `pop`) and ensure that the appropriate messages are printed for each operation.

### Expectation
```python3
#!/usr/bin/python3


class VerboseList(list):

    def append(self, item):
        print(f"Added {[item]} to the list.")

    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with {[item]} items.")

    def remove(self, item):
        print(f"Removed {[item]} from the list.")

    def pop(self, index=-1):  # -1 par défaut pour suivre comportement list.pop
        item = self[index]  # Récupération élément
        print(f"Popped {[item]} from the list.")
        return super().pop(index)  # Supprimer et retourner élément
```
### Result
```bash
Added [4] to the list.
Extended the list with [2] items.
Removed [2] from the list.
Popped [6] from the list.
Popped [1] from the list.
```

## 3. CountedIterator - Keeping Track of Iteration
Create a class named `CountedIterator` hat extends the built-in iterator obtained from the iter function. The `CountedIterator` should keep track of the number of items that have been iterated over. Specifically, you will need to override the __next__ method to increment a counter each time an item is fetched.

### Instructions
__Setting up the CountedIterator Class__:
Define a class `CountedIterator`.
In the constructor (__init__), initialize two attributes: the iterator object (using the `iter` function) and a counter to track the number of items iterated.
Provide a method `get_count` to return the current value of the counter.

Overriding the next Method:
Within the `CountedIterator` class, override the __next__ method.
In this method, increment the counter each time the __next__ method is called.
Fetch the next item from the original iterator and return it. If there are no items left to iterate, the method should raise the `StopIteration` exception.

Testing:
Instantiate a `CountedIterator` object using a list or another iterable.
Iterate over items using a loop or manual calls to the __next__ method.
Use the `get_count` method to retrieve and print the number of items that have been fetched.

### Expectation
```python3
#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iters):
        self.iterator = iter(iters)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item
```
### Result
```bash
Got 1, total 1 items iterated.
Got 2, total 2 items iterated.
Got 3, total 3 items iterated.
Got 4, total 4 items iterated.
No more items.
```

## 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
Construct a `FlyingFish` class that inherits from both a `Fish` class and a `Bird` class. Within `FlyingFish`, override methods from both parents. The goal is to comprehend multiple inheritance and how Python determines method resolution order.

### Instructions
__Parent Classes Setup__:
Create a `Fish` class with methods `swim` (which prints “The fish is swimming”) and `habitat` (which prints “The fish lives in water”).
Create a `Bird` class with methods `fly` (which prints “The bird is flying”) and `habitat` (which prints “The bird lives in the sky”).

__Implementing FlyingFish__:
Construct a `FlyingFish` class that inherits from both `Fish` and `Bird`.
Override the `fly` method to print “The flying fish is soaring!”.
Override the `swim` method to print “The flying fish is swimming!”.
Override the `habitat` method to print “The flying fish lives both in water and the sky!”.

__Testing and MRO Exploration__:
Instantiate an object of the `FlyingFish` class.
Call the `fly`, `swim`, and `habitat` methods and observe the outputs.
Use the `mro()` method or the .__mro__ attribute on the `FlyingFish` class to investigate the method resolution order. For instance, `print(FlyingFish.mro())`.
### Expectation
```python3
#!/usr/bin/python3

class Fish:

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
```
### Result
```bash
The flying fish is swimming!
The flying fish is soaring!
The flying fish lives both in water and the sky!
```

##
### Instructions
### Expectation
```python3
```
### Result
```bash
```
