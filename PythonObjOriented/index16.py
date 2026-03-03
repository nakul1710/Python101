# @property = Decorator used to define a method as a property (It can be accessed like an attribute)
#             Benefits: add additional logic with read, write, or delete access to an attribute


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        print("Width has been deleted")
        del self._width

    @height.deleter
    def height(self):
        print("Height has been deleted")
        del self._height

    @property
    def pretty_width(self):
        if hasattr(self, "_width"):
            return f"{self._width:.1f}cm"
        else:
            return "Width not set"

    @property
    def pretty_height(self):
        if hasattr(self, "_height"):
            return f"{self._height:.1f}cm"
        else:
            return "Height not set"


rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = 7

del rectangle.width
del rectangle.height

# Let's attempt to print pretty_width and pretty_height to see formatted values or fallback if deleted
print(rectangle.pretty_width)
print(rectangle.pretty_height)