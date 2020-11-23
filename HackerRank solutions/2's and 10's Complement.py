import math

def Complement(n):
    # 1) To find how many digits in order to decide the power
    
    temp=n # temporary variable to make changes in n
    len1=0 # To know the number of digits
    
    while(1):# To find the number of digits in a number divide that number by 10 
        len1=len1+1 # Till the numerator is 0
        n=int(n/10)
        
        if(abs(n)==0):
           break
    
    n=temp # Restoring the number from temp
    
    # 2's Complement
    comp=math.pow(10,len1)-n
    return int(comp) 
    
n=int(input("Enter the number : "))
comp=Complement(n)

print("10's Complement of {} is {}".format(n,comp))
        
        
        