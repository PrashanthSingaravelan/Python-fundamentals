#1) \s => Matches any white space character (newline,tabs,spaces)
#2) \S => Pulls out all the words without spaces.Matches non white space character 

import re
string="Hi hello"
print(re.search("\S+",string).group()) # Hi

print(re.search("\s+"," Chandler bing").group())  #\s=> white space before Chandler
# <space>

string2="Joey its me Chandler from USA. Monica Its me Pheebs from California"
print(re.findall("\S+",string2)) # Returns as List
# ['Joey', 'its', 'me', 'Chandler', 'from', 'USA.', 'Monica', 'Its', 'me', 'Pheebs', 'from', 'California']

print(" ".join(re.findall("\S+",string2))) # Lists are joined and return as a normal phrase
# Joey its me Chandler from USA. Monica Its me Pheebs from California

string3="Ross your are very disgusting"
print(re.search("\S+\s+\S+\s+\S+\s+\S+\s+\S+",string3))

print(re.search("\S+",string2).group())