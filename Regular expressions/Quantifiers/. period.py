# '.' => Matches all character except new line

import re

string='''Honourable Prime Minister Mr.Narendra Modi
 Pls resign your job after stabalising our Indian economy'''

print(re.search(".+",string).group()) # After New line it is not included
print(re.search(".+",string,flags=re.DOTALL).group()) #flags=re.DOTALL  => New line is included

#Honourable Prime Minister Mr.Narendra Modi
#Pls resign your job after stabalising our Indian economy

