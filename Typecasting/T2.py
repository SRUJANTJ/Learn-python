# Explicit Import Example
from math import sqrt  # Only importing the sqrt function

number = 16
result = sqrt(number)  # Using the imported sqrt function
print(result)  # Output: 4.0














# Explicit Type Hinting Example
def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(3, 5)
print(result)  # Output: 8








# Explicit Casting to Set
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)  # Converts list to set, removing duplicates
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}


# Implicit Type Conversion Example
# Done by Python automatically
# when performing operations between different numeric types
num_int = 10
num_float = 5.5
result = num_int + num_float  # Python automatically converts num_int to float
print(result)  # Output: 15.5