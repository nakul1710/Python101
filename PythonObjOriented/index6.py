#Super() = Function used in a child  to call methods  from a parent class (superclass)
#           Allow you to extend the functionality  of the inherited method


class Shape:
    def __init__(self, is_filled, color):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        print(f"It is a square with an area of { self.width * self.width}cm^2")

class Triangle(Shape):
    def __init__(self, color, is_filled, width,height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    
    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")



circle = Circle(color="Red", is_filled=True, radius=5)
square = Square(color="blue",is_filled=False,width=10)
triangle = Triangle(color="Green",is_filled=True,width=10,height=5)


circle.describe()

print(circle.color)
print(circle.is_filled)
print(circle.radius)

square.describe()
print(square.width)


triangle.describe()
print(triangle.width)
print(triangle.height)


