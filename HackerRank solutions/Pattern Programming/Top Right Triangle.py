n=int(input("Enter the number : "))

for i in range(n+1): # Outer loop
    for j in range(i):
        print(" ",end="") # Loop for spaces
    for j in range(i,n+1):
        print("*",end="")
    print()