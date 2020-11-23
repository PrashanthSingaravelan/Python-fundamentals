position=3 # Global variable
def linear_search(list1,m):
    for i in range(len(list1)):
        if list1[i]==m:
            globals()['position']=i # Inorder to access it locally
            return True

list1=[859,39,90,19]
m=90

if linear_search(list1,m):
    print("The element {} is found at the position {} in the list ".format(m,position+1))
else:
    print("The element {} is not found in the list".format(m))
