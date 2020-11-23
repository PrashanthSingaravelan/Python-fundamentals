# split method
# The re.split method splits the string where there is a match and returns
# a list of strings where the splits have occurred.

import re

result=re.split('i','Anlaytics Vidhya')
print(result) # ['Anlayt', 'cs V', 'dhya']

result1=re.split('i','Analytics Vidhya',maxsplit=1)
print(result1) # ['Analyt', 'cs Vidhya']    

print(re.split("\d+","Twelve:12, Hundred:100")) #['Twelve:', ', Hundred:', '']

print((re.split(r'\s','we are splitting the words'))) # Though it is raw string \s behaves as only \s
# Now the split occurs at every blank spaces
# ['we', 'are', 'splitting', 'the', 'words']

print(re.split(r's','we are splitting the words')) #Now the split occurs only at s
# ['we are ', 'plitting the word', '']

