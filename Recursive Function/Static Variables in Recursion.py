def fun(m):
    if m==0:
        return 0  
    else:
        return fun(m-1) + m   #Addition will be done as 0+1+2+3+4+....m

n=int(input("Enter a number:"))
b=fun(n)
print(b)
