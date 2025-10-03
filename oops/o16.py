# Abstraction
#  Abstraction hides implementation details and shows only the necessary features. In Python,
#  abstraction is achieved using abstract base classes (ABC)

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
circle = Circle(5)
print(circle.area())