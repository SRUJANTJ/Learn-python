# else if 
x = 10
if x > 10:
  print("x is greater than 10")
elif x == 10:
  print("x is equal to 10")  # This will execute
else:
  print("x is less than 10")




#   Logical Operators

a = 10
b = 20
if a > 5 and b > 15:
    print('Both conditions are true')  # Output: Both conditions are true
else:
    print('One or both conditions are false')



# 'or' returns True if at least one condition is true
a = 10
b = 5
if a > 15 or b < 10:
    print('At least one condition is true')  # Output: At least one condition is true
else:
    print('Both conditions are false')
    