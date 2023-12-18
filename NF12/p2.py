#Random number  function

import random

# creating a string first 

s="abcda"

print("choice of (abcda) is ", random.choice(s))

# creating  a list first 

l=[10,3,2,4,67]

print("shuffle of the list is:", random.shuffle(l))

print("Random seed of the number 20 is:", random.seed(20))

print("A random number is:", random.random())

print("Uniform between (2,3) is:", random.uniform(2,3))