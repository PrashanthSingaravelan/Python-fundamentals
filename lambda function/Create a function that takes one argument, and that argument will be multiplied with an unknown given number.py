def func1(x,y):
    a = lambda x,y:x*y
    return a(x,y)

n=int(input("Enter a number : "))
print('Double the number of {} : {}'.format(n,func1(n,2)))
print('Triple the number of {} : {}'.format(n,func1(n,3)))
print('Quadruple the number of {} : {}'.format(n,func1(n,4)))
print('Quintuple the number {} : {}'.format(n,func1(n,5)))