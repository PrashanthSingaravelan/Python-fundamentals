class Circle:
    pi=3.14 # Class object attribute
    def __init__(self,radius=1):
        self.radius=radius
        self.area=Circle.pi*radius*radius
    def circumference(self):
        self.circum=self.radius*Circle.pi*2
        print("The circumference of the circle of radius {} is:{}".format(self.radius,self.circum))


obj1=Circle(30)
print("The area of the circle of radius {} is :{}".format(obj1.radius,obj1.area))
obj1.circumference()  # Goes to cicumference() and then prints there itself doesn't return anything
print(obj1.circumference()) # Goes to circumference () and then prints there itself 
                           # While returning there is nothing to print so it prints none

