               # search and match

# searches anywhere throughout the string
import re
x=re.search("c","abcdef")
print(x) #<re.Match object; span=(2, 3), match='c'>

# matches only at the beginning of the string 
# span ->the index location
y=re.match("c","abcdef")
z=re.match("c","cdefgh")
print(y) #None
print(z) #<re.Match object; span=(0, 1), match='c'>

# only search first instance
# Here 1st instance span(2,3) 2nd instance span(6,7) 3rd instance span(9,10)
# re.search will only search 1st instance

a=re.search("c","abcdecgjc")
print(a) #<re.Match object; span=(2, 3), match='c'>

 # Mutiline concept
b=re.search("c","abefg\nghc")
print(b) #<re.Match object; span=(8, 9), match='c'>

c=re.match("c","abgh\nc")
print(c) #None

# Using bool expression
print(bool(re.search("c","abefg\nghc"))) # True
print(bool(re.match("c","abcdef"))) # False