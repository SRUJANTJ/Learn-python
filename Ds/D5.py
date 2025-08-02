# Queue — FIFO (First In, First Out)

# A Queue is a FIFO (First In, First Out) data structure.

# First element added → First element removed

# Think of it like a line at a ticket counter:

# The person who comes first gets served first.

# 🛠 Queue Operations
# We mainly have two operations:

# | Operation   | Meaning                                           | Example                                    |
# | ----------- | ------------------------------------------------- | ------------------------------------------ |
# | **Enqueue** | Add an element to the **end** of the queue        | People joining the line                    |
# | **Dequeue** | Remove an element from the **front** of the queue | First person leaves after getting a ticket |

print("Queue Implementation using import deque")
from collections import deque

queue = deque()
queue.append('A')   # Enqueue
queue.append('B')
queue.popleft()     # Dequeue

# 🔧 Built-in Methods:

queue.append('C')        # Enqueue
queue.popleft()          # Dequeue
len(queue)               # Size of queue
print("Queue after operations:", queue)

# User-Defined Queue Implementation
print("User-Defined Queue Implementation")
def queue_operations():
    q = deque()
    q.append('1')
    q.append('2')
    print(q.popleft())

queue_operations()





print("Stack Implementation without Importing deque")

# Without Importing deque

class SimpleQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    q = SimpleQueue()
    q.enqueue('X')
    q.enqueue('Y')
    print("Dequeued:", q.dequeue())
    print("Front element:", q.peek())
    print("Is empty?", q.is_empty())
    print("Size:", q.size())
