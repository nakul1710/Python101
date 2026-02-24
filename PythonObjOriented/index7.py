# Polymorphism : It's a Greek word which means to "have many forms or faces"
# poly = Many
# morphe = forms

# Two ways to achieve polymorphism:
# 1. Inheritance
# 2. Duck typing  

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class pizza(Circle):
    def __init__(self,Toppings,radius):
        super().__init__(radius)
        self.Toppings = Toppings

shapes = [Circle(5), Square(4), Triangle(3, 5),pizza("tamato",15)]

for shape in shapes:
    print(f"{shape.area()}cm^2")