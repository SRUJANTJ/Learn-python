# Static Methods

# static methods are methods defined within a class that do not operate on an instance of the class
# 
# In simple static method mean it not either belong to object or class
# It’s simply a method that resides within a class for organizational purposes but does not access or modify instance (self) or class (cls) attributes
# Static methods are ideal when you want a function to logically belong to a class but don’t need to access or modify any instance (self) or class-level (cls) attributes.
# 
# 1. Utility Functions Related to the Class:If a function performs operations relevant to a class but doesn’t operate on instance-specific data, it makes sense to define it as a static method within that class. For example, a class representing mathematical operations might include methods for basic arithmetic operations (like addition or subtraction) that don’t rely on the state of an instance.
# 
# 2. Alternative Constructors: Static methods can be used as alternative constructors to create an instance of a class in a specific way without using the standard __init__ constructor. This is often used in cases like parsing data to create an instance of a class.
# 
# 3. Grouping Utility Functions:Sometimes, static methods are used to keep utility functions organized within the context of a class, even if they could theoretically exist as standalone functions. This keeps the code modular and grouped under relevant class names.
# 
# 4. Avoiding Unnecessary Instantiation: Static methods allow you to call methods on a class without creating an instance. This is especially useful if the method doesn’t require any instance data. Static methods are essentially class-level utility functions, and using them appropriately reduces memory usage since no instance is created.
# 
# 5. Consistency and Code Organization:Static methods bring consistency and help keep your codebase organized by grouping related functionality within classes rather than as standalone functions. This is particularly useful in larger projects, where logically grouping code can reduce confusion and simplify maintenance.


# It start with keyword @staticmethod
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b
# Using static methods without creating an instance of MathOperations
print(MathOperations.add(5, 3))       # Output: 8
print(MathOperations.subtract(10, 4)) # Output: 6