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