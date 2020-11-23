my_set={1,3,6,4,2}
print(my_set)

# remove() If the elements are not a member of the set, it raises an error
my_set.remove(6)
print(my_set)

# discard() If the elements are not a member of the set, it will ignore and raises no error
my_set.discard(18)
print(my_set)

print(my_set.pop())