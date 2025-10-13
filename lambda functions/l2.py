# map(), filter(), sorted(), and reduce()

# 1. map()
# The map() function applies a given function to all items in an iterable (like a list) and returns a map object (which can be converted to a list).
# Usage: Use map() when you want to transform each element in a collection.


# Function to square a number

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]



# 2. filter()
# The filter() function constructs an iterator from elements of an iterable for which a function returns True.
# Usage: Use filter() when you want to filter out elements from a collection based on a condition.


# Function to check if a number is even

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))

print(even_numbers)  # Output: [2, 4]



# 3. sorted()
# The sorted() function returns a new sorted list from the elements of any iterable.
# Usage: Use sorted() when you need to sort a collection.



numbers = [5, 3, 1, 4, 2]
sorted_numbers = sorted(numbers)

print(sorted_numbers)  # Output: [1, 2, 3, 4, 5]

# Sorting in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)  # Output: [5, 4, 3, 2, 1]



# 4. reduce()
# The reduce() function from the functools module applies a rolling computation to sequential pairs of values in a list. It reduces the list to a single value.
# Usage: Use reduce() when you want to aggregate elements in a collection to a single result.


from functools import reduce

# Function to multiply two numbers
def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4]
product = reduce(multiply, numbers)

print(product)  # Output: 24 (1 * 2 * 3 * 4)