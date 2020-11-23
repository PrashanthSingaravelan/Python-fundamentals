#To find the sum of the numbers in the list
# 1) First method
my_list=[23,67,0]
a=0;
for i in range(len(my_list)):
    a=a+my_list[i]
print(a)

# 2) Second method
my_list=[23,67,0]
sum=0
for i in my_list:
    sum=sum+i
print(sum)