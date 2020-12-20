
print("Enter the list elements")
list1 = list(map(int,input().split()))
a = ''.join(str(i) for i in list1) ## joining the list without spacing 
if '007' in a:
    print("007 is present in list-1")
else:
    print("007 is not present in list1")