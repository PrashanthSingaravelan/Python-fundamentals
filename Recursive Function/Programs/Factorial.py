def fact(n):
    if n==1:     #  0!=1
       return 1
    else:
       return fact(n-1)*n



n=int(input("Enter a number:"))
a=fact(n)
print("The factorial of {} is :{}".format(n,a))