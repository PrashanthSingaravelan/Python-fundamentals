dict1={"a":100,"b":900,"c":800,"d":300}
dict2={"c":200,"a":400,"b":300,"z":0}
dict3={}

for i,j in dict1.items():
    for p,q in dict2.items():
        if i==p:dict3[i]=j+q

from collections import Counter
print(dict3)
print("Counter(dict1) : ",Counter(dict1))
print("Counter(dict2) : ",Counter(dict2))

print(type(Counter))