
positive=0
negative=0
zero=0

n=int(input())

list1=list(map(int,input().split()))
for i in range(len(list1)):
    if list1[i]==0:zero+=1
    elif (list1[i]>0):positive+=1
    else:negative+=1

positive=positive/n
negative=negative/n
zero=zero/n

print(round(positive,n))
print(round(negative,n))
print(round(zero,n))
