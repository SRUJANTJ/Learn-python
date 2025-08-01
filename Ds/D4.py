#  Stack — LIFO (Last In, First Out)

# ✅ Using collections.deque
from collections import deque

stack = deque()
stack.append('A')   # Push
stack.append('B')
stack.pop()         # Pop

# 🔧 Built-in Method

stack.append(stack)  # Push
stack.pop()         # Pop
len(stack)          # Size of stack
print(stack)         # Output the stack


# 👤 User-Defined Example:

def stack_operations():
    s = deque()
    s.append('X')
    s.append('Y')
    print(s.pop())

stack_operations()
