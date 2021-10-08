def fun1(a=10,b=20,c=30):
	return (a+b+c)

print(fun1())        # Default a,b,c values from the functions are taken
print(fun1(b=1))     # b is over-written
print(fun1(a=2,b=3)) # a and b are over-written