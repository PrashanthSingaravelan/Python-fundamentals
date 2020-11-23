# Using iteration
n=int(input("Enter a number loop : "))
list1=[]
while(n):
    m=n%2
    list1.append(m)
    n=int(n/2)

list1.reverse()
print(*list1)

# Using Recursive Function
def DecimaltoBinary(n):
    if n>1:
        DecimaltoBinary(int(n/2))    
    print(n%2,end=' ')    
    
list2=[]
m=int(input("Enter a number recursion : "))
print(DecimaltoBinary(m))