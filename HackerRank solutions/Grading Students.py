def grad(a,n,b):
    if n<38: return n
    elif b-n<3: return b
    else: return n

def Roundoff(n):
    a=int(n/10)*10
    b=a+5
    if a<n<b:
        return grad(a,n,b)
    else:
        return grad(b,n,a+10)
    
def separate(list1):
    for i in range(len(list1)):
        list1[i]=Roundoff(list1[i])
    return list1
   
u=int(input())
list1=list(map(int,input().split()))
print(*separate(list1))
