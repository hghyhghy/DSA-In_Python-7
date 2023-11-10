

# remove duplicate words from a given sentence 

from collections import Counter

def ofcount(s):

    s=s.split(" ")

    uniq=Counter(s)

    temp=" ".join(uniq.keys())

    print(temp)

s="Subham is there and shreyoshi is also there"

ofcount(s)


# approach 2 

l="Subham is there and shreyoshi is also there"

num=l.split(" ")

# creating an empty list 

k=[]

for i in num:

    if (l.count(i)>1 and (i not in k)):

        k.append(i)


print("".join(k))


