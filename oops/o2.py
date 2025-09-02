# Constructors
# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.
class MyClass:
    def __init__(self):
        self.value = None
        print("Constructor called!")

# Example usage
obj = MyClass()


# Types of Constructors in Python
# 1.Parameterized Constructor
# 2.Default Constructor


# Parameterized Constructor
# When the constructor accepts arguments along with self, it is known as parameterized constructor
print("\nParameterized Constructor")
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group
obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")
#Output Crab belongs to the Crustaceans group.


# Default Constructor
# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor

print("\nDefault Constructor")
class Details1:
  def __init__(self):
    self.animal = "Crab"
    print("animal Crab belongs to Crustaceans group")

obj2 = Details1()
print(obj2.animal)
#animal Crab belongs to Crustaceans group


# Decorators

# A decorator is a callable object that takes another function as its argument and returns a new function. This new function is typically a modified version of the original function, with additional functionality added.

print("\nDecorators")


def my_decorator(func):
    # Define a decorator function called my_decorator that takes another function (func) as an argument.
    def wrapper():
        # This is the wrapper function inside the decorator that will run before and after the original function.
        print("Something is happening before the function is called.")
        # Print a message before executing the original function to indicate pre-function behavior.
        func()  
        # Call the original function passed into the decorator (say_hello in this case).
        print("Something is happening after the function is called.")
        # Print a message after executing the original function to indicate post-function behavior.
    return wrapper
    # Return the wrapper function which will replace the original function when it's decorated.

@my_decorator
# Apply the my_decorator to the say_hello function using the @ decorator syntax.
def say_hello():
    # Define a simple function say_hello that prints "Hello!".
    print("Hello!")
    # Print the message "Hello!" when the say_hello function is called.

# Calling the decorated function.
say_hello()
# Invoke the say_hello function, which is now wrapped by the my_decorator. This will print the before and after messages, followed by "Hello!".
