# Inheritance
# Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). This enables code reuse and establishes a relationship between classes


class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):
        return "Meow"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Woof"

my_cat = Cat()
my_dog = Dog()
print(my_cat.speak())  # Output: Meow
print(my_dog.speak())  # Output: Woof