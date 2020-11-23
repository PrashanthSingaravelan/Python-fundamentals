class age:
    def __init__(self,age1):
        self.age1=age1
    def compare(self,other):  # self->obj1  and other->obj2
        if self.age1==other.age1:
           return True
        else:
           return False



n=int(input("Mr Prashanth pls enter your age:"))
m=int(input("Mr Mothish pls enter your age:"))
obj1=age(m) # Constructor will be executed
obj2=age(n)
if obj1.compare(obj2):
    print("The age is same")
else:
    print("The age is different")

