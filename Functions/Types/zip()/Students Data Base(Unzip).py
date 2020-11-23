# Unzipping the Data Base
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

# Zip the entities

final=zip(list1,list2,list3)
final=set(final)
print("The complete Data Base is:",final)

# Unzip the entities

ulist1,ulist2,ulist3=zip(*final)  # Or simply use their respective list name

print("The unzipped result is:")

print("The names of the student are:",ulist1)
print("The DOB of the students are:",ulist2)
print("The blood group of the students are:",ulist3)
