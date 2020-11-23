# Nested Recursion

def fun(n):
    if n>100:
        return n-10
    else:
        return fun(fun(n+11))

m=int(input("Enter a number:"))
a=fun(m)
print(a)