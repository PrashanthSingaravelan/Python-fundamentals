#Class method

class Car:
      wheels=4
      def __init__(self,make,speed):
         self.make=make
         self.speed=speed
         self.year=2001
      @classmethod
      def info(cls):
          return cls.wheels

obj1=Car("Ford",89)
print("The number of wheels is :{}".format(Car.info()))






