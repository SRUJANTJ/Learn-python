# Queue — FIFO (First In, First Out)

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

