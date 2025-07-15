# Creating a set
fruits = {'apple', 'banana', 'cherry'}

# Adding an element
fruits.add('orange')
print('After add:', fruits)  # {'apple', 'banana', 'cherry', 'orange'}

# Removing an element
fruits.remove('banana')
print('After remove:', fruits)  # {'apple', 'cherry', 'orange'}

# Union of sets
tropical = {'mango', 'pineapple'}
all_fruits = fruits.union(tropical)
print('Union:', all_fruits)  # {'apple', 'cherry', 'orange', 'mango', 'pineapple'}

# Intersection of sets
berries = {'cherry', 'blueberry'}
common = fruits.intersection(berries)
print('Intersection:', common)  # {'cherry'}