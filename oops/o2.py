# Constructors
# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.
class MyClass:
    def __init__(self):
        self.value = None
        print("Constructor called!")

# Example usage
obj = MyClass()


# Types of Constructors in Python
# 1.Parameterized Constructor
# 2.Default Constructor


# Parameterized Constructor
# When the constructor accepts arguments along with self, it is known as parameterized constructor
print("\nParameterized Constructor")
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group
obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")
#Output Crab belongs to the Crustaceans group.


# Default Constructor
# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor

print("\nDefault Constructor")
class Details1:
  def __init__(self):
    self.animal = "Crab"
    print("animal Crab belongs to Crustaceans group")

obj2 = Details1()
print(obj2.animal)
#animal Crab belongs to Crustaceans group