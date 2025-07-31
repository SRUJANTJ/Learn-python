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
