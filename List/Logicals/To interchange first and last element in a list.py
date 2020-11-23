# Pls do the program with help of functions
def interchange(list1):
    last_element =list1.pop(-1)
    first_element=list1.pop(0)
    list1.append(first_element)
    list1.insert(0,last_element)
    return list1

n=input("Enter the elements of list1:")
list1=n.split()

print("List1 before interchange: ",list1)

result=interchange(list1)
print("List after interchange: ",list1)

# 2) Using swap technique
list2=[49,27,90,12]
list2[0],list2[-1]=list2[-1],list2[0]
print(list2)
