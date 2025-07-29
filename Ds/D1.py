# List – Ordered
# 📌 Meaning:
# Mutable (changeable)

# Ordered

# Allows duplicates

# Create a list
fruits = ['apple', 'banana', 'cherry']

# 🔧 Built-in Methods:

fruits.append('orange')     # Add at end
fruits.insert(1, 'grape')   # Insert at index
fruits.remove('banana')     # Remove by value
fruits.pop()                # Remove last item
fruits.sort()               # Sort list
fruits.reverse()            # Reverse order
len(fruits)                 # Length of list

print(fruits)  # Output the list


# User Defined Methods:

def print_list(lst):
    for item in lst:
        print(item)

print_list(fruits)
