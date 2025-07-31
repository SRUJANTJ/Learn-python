# Dictionaries — Mapping
# A dictionary stores data in key-value pairs.

# ✅ No Import Needed

student = {"name": "Alice", "age": 22}

# 🔧 Built-in Method
student.get('name')         # Get value
student.keys()              # Get keys
student.values()            # Get values
student.items()             # Get key-value pairs
student.update({"age": 23}) # Update value
student.pop("age")          # Remove item


print(student)  



# 👤 User-Defined Example:


def print_dict(d):
    for k, v in d.items():
        print(f"{k}: {v}")

print_dict(student)




# Sets — Unique

# A set is an unordered, mutable collection with no duplicates.

# ✅ No Import Needed


numbers = {1, 2, 3, 4, 5}

# 🔧 Built-in Methods

numbers.add(6)             # Add element
numbers.remove(3)          # Remove element
numbers.union({7, 8})      # Union of sets
numbers.intersection({4, 5, 6})  # Common elements



# 👤 User-Defined Example:

def display_set(s):
    for item in s:
        print(item)

display_set(numbers)
