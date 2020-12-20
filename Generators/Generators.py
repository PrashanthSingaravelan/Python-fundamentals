def square_number(nums):
    for i in nums:
        yield (i*i)

result = square_number([1,2,3,4,5])

print(result)
# dir(result) # contains iter() and next() 

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

print(next(result))  # Will give StopIteration exception

## Stop iteration exception is handled by for loop
for i in result:
    print(i)