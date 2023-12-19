
# creating a set

s={22,33,4,55,6,71}

print("The newly created set is ")

print(s)

s1={11,21,33,43}

print("The second set is ")

print(s1)

# isdisjoint 

print(f"Are two sets {s} and {s1} isdisjoint to each other ")

print(s.isdisjoint(s1))

# issubset 

print(f"Are two sets {s} and {s1} issubset to each other ")

print(s.issubset(s1))

# issuperset

print(f"Are two sets {s} and {s1} issuperset to each other ")

print(s.issuperset(s1))

# frozensets are immutable 

# creating a frozenset 

a=frozenset({22,34,5,4})

b=frozenset({1,4,2,3,5})

print("The two frozensets are ")

print(a,b)

# intersection of two frozensets

print(f"The intersection of two frozensets {a} and {b} is ")

print(a.intersection(b))