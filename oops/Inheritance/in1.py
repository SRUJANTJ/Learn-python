# Single Inheritance in Python
# Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.
# Syntax:
# class ChildClass(ParentClass):

class ParentClass:
    def parent_method(self):
        return 'This is the parent method.'

class ChildClass(ParentClass):
    def child_method(self):
        return 'This is the child method.'

# Create an instance of ChildClass
child = ChildClass()

# Access methods from both parent and child
print(child.parent_method())  # Output: This is the parent method.
print(child.child_method())   # Output: This is the child method.
    








# Multiple Inheritance
# Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.

# syntax

# class ChildClass(ParentClass1, ParentClass2, ParentClass3):


# In this example, the ChildClass inherits attributes and methods from all three parent classes: ParentClass1, ParentClass2, and ParentClass3.
# It's important to note that, in case of multiple inheritance, Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes. The MRO determines the order in which parent classes are searched for attributes and methods.


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Sound made by the animal")

class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

class Dog(Mammal):
    def __init__(self, name, breed, fur_color):
        super().__init__(name, "Dog", fur_color)
        self.breed = breed

    def make_sound(self):
        print("Bark!")

if __name__ == "__main__":
    d = Dog("Buddy", "Golden Retriever", "Golden")
    print(f"Name: {d.name}, Species: {d.species}, Breed: {d.breed}, Fur Color: {d.fur_color}")
    d.make_sound()

Animal.make_sound(Animal("Generic Animal", "Unknown"))  


