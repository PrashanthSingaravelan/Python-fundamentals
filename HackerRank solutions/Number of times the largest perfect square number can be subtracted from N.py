from math import sqrt

def Step(n,count):
    while(n>0):
      i=int(sqrt(n))
      n=n-(i*i)
      count=count+1
    print(count)


n=int(input("Enter a number : "))
count=0
Step(n,count)

