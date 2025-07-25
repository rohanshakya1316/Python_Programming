from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        return f"A shape with color {self.color}."
    
class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return round((pi * self.radius ** 2), 2)
    
c = Circle(7, "black")
print(c.area())
print(c.describe())