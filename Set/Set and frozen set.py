normal_set=set(["2","1","Hi hello","Bye"])
frozen_set=frozenset(["Hello","everybody","Good","Night"])

#Sets are mutable
print(normal_set)  # {'Bye', '2', 'Hi hello', '1'}

normal_set.add("Pls add me")

print(normal_set)  # {'Bye', 'Pls add me', '1', '2', 'Hi hello'}

#Frozen sets are always immutable
frozen_set.add("Its me Prashanth") # Raises an error since frozen set has no attribure add
print(frozen_set)  

