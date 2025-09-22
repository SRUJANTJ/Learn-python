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


# __str__ and __repr__
# The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.
print("\n __str__ and __repr__ example _\n")
class Person1:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person named {self.name}"

    def __repr__(self):
        return f"Person('{self.name}')"

p = Person1("Alice")
print(p)  # Output: Person named Alice
print(repr(p))  # Output: Person('Alice')



# __add__ method
# The __add__ method allows you to define custom behavior for the + operator for instances of your class. This can be useful if you want to add objects of your class or combine their properties in a specific way.

print("\n __add__ method example _\n")

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(5)
n2 = Number(10)
print(n1 + n2)  # Output: 15



# __len__ method
# The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.
print("\n __len__ method example _\n")

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

lst = MyList([1, 2, 3])
print(len(lst))  # Output: 3