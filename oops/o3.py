# Getters and Setters
# Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator\
# Getters are methods designed for retrieving the value of an attribute in a class.

print("Getters")


class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    

# n this example, the MyClass class has a single property, _value, which is initialized in the init method. The value method is defined as a getter using the @property decorator, and is used to return the value of the _value property.

# To use the getter, we can create an instance of the MyClass class, and then access the value property as if it were an attribute:

obj = MyClass(10)
print(obj.value)


#Setters
print("\nSetters")
# Setters are methods specifically designed to set (or update) the value of an attribute, often including validation or additional logic to ensure the attribute is updated in a controlled manner. For that we need setter method which can be added by decorating method with @property_name.setter

class MyClass1:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        self._value = new_value

        # We can use setter method like this:

obj1 = MyClass1(10)
obj2= MyClass1(20)
print(obj1.value)  # Output: 10



# getters and setters are used when you want to control access to an attribute (variable) of a class.