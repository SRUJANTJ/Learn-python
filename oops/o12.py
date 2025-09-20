# Super keyword in Python
# The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

# When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.

# In simple super() keyword used to inherit the properties and behavior of other class to new class.


class ParentClass:
    def parent_method(self):
        print("This is the parent method.")
class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()
child_object = ChildClass()
child_object.child_method()

#Output 
#This is the child method.
#This is the parent method.



# Magic/Dunder Methods
# Magic methods, also called dunder (short for “double underscore”) methods, in Python are special methods with names that start and end with double underscores (e.g., __init__, __str__, etc.). They enable Python classes to have custom behaviors when using built-in functions and operators.

# __init__ method
# The init method is a special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object’s initial state, and it is where you would typically define any instance variables that you need. Also called "constructor", we have discussed this method already


class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.name)  # Output: Alice