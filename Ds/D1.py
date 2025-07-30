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



# A shorter syntax to create lists using a loop.



squares = [x**2 for x in range(5)]
even = [x for x in range(10) if x % 2 == 0]



# | Symbol / Word   | Meaning                                                        |
# | --------------- | -------------------------------------------------------------- |
# | `squares`       | Variable name to store the final list.                         |
# | `=`             | Assignment operator (stores result in `squares`).              |
# | `[` `]`         | Denotes a **list comprehension** (creates a list).             |
# | `x`             | Loop variable (represents each number in the range).           |
# | `**`            | Exponentiation operator (`x**2` means x squared).              |
# | `x**2`          | Expression to calculate square of each `x`.                    |
# | `for`           | Start of the loop — iterates over the sequence.                |
# | `x in range(5)` | Generates values from `0` to `4` (range is from `0` to `n-1`). |
