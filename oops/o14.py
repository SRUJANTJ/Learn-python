# Method Overriding
# Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class (child class) is said to override the method in the base class ( parent class ). When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.


class Animal:
    def sound(self):
        return "Some sound"  # Parent class method that returns a generic sound

class Dog(Animal):
    def sound(self):
        return "Bark!"  # Overridden method in the Dog class to return 'Bark!'

class Cat(Animal):
    def sound(self):
        return "Meow!"  # Overridden method in the Cat class to return 'Meow!'

dog = Dog()  # Creating an instance of the Dog class
cat = Cat()  # Creating an instance of the Cat class

print(dog.sound())  # Output: Bark!  # Calling the overridden method for dog
print(cat.sound())  # Output: Meow!  # Calling the overridden method for cat









# Operator Overloading
# Operator Overloading in Python allows you to define custom behavior for operators (like +, -, *, etc.) when they are applied to objects of a class. This is done by defining special methods in the class, known as magic methods or dunder methods (because they start and end with double underscores, like __add__, __sub__, etc.).
print("\nOperator Overloading Example:\n")

class Number:
    def __init__(self, value):
        self.value = value

    # Overloading the + operator
    def __add__(self, other):
        return self.value + other.value

# Create instances of the Number class
num1 = Number(5)
num2 = Number(10)

# Using the overloaded + operator
result = num1 + num2  # Calls the __add__ method

print(result)  # Output: 15



# Some common magic methods for operator overloading:
# __add__(self, other): Overloads the + operator

# __sub__(self, other): Overloads the - operator

# __mul__(self, other): Overloads the * operator

# __eq__(self, other): Overloads the == operator

# __lt__(self, other): Overloads the < operator

# __gt__(self, other): Overloads the > operator

# __truediv__(self, other): Overloads the / operator