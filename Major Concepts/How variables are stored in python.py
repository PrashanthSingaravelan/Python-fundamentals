# Case 1:
x=10
y=10

print("Address of x : ",id(x))   # Address of x :  140736041034416
print("Address of y : ",id(y))   # Address of y :  140736041034416

# id() will return an objects memory address (object's identity)

# Case 2:
a=20
print("Address of a : ",id(a))  # Address of a :  140736041034736

b=20
print("Address of b : ",id(b))  # Address of b :  140736041034736

# Case 3:
p=-100000000000000058
q=-100000000000000058
print("Address of p : ",id(p))
print("Address of q : ",id(q))