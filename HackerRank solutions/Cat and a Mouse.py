def catAndMouse():
 
 list1=list(map(int,input().strip().split()))[:3]  
 #if(1<=list1[0],list1[1],list1[2]<=100):
 if abs(list1[2]-list1[0])==abs(list1[2]-list1[1]):
     print("Mouse C")
 if abs(list1[2]-list1[0]) < abs(list1[2]-list1[1]):
     print("Cat A")
 if abs(list1[2]-list1[0]) > abs(list1[2]-list1[1]):
     print("Cat B")
 del list1[:3]
 
n=int(input())
if 1<=n<=100:
   for i in range(n): catAndMouse()