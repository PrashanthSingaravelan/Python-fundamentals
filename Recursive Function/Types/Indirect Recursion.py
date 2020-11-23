# Indirect recursion
def funA(n):
    if n>0:
        print(n)
        funB(n-1)
    return 0
def funB(n):
    if n>0:
        print(n)
        funA(n//2)
    return 0

m=int(input("Enter a number:"))
a=funA(m)
print(a)












