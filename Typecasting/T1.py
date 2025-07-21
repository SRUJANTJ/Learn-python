# Explicit Type Conversion Example
string_number = '123'
integer_number = int(string_number)  # Converts string to integer
print(integer_number)  # Output: 123

float_number = float('45.67')  # Converts string to float
print(float_number)  # Output: 45.67

# Other Examples
list_from_tuple = list((1, 2, 3))  # Converts tuple to list
print(list_from_tuple)  # Output: [1, 2, 3]

tuple_from_list = tuple([4, 5, 6])  # Converts list to tuple
print(tuple_from_list)  # Output: (4, 5, 6)