# dir(), __dict__ and help() methods in python
# We must look into dir(), __dict__() and help() attribute/methods in python. They make it easy for us to understand how classes resolve various functions and executes code. In Python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help(). Let's take a look at each of them:

# The dir() method
# dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.

# It returns a list of attributes and methods associated with an object, including both public and private (dunder) methods. This information can be invaluable for understanding the capabilities of an object and exploring its potential uses.


# Where is dir() used?

# 1. Introspection and Exploration:
# Understanding built-in objects: When working with built-in data structures like lists, dictionaries, or strings, dir() can reveal the available methods and attributes.

# Exploring custom classes: It can help you discover the methods and properties of your own custom classes, including those inherited from parent classes.

# 2. Debugging:
# Identifying available attributes and methods: When debugging code, dir() can help you identify the properties and methods of an object that might be relevant to the issue.

# Inspecting object state: By examining the attributes of an object, you can gain insights into its current state and behavior.

# 3.Dynamic Code Generation
# Creating dynamic scripts: dir() can be used to dynamically generate code based on the attributes and methods of an object. For example, you could create a script that automatically iterates over the properties of an object and prints their values.

x = [1, 2, 3]
print(dir(x))