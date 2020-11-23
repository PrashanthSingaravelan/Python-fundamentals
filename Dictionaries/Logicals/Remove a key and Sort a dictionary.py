# 1) Remove a key
dict1={"1st item":100,"2nd item":200,"3rd item":250}

def Remove(r):
  a=0
  for i,j in dict1.items():
   if i==r:a=r
  del dict1[a]
  
print("Before Deleting : ",dict1)
Remove("1st item")
print("After Deleting  : ",dict1)

# 2) Sort a Dictionary
import operator

dict2={"Biriyani":"Patchadi",
       "Rice":"Dhal",
       "Idly":"Sambar"}

#print(sorted(dict2))           # Sorts the key
#print(sorted(dict2.values()))  # Sorts the values

for i,j in sorted(dict2.items()):
    print(i,j)
    


 
