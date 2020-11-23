def sum(n):
    if n==0:
       return 0
    else:
       return sum(n-1)+n



n=int(input("Enter a number:"))
a=sum(n)
print("The sum of {} is :{}".format(n,a))