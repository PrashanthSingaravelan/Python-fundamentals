# * args --> non-keyword arguement [Cannot able to Provide a name to that variable]
############################## eg-1 ######################
def myfun1(*args):
    print("The arguements in *args are : ")
    for i in args:
        print(i)

myfun1('Hello',9,[24,44,55],{"key":"value"})

############################## eg-2 ######################
def myfun2(main_arguement,*args):
	print("The main arguement is : ",main_arguement)
	print("The arguements in *args are : ")
	for i in args:
		print(i)

myfun2('Hello',9,[24,44,55],{"key":"value"})

'''
**kwargs --> keyword arguement [Provide a name to a variable]
After passing the arguements, kwargs beehaves as a dictionary 
name of the variable(key) : value of that variable(value)
'''

############################## eg-3 ######################
def myfun3(**kwargs):
	print("The type of **kwargs : ",type(kwargs))
	for i in myfun3.items():
		print(i)

myfun3(name="Prashanth",age=18,dob="24th April 2001")

############################## eg-4 ######################
def myfun4(**kwargs):
	for key,value in myfun3.items():
		print(key,value)

myfun4(name="Prashanth",age=18,dob="24th April 2001")