def Round(n,r):
    a=int(n/10)*10
    b=a+r
    if(b-n<n-a):
        return b
    else:
        return a


n=int(input("Enter a number : "))
r=int(input("Enter the round off term : "))
t=Round(n,r)
print(t)
