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






# Modifying Global Variables Inside a Function:
mx = 10  # Global variable

def my_function():
    global mx
    mx = 20  # Modify the global variable
    print("Modified ",mx)

my_function()
print("Modified ",mx) # Global 'x' has been modified by the function



# Without the global keyword
wx = 10  # Global variable

def my_function():
    x = 20  # Local variable, doesn't affect the global 'x'
    print("Withoutgloble",wx)

my_function()
print("Withoutgloble",wx)
 # Global 'x' is still 10