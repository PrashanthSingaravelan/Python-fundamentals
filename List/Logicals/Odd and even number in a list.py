n=input("Enter the values:")
my_list1=n.split()
my_list1=list(map(int,my_list1))
my_list2=[]
my_list3=[]
for i in my_list1:
    if i%2==0:
        my_list2.append(i)
    else:
        my_list3.append(i)
print("The even numbers are:",*my_list2)
print("The odd numbers are:",*my_list3)

