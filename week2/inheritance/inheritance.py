"""

- Create a base class Shape with method area() that raises
NotImplementedError.
- Implement Rectangle(width, height) and Circle(radius) subclasses
that override area().
- Create a list of mixed shapes and print each area (rounded to 2 decimals).
"""


# Base class
class Shape:
    def area(self):
        # Force subclasses to implement their own area() method
        raise NotImplementedError("Subclasses must implement area()")


# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


shapes = [
    Rectangle(5, 10),
    Circle(7),
    Rectangle(3, 4),
    Circle(2.5)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")