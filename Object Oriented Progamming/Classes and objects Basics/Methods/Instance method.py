# Accessor and mutator method in Instance method

class Car:
      wheels=4
      def __init__(self,make,speed):
          self.make=make
          self.speed=speed
          self.year=2001
#Accessor method 
      def get(self):
         return self.make
#Mutator method
      def sets(self,other):
          self.speed = other
          return self.speed

obj1=Car("Ford",89)
obj2=Car("Bentley",92)
print(obj1.get())
print(obj2.get())

print(obj1.sets(98))








