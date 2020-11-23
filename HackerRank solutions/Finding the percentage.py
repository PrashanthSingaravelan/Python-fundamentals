n=int(input())
dict1={}
for i in range(n):
    str1,*line  = str(input()).split()
    list1  =  list(map(float,line))
    dict1[str1] = list1

str1 = str(input())
sum1 = sum(dict1[str1])/3)

# Upto 2 decimal places
print("{:.2f}".format(sum1))
