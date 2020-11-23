# \b => Used to find as a word boundary
#       Matches the empty string at the beginning or end of a word.        

# \B => Used to find the match at the middle
#       Matches the empty string neither at the beginning nor end of a word. 

import re
string="Pls provide!! me??? a tissue"
print(re.findall(r"\b\w",string)) # Only first letter

print(re.findall(r"\b\w\w",string)) # First and second letter

print(re.findall(r"\b\w\w\b",string)) # Middle word

print(re.findall(r"\b\w+\b",string)) # Boundary words Boundary



