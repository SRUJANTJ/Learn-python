person = {"name": "Alice", "age": 25, "city": "New York"}
# Accessing a value with get
print("Name:", person.get("name"))  # Alice
# Adding a new key-value pair
person["email"] = "alice@example.com"
print("After adding email:", person)
# Removing a key-value pair with pop
person.pop("age")
print("After pop age:", person)
# Getting all keys
print("Keys:", person.keys())  # dict_keys(['name', 'city', 'email'])
# Getting all values
print("Values:", person.values())  # dict_values(['Alice', 'New York', 'alice@example.com'])
# Updating with another dictionary
person.update({"phone": "123-456-7890"})
print("After update:", person)