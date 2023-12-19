
# creating a set 

s={22,33,4,55,6,71}

print("The newly created set is ")

print(s)

# creating another set 

s1={11,21,33,43}

print("The second set is ")

print(s1)

# intersection of two sets

print(f"The intersection of two sets {s} and {s1} is")

set3=s.intersection(s1)

print(set3)

# difference between two sets

print(f"The difference between two sets {s} and {s1} is ")

a=s.difference(s1)

print(a)

# symmetric difference of two sets 

print(f"The symmetric difference of two sets {s} and {s1} is ")

b=s.symmetric_difference(s1)

print(b)

