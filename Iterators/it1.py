# How Iterators Work:
# When you use a for loop to go over a list or other collection, Python automatically creates an iterator and uses the next() method internally to get the next item until the collection is exhausted.

# Custom Iterator:
# You can also create custom iterators by defining a class with __iter__() and __next__() methods.

class MyNumbers:
    # Initialize the iterator and set the starting value to 1
    def __iter__(self):
        self.a = 1
        return self
    
    # Define what happens when calling next()
    def __next__(self):
        # Check if the current value is less than or equal to 5
        if self.a <= 5:
            x = self.a  # Store the current value
            self.a += 1  # Increment the value for the next call
            return x  # Return the current value
        else:
            # If the value exceeds 5, stop the iteration
            raise StopIteration

# Create an instance of MyNumbers
my_numbers = MyNumbers()
# Get an iterator from the MyNumbers instance
my_iter = iter(my_numbers)

# Loop through the iterator and print each value
for num in my_iter:
    print(num)

# Output: 1 2 3 4 5