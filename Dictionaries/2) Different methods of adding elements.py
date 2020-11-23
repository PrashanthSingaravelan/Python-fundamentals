# Note- While adding a value, if the key value already exists
# the value gets updated otherwise a new Key with the value is added to the Dictionary.

# 1) In order to add elements, should create an empty set then add
dict1={} # Empty dictionary
dict1["Apple"]="Red"
dict1["Banana"]="Yellow"
print("After adding the element: ",dict1)

# 2) Adding a set of values to a single key
dict1["Vegetables"]= 1,2,3
print("Adding a set of values to single key: ",dict1)

# 3) Updating the values
# Before:  {'Apple': 'Red', 'Banana': 'Yellow', 'Vegetables': (1, 2, 3)}
dict1["Banana"]="Sweet Banana"
print("After updating : ",dict1)
# After: {'Apple': 'Red', 'Banana': 'Sweet Banana', 'Vegetables': (1, 2, 3)}


# 4) Adding list to the dictionary
jobs=[]
jobs.append("Developer")
jobs.append("Manager")
empty={}
empty["name"]="Suresh"
empty["age"]="29"
empty["job"]=jobs
print(empty)

dict2={1:"eggs",2:"omelete",3:"Bread"}
print(*dict2.items()) #(1, 'eggs') (2, 'omelete') (3, 'Bread')

dict3=dict(Breakfast="Dosa",Drink="Coffee")
dict2.update(dict3) #None  No return type
print(*dict2.items())
 # (1, 'eggs') (2, 'omelete') (3, 'Bread') ('Breakfast', 'Dosa') ('Drink', 'Coffee')
