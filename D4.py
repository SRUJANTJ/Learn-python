# Storing a Dictionary
my_dict = {'name': 'Alice', 'age': 25, 'is_student': True}
print(my_dict) 
#Type Chek 
print(type(my_dict))
#Output {'name': 'Alice', 'age': 25, 'is_student': True} 


# Set Type

# Storing a Set
my_set = {1, 2, 3, 4, 5}
print(my_set)
#Type check
print(type(my_set))
#Output {1, 2, 3, 4, 5}

# Storing a Duplicate Set
dupclite_set = {1, 5,5,5}
print(dupclite_set)
#Output {1, 5} 






# Binary Type

# A bytes object representing the ASCII characters 'hello'
b = b'hello'
print(b)
#Type check
print(type(b))

# Creates a mutable bytearray from a bytes object
ba = bytearray(b'hello')
# Changes 'h' (104) to 'H' (72)
ba[0] = 72
print(ba)
# Output: bytearray(b'Hello')  














# complex type

# Storing a Complex Number
c = 3 + 4j
print(c)  # Output: (3+4j)
# Type check
print(type(c))  # Output: <class 'complex'>

# Using literal notation
z1 = 2 + 4j

# Using complex() constructor
z2 = complex(2, 4)  # 2 is real part, 4 is imaginary part

print(z1, z2)   # (2+4j) (2+4j)



# Accessing Real and Imaginary Parts
z = 5 + 2j
print(z.real)  # 5.0
print(z.imag)  # 2.0




# Built-in Functions for Complex Numbers

import cmath

z = 1 + 1j
print(abs(z))           # Magnitude -> 1.4142135623730951
print(cmath.phase(z))   # Phase angle (radians) -> 0.7853981633974483
print(cmath.polar(z))   # Polar form -> (1.414..., 0.785...)
print(cmath.rect(2, cmath.pi/4))  # Rectangular form -> (1.4142+1.4142j)
