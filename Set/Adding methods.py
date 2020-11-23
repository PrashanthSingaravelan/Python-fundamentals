my_set={1,3}
print(*my_set) # 1 3

# For adding each element in a set
my_set.add(2)
print(*my_set) # 1 2 3

# For adding multiple elements in a set
my_set.update([2,3,4])
print(*my_set) # 1 2 3 4

# Add a list and a set into a set
my_set.update([4,5],{1,6,8})
print(*my_set) # 1 2 3 4 5 6 8