n=int(input("Enter the size of a sqaure : "))
p=1
for i in range(1,n+1):
    for j in range(i):
        print(p,end=" ")
        p+=1
    print() # This is also normal print("\n")
    