from heapq import nlargest
from operator import itemgetter
Things={"item1":45 , "item2":90 , "item3":55 , "item4":78 , "item5": 64}

# Without sorting                    #item1 45
for things,values in Things.items(): #item2 90
    print(things,values)             #item3 55
                                     #item4 78
                                     #item5 64

# dict.items() . nlargest (n, Things to find out , Number of things to find out)

#                                        n   => Number of individual dictionary pairs
#                      Things to find out    => eg:Things.items()
# NUmber of things to findout at every stage => eg:itemgetter(1)

print("The top three items are ")
for p,q in (nlargest (3,Things.items(),itemgetter(1)) ):
    print(p,q)
    
