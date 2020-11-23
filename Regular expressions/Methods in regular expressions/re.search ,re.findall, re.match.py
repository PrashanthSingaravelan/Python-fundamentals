import re
Substring ="Prashanth"

String =''' What is your view about Chandrayan-2 Prashanth?
           Hello everyone its me prashanth from Chennai
           My view is that it has accomplished 95% of its job'''

#re.IGNORECASE : This flag allows for case-insensitive matching of
#  the Regular Expression with the given string
#  i.e. expressions like [A-Z] will match lowercase letters, too.
#  Generally, It’s passed as an optional argument to re.compile().

# 1) re.search=searches only for the first instance if got that first instance it will quit by itself

print(re.search("boy","Prashanth is a good boy and he is a naughty boy"))
# Only boy after good will be searched and not the boy after naughty
# span=(20, 23), match='boy'
print(re.search("c","abcdefg")) # span=(2, 3), match='c'

print(re.search(Substring,String,re.IGNORECASE).group()) # Prashanth

# 2) re.findall= finds all the instances if got also it will go throughout the entire string

print(re.findall(Substring,String,re.IGNORECASE)) # ['Prashanth', 'prashanth']
print(*re.findall("info","Spread this info to all the information persons")) # info info
print(re.findall("p","abch skpais afp")) # ['p', 'p']

# 3) re.match() => Matches only at the beginning of the string

print(re.match(Substring,String,re.IGNORECASE)) # None because Prashanth is only in 2nd line

