dict1=dict(a=1,b=2,c=3)
print(dict1.keys()) # Only keys

print(dict1.values()) # Only the values

print(dict1.items()) # Full dictionary

# 1) zip()
for (i,j) in zip(['a','b','c'],[1,2,3]):
    print(i,j)

        # (or)

dict1=dict(a=1,b=2,c=3)  # a 1
for x,y in dict1.items():# b 2
    print(x,y)           # c 3

# 2) join()
dict5=dict(Iphone="XR max",Samsung="Note11",Nokia="Lumia")
print(" and ".join(dict5)) # Iphone and Samsung and Nokia

# 3) sorted()
for keys,items in sorted(dict5.items()):
    print(keys,items) # Iphone XR max
                      # Samsung Note11
                      # Nokia Lumia
# Incase of same key and values
dict2={p:p for p in [1,2,3,4]}
print(dict2) # {1: 1, 2: 2, 3: 3, 4: 4}

# To square only the values
#for key :  for values square
dict3={q : q**2 for q in [1,2,3,4]}
print(dict3) # {1: 1, 2: 4, 3: 9, 4: 16}

# Keys=>lower   : values=>as such
dict4={s.lower():s + '!' for s in ["Bread","Butter","Jam"]}
print(dict4) #{'bread': 'Bread!', 'butter': 'Butter!', 'jam': 'Jam!'}

