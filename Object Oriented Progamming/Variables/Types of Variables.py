# Instance Variables=> Variables whose values is assigned inside a 
# 1)Construtor or a 2)Method with self

# 1) Using Constructor

class Computer_Science:
    a="Prashanth"       # Class variables => Variables declared within the class

    def __init__(self,roll):
        self.roll=roll  # Instance variables


obj1=Computer_Science(89)
obj2=Computer_Science(78)

# Instance variable assigning
print(obj1.roll)
print(obj2.roll)

# Class variables accessing
# 1) Using objects
print("Class variables accessing through objects :", obj1.a)

# 2) Using class name
print("Class variables accessing through class name : ",Computer_Science.a)

##########################################

# 2) Using other methods

class Michell:
    def __init__(self,roll):
        self.roll=roll
    def Address_Storing(self,address):
        self.address=address
    def Address_Retrival(self):
        return self.address
obj1=Michell(67)
obj1.Address_Storing("Kodambakkam")
print("The Address used : ",obj1.Address_Retrival())

# 3) Empty class 

class Test:
    pass
