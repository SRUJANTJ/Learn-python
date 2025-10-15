# Step 1: Create an Iterable
# An iterable is something you can loop over, like a list, string, or tuple.

# Example iterable: a list
my_list = [10, 20, 30]

# Step 2: Get an Iterator
# You can turn an iterable into an iterator using the iter() function.

# Turn the list into an iterator
my_iterator = iter(my_list)

# Step 3: Use next() to Get Items
# The next() function lets you access each item one by one from the iterator.


# Get the first item
print(next(my_iterator))  # Output: 10

# Get the second item
print(next(my_iterator))  # Output: 20

# Get the third item
print(next(my_iterator))  # Output: 30


# Step 4: Handle the End of the Iterator
# When there are no more items to get, next() raises a StopIteration exception. You can handle this using a loop or try/except block.


my_iterator = iter(my_list)

# Use a loop to automatically stop at the end
for item in my_iterator:
    print(item)

#10
#20
#30