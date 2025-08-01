#  Stack — LIFO (Last In, First Out)



# Operations:
# Push → Add an item to the top of the stack

# Pop → Remove the top item from the stack

# Peek/Top → Look at the top item without removing

# isEmpty → Check if stack is empty

# Size → Count items in the stack


# ✅ Using collections.deque
from collections import deque

# Create empty stack
stack = deque()

# Push elements (add to top)
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushes:", stack)
# Pop element (remove from top)
top = stack.pop()
print("Popped:", top)
print("Stack now:", stack)

# Peek (check top element)
print("Top element:", stack[-1])

# Size
print("Stack size:", len(stack))



# 👤 User-Defined Example:

print("User-Defined Stack Implementation")
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):          # Add item
        self.items.append(item)

    def pop(self):                 # Remove top item
        if not self.is_empty():
            return self.items.pop()
        return "Stack is Empty"

    def peek(self):                # View top item
        if not self.is_empty():
            return self.items[-1]
        return "Stack is Empty"

    def is_empty(self):            # Check if empty
        return len(self.items) == 0

    def size(self):                # Size of stack
        return len(self.items)

# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top:", s.peek())     # 30
print("Popped:", s.pop())   # 30
print("Now Top:", s.peek()) # 20

