# Access Modifiers
# Access modifiers in Python control the visibility of class members (attributes and methods). They help encapsulate data, allowing for better control over how an object's data is accessed and modified. Python primarily uses three types of access modifiers:

# Default Access: By default, all members in Python are public unless specified otherwise.

# Public
# Public members are accessible from outside the class. They can be accessed and modified freely. By default, all members in Python are public unless specified otherwise.


class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute

    def display_info(self):
        return f"Car: {self.brand} {self.model}"

# Creating an object of the Car class
my_car = Car("Toyota", "Camry")
print(my_car.display_info())  # Output: Car: Toyota Camry
print(my_car.brand)           # Output: Toyota



# Protected
# Protected members are indicated by a single underscore prefix (_). They are intended to be accessed only within the class and by derived classes (subclasses). They should not be accessed directly from outside the class, although they can still be accessed if necessary (it’s more of a convention).

class Animal:
    def __init__(self, name):
        self._name = name  # Protected attribute

    def _make_sound(self):  # Protected method
        return "Some sound"

class Dog(Animal):
    def bark(self):
        return f"{self._name} says Woof!"

# Creating an object of the Dog class
my_dog = Dog("Buddy")
print(my_dog.bark())  # Output: Buddy says Woof!
print(my_dog._make_sound())  # Output: Some sound (not recommended)