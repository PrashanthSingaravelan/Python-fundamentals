# Power a number
# To find the power a number (i,e) 2^9 we have to do 9 multiplications

def pow(a,b):
    if b==0:
       return 1
    else:
       return pow(a,b-1) * a

a=int(input("Enter a number:"))
b=int(input("Enter the power term:"))
c=pow(a,b)
print("The result of {} to the power {} is : {}".format(a,b,c))

# Another method to reduce the number of multiplications
# even power 2^9 = 2*2^8
# odd power  2^8 = 2^8
def pow1(p,q):
    if q==0:
        return 1
    elif q%2==0:    # If the power term is even.
        return pow1(p*p,q/2)
    else:          # If the power term is odd
        return pow1(p*p,(q-1)/2)*p


p=int(input("Enter a number:"))
q=int(input("Enter the power term:"))
r=pow1(p,q)
print("The result of {} to the power {} is : {}".format(p,q,r))


