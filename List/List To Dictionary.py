# 1) Lists with full of integers

# a) With eval()
test_string ='[1:456,2:903,3:289]' # It is a normal string
res = eval(test_string.replace("[", "{").replace("]", "}"))
print(res)       # {1: 456, 2: 903, 3: 289}
print(type(res)) # <class 'dict'>

# b) Without eval()
string1='[1:9003,2:3075,3:249]'
pos=string1.replace("[","{").replace("]","}") # pos takes as only string
print(pos)       # {1:9003,2:3075,3:249}
print(type(pos)) # <class 'str'>

# 2) List with strings
test_string = '[Nikhil:1, Akshat:2, Akash:3]'
