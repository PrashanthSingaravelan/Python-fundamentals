class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):  # Should return a 
        return "The elements inside the object"

  ### Inheritance ###
class Student(Person):   # Student --> child  and Person --> parent 
    def __init__(self,name,age,student_college,student_roll,student_group):
        super(Student,self).__init__(name,age)  # Connecting the parent class
        self.college = student_college
        self.roll = student_roll
        self.group = student_group

     def age(self):
     	self.age = age

    def __str__(self):
        print(self.college,self.roll,self.group)

obj1 = Person("Prashanth",10)
print(obj1)       # Prints what are all present in __str__()
print(dir(obj1))  # Already has __init__() and str()

obj2 = Student("Prashanth",12,"VIT",201,"easy")  ## 1st two --> parent class attributes and next 3 are child class attributes
print(isinstance(obj1,Person))
print(isinstance(obj1,Student))

print(type(obj1))
print(type(obj2))

print("Before using over-riding : " ,obj2.age)
 # Over-riding the age 
obj2.age = 100 
print("After using over-riding : ",obj2.age)