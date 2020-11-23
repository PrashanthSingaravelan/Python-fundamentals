list1=[1,2,3,4,5]


def Sum(list1):
    sum1=0
    for i in range(len(list1)):
        sum1=sum1+list1[i]
    print("Sum : ",sum1)
    return sum1


for i in range(len(list1)):
    for j in range(0,1):
        poped_element=list1.pop(i)
        
        a=Sum(list1)
        list2.append(a)
        list1.append(poped_element)
        list1.sort()
        
min1=-32768
max1=32768
for i in range(len(list2)):
    if(min1<list2[i]):
       min1=list2[i]
    if(max1>list2[i]):
       max1=list2[i]

print(min1," ",max1)
        
        

