

# keys associated with values in dictionaries 

from collections import defaultdict

# creating the dict

d={'geeks':[1,2,3],'is':[1,4],'best':[2,3,4]}

print("The original dictionary  is ")

print(str(d))

temp=defaultdict(list)


for key,value in d.items():

    for ele in value:

        temp[ele].append(key)


print("The key associated with the values is ")

print(str(temp))

# alternative approach 

d1={'geeks':[1,2,3],'is':[1,4],'best':[2,3,4]}

# empty dict 

res={}

for key,value in d1.items():

    for ele in value:

        if ele in res:

            res[ele].append(key)

        else:

            res[ele]=key


print("After operation the dictionary is ")

print(str(res))
 
