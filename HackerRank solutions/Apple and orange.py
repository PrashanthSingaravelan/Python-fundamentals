def countApplesandOranges():
  for i in range(len(list2)):
   for j in range(len(list4)):
     listsum1[j]=list2[i]+list4[j]
   break

  for i in range(1,len(list2)):
   for k in range(len(list5)):
     listsum2[k]=list2[i]+list5[k]
   break

  count1=0
  count2=0

  for i in range(len(listsum1)):
   if list1[0]<=listsum1[i]<=list1[1]:
    count1=count1+1

  for i in range(len(list1)):
   if list1[0]<=listsum2[i]<=list1[1]:
    count2=count2+1
    
  print(count1)
  print(count2)

# Input start

list1=list(map(int,input().strip().split()))[:2]  # Values of the house boundary
list2=list(map(int,input().strip().split()))[:2]  # Respective locations of the trees
list3=list(map(int,input().strip().split()))[:2]  # Number of apples and oranges

list4=list(map(int,input().strip().split()))[:3] # Distance covered by apples
list5=list(map(int,input().strip().split()))[:3] # Distance covered by oranges

# Input ends
listsum1=[0,0,0]
listsum2=[0,0,0]

cnt=0

for i in range(len(list1)):
 if ( (1<=list1[i] and list2[i] and list3[i]<=pow(10,5)) and (pow(-10,5)<=list1[i]<=pow(10,5)) ): 
  cnt=cnt+1
    
if (list2[0]< (list1[0] and list1[1])) and (list2[1]>(list1[0] and list1[1])):
 cnt=cnt+1
    
if(cnt==3):
   countApplesandOranges()




    


