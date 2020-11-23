# 1) Traversing method
def unique(list2):
    unique_list=[]
    for i in list2:
        if i not in unique_list:
           unique_list.append(i)
    return unique_list
n=input("Enter the elements of the list : ")
list1=n.split()
list2=[]
list2=list(map(int,list1))

print("The unique elements are : ",*unique(list2))

# 2) Using set method => As set doesn't hold any duplicate values
def unique_set(list4):
    # Convert the list to a set so that it holds only unique values
    list5=set(list4)
    # Convert the set to list to get the desired output
    unique_list2=list(list5)
    return unique_list2

m=input("Enter the elements of the list : ")
list3=m.split()
list4=[]
list4=list(map(int,list3))

print("The unique elements are : ",*unique_set(list4))

#3) numpy function

import numpy as np
# function to get unique values
def unique(list6):
    x = np.array(list6)  # Convert the array elements into single dimensional array
    print(np.unique(x))  # Returns only unique values in a list

list6 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is : ",unique(list6))
