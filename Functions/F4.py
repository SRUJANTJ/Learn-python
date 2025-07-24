# Function with arguments
def greet(name):  # Define a function that takes one parameter, 'name'
    print(f'Hello, {name}!')  # Print a greeting using the provided name

# Call the function with different arguments

greet('Alice')  # Output: Hello, Alice!
greet('Bob')  # Output: Hello, Bob!









# Variable-Length Arguments


# Arbitrary positional arguments:
# Use *args to collect any number of positional arguments into a tuple.


def my_function(*args):
    for arg in args:
       print(arg)
my_function(1, 2, 3, 4, 5)  # Output: 1 2 3 4 5