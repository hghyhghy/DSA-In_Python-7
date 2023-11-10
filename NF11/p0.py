

# sorted key and values in dictionaries 

# creating a dict

di={'is':[1,2,3],'gfg':[10,20,30],'best':[12,23,34]}

print("The original dictionary is ")

print(str(di))

rest=dict()

for key in sorted(di):

    rest[key]=sorted(di[key])


print("After operation the dictionary becomes ")

print(rest)

# handling missing keys in dictionary 

d={'a':1,'b':2}

if "q" in d:

    print(d['a'])

else:

    print("Key Not found")

# approach 3

# using get()

Country={'India':'0091','America':'1200','Bangladesh':'0089'}

print(Country.get('India','Not Found'))

print(Country.get('Japan','Country Not Found'))


