import re
string1="Morris Garage is one of the famous automobile company"

# Extracing consecutive two characters in each word
print(re.findall("\w\w",string1))

# \b => Used to find a match at the beginning / at the end of the word
# Extracting first character in each word
print(re.findall(r"\b\w",string1))
# ['G', 'M', 'i', 'o', 'o', 't', 'f', 'a', 'c']

# Extracting first two characters in each word
print(re.findall(r"\b\w\w",string1))
# ['Ga', 'Mo', 'is', 'on', 'of', 'th', 'fa', 'au', 'co']
