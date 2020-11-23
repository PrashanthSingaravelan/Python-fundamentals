# Factorial using recursion
print("Factorial using Recursion")
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)


m=int(input("Enter a number:"))
result=factorial(m)
print("The result is:",result)

#Factorial using for loop

print("Factorial using for loop")
p=int(input("Enter a number:"))
result=1
for i in range(1,p+1):
    result=result*i
print("The answer  is:",result)
