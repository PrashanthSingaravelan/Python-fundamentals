import numpy as np

# 1) np.copy(arr1) 
# Create an array x, with refrence to y and a copy to z
x=np.array([[10,20,30],[40,50,60],[70,80,90]])

y=x           # Here y is a reference
z=np.copy(x)  # And z is a copy

        # Trying to modify the array elements
# Modyfying x will affect only in y and not in z
x[0,0]=60



# 2) arr=np.append(arr1,arr2, axis=0)
# axis is defined only in multi-dimensional array
# By default the it returns the flattened array(all the elements in a single row)

p=np.arange(10,30,2).reshape(5,2)
q=np.arange(40,60,2).reshape(5,2)

a=np.append(p,q)
print("Flattened Array : ",a)

a=np.append(p,q,axis=0)
print("Axis-0 : ",a)
# Will Append along the axis=0
#   [[10 12]
#    [14 16]
#    [18 20]
#    [22 24]
#    [26 28]
#    [40 42]
#    [44 46]
#    [48 50]
#    [52 54]
#    [56 58]]

a=np.append(p,q,axis=1)
print("Axis-1 : ",a)
# Will Append along the axis=1
#  [[10 12 40 42]
#   [14 16 44 46]
#   [18 20 48 50]
#   [22 24 52 54]
#   [26 28 56 58]]

