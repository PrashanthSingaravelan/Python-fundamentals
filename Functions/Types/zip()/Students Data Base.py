# Database of a student
list1=[]
n=input("Enter the students name:")
list1=n.split()
list2=[]
m=input("Enter the students DOB:")
list2=m.split()
list3=[]
p=input("Enter the students Blood group:")
list3=p.split()

final=zip(list1,list2,list3)
final=set(final)
print("The complete Data Base is:",final)
