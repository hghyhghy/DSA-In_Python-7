

from collections import OrderedDict

# appending dictionary keys 

# creating a dictionary 


test_dict={'subham':1,'shreyoshi':2,'bipasha':3}

print("The original dictionary is ")

print(str(test_dict))

a=list(test_dict.keys())

b=list(test_dict.values())

a.extend(b)

temp=a

print("After appending the dictionary becomes ")

print(str(temp))


# sorting the keys in the dictionaries 

test_dict1={'subham':1,'nuveksha':2,'bipasha':3}

print("The original dictionary is")

print(str(test_dict1))

t1=list(test_dict1.keys())

t1.sort()

print(t1)


# by using order dict 


tes1={'subham':1,'nuveksha':2,'bipasha':3,'aman':20}

dict1=OrderedDict(sorted(tes1.items()))

print("After operation the output is ")

print(dict1)