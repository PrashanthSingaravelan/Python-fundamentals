n=(input("Enter the list : "))
list1=n.split()
print(list1) # ['35', '49', '29', '199', '300']
list1.sort()  # List1 is not sorted as it accepts as individual string
print(list1) # ['199', '29', '300', '35', '49']

list2=[774,21,294,1002,399]
print(sorted(list2)) # List is sorted as it accepts as individual integer
# [21, 294, 399, 774, 1002]