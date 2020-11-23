list1=[78,23,91,20,19,30]
list1.sort()
print("The list after sorting : ",*list1)
list1.reverse()
print("The list after reversing : ")
for i in list1:
    print(i,end=" ")