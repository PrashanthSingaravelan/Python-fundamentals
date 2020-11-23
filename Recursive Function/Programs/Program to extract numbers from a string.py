# Program to extract numbers from a string
import re
string1="Prashanth was born on 24th April 2001"
print(re.findall("\d+",string1))