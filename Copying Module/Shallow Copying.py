import copy

list1=["Prashanth",24,"Praveen",2]
list2=[]
list2=copy.copy(list1)

print("Before changing List1",list1)
print("Before changing List2",list2)

print("After changing List1",list1)

list2[2]="Super"

print("After changing List2",list1)

