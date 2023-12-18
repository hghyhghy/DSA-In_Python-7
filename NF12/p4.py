# creating a string first 

s="learning python is a fun "

print(f"The length of the string {s} is ", len(s))

# changing to the upper case 

print(f"The uppercase of the string {s} is ",s.upper())

s1="HELO I AM PYTHON "

print(f"The lowercase  of the string {s1} is ",s1.lower())

s2="LEARNING pythON IS  FUn"

print(s2.swapcase())

# changing all first char of first word in uppercase 

print(s.capitalize())

# changing all the first char of all word in uppercase 

print(s.title())

a="leraning python is a fun *****"

print("Before stripping the string is ",a)

print(f"After stripping of {a} it becomnes ", a.strip('*'))

# demo of the replace 

a0="This python language is very new . This is very good "

print("Before replacing the string is ", a0)

print(f"After replacing of {a0} is ")

print(a0.replace('is','was'))

#islower  

a1="Python Language is very good " 

print(a1.islower())

a2="python language is very good " 

print(a2.islower())

#isupper 

print(a1.isupper())

a3="PYTHON PROGRAMMING"

print(a3.isupper())
