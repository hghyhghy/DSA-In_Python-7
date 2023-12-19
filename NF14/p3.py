

# some built in set methods 

# creating a set first 

s1={2,4,3,1,70,99}
 
print("The newly created set is ")

print(s1)

# adding new element to the set 

print("After adding new element to the set it becomes ")

s1.add(100)

print(s1)


# removing the object from the set 

print("After removing the set becomes ")

s1.remove(99)

print(s1)

# set union operation in the python 

s2={23,34,4,56,66,7}

print(f"The union of two sets {s1} and {s2} are ")

print(s1.union(s2))

# updating one set by another 

print("After updationg the value of set2 becomes ")

s2.update(s1)

print(s2)

