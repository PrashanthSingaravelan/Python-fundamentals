def Roundoff(n):
    a=int(n/10)*10
    b=a+5
    a=b+5
    print(n,a,b)
    if n-b>a-n: return a
    else: return b


n=int(input("Enter a number : "))
print("The Round off number is",Roundoff(n))