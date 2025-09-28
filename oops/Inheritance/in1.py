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
    

