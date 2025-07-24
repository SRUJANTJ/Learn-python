# Function with arguments
def greet(name):  # Define a function that takes one parameter, 'name'
    print(f'Hello, {name}!')  # Print a greeting using the provided name

# Call the function with different arguments

greet('Alice')  # Output: Hello, Alice!
greet('Bob')  # Output: Hello, Bob!









# Variable-Length Arguments


# Arbitrary positional arguments:
# Use *args to collect any number of positional arguments into a tuple.
# use when Don't know how many arguments will be passed to the function.


def my_function(*args):
    for arg in args:
       print(arg)
my_function(1, 2, 3, 4, 5)  # Output: 1 2 3 4 5






# Use **kwargs to collect any number of keyword arguments into a dictionary.
# use when Don't know how many keyword arguments will be passed to the function.

def my_function(**kwargs):
    for key, value in kwargs.items():
       print(key, value)
my_function(name="Alice", age=30, city="New York")
  # Output: name Alice age 30 city New York