list1 = [1,2,3,4,5,6,7,8,9,10]

## Even and odd number
print("Even number list : ",list(filter(lambda x:x**2,list1)))
print("Odd number list  : ",list(filter(lambda x:x**3,list1)))

## Square and cube number
square = lambda x:x**2
cube = lambda x:x**3

print("Square : ",end=' ')
for i in list1:
    print(square(i),end=' ')

print()
print("Cube : ",end=' ')
for i in list1:
    print(cube(i),end=' ')

print()
print("Square : ",list(map(lambda x:x**2,list1)))
print("Cube   : ",list(map(lambda x:x**3,list1)))