n=int(input("Enter the number of lines : "))
p=1
for i in range(1,n+1):    ## for i in range(n+1) => If i=0, then the i loop doesn't enter once.    
    for j in range(i):
        print(p,end=" ")
        p=p*2
    p=1
    print()