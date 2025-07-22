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