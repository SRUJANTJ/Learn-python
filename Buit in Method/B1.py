class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to describe the dog
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Method to make the dog bark
    def bark(self):
        return "Woof!"

# Creating an instance
my_dog = Dog("Buddy", 4)

# Calling methods on the instance
print(my_dog.description())  # Buddy is 4 years old.
print(my_dog.bark())  # Woof!