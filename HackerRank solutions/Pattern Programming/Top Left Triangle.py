n=int(input("Enter the number : "))

for i in range(n+1):
    for j in range(i,n+1):
        print("*",end=" ")
    print()