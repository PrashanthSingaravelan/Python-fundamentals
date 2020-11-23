import math
sum1=0
n=int(input())
list1=[]
if(1<=n<=10):
   for i in range(n):
       a=int(input())
       if(0<=a<=pow(10,a)):
          list1.append(a)

list1=list(map(int,list1))
for j in range(n):
    sum1=sum1+list1[j]

print(sum1)
   
      