
import operator

# counting the frequency in a list dictionary in python 


# creating a func

def offre(d):

    # creating an empty dict 

    temp={}

    for i in d:

        if i in temp:

            temp[i]+=1

        else:

            temp[i]=1

    
    # using another for loop 

    for key,values in temp.items():

        print("%d : %d " % (key,values))



# creating the list 

d=[1,1,2,3,4,5,5,6,6,3,3,1,1]

offre(d)

# approach 2 

# by using list count()  method 

def frequency(l):

    temp={}

    for i in l:

        temp[i]=l.count(i)

    
    # using another for loop 

    for key ,values in temp.items():

        print("%d : %d" % (key,values))


l=[1,1,2,3,4,5,5,6,6,3,3,1,1]

# calling the function 

frequency(l)

