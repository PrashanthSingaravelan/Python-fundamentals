#Top Right half diamond
n=int(input("Enter the number of rows:"))
k=2*n-2
for i in range(1,n+1):    # Row incrementing
   for j in range(0,k):   # Space incrementing
     print(end=" ")
   k=k-2
   for l in range(1,i+1): # Star printing 
      print("#",end=" ")
   
   print("\n")

    
