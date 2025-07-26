# Writing to a File
# You can write to a file using the .write() or .writelines() methods.
# Writing to a file
with open('example1.txt', 'w') as file:
    file.write("Hello, Worldd!")  # Writes a single line to the file





# Appending to a File
# To add content to an existing file without overwriting it, use the append mode 'a'.    



# Appending to a file
with open('example.txt', 'a') as file:
    file.write("Appending this line.")  # Adds a line to the end of the file




# Reading and Writing in Binary Mode
# If you're dealing with binary files (like images or audio), open the file in binary mode.


# Writing binary data
with open('example.bin', 'wb') as file:
    file.write(b'\x00\xFF\x00\xFF')  # Writes binary data

# Reading binary data
with open('example.bin', 'rb') as file:
    content = file.read()  # Reads the binary data
    print(content)