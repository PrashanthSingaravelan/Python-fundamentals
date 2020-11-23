import random
# 1) radiant() picks a random integer from 1 to 9. No return type
print(random.randint(1,9))

# 2) end=" " => To disable newline that gets added to the end of the print() 
print("Prashanth")         # Prashanth
print("Don't Hesitate")    # Don't Hesitate

print("Prashanth",end=" ") # end="<space>" => Leaves one blanck space
print("Don't Hesitate")    # Prashanth Don't Hesitate

# 3) When you pass multiple string values to print(), the function
# will automatically separate them with a single space
print("Hello","World","Sleep well")  # Hello World Sleep well

# 4) But you could replace the default separating string by passing the sep  keyword argument.
print("Hello","World","Sleep well",sep=",") # Hello,World,Sleep well

