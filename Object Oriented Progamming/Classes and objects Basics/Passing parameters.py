class Computer:
     def __init__(self,cpu,ram):
         self.cpu=cpu
         self.ram=ram
     def config(self):
         print("Configuration is :",self.cpu,self.ram)

obj1=Computer("i5",8)
obj2=Computer("Ryzen",16)

obj1.config()
obj2.config()

