dict1={"Prashanth":"24th April","Sairam":"18th June","Mothish":"23rd March"}
while True:
    name=input(("Enter your friends name : "))
    if name in dict1:
        print("{} birthday is on {}".format(name,dict1[name]))
    else:
        print("Birthday info is not available for the name : ",name)
        bday = input("When is his birthday ? ")
        dict1[name]=bday
        print("Birthday Database is successfully updated")

