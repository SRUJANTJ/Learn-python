# Lists Method
my_list = [1, 2, 3]  # Create a list
print(my_list.append(4))  # Add 4 to the end
print(my_list)  # Show list after append

print(my_list.extend([5, 6]))  # Add multiple items
print(my_list)  # Show list after extend

print(my_list.insert(1, 'a'))  # Insert 'a' at index 1
print(my_list)  # Show list after insert

print(my_list.remove(2))  # Remove the first occurrence of 2
print(my_list)  # Show list after remove

item = my_list.pop()  # Remove and return the last item
print(item)  # Show popped item
print(my_list)  # Show list after pop

print(my_list.remove('a'))  # Remove 'a' before sorting to avoid TypeError
print(my_list)  # Show list after removing 'a'

print(my_list.sort())  # Sort the list in place
print(my_list)  # Show list after sort