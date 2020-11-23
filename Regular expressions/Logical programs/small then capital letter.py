n=input("Enter your string:")

import re
a=re.findall("[a-z]",n)
b=re.findall("[A-Z]",n)

for i in range(len(a)):
    print(a[i],end="")
for j in range(len(b)):
    print(b[j],end="")