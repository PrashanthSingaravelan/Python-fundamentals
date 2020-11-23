x=input().lower()
y=[x]
for i in range(0,len(x)):
    x = x[1:]+x[0]
    y = y+[x]
print(len(set(y)))