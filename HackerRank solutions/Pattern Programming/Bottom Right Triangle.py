n=int(input("Enter the number : "))

k=2*n-2

for i in range(0,n):  # Number of lines
    for j in range(0,k):  # Spaces if n=5 8 spaces
        print(" ",end="")#                 6 spaces
    k=k-2
    for j in range(0,i+1): # To print the star 
        print("*",end=" ")
    print()