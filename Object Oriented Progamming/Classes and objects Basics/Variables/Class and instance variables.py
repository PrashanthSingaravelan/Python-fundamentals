# Class/static and instance variables

class car:
    wheels=4
    def __init__(self):
        self.mileage=10
        self.company="Morris Garage"

obj1=car()
obj2=car()
car.wheels=6 # 
print("The mileage is {} and the company is {}".format(obj1.mileage,obj2.company))
print("The number of wheels:{}".format(obj1.wheels))