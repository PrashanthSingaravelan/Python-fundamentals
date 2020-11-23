# Using Recursive method:
def fibR(n):
    if n<=1:
        return n
    else:
        return fibR(n-1)+fibR(n-2)
n=int(input("Enter a number : "))
print("The fibonacci using Recursion : ",fibR(n))

# Using Iterative method
def fibL(m):
    a=0
    b=1
    sum=0
    for i in range(2,n+1):
        sum=a+b
        a,b=b,sum
    return sum
m=int(input("Enter a number : "))
print("The fibonacci using Loop : ",fibL(m))

