
# Use of iterators in real world applications
# Iterators are commonly used in real-world applications to handle large datasets or streams of data efficiently.

# Data Processing in Files
# When dealing with large files, reading the entire file into memory may not be efficient. Iterators allow you to read the file line by line.


# Reading a large text file using an iterator
with open('large_file.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Process each line individually

        