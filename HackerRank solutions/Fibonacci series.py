n=int(input())
list1=[]
list1.append(0)
list1.append(1)
for i in range(2,n):
    list1.append(list1[i-1]+list1[i-2])    
print('Final : ',*list1)    