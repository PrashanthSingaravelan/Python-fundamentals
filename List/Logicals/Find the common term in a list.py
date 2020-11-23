a=input("Enter the list1 elements separated by space ") # To accept list1
list1  =a.split()
b=input("Enter the list2 elements separated by space ") # To accept list2
list2 =b.split()
for x in list1:
   for y in list2:
      if x==y:
         print("The common term is",y)
