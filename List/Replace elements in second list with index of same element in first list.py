# Replace elements in second list with index of same element in first list
n=input("Enter the elements of list1:")
list1=n.split()

m=input("Enter the elements of list2:")
list2=m.split()

list3=[]

for i in list2:
    for j in list1:
        if i==j:
            list3.append(list1.index(j))

print("The reusltant list is :",list3)