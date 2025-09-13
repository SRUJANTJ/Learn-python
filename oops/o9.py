# Instance variables vs Class variables in Python
# Instance variables
# Instance variables are attributes that belong to each specific instance (object) of a class. Each object can have different values for these variables.

# Declaration: They are usually defined within the __init__ method using self, which associates them with the particular instance.

# Scope: Accessible only by the instance they belong to.
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable
# Creating instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
print(dog1.name)  # Output: Buddy
print(dog2.name)  # Output: Max





# Class Variables
# Definition: Class variables are attributes shared across all instances of a class. They are defined directly within the class, outside of any instance methods.
# 
# Declaration: Defined directly under the class definition, without using self.
# 
# Scope: Shared among all instances of the class; if modified through the class name, the change is reflected across all instances.


class Dogs:
    species = "Canis lupus familiaris"  # Class variable
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable
# Creating instances
dogs1 = Dogs("Buddy", 3)
dogs2 = Dogs("Max", 5)
print(dogs1.species)  # Output: Canis lupus familiaris
print(dogs2.species)  # Output: Canis lupus familiaris
# Modifying the class variable
Dogs.species = "Canis lupus"
print(dogs1.species)  # Output: Canis lupus
print(dogs2.species)  # Output: Canis lupus