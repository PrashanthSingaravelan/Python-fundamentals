str1 = input()
list1 = list(str1)
list2 = []
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j]:
            list2.append((list1[j],j))
duplicate_str = [str(i) for i,j in list2]
print("The duplicate elements are : {}".format(' '.join(duplicate_str)))
for i,j in reversed(list2):
    del list1[j]
print("The string after removing duplicate elements are : {}".format(''.join(list1)))