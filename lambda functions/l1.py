# lambda functions are small, anonymous functions.
# defined using the lambda keyword.
# Unlike regular functions defined with the def keyword, lambda functions are typically used for short, throwaway functions that are not reused elsewhere in the code.

# lambda arguments: expression

# Key Characteristics
# 1: Anonymous: Lambda functions do not have a name.

# 2: Single Expression: They can only contain a single expression, which is evaluated and returned. They cannot contain statements or multiple expressions.

# 3: Used for Short Tasks: Commonly used for functions that are short and only needed temporarily, such as in functional programming constructs (e.g., map(), filter(), sorted()).

add = lambda x, y: x + y
result = add(2, 3)
print(result)
# result is 5

# Usage
# Lambda functions are often used in combination with functions like map(), filter(), and sorted(). Here’s an example with filter():


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # even_numbers will be [2, 4, 6]
print(even_numbers),

# When to Use
# 1: Short, Simple Functions: Use lambda functions for simple operations that can be defined in one line.

# 2: Higher-Order Functions: When passing a function as an argument, especially when the function is not needed elsewhere in the code.
