dict1=dict(Apple="Iphone 10",Samsung="Note 11",One_plus="One plus 7 pro")
def tocheck(p):
    if p in dict1: # Checks dict1.keys()
        print("{} is in the dictionary".format(p))
    else:
        print("{} is not in the dictionary".format(p))

n=input("Pls enter your brand : ")
tocheck(n)
