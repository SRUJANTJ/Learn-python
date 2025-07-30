#  Tuples — Immutable

# A tuple is an ordered, immutable collection.

# ✅ No Import Needed

coordinates = (10, 20)

# 🔧 Built-in Methods
coordinates.count(10)       # Count occurrences
coordinates.index(20)       # Get index


# 👤 User-Defined Example:

def display_tuple(tup):
    for val in tup:
        print(val)

display_tuple(coordinates)
