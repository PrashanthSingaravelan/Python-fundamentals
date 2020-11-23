from collections import Counter 
str1 = "Today is Monday"
str1 = str1.replace(' ','')
list_max = []
x = Counter(str1)
x = list(x.items())

maxi = 0
for i,j in x:    
    temp = (i,j)
    for m in range(len(x)):
        if temp[1]>x[m][1]:
            maxi = temp
    list_max.append(maxi)
list_max.remove(0)

list_max = list(set(list_max))
for i,j in list_max:
    print("{} occured {} times".format(i,j))