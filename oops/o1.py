# A class serves as a blueprint for creating objects, which are instances of that class. In this example, we define a Dog class with attributes for name and age and a method for barking.

# A class is like a blueprint, and an object is the actual thing created from that blueprint.

# __init__ is a special method in Python classes.

# It is called automatically when you create (instantiate) an object from a class.

# Its main job is to initialize the object’s attributes.

# It’s similar to a constructor in other languages like Java or C++.
# it is used to accept the parameter with define the parameter name
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def bark(self):
        return f"{self.name} says Woof!"

# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Output: Buddy says Woof!