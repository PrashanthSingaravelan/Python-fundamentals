import re
string1="Apple Iphone eleven sales starts from October"
print(re.findall(r"[aeiouAEIOU]\w+",string1))
# ['Apple', 'Iphone', 'ales', 'arts', 'om', 'October']
# sales  => ales  (Ignors s ,then it gets "a"les and prints)
# starts => arts  (Ignors s and t, then it gets "a"rts and prints )
# from   => om    (Ignores f and, the it gets "o"m and prints)

# Starting with vowel (\b => For word boundary)
print(re.findall(r"\b[aeiouAEIOU]\w+",string1))
# ['Apple', 'Iphone', 'eleven', 'October']

print(re.findall(r"\b[^aeiouAEIOU]\w+",string1)) # Prints words starting with spaces
# [' Iphone', ' eleven', ' sales', ' starts', ' from', ' October']

# Print consanants
print(re.findall(r"\b[^aeiouAEIOU ]\w+",string1)) # Leave space at the end [^aeiouAEIOU ]
# ['sales', 'starts', 'from']