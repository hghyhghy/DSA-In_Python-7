

from collections import deque

# using lists as stacks 

# creating a stack list first 

stack=[10,20,30,40,50]

# appending the value in the stack 

stack.append(60)

print("After appending the stack becomes ")

print(stack)

# popping the value from the stack 

stack.pop()

print("After popping it becomes ")

print(stack)

# using list as deque

queue=deque(["subham","shreyoshi","shreya"])

print("The newly created queues is ")

print(queue)

# appending the new value on the queue

queue.append("sayanton")

queue.append("sayan")

print("The queue after appending becomes")

print(queue)

# popping the value from the queue 

queue.popleft()

print(queue)