

small=[10,20,30,40,50,.60]
 
print("The list before pop operaton ")

print(small)

print("The list after pop operation ")

small.pop(-1)

print(small)

# clear() to clear the elements of the list 

s=[10,20,30,40,50,.60]

print("The list  before clear operation")

print(s)

print("The list after clear operation ")

s.clear()

print(s)

# copy ( ) to copy elements from one list to another 

print("The list before copying ")

print(s)

print("The list after copying ")

s=small.copy()

small.clear()

print(s)
