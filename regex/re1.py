# Regular Expressions (Regex)
# Regular expressions (regex) in Python are patterns used to match, search, and manipulate strings. Python provides the re module to work with regular expressions.


# Key Concepts:
# Pattern: A sequence of characters that defines the desired match.

# String: The text to be searched.

# Match: A successful finding of the pattern within the string.

# Basic Regex Functions in Python
# Regex functions to search and manipulate strings.

import re
result = re.search(r'cat', 'The cat is on the roof')
print(result)  # Output: <re.Match object; span=(4, 7), match='cat'>




print('\n regex re.match() example \n')

# re.match()
# # Checks if the beginning of the string matches the pattern.

result1 = re.match(r'cat', 'cat on the roof')
print(result1)  # Output: <re.Match object; span=(0, 3), match='cat'>




print('\n regex re.findall() example \n')

# re.findall()
# Finds all occurrences of a pattern in a string and returns them as a lis
result2 = re.findall(r'\d+', 'There are 12 cats, 4 dogs, and 7 birds')
print(result2)  # Output: ['12', '4', '7']





print('\n regex re.sub() example \n')
# re.sub()
# Replaces all occurrences of a pattern with a new string.


result3 = re.sub(r'cat', 'dog', 'The cat is cute')
print(result3)  # Output: 'The dog is cute'