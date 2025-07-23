# range()

# start (optional): The starting value of the sequence (inclusive). Default is 0

# stop: The ending value of the sequence (exclusive).

# step (optional): The difference between each number in the sequence. Default is 1.

# In range step mean skip the number passed in range.
# range(start, stop, step)

for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
for i in range(2, 10, 2):
    print(i)  # Output: 2, 4, 6, 8
for i in range(10, 0, -1):
    print(i)  # Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1







#  enumerate()


# Enumerate is a built-in function that adds a counter to an iterable and returns it as an enumerate object.

# enumerate(iterable, start=0)


fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

#Output 
# 0 apple
# 1 banana
# 2 cherry
# 1 apple
# 2 banana
# 3 cherry
