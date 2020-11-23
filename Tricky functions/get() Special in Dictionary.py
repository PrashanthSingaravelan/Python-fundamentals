# get (1st arguement , 2nd arguement)
# get (The key of the value to retrieve , Fallback value to return if the key doesn't exist)

picnicitems={"Bread":"6 nos","Jam":"1 nos"}
 # Jam is already a key
# Important => Compares the key and returns that key's value
print("I am bringing " +  picnicitems.get("Jam",0)    + " Jam immediately")
                       # str not required bc get() returns Jam
# Output => I am bringing 1 nos Jam immediately

# Butter is not a key so it takes the fallback value
print("I am bringing " +  str(picnicitems.get("Butter",0)) + " Butter immediately ")
# I am bringing 0 Butter immediately

# str() => Converts the entire thing into a normal string
# print("I am bringing " +  str(picnicitems.get("Butter",0)) + " Butter immediately ")
                        # str required bc get() returns 0. And 0 should be included in print
a=10 
print(str(a)) # Integer 10 => String 10