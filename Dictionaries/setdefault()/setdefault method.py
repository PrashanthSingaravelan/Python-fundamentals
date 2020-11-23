# setdefault(2 arguements)
# setdefault(key to check for, value to set at that key if the key does not exist)
#        if key exists  => returns the orginal value of that key (Orginal key values cannot be changed)
# if key doesn't exists => returns the value added to that key


dict1=dict(Iphone="10X Max",Samsung="Note 11",Google="Pixel")
print(dict1.setdefault("Nokia","Lumia 30"))  # Lumia 30 

print(dict1.setdefault("Iphone","11pro")) # 10X Max
dict1["Iphone"]=dict1["Iphone"] + " 11 pro"

for keys,items in dict1.items():
    print(keys,items)
# Iphone 10X Max 11 pro
# Samsung Note 11
# Google Pixel
# Nokia Lumia 30


