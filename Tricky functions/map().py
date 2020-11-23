# map() => Returns a list of the results after applying the given function
#          to each item of a given iterable (list, tuple etc.)

# map(function,iterable)
# function => It is a function to which map passes each element of given iterable
# iterable => It is a iterable which is to be mapped

def addition(n):
    return n + n

numbers=(1, 2, 3, 4)
result=map(addition, numbers)   # <class 'map'>
print(list(result))             # <class 'type'>