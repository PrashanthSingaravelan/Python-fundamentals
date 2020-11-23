
# 1) Local variables cannot be used in Global scope
def spam():
    eggs=90  # Local eggs=90 dies as soon as the function terminates
spam()
#print(eggs)

# 2) Global variables can be read from a local scope
def spam1():
    print(eggs)
eggs=49  # Global eggs=49 can be accessed by the local eggs
spam1()

# 3) Global statement inside a function
def spam2():
    global name
    name= "Prashanth"    # In name Singaravelan overwrites by Prashanth
name="Singaravelan"
spam2()
print(name)