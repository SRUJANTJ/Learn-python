# Hybrid Inheritance
# Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of the derived class into a sub-derived class. 

# The syntax for implementing Hybrid Inheritance in Python is the same as for implementing Single Inheritance, Multiple Inheritance, or Hierarchical Inheritance.


# class BaseClass1:
  # attributes and methods
# class BaseClass2:
  # attributes and methods
# class DerivedClass(BaseClass1, BaseClass2):
  # attributes and methods

# Consider the example of a Student class that inherits from the Person class, which in turn inherits from the Human class. The Student class also has a Program class that it is associated with.


class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def show_details(self):
    print("Name:", self.name)
    print("Age:", self.age)
    
class Person(Human):
  def __init__(self, name, age, address):
    Human.__init__(self, name, age)
    self.address = address
    
  def show_details(self):
    Human.show_details(self)
    print("Address:", self.address)
    
class Program:
  def __init__(self, program_name, duration):
    self.program_name = program_name
    self.duration = duration
    
  def show_details(self):
    print("Program Name:", self.program_name)
    print("Duration:", self.duration)
    
class Student(Person):
  def __init__(self, name, age, address, program):
    Person.__init__(self, name, age, address)
    self.program = program
    
  def show_details(self):
    Person.show_details(self)
    self.program.show_details()

# To create a Student object
program = Program("Computer Science", 4)
student = Student("John Doe", 25, "123 Main St.", program)
student.show_details()

# Output:
# Name: John Doe
# Age: 25
# Address: 123 Main St.
# Program Name: Computer Science
# Duration: 4
# As we can see from the output, the Student object has access to all the attributes and methods of the Person and Human classes, as well as the Program class through association.

# In this way, hybrid inheritance allows for a flexible and powerful way to inherit attributes and behaviors from multiple classes in a hierarchy or chain.

# Hierarchical Inhe

# As we can see from the outputs, the Dog and Cat classes have inherited the attributes and methods of the Animal class, and have also added their own unique attributes and methods.

# In conclusion, hierarchical inheritance is a way of establishing relationships between classes in a hierarchical manner. It allows multiple subclasses to inherit from a single base class, which helps in code reuse and organization of code in a more structured manner.