#  list1=input().split()
#  list1=list(map(int,list1))
# Instead of doing it in a double line, it could be achieved in single line itself
list1=list(map(int,input().split())) # Alice mark
list2=list(map(int,input().split())) # Bob mark

alice=[]
bob=[]
counter1=0
counter2=0

for i in range(len(list1)):
    if(list1[i]!=list2[i]):
       if(list1[i]<list2[i]):
          counter2=counter2+1
       else:
          counter1=counter1+1

alice.append(counter1)
bob.append(counter2)

print(*alice,*bob)

        