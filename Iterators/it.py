# terator is an object that allows you to traverse/accessing each element through all the elements in a collection (like a list or a tuple) one at a time.
# Iterators is similar to for loop but make easy to iterate/repetly task

# Key Concepts:
# 1: Iterable: Any object in Python that can return an iterator. Examples include lists, tuples, and strings. These objects implement the __iter__() method.

# 2: Iterator: An object that represents a stream of data. It implements two methods:

# __iter__() returns the iterator object itself.

# __next__() returns the next element in the sequence and raises a StopIteration exception when there are no more elements.



# A list is an iterable
my_list = [1, 2, 3]

# Getting an iterator from the list
my_iterator = iter(my_list)

# Using the iterator to go through the list
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3

# If you call next() again, it will raise StopIteration because there are no more elements.