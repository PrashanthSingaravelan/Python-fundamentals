class Computer:
    def __init__(self):
       print("HP Pavilion")

obj1=Computer()
# Constructor name Should be the same as that of the class name
# Each and every object has its own methods and data

class Computer:
     def __init__(self,cpu,ram):  # Similar to constructor in C++, Executed at the time of creating an object
         self.cpu=cpu
         self.ram=ram
     def config(self):
         print("Configuration is :",self.cpu,self.ram)

obj1=Computer("i5",8)
obj2=Computer("Ryzen",16)

obj1.config()
obj2.config()

