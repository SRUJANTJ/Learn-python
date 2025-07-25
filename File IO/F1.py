# Opening a File


# File method
# 'r' - Read (default mode)
# 'w' - Write (overwrites the file if it exists)
# 'a' - Append (adds to the end of the file)
# 'b' - Binary mode
# 't' - Text mode (default)


# Reading a file
with open('example.txt', 'r') as file:
    # Read the entire file
    content = file.read()  
    print('Entire File Content:\n', content)
    
    # Reset the file cursor to the beginning
    file.seek(0)
    
    # Read the first line
    first_line = file.readline()
    print('First Line:', first_line.strip())
    
    # Reset the file cursor again
    file.seek(0)
    
    # Read all lines into a list
    all_lines = file.readlines()
    print('All Lines:', all_lines)
    
    # Iterating over each line
    print('Iterating over lines:')
    for line in all_lines:
        print(line.strip())