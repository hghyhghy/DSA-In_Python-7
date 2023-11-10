

# dictionarie with keys having multiple inputs 

# creating a dictionary 

d={}

# created an empty dict

x,y,z=10,20,30

d[x,y,z]=x+y-z

print(d)

# creating another empty dictionary 

test_dict={}

a,b,c=3,4,1

test_dict[a,b,c]=a+b-c

print("after operation the dictionary is")

print(test_dict)