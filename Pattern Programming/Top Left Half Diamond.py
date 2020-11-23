#Top Left Half Diamond 
n=int(input("Enter a number:"))
for i in range(1,n+1): #i for rows
   for j in range(i):  #j for columns
    print("#",end=" ")
   print()

#Another method
a=int(input("Enter a number:"))
x= '*'
for a in range(1,a+1):
 print(x * a)
