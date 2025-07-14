my_string = ' Hello, World! '  # Create a string
lower_string = my_string.lower()  # Convert to lowercase
upper_string = my_string.upper()  # Convert to uppercase
stripped_string = my_string.strip()  # Remove whitespace
replaced_string = my_string.replace('World', 'Python')  # Replace 'World' with 'Python'
split_string = my_string.split(',')  # Split string by comma

print(lower_string)  # hello, world!
print(upper_string)  # HELLO, WORLD!
print(stripped_string)  # Hello, World!
print(replaced_string)  #  Hello, Python!
print(split_string)  # [' Hello', ' World! ']
