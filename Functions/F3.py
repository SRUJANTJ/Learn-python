# Local Variables

def my_function():
    x = 10  # Local variable
    print(x)  # This will work

my_function()

# print(x)  # This will cause an error since 'x' is not defined outside the function



# Global Variables:
xg = 10  # Global variable

def my_function():
    print(xg)  # Accessing the global variable inside the function

my_function()
print(xg)  # This will work since 'x' is globally defined