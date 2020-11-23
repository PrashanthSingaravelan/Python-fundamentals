# input -->  Hello
# output --> elleH

str1 = input("Enter the string : ")
list1 = []

for i in range(len(str1)-1,-1,-1):
	list1.append(str1[i])

print("The string before reversing : ",str1)
print("The string after reversing  : {}".format(''.join(list1)))
