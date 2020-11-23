# Fibonacci series

# Using recursion
def fib(m):
          if m<=1:
                 return m
          else:
               return fib(m-1)+fib(m-2)

n=int(input("Enter a number : "))
p=fib(n)
print("The fibonacci series of {} using recursion is: {}".format(n,p))

# Using loop

def fib1(c):
           t0=0 
           t1=1 
           sum=0
           if c<=1:
                   return c
           else:
                 for j in range(2,c+1):
                     sum=t0+t1
                     t0=t1
                     t1=sum
                 return sum

a=int(input("Enter a number: "))
b=fib1(a)
print("The fibonacci series of {} using loop is: {}".format(a,b))

# Using memoization


def fib3(x):
          if (x<=1):
            F[x]=x
            return x
          else:
            if(F[x-2]==-1):
                F[x-2]=fib(x-2)
            elif(F[x-1]==-1):
                F[x-1]==fib(x-1)
            F[x]=F[x-1] + F[x-2]
            return F[x-1] + F[x-2]

F=["-1","-1","-1","-1","-1","-1","-1","-1",]
a=fib3(4)
print(a)