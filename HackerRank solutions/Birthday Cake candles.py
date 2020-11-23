n=int(input())
list1=list(map(int,input().split()))

min1=-32768
for i in range(len(list1)):
   if min1<list1[i]:
      min1=list1[i]
print(min1)

count=0
for i in range(len(list1)):
    if(min1==list1[i]):
      count+=1

print(count)

