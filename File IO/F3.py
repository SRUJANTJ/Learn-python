# seek(offset, whence=0)
with open('example1.txt', 'r') as file:
    file.seek(10)  # Move the cursor to the 10th byte in the file
    content = file.read(5)  # Read the next 5 bytes
    print(content)



# tell()

# Purpose: The tell() method returns the current position of the cursor in the file stream.


with open('example1.txt', 'r') as file:
    position = file.tell()  # Get the current position (should be 0 at the start)
    print("Current Position:", position)
    file.read(10)  # Read the first 10 bytes
    position = file.tell()  # Get the new position after reading    print("New Position:", position)



    
# truncate()
# The truncate() method in Python is used to resize a file to a specific length.
# in simple remove the characters after the specified length.

with open('example1.txt', 'r+') as file:
    file.write("Hello, World!")
    file.truncate(5)  # Keeps only the first 5 characters, cutting it to "Hello"








    # flush
# Purpose:The flush() method is used to clear the internal buffer of a file stream, writing any buffered data to the underlying file. This is particularly important when you're writing to a file and want to ensure that all data is physically written to the file before closing it or performing other operations.

# Usage:flush() when you need to make sure that all data written to the file is saved, especially when dealing with large data writes or when the program may terminate unexpectedly.

with open('example.txt', 'w') as file:
    file.write('Hello, World!')
    file.flush()  # Ensure the data is written to the file
    print("Data flushed to file.")