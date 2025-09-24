# Method Overriding
# Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class (child class) is said to override the method in the base class ( parent class ). When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.


class Animal:
    def sound(self):
        return "Some sound"  # Parent class method that returns a generic sound

class Dog(Animal):
    def sound(self):
        return "Bark!"  # Overridden method in the Dog class to return 'Bark!'

class Cat(Animal):
    def sound(self):
        return "Meow!"  # Overridden method in the Cat class to return 'Meow!'

dog = Dog()  # Creating an instance of the Dog class
cat = Cat()  # Creating an instance of the Cat class

print(dog.sound())  # Output: Bark!  # Calling the overridden method for dog
print(cat.sound())  # Output: Meow!  # Calling the overridden method for cat