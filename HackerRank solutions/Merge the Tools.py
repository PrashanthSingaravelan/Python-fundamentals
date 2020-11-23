from collections import OrderedDict 
str1 = str(input())
n    = int(input())

k=0
for i in range(1,len(str1)+1):
    if i%n==0:
        print("".join(OrderedDict.fromkeys(str1[k:i])))
        k=i