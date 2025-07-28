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


with open('example1.txt', 'r+') as file:
    file.write("Hello, World!")
    file.truncate(5)  # Keeps only the first 5 characters, cutting it to "Hello"