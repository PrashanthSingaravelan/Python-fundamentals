import operator

dict1={1:2, 7:1, 10:12, 3:4 ,4:5}
print("Original Dictionary : ",dict1)

# Sort by keys and returns as list of Dictionary
a=sorted(dict1.items())  

# Sort by values and returns as a single list 
b=sorted(dict1.values()) 

# Sort by values and returns as a list of dictionary
s=sorted(dict1.items(),key=operator.itemgetter(1))
print("Ascending Order  : ",s)

p=sorted(dict1.items(),key=operator.itemgetter(1),reverse=True)
print("Descending Order : ",p)

