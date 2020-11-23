list1=[89,38,20,65,21,28,90]
del list1[2:5]      # Deletes the element at index 2,3,4 Not 5
print(list1)        # [89, 38, 28, 90]
print(list1.pop(2)) # Popped element => 28
