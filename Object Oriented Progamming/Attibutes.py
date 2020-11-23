# Object 1) Attributes => Variables
#        2) Functions => Methods (call only in oops)

# Working with attributes

x =10           # x => Inbuilt class ( X is the object of inbuilt class)
print(type(x))  # <class 'int'>

class PC:
    def config(self):
        print("i5,Ram:16GB,HDD:1TB")
obj1=PC()          # obj1 => Userdefined class PC
print(type(obj1))  # <class '__main__.PC'>

# IN python all the variables belongs to inbuilt classes

obj1=PC()
obj2=PC()

# Procedure to call the class

# 1st Method (Appropriate Usage)
PC.config(obj1)   # i5,Ram:16GB,HDD:1TB
PC.config(obj2)   # i5,Ram:16GB,HDD:1TB

# 2nd Method (Actual Usage)
obj1.config() # At the back end congfig() is passing obj1 as a parametre
obj2.config()

a=5
a.bit_length
