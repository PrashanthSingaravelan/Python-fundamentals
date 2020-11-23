def alphabetical(list1):
    for i in range(len(list1)-1,0,-1):
        for j in range(i):
            if list1[j]>list1[j+1]:
                list1[j+1],list1[j]=list1[j],list1[j+1]
    return list1

string1="helloeveryone"
list1=list(string1)
print("Before sort : ",*list1)
a=alphabetical(list1)
print("After sort  : ",*a)