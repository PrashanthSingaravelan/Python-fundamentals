# To assign a constant value to all the keys
dict1={i:"Nope" for i in ['a','b','c']}
print(dict1) #{'a': 'Nope', 'b': 'Nope', 'c': 'Nope'}

# Intialise dictionary using fromkeys()
dict2=dict.fromkeys(['a','b','c'],"Constant")
print(dict2) #{'a': 'Constant', 'b': 'Constant', 'c': 'Constant'}

dict3={j.upper():j*3 for j in "Apple"}
print(dict3) # {'A': 'AAA', 'P': 'ppp', 'L': 'lll', 'E': 'eee'}

print(str(dict3))