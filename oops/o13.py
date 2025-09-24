# __getitem__ and __setitem__
# The __getitem__ method is called when you access an element of an object using the indexing syntax ([]). It allows you to retrieve the value associated with a given index or key.

# The __setitem__ method is called when you assign a value to an element of an object using the indexing syntax ([]). It allows you to modify or set the value at a specific index or key.


class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

lst = MyList([1, 2, 3])
print(lst[1])  # Output: 2
lst[1] = 20
print(lst[1])  # Output: 20

# __call__ method
# The __call__ method is useful for making objects behave like functions, enabling more flexible and dynamic behavior. It allows objects to execute code when "called," which can be useful in many scenarios like callbacks, decorators, or simplifying code structure.
print("\n __call_ method example _\n")

class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return f"Hello, {self.name}!"

greet = Greeter("Alice")
print(greet())  # Output: Hello, Alice!





