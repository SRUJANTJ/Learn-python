# seek(offset, whence=0)
with open('example1.txt', 'r') as file:
    file.seek(10)  # Move the cursor to the 10th byte in the file
    content = file.read(5)  # Read the next 5 bytes
    print(content)