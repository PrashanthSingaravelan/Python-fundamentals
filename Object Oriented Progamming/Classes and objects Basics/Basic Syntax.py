class Dog:
      species="Mammal"
      def __init__(self,param1,param2,param3):
          self.class_attribute1=param1
          self.class_attribute2=param2
          self.class_attribute3=param3

obj1=Dog(param1="Lab",param2="jimmy",param3="wild")
print(obj1.class_attribute1)
print(obj1.class_attribute2)
print(obj1.class_attribute3)