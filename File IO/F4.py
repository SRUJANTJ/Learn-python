# Closing Files
# When you open a file using with, it automatically closes the file for you after the block of code is executed. If you don’t use with, you should explicitly close the file with file.close().


# Manually closing a file
file = open('example.txt', 'r')
# Perform file operations
content = file.read()
file.close()  # Always close the file

print(content)






# Error Handling

try:
    with open('examplse.txt', 'r') as file:
        content = file.read()
        print(f"Exception: {content}")
except FileNotFoundError:
    print("File not found. Please check the file path.")