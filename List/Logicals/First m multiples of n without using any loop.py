# range(start,stop,step)
def mutiple(m,n):
    a=range(n , (m*n)+1 , n)
    print(*a)


m=int(input("Enter the value of m : "))
n=int(input("Enter the value of n : "))
mutiple(m,n)