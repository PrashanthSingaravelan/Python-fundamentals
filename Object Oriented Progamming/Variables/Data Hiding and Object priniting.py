# 1) Hidden Variable
# Data hiding => If we use _ before any attribute. Then that attribute will not be directly visible outside
# But can be accessed within the class only

class MyClass: 
  
    # Hidden member of MyClass 
    __hiddenVariable = 0
    def add(self, increment):  # Hidden variable => Can be accessed only within the class 
        self.__hiddenVariable += increment 
        print (self.__hiddenVariable) 
   
# Driver code 
obj1=MyClass()      
obj1.add(2) 
obj1.add(5) 

# Error => 'MyClass' object has no attribute '__hiddenVariable'
#print(obj1.__hiddenVariable) # Cannot be accessed outside the class,

# This can be solved by a tricky function
# Even the hidden variables can be used outside the class by using the following method
print(obj1._MyClass__hiddenVariable)

# 2) str() and repr() => Return type Compulsory should be string

# str() => Returns the string representation of the object.
# This method is called when str() or print() is invoked on the object.

# repr() => Returns the object representation. It could be any valid expression 
# of the objects like tuples,dictionaries

class Difference:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "From str() Test a:%s and b:%s " % (self.a,self.b)
    def __repr__(self):
        return "From repr() Test a:%s and b:%s "% (self.a,self.b)
obj1=Difference(24,49)
print(obj1)
print({obj1})   # Here the object is in the type dict

class Diiference1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __repr__(self):
        return "{From repr() Test a:"+self.a+"and b:"+self.b+"}"  
    #{From repr() Test a:self.a and b:self.b} => Don't implement this because the return type is dictionar
    # But both str() and repr() return type should be string
    # In repr() the type in which the object has been sent the output will be in the same form.
