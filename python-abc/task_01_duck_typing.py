#!/usr/bin/python3

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * 3.14 * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
