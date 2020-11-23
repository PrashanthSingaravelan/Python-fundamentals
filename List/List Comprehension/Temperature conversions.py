n=input("Enter the temperature in Celcius:")
mylist1=n.split()
mylist2=[]
# Float coversion not possible
mylist2=[((1.8*temp)+32) for temp in mylist1]
print("The temperature in Fahrenheit:")
print(mylist2)
