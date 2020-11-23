#To find the greatest number in a list
#Using sort and then print the last one
my_list=[1,4,6,20,19]
my_list.sort() # After sorting,the largest element automatically comes to the last
print("The Largest element is:",my_list[-1])

#Using max function
my_list=[1,4,6,7,10]
print("The Largest element is:",max(my_list))

# 1) User input
list1=[]
n=int(input("Enter the number of elements:"))

for i in range(n):
    m=int(input("Enter the elements:"))
    list1.append(m)
print("The maximum is :",max(list1))

# 2) User input
n=input("Enter the list elements :")
list2=n.split()
print(max(list2))