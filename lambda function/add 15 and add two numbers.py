n=int(input("Enter 1st number : "))

output1 = lambda x:15+n
print("{} + 15 is {} : ".format(n,output1(10)))

a=int(input("Enter 2nd number : "))
b=int(input("Enter 3rd number : "))

output2 = lambda a,b:a+b
print("{} + {} is : {} ".format(a,b,output2(a,b)))



