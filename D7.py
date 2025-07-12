# Assignment operators
# Assignment
a = 5

# Add and assign
a += 3  # a = a + 3
print("After Add and Assign:", a)
# Subtract and assign
a -= 2  # a = a - 2
print("After Subtract and Assign:", a)
# Multiply and assign
a *= 4  # a = a * 4
print("After Multiply and Assign:", a)
# Divide and assign
a /= 2  # a = a / 2
print("After Divide and Assign:", a)
# Modulus and assign
a %= 3  # a = a % 3
print("After Modulus and Assign:", a)
# Exponentiation and assign
a **= 2  # a = a ** 2
print("After Exponentiation and Assign:", a)





# Logical Operators

# Logical AND
a = True
b = False
print("Logical AND:", a and b)
# Logical OR
print("Logical OR:", a or b)
# Logical NOT
print("Logical NOT:", not a)



# Bitwise Operators
# Bitwise AND
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print("Bitwise AND:", a & b)  
# Bitwise OR
print("Bitwise OR:", a | b) 

# Bitwise XOR
print("Bitwise XOR:", a ^ b)

# Bitwise NOT
print("Bitwise NOT:", ~a)
# Bitwise Left Shift
print("Bitwise Left Shift:", a << 1)  # Shifts bits to the left
# Bitwise Right Shift
print("Bitwise Right Shift:", a >> 1)  # Shifts bits to the right




# Membership Operators

# Membership in a list
my_list = [1, 2, 3, 4, 5]
print("Membership in list (in):", 3 in my_list)
print("Membership in list (not in):", 6 not in my_list)

# Membership in a string
my_string = "Hello, world!"
print("Membership in string (in):", 'H' in my_string)
print("Membership in string (not in):", 'z' not in my_string)



# Identity Operators

ident = 5

# Identity is
print("Is ident 5:", ident is 5)