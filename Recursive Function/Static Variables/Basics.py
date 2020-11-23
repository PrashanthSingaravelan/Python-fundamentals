def fun(n):
    if n>0:
       return fun(n-1) + n
    return 0
a=fun(5)
print(a)


def fun1(m):
    staticm=0
    if m>0:
       return fun(m-1) + m
    return 0
b=fun1(5)
print(b)
