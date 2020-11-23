n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
    
for m in range(1,n):
    for p in range(1,n+1-m):
        print(p,end=" ")
    print("\n")