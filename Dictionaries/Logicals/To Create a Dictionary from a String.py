# Method 1
string=input("Enter the string 1 : ")
dict1={}

for i in string:
 count=0
 for j in string:
  if i==j:
   count=count+1
  dict1[i]=count

print("Method1 : ",dict1)

# Method 2
string2=input("Enter the string 2 : ")
dict2={}
for i in string2:
    dict2[i]=dict2.get(i,0)+1
print("Method2 : ",dict2)
    