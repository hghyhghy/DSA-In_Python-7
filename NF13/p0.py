

#istitle()

# returns is string is properly titlecased and falsed otherwise 

s="python programming is very easy"

print(f"If the string {s} is titlecased ",s.istitle())

s0="Python Programming Is Very Easy"

print(f"If the string {s0} is titlecased ",s0.istitle())

# join()

# returns concatenated string 

a="-"

seq=("Python","Programming")

print("The concatenated version of the string is ", a.join(seq))

# joining by using *


b="*"

s1=("Python","programming")

print("The concatenated version of the string is ", b.join(s1))

# split()

# splitting those strings 

a1="I Am Subham Sarkar"

print(f"The splitted string of {a1} is>>", a1.split(' '))

